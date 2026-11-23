# AT2 Part C: Red / Blue / Purple Team Exercise and Incident Report

**Unit:** VU23221 Evaluate and test an incident response plan for an enterprise (with VU23219)
**Scenario:** NovaStyle (fictional company), brute-force login attack against an SSH server in a controlled lab
**Topics:** red teaming, blue teaming, purple team analysis, SIEM (Wazuh), incident response plan (IRP), gap analysis, cyber hygiene, evidence-based report writing

---

## 1. Big picture

A Red/Blue/Purple exercise tests an organisation's **people, process and technology** against a realistic attack, then turns the findings into improvements.

| Team | Goal | Output in this exercise |
|---|---|---|
| **Red** | Simulate the attacker; find weaknesses that can really be exploited | Attack chain, tools/TTPs, successful breach points, screenshots |
| **Blue** | Detect, investigate and respond using the SIEM and the IRP | Alerts, triage, containment/eradication/recovery steps, findings |
| **Purple** | Connect Red and Blue results; find gaps; recommend fixes | Gap analysis, lessons learned, recommendations, conclusion |

**Exercise lifecycle:** plan scope and rules of engagement → Red executes → Blue monitors and responds → collect evidence → Purple analyses → report and present.

**Rules of engagement (scope):**
- Authorised lab only. Test accounts only. No production systems, no real customer data, no external systems.
- Record **dates, targets and evidence** so the report can be verified later.

---

## 2. Red Team: the attack chain

Target in the lab: Ubuntu 16.04 server with SSH, FTP (ProFTPD 1.3.3c) and a web server (Apache 2.4.18).

### 2.1 Reconnaissance and enumeration
- **Nmap**: host discovery, port scan, service/version detection. Result: open FTP, SSH and web services.
- **Nikto**: web server scan. Result: outdated Apache version and missing security headers.
- **Searchsploit**: searches a local copy of Exploit-DB for known exploits matching the discovered versions.
- **Meaning of the findings:** outdated software = larger attack surface; missing headers = weak hardening.
- **Important caveat:** Apache 2.4.18 is the version shipped with Ubuntu 16.04. Distributions often *backport* security fixes without changing the version number, so a version banner alone does not prove the server is vulnerable. Confirm before claiming a specific vulnerability.
- Ubuntu 16.04 passed the end of its standard support in April 2021 (end-of-life), which is a real risk: no regular security updates.

### 2.2 Exploit research (not pursued)
- Metasploit module for the **ProFTPD 1.3.3c backdoor** was located and examined.
- No successful exploitation was demonstrated, so the attack moved on.
- **Reporting lesson:** write "investigated, not pursued", never "exploited".

### 2.3 Brute force with Hydra
- **Online brute force / password guessing**: many login attempts sent to a live service (SSH) using username and password lists.
- Hydra needs: a **target and protocol** (`ssh://<ip>`), a **username** or user list, a **password list**, and optionally threads.
- **Why it worked:** the account's password was the same as its username, and there was **no account lockout and no rate limiting**.
- **Practical issue:** wrong file paths for the password list caused errors. Pre-check the working directory and file names before running.
- Only run against systems you are authorised to test.

### 2.4 Initial access and privilege escalation
- Valid credentials found by Hydra were used to log in over **SSH** (initial foothold).
- **sudo su**: the system *did* ask for a password, but the compromised account's own password was accepted, so the account had broad sudo rights. `whoami` showed `root`.
- Root = full administrative control of the server.
- **Lesson:** "no exploit needed" privilege escalation is a **least-privilege** failure (sudoers too permissive) combined with weak credentials.
- Do not write "no password was needed" unless that is what happened. Accuracy matters.

### 2.5 Successful breach points (what made the attack work)
1. Weak authentication (password = username).
2. No account lockout or rate limiting.
3. SSH access with the guessed credentials (foothold).
4. Privilege escalation to root via sudo with the same password.
5. No multi-factor authentication (MFA).

### 2.6 MITRE ATT&CK mapping

| Stage | Technique | ID |
|---|---|---|
| Recon | Network Service Discovery | T1046 |
| Recon | Active Scanning: Vulnerability Scanning | T1595.002 |
| Exploit attempt (not achieved) | Exploit Public-Facing Application | T1190 |
| Credential attack | Brute Force: Password Guessing | T1110.001 |
| Initial access | Valid Accounts | T1078 |
| Remote access | Remote Services: SSH | T1021.004 |
| Privilege escalation | Abuse Elevation Control Mechanism: Sudo and Sudo Caching | T1548.003 |

---

## 3. Blue Team: detection, investigation and response

### 3.1 Wazuh SIEM basics
- Components: **agents** on endpoints → **manager/server** (rules and decoders) → **indexer** (storage) → **dashboard** (search and visualisation).
- **Discover** page: search events (for example "brute force"), filter by time range, open an event to see details.
- Useful fields: agent name/ID/IP, rule ID and description, rule level, source IP, username, timestamp.
- **Endpoints** page: confirms whether an agent is active.
- **File Integrity Monitoring (FIM)**: shows changes to files. No FIM events does not prove nothing happened.
- **Active Response**: Wazuh can run automatic actions (for example block an IP, temporary lockout) when a rule fires. This is what turns detection into containment.

### 3.2 How brute-force detection works
- Typical logic is **frequency-based correlation**: many failed logins from the same source within a time window → one higher-level alert.
- SSH logs on Ubuntu: `/var/log/auth.log` (`Failed password for ...` vs `Accepted password for ...`).
- **Alerts of failed attempts do not prove compromise.** To confirm a successful login, correlate with the host's authentication log (successful login after many failures from the same source is the classic sign).
- **Counts depend on filters.** The same search can show different numbers (for example 36 alerts over 5 days vs 16 events in a 7-day view) because of time range and query. Always state the filter and time range, or explain the difference.

### 3.3 Triage questions
1. Which system generated the alert (agent, IP, OS)?
2. Which accounts are targeted (admin/root are higher priority)?
3. Which source IPs, and how many attempts over what time?
4. Was there any successful login or privilege escalation?
5. Is this one incident or several? What is the impact?

### 3.4 IRP phases and example actions (NIST SP 800-61)
Rev. 2 describes four phases: **Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity**. Rev. 3 (2025) maps incident response to the NIST CSF 2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover).

| Phase | Example actions for a brute-force incident |
|---|---|
| Detect and analyse | Review alerts, identify host/accounts/IPs, preserve logs, classify severity |
| Containment | Block attacking IPs, lock or disable affected accounts, restrict the login service, isolate the host (keep logs available as evidence) |
| Eradication | Reset passwords, remove unauthorised accounts/changes, scan for malware, patch and harden, enable lockout/MFA |
| Recovery | Restore from verified backup if needed, check data integrity, test services, return to normal only after checks, increase monitoring |
| Post-incident | Lessons learned, update IRP and detection rules, retest |

- **Evidence handling:** save relevant logs *before* changing accounts or firewall rules; keep a chain of custody.
- **Short-term vs long-term containment:** short-term stops the attack now (block IP); long-term allows safe operation while fixing (segmentation, restricted network).

### 3.5 Detection is not response
In this exercise Wazuh generated brute-force alerts, but the evidence showed **no containment, eradication or recovery actions**. Steps in the report were therefore written as **recommended actions, not performed actions**.

---

## 4. Purple Team: gap analysis and recommendations

### 4.1 Gap analysis (People / Process / Technology)

| Area | Gaps found |
|---|---|
| **People** | Weak password habits; poor awareness of least privilege; patching not treated as routine |
| **Process** | No lockout/rate-limit policy; no enforced password policy; no patch management process; IRP not exercised for authentication attacks; no clear response steps after an alert |
| **Technology** | No MFA; outdated Apache and end-of-life Ubuntu; missing security headers; alerts without automatic or semi-automatic containment; weak correlation; sudo too permissive |

### 4.2 Core Purple message
**Detection ≠ Response.** Alerts existed, but nothing stopped the attacker. Real value comes from linking detection to a documented, rehearsed response.

### 4.3 Linking Red and Blue evidence
- Match by **time, source IP, target host, and username**.
- Be careful: the host that *generated the Wazuh alerts* (agent) may not be the host Red *attacked*. If they differ, or the dates differ, say that the link is **not verified** rather than claiming the alerts detected the Red attack.
- Different observations (for example admin/root in alerts vs the account Red actually used) must be explained, not hidden.

### 4.4 Recommendations

**Short-term**
- Account lockout after 5–10 failed attempts (PAM: `pam_faillock` / `pam_tally2`) and SSH rate limiting (for example fail2ban or firewall rate limits).
- Strong password policy (length, complexity, no password equal to username).
- Restrict sudo to the minimum needed; apply role-based permissions.
- Apply critical security patches; upgrade or harden Apache; upgrade Ubuntu.
- Tune Wazuh rules: correlate repeated failures into one high-severity alert and enable Active Response.
- Log and alert on all sudo / privilege escalation events.

**Long-term**
- MFA for remote access, admin interfaces and privileged accounts.
- Formal, risk-based patch management with maximum patch age per severity, automation and a compliance dashboard.
- Network segmentation and least-privilege architecture.
- Recurring Red/Blue/Purple exercises (about every six months) and periodic audits plus an annual external assessment.

**Training**
- Security awareness (password hygiene, social engineering).
- Admin training: least privilege, secure sudo configuration, patching.
- Blue Team: Wazuh rule development, correlation and active response.

**IRP updates**
- New playbook for authentication brute force / credential stuffing: detection thresholds, immediate containment actions (lockout, temporary IP block, forced password reset).
- Add privilege-escalation detection and response (review sudo logs, isolate compromised accounts).
- Reference SIEM use cases and any automatic responses in the IRP.
- Regular tabletop exercises.

### 4.5 Security policy awareness and cyber hygiene
Pattern: **issue → awareness strategy → implementation → evaluation**.

| Issue | Strategy and implementation | How to evaluate |
|---|---|---|
| Weak passwords, no lockout | Quarterly training or e-learning; password policy; lockout; MFA | Password audits, simulated brute-force tests |
| Outdated software | Monthly patch review cycle; patch compliance dashboard; automated patching | Average time from patch release to application |
| Excessive privileges | Per-role sudo review; approval process for elevated access; sudo logging/alerts | Regular audit of sudo logs and privilege changes |

Cyber hygiene practices: strong unique passwords, MFA, timely patching, least privilege, logging and monitoring, regular audits and awareness training.

---

## 5. Writing the incident report: lessons learned

### 5.1 Report structure (Part C template)
1. Team composition
2. Introduction: 2.1 engagement objectives, 2.2 scope and timeline
3. Red Team simulated attack: methodology, threat scenarios, TTPs, attack scenarios executed, breach points (with screenshots)
4. Blue Team responses: initial alert and triage, detection and investigation, containment, eradication, recovery, findings and observations
5. Purple Team analysis: gap analysis, lessons learned, recommendations, security policy awareness and cyber hygiene
6. Conclusion: summary, future recommendations, sign-off
7. Appendix: evidence, tools and references, technical terms

### 5.2 Evidence-based writing rules
- **Say only what the evidence shows.** Separate *performed* from *recommended* and *observed* from *assumed*.
- **Use hedging only where needed**, and be specific: "the screenshots do not show X" is better than vague wording.
- **Keep facts identical across all sections and all teams:** target IP, OS and software versions, usernames, dates, alert counts, number of attempts.
- **Match the scenario:** the attack was on the **SSH service**, not a web login page. A mismatch between sections makes the whole report look unreliable.
- **Describe privilege escalation precisely** (password required and reused).
- **Avoid absolute words** unless proven (for example "unrestricted"; prefer "excessive").
- **Figures:** caption format `Figure N — Title`, followed by a one- or two-sentence description of what the screenshot proves.
- **Do not delete teacher instructions** from the template; write the answer below them.

### 5.3 Consistency problems found and fixed during review
| Problem | Fix |
|---|---|
| Target described as a login page in some sections and an SSH server in others | Use the SSH server everywhere |
| Sudo described as needing no password | State that a password was required and the same compromised password worked |
| Blue sections claimed actions that were never performed | Rewrite as "recommended, not performed" |
| 36 vs 16 Wazuh alerts | Explain the different filter/time range |
| Red attack date vs Wazuh alert date; different hosts | State that the link between Red activity and Blue alerts is not verified |
| Software version mentioned inconsistently | Use the version actually observed (Apache 2.4.18, Ubuntu 16.04) |
| Duplicate/incorrect automatic heading numbers | Use one consistent numbering scheme |

### 5.4 Workflow that worked
1. Agree scope, roles and deadlines.
2. Run the exercise; take labelled screenshots as you go (command, output, time).
3. Write sections with evidence; add captions.
4. Review for cross-section consistency (a checklist, not a re-write).
5. Purple team reviews all sections, identifies gaps, then writes analysis and recommendations.
6. Final formatting pass (fonts, headings, captions, tables, images) without changing content.
7. Record presentation parts, merge, submit, and acknowledge any AI use.

---

## 6. Quick command and log reference (authorised lab only)

| Purpose | Example |
|---|---|
| Find hosts / services | `nmap -sn <network>` ; `nmap -sV <target>` |
| Web server scan | `nikto -h http://<target>` |
| Search known exploits | `searchsploit proftpd 1.3.3c` |
| SSH online guessing (concept) | `hydra -L users.txt -P passwords.txt ssh://<target>` |
| Check sudo rights (on target) | `sudo -l` |
| Confirm current user | `whoami` |
| Failed / successful SSH logins | `grep "Failed password" /var/log/auth.log` ; `grep "Accepted" /var/log/auth.log` |
| Recent logins | `last` ; `lastb` |
| Pending updates (Ubuntu) | `apt list --upgradable` |

---

## 7. Key terms

- **TTPs**: tactics, techniques and procedures used by an attacker.
- **IOC**: indicator of compromise (for example a source IP, username, file hash).
- **SIEM**: system that collects, correlates and alerts on security events.
- **IRP**: documented procedures for responding to security incidents.
- **Least privilege**: give accounts only the access they need.
- **MFA**: authentication using more than one factor.
- **Account lockout / rate limiting**: temporarily blocking an account or source after repeated failures.
- **Containment / eradication / recovery**: stop the spread / remove the cause / restore normal service safely.
- **Chain of custody**: documented handling of evidence so it stays trustworthy.
- **Active Response**: automatic action taken by Wazuh when a rule triggers.
- **Backporting**: distributions fix vulnerabilities in old versions without changing the version number.

---

## 8. Self-check questions

1. Why is "Detection ≠ Response" the main finding of this exercise?
2. Why can failed-login alerts alone not prove an account was compromised?
3. How would you prove that a Wazuh alert belongs to the Red Team's attack?
4. What makes sudo privilege escalation a least-privilege problem and not an exploit?
5. Why can an Apache version banner be misleading on Ubuntu?
6. Which controls would have stopped this attack at each step (lockout, MFA, password policy, sudo restriction, patching, active response)?
7. How do you word a report section when an action was only recommended?

---

## References
- NIST SP 800-61 (Computer Security Incident Handling Guide), Rev. 2 and Rev. 3
- MITRE ATT&CK: T1046, T1595.002, T1190, T1110.001, T1078, T1021.004, T1548.003
- Wazuh documentation: rules, alerts, FIM, Active Response
- Class materials: Red-teaming fundamentals, Blue-teaming and evidence handling, cyber hygiene
