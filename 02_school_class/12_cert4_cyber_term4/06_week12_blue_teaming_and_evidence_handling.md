# Session 12 – Blue Teaming & Evidence Handling

- **Course:** Cert IV Cyber Security (VU23219 / VU23221) – Holmesglen Institute
- **Date:** 2026-10-27 (Tue, 1:30 pm class)
- **Related assessment:** Assessment Task 2 (Practical Tasks), Part B – Incident Response Plan (IRP)
- **Key reference:** NIST SP 800-61r3 (April 2025), *Incident Response Recommendations and Considerations for Cyber Risk Management*

---

## 0. Session Overview

Last session was **Red Team** (attack simulation: SQL injection against a deliberately vulnerable Linux VM from an attacking VM). Today is the mirror image, **Blue Team**: detect, respond, preserve evidence, analyse, report, and evaluate.

The six learning objectives, which also form the end-to-end incident response (IR) cycle:

1. SOC monitoring and incident detection
2. Apply Blue Team response strategies
3. Collect, process and preserve evidence
4. Analyse incident data and response actions
5. Report incident outcomes and findings
6. Evaluate security controls and monitoring effectiveness

Core principle repeated all day: **"If it wasn't documented, it didn't happen."**

---

## 1. SOC Monitoring and Incident Detection

### SOC (Security Operations Centre)
- Monitors an organisation's systems 24/7 and detects/responds to cyber threats.
- Watches network traffic for abnormal activity and unauthorised access.

### SIEM (Security Information and Event Management)
A central visibility platform for SOC analysts. Four core functions:
1. **Collect logs** from servers, network devices (firewalls, routers) and applications.
2. **Analyse security events** in real time.
3. **Correlate** data across sources (algorithms/statistics) to find threats; ties into threat modelling.
4. **Generate alerts** on suspicious activity or unauthorised access (the most important function).

### Holmesglen tooling
| Tool | Role |
|---|---|
| **Wazuh** | Open-source SIEM/XDR. Detects suspicious activity, generates **alerts**. Endpoint monitoring: file changes, malware, policy violations, intrusion detection, compliance monitoring. |
| **ELK Stack** | **Elasticsearch** (store + index logs), **Logstash** (collect + process logs), **Kibana** (dashboards/visualisation). Fast search, anomaly/pattern finding, event correlation, timelines. |

Rule of thumb: **Wazuh = "something is wrong" (alert); ELK = "dig into the logs" (investigate).**

### Wazuh architecture
1. **Wazuh Agents**: installed on endpoints (Windows/Linux/macOS); collect system logs, security events, file-integrity data; send to the server.
2. **Wazuh Server**: receives agent data, analyses it with predefined rules, detects anomalies, malware, unauthorised changes.
3. **Wazuh Indexer** (OpenSearch/Elasticsearch based): stores alerts/logs, enables fast search.
4. **Threat detection and Active Response**: predefined + custom rules; real-time blocking (e.g. block IPs, kill processes).
5. **Compliance monitoring**: PCI DSS, GDPR, HIPAA, NIST 800-53 modules.
6. **Integrations**: Shuffle, OpenCTI, ELK; automates threat-intel and response; can interact with firewalls.

### Alert severity = rule level
| Severity | Rule level |
|---|---|
| Low | 0–6 |
| Medium | 7–11 |
| High | 12–14 |
| Critical | 15+ |

Prioritisation is based on severity (e.g. repeated failed logins on an internet-facing server = High).

### 10-step "Wazuh + ELK in the SOC" workflow
1. **Review the alert** (rule, severity, host/user, time)
2. **Prioritise** by severity
3. **Investigate logs in ELK** (same user/IP across log sources)
4. **Correlate events** (failed logins → firewall block → successful login → sensitive file access)
5. **Identify scope and timeline** (start time, affected systems/users)
6. **Collect evidence** (logs, alerts, screenshots, IP/account/time; record the attack source)
7. **Escalate to the IRT** (what was detected, why, affected systems, evidence, recommended next steps)
8. **Support containment and remediation** (block IP, disable account, isolate host, remove malware, patch)
9. **Continue monitoring** to confirm alerts stop and no further attacks occur
10. **Document the incident** (this flow maps directly onto the assessment response plan)

---

## 2. Blue Team Response Strategies

**Blue teaming** = defensive security operations: **detect, respond, mitigate**, using tools *and* processes to protect systems, data and users (mostly in a SOC).

**Objectives:** detect early; respond quickly; contain before spread; minimise business/operational impact; strengthen security posture.

**Effective response** = containing the threat + minimising impact + preventing recurrence.

### Choosing a response action
Based on: **type of attack** (malware, phishing, insider threat…), **severity**, and **systems affected**.

### Common response actions
| Action | What it does |
|---|---|
| **Isolation** | Disconnect infected system from the network; usually the first immediate action to stop spread |
| **Blocking** | Block malicious IPs/domains/URLs in firewall/SIEM (after identifying the source) |
| **Account control** | Disable compromised accounts or reset passwords |
| **Process termination** | Stop malicious processes on endpoints |
| **Patch / update** | Fix the exploited vulnerability to prevent recurrence |

### Six-stage flow: Stop the threat → Limit damage → Secure the environment
| # | Stage | What happens | Goal |
|---|---|---|---|
| 1 | **Detect** | Review Wazuh SIEM alert | Identify potential threat |
| 2 | **Investigate** | ELK/Kibana: endpoint, user, network logs | Confirm and understand the incident |
| 3 | **Identify** | Which systems affected, scope | Identify impacted assets |
| 4 | **Contain** | Isolate host, block attacker IP, disable accounts | Prevent further damage |
| 5 | **Mitigate** | Patch vulnerability, remove malware, enforce MFA | Eliminate threat, strengthen security |
| 6 | **Secure & Restore** | Validate systems, monitor risk, restore normal ops | Safe return to operations |

**Contain vs mitigate:** containment is the emergency stop of spread; mitigation fixes the underlying cause.

### Evaluating response effectiveness
Four lenses: **Timeliness** (detection → first action time), **Containment effectiveness** (isolation/blocking/account control done correctly?), **Escalation and coordination** (IRT and stakeholders notified in time?), **Documentation review** (timestamps, decisions, outcomes recorded; evidence stored securely).

Key questions (flip-card activity): Was the threat contained quickly? Was business impact reduced (minimal downtime)? Did the attacker regain access? (Re-entry means weak mitigation; add controls such as MFA, patching, access control.)

Overall goal: reduce cyber risk, minimise business disruption, improve future security posture.

### Gaps and continuous improvement
- **No incident response is perfect.** After every incident, review the process, identify weaknesses, and implement control measures.
- Maps to NIST **Post-Incident Activity** (r3: **Improvement / lessons learned**).

---

## 3. Digital Forensics: Collect, Process and Preserve Evidence

**Digital forensics** = identifying, collecting, preserving, analysing and reporting digital evidence so it is accurate, unaltered, trusted and legally admissible. Analysts must ensure evidence is:
- accurate and unchanged,
- trusted during analysis,
- compliant with organisational and legal requirements.

### Five-phase forensic process
1. **Identification**: find relevant sources of evidence.
2. **Collection**: use approved tools/methods without altering data.
3. **Preservation**: protect integrity (hashing, write-blocking, chain of custody).
4. **Examination and Analysis**: interpret evidence (cause, impact, sequence).
5. **Reporting**: document and communicate findings to stakeholders.

Principles: **Integrity, Accuracy, Accountability, Justice.**

*Incident handling* (detect → analyse → mitigate → report) and *evidence handling* (identify → collect → preserve → analyse → report) run **in parallel**.

### 3.1 Identification: sources and volatility
Evidence sources:
- **Network logs**: firewall, DNS, load balancer
- **Host-based data**: Event Viewer/Syslog, registry, running processes
- **Security alerts**: SIEM and EDR telemetry (Wazuh, ELK)
- **Volatile data**: RAM, active connections, memory artefacts (**highest priority**; lost when power is off)

### 3.2 Collection: Order of Volatility
Collect the most volatile first:
1. Memory: registers, cache, RAM (includes active sessions and encryption keys)
2. System/network state: routing table, ARP cache, running processes
3. Temporary files and disk (non-volatile) data, remote logs, monitoring data
4. Physical configuration, archival backups (least volatile)

Best practices: follow **SOPs**; take **forensic images** (bit-by-bit copies capture deleted data and hidden traces); **filter and normalise** to remove noise and focus on anomalies. Do **not** casually power off a compromised host; RAM evidence would be lost.

### 3.3 Preservation
- **Hashing** (SHA-256, MD5): fixed-length digital fingerprint; any change alters the hash. Compare the hash at collection with the hash at analysis; a mismatch means tampering.
- **Chain of custody**: record **Who, When, Where, Why** for every handling of the evidence, with no gaps. Without it, evidence can be challenged in court or audit.
- **Write-blocking**: prevents accidental modification of original evidence.

### 3.4 Examination
Filter and extract relevant data; **decode / decompress / decrypt** (e.g. decoding JWT tokens); remove duplicates and irrelevant data to prepare for deep analysis.

### 3.5 Analysis
Determine **cause, scope/impact, cost, severity and sequence of events**; connect the dots across sources.
- **Event correlation**: link logs, alerts and system data (done by SIEM algorithms).
- **Timeline creation**: reconstruct when and how the attack unfolded.
- **Impact assessment**: affected systems/data, severity (critical/high/low), business impact.

### 3.6 Reporting
Documentation (findings, evidence, actions → investigation record), communication (clear to stakeholders), recommendations (gaps and improvements to prevent recurrence).

---

## 4. Analysing Incident Data and Response Actions

After containment, analysts examine collected evidence to determine **cause, scope and impact**: how the attack occurred, what systems were affected, and the overall impact on the organisation. This aligns with the **Detection and Analysis** phase of NIST SP 800-61.

### Four-step analysis guide
1. **Data review**: analyse logs, alerts, system data (SIEM dashboard); understand attacker activity.
2. **Root cause identification (RCA)**: how it started (phishing, malware, vulnerability exploit); find the entry point and method.
3. **Impact analysis**: affected systems/data; business and operational impact (data at risk, downtime, financial impact).
4. **Correlate data sources**: SIEM alerts + system logs + firewall logs + user activity → full incident timeline.

**RCA = Root Cause Analysis.** Fix the cause, not just the symptom, otherwise the incident recurs.

---

## 5. NIST SP 800-61r3 (April 2025)

- Supersedes SP 800-61r2 (2012). Cite **Rev. 3** (the older 4-phase model of Preparation → Detection and Analysis → Containment, Eradication and Recovery → Post-Incident Activity is Rev. 2).
- r3 aligns incident response with **NIST CSF 2.0 functions**: **Govern, Identify, Protect** (preparation) and **Detect, Respond, Recover** (incident response), with **Improvement / lessons learned** feeding back from every activity.
- Covers roles and responsibilities (leadership, incident handlers, technical staff, legal, HR, and others who are all stakeholders) and incident categorisation by impact (high / medium / low).
- Useful as an assessment **reference** (the teacher explicitly said it may be cited).

---

## 6. Reporting Incident Outcomes and Findings

### Standard report structure
1. **Incident Summary**: quick overview of what happened
2. **Timeline**: step-by-step sequence of events (log timestamps)
3. **Root Cause Analysis**: how and why it occurred (phishing, vulnerability, malware, ransomware…)
4. **Actions Taken**: what was done to contain and fix it (e.g. blocked IP, patched vulnerability), with evidence (logs, alerts, screenshots)
5. **Impact Assessment**: business and technical impact (downtime, data loss, risk)
6. **Recommendations**: what to improve to prevent future incidents

### What to document
Timeline of events, affected systems, actions taken, evidence collected (SIEM alerts, firewall logs, **screenshots**, analyst notes).

### "If it wasn't documented, it didn't happen"
Timestamp every action, record tools used, keep clear notes, create proof for review. **No documentation = no proof = didn't happen.** Good documentation protects the organisation during audits, investigations, legal review and lessons-learned reviews, and supports handover and further improvement.

### Communicating findings: know your audience
| Audience | Needs |
|---|---|
| **Technical teams** | Logs, IOCs (indicators of compromise), attack methods, technical steps |
| **Management** | Business impact, risk level, operational disruption |
| **Executives** | High-level summary, key decisions, strategic impact (no command-line output) |

Communication should be **clear, concise and action-focused**. A good incident report is a **decision-making tool**: improves response strategies, strengthens controls, prevents future incidents.

---

## 7. Hands-on Activities (Brightspace)

1. **SOC Mission: Alert to Action**: scenario: SIEM alert shows *multiple failed logins → successful login → malware process detected* on a user device. Assign IRT roles (**Team Lead, Log Analyst, Containment Officer, Reporter**), identify the affected system (User Device/Laptop), choose two containment actions (isolate device, disable account, block attacker IP; *not* "ignore the alert" or "shut down everything"), then explain the response in writing.
2. **"If it wasn't documented, it didn't happen"**: compare actions with vs without documentation.
3. **Report Incident Outcomes and Findings**: Document details → Structure reports → Communicate findings.
4. **Evaluate effectiveness flip cards** with a reflection question.

### Wazuh lab access
- Connect **SoftEther VPN** (required when off campus), open `https://10.12.237.42`, log in with a provided read-only account (`user1`–`user10`; credentials in the Wazuh User Guide on Brightspace).
- Dashboard shows agents summary (active/disconnected) and last-24h alerts by severity (e.g. Critical 0, High 100, Medium 873, Low ~15,000).
- **Discover** view: search/filter raw alerts by `agent.id`, `agent.ip`, `rule.level` (e.g. `rule.level=10`; level ≥ 12 reduces hits to ~125), absolute or relative time ranges, expandable events with timestamp/IP/agent details.
- **Threat Hunting** dashboard: totals, level-12+ alerts, authentication failures/successes, alert-level evolution over time, MITRE ATT&CK.
- TSOC remote access portal (Heimdall): `http://10.12.239.215:8080` with **BLUE** and **PURPLE** environments.
- Practical analysis of Wazuh continues next week.

---

## 8. Assessment Task 2 – Part B: IRP Requirements

Your Incident Response Plan must include:
1. IRT structure and membership
2. Roles and responsibilities
3. Business impact of the cyber incident (operational disruption, financial loss, legal/regulatory consequences, reputational damage; explain why a coordinated IRT response is critical)
4. Communication and escalation procedures
5. Detailed response actions for the chosen incident
6. Evidence collection and preservation steps
7. Reporting, documentation and notification requirements
8. Post-incident review actions and improvements

Teacher's guidance: the IRP template is only a **guideline**; meet the **requirements** rather than copying the template exactly; the appendices do not all need to be filled (Appendix C is the useful one). Check for gaps. Screenshots/snapshots of tools (e.g. Wazuh) are expected as evidence.

---

## 9. Key Terms Glossary

| Term | Meaning |
|---|---|
| Blue team / Red team | Defensive / offensive security teams |
| SOC | Security Operations Centre |
| SIEM | Security Information and Event Management |
| IRT / IRP | Incident Response Team / Plan |
| IOC | Indicator of Compromise |
| EDR | Endpoint Detection and Response |
| RCA | Root Cause Analysis |
| Containment / Mitigation | Stop spread / fix the cause |
| Order of volatility | Collect the most short-lived evidence first |
| Chain of custody | Documented who/when/where/why history of evidence |
| Write-blocker | Prevents writes to original evidence |
| Forensic image | Bit-by-bit copy of storage |
| Hash | Fixed-length fingerprint used to verify integrity |
| ROE | Rules of Engagement (red team scope) |
| RBAC / LDAP | Role-based access control / directory authentication used by Wazuh |
