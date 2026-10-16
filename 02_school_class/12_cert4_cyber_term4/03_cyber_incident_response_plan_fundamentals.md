# Cyber Incident Response Plan (CIRP) Fundamentals

> **Unit:** VU23219 Manage the security infrastructure for an organisation / VU23221 Evaluate and test an incident response plan
> **Type:** Self-study notes (based on a Victorian Government-style CIRP template, which itself draws on NIST SP 800-61)
> **Date:** 16 Oct 2026

---

## 1. What Is a Cyber Incident Response Plan?

A **Cyber Incident Response Plan (CIRP)** documents *how an organisation prepares for, detects, responds to and recovers from* cyber incidents, so that response is organised, fast and repeatable instead of improvised.

**Goals**

- Reduce the **scope, impact and severity** of incidents
- Protect sensitive data (customer, payment, personal information)
- Maintain business operations and stakeholder trust
- Coordinate people, roles and communications during a crisis

**Standard sections of a CIRP**

| Section | Purpose |
|---|---|
| 1. Introduction | Context, purpose, authority (who owns/approves the plan), review cycle |
| 2. Terminology | Defines "cyber event" and "cyber incident" |
| 3. Common incidents and responses | Incident types, initial response, threat vectors |
| 4. Roles and responsibilities | Incident Management Team (IMT) and Senior Executive Management Team (SEMT) |
| 5. Incident response process | Step-by-step process, classification, notifications, evidence, communications |
| Appendices | Reusable templates (situation update, incident log, action plan, evidence register, assets/contacts) |

**Reference frameworks**

- **NIST SP 800-61** (*Computer Security Incident Handling Guide*): lifecycle of *Preparation → Detection & Analysis → Containment, Eradication & Recovery → Post-Incident Activity*.
- Many government templates restate this as five operational steps (see Section 7 below).

**Plan governance**

- Owned and maintained by a nominated security lead (in a small organisation, a senior staff member working with the external IT provider).
- Endorsed by the CEO / top executive, who is accountable for a dependable, secure ICT environment.
- **Reviewed at least annually, after any incident, and after major system changes.** Lessons learned feed back into the plan.

---

## 2. Terminology: Cyber Event vs Cyber Incident

**Cyber security** protects information and supporting systems from internal and external threats, focusing on the **CIA triad**:

- **Confidentiality**: only authorised parties can access information
- **Integrity**: information is accurate and not tampered with
- **Availability**: systems and data are accessible when needed

| Term | Definition | Key point |
|---|---|---|
| **Cyber event** | Any *observable occurrence* in a system or network | Does **not** necessarily cause harm; most events are normal activity, but some need investigation |
| **Cyber incident** | An event that has **harmed, or is likely to harm**, the confidentiality, integrity or availability of information or systems | Confirmed or highly probable impact |

**Examples of cyber events**

- Multiple failed sequential logons on one account in a short time
- Logins from an unusual country/IP address
- Antivirus disabled on a device
- System files modified/deleted, unexpected server restart
- An unapproved device or account attempting access

**Examples of cyber incidents**

- Denial-of-service (DoS) taking a service offline
- Malware or ransomware infection
- Compromise or disclosure of sensitive/personal information
- Compromise of network credentials or an email account
- A successful unauthorised login

**Event → incident escalation (example)**

> Repeated failed logins on one account = **event**. The moment an attacker **logs in successfully** = **incident**.

---

## 3. Common Incident Types and Initial Responses

| Type | Description | Typical initial response |
|---|---|---|
| **Ransomware** | Encrypts/locks data until a ransom is paid | Immediately remove infected devices from the network; capture logs; isolate devices while containment/eradication is planned |
| **Malware infection** | Virus, worm, Trojan or other malicious code on a host | Disconnect infected devices; capture logs; isolate; confirm containment, then eradicate |
| **DoS / DDoS** | Overwhelms a network/service with traffic | Ask gateway/ISP provider to identify the attack type and vector; apply filters at the network edge and/or increase capacity |
| **Phishing / social engineering** | Deceptive messages to obtain credentials/sensitive data | Review web and email logs; ask users what they clicked/provided; reset passwords; monitor accounts for unauthorised access |
| **Data breach** | Unauthorised access to sensitive or personally identifiable information | Contain the loss quickly; alert privacy, legal and communications teams; investigate the cause |
| **Brute force login attack** (added for a specific scenario) | Automated, repeated guessing of credentials | Lock the account after a failed-attempt threshold; review authentication logs for source IPs and patterns; block or rate-limit offending IPs at firewall/WAF; notify the user and force a password reset |

---

## 4. Potential Threat Vectors

A **threat vector** is the *route* by which an incident can arise. Knowing the vectors helps find "weak spots". NIST SP 800-61 groups common attack vectors as:

| Vector | Description / example |
|---|---|
| **External / removable media** | Attack launched from a malicious USB drive |
| **Attrition** | Brute-force-style attacks against systems or services, e.g. **DDoS**, or **password-guessing attacks against logins** |
| **Web** | Redirection to a malicious URL that installs malware |
| **Email** | Phishing that steals information or delivers malware |
| **Impersonation** | Look-alike domains/identities used to deceive victims (often tied to phishing) |
| **Improper usage** | Human error breaching policy (e.g. weak passwords, misconfiguration) or a malicious insider |
| *Loss or theft of equipment* | Lost laptop, phone or media (listed separately in NIST) |
| *Other* | Anything that fits none of the above |

> Note: the exact wording of the NIST categories should be verified against the original document before being cited.

---

## 5. Brute Force Attacks (Worked Example)

**Brute force attack:** an attacker systematically tries many username/password combinations until one works.

**MITRE ATT&CK technique T1110: Brute Force** and its sub-techniques:

| ID | Sub-technique | How it works |
|---|---|---|
| T1110.001 | **Password guessing** | Tries many passwords against a known account |
| T1110.002 | **Password cracking** | Recovers passwords offline from stolen hashes |
| T1110.003 | **Password spraying** | Tries one or a few common passwords across *many* accounts (avoids lockouts) |
| T1110.004 | **Credential stuffing** | Reuses username/password pairs leaked from other breaches |

**Indicators (detection)**

- Many failed logins on the same account in a short time
- One IP failing against many accounts (spraying)
- Logins from unfamiliar countries/IPs; unusual hours
- Account lockouts reported by staff or customers
- A successful login immediately after a long run of failures (**possible compromise**)

**Prevention / mitigation**

- Strong password policy (minimum length, complexity, no reuse) and **multi-factor authentication (MFA)**
- **Account lockout / throttling** after repeated failures
- **Rate limiting** and blocking of abusive IPs; **WAF** protection
- CAPTCHA on public login pages
- Central **logging and alerting** (e.g. SIEM) for authentication failures
- Staff awareness and training; clear access-control policy

**Response**

Contain (lock account, block IP) → analyse logs (did any login succeed? what was accessed?) → reset credentials → check for further compromise → record evidence → review and improve controls.

---

## 6. Roles and Responsibilities

### 6.1 Incident Management Team (IMT)

The **IMT** is the team responsible for *managing the response* to a cyber incident. Roles are suggested and scaled to organisation size (**one person may hold several roles; `*` roles are optional and activated only if needed**).

| IMT role | Responsibilities |
|---|---|
| **Incident manager** (e.g. IT security manager) | Leads the response; planning and operations; intelligence and analysis; technical advice; advises when to stand down |
| **Organisation security manager** | Investigation, particularly if an **internal threat** is suspected; law-enforcement liaison |
| **Business continuity advisor*** | Facilities support; analysing and managing business/community consequences |
| **Communications, engagement and media advisor*** | Information and warnings; internal communications; media and community liaison |
| **Legal advisor*** | Legal advice including regulatory compliance |
| **Finance and procurement advisor*** | Facilities and finance support |
| **Administration and record keeping*** | Maintains the incident log, evidence register and situation reports |
| **System/application lead contact** | Support for specific systems; third-party vendor contacts |
| **External support** | Government cyber incident response service, national CERT (e.g. AusCERT) for technical advice, analysis, containment, eradication and recovery |

### 6.2 Senior Executive Management Team (SEMT)

- Formed for **more serious incidents**, at the request of the Incident Manager or at the CEO's discretion.
- Provides **strategic oversight, direction and support** to the IMT, focusing on:
  - Strategic issues
  - Stakeholder engagement and communications
  - Resource and capability demands (urgent logistics, finance, HR)
- If a SEMT cannot form, **someone must hold delegated authority** to make critical decisions.

| SEMT role | Function |
|---|---|
| CEO | SEMT chair |
| CIO | Deputy chair |
| CISO | Deputy |
| Finance / procurement | Emergency procurement and spending oversight |
| Legal | Regulatory compliance; cyber insurance |
| Communications | Public relations and stakeholder engagement |
| People and culture | Staff welfare |

**IMT vs SEMT:** the IMT *handles the incident* (operational); the SEMT *directs and supports at strategic level*.

---

## 7. The Incident Response Process

### 7.1 Quick reference checklist

1. Analyse whether an incident has occurred / is occurring
2. Determine **scope, impact and severity**; categorise it
3. **Activate the IMT** (and SEMT if appropriate); start documenting
4. Develop and implement a **Resolution Action Plan** (containment, eradication, recovery); gather and record evidence
5. Identify affected **stakeholders**
6. Develop a **notifications strategy**; communicate key messages
7. Confirm the threat is **eradicated**; restore and test systems
8. **Stand down** the IMT/SEMT when authorised; decide any final communications
9. Hold a **post-incident review**; document lessons learned
10. **Update the plan** with those lessons

### 7.2 The five steps

| Step | Contents |
|---|---|
| **1. Detection and analysis** | Detection, analysis, classification, IMT activation, notifications, documentation |
| **2. Containment and eradication** | Resolution Action Plan, evidence preservation |
| **3. Communications and engagement** | Internal and external communications |
| **4. Recover** | Restore systems, monitor, remediate vulnerabilities |
| **5. Learn and improve** | Stand down, post-incident review, update the plan |

### 7.3 Incident detection

Detection has no single process. Sources include:

- **Precursors**: signs an attack *might* occur (e.g. a threatening email, news of a global ransomware campaign). Rare.
- **Indicators**: signs an incident *may have occurred* (IDS alerts, odd file names, configuration changes).
- **Security monitoring**: referral from a managed security provider or another organisation.

**Common indicators**

| Indicator | Examples |
|---|---|
| Suspicious reports | Phishing emails received; many staff locked out; external parties reporting spam from you |
| System not behaving as expected | Services down without a planned reason; broken SSL certificate |
| Unusual activity | Bounced emails; traffic spikes; **multiple failed logins from unfamiliar/overseas systems**; antivirus alerts; admin accounts changing permissions; unusual file names |

### 7.4 Incident analysis

Confirm whether an incident is real. Useful actions:

- Make sure you have **up-to-date resources**: network diagrams, IP schemas, port lists, system documentation
- **Review logs and security alerts** for unusual entries
- Use **Standard Operating Procedures (SOPs)** per operating system (Windows, Linux/Unix)
- **Consult network/application experts**: is there a legitimate explanation?
- **Research** open-source information on unusual indicators
- Keep a **watch/monitor list** of suspected accounts or IPs
- **Important:** do **not** ping or contact a suspected malicious IP/URL from your own network; it may tip off the attacker. Have a third party do it securely and anonymously.
- **Timing:** keep the initial analysis to roughly **one hour** before seeking outside help. Over-long analysis can delay response.

### 7.5 Incident classification

Incidents are categorised by impact so the right escalation and notification occurs. A government-style scale:

| Category | Business impact level | Meaning | Escalate when |
|---|---|---|---|
| **Cyber event** | Level 0 | Suspected/unconfirmed, no impact | Alerts increase substantially, or continued alerts could breach controls |
| **Cyber incident** | Level 1 | Successful compromise of security controls; minor impact | Likely limited/major service impact, multiple organisations affected, or a data breach |
| **Significant cyber incident** | Levels 2-3 | Compromise with limited/major impact (or involving critical infrastructure, multiple organisations or a data breach) | Potential for loss of life/major damage, or significant community impact |
| **Cyber emergency** | Levels 4-5 | Serious/exceptional compromise; threat to life, property, infrastructure or community | Immediate notification and emergency management arrangements |

> The impact levels and notification contacts above come from a Victorian Government template. A private organisation would adapt the wording, thresholds and who must be notified.

### 7.6 IMT activation and notifications

- Activate the IMT when an incident is **confirmed and needs a coordinated response** (small incidents may not need activation).
- The IMT works from a dedicated **operations room** (with after-hours access arrangements).
- **Notify stakeholders** proportionate to scope, impact and severity: government cyber response service, senior executives, regulators/relevant agencies, police (e.g. ReportCyber), and the **cyber insurance provider**.
- The **Incident Manager or communications lead** manages notifications.

### 7.7 IMT documentation

Start documenting **immediately** when the IMT forms.

**Situation update** (issued regularly to stakeholders; proactive updates reduce ad-hoc questions):

- Date/time of the incident (usually when confirmed)
- Status (new / in progress / resolved)
- Type and classification
- **Scope** (affected networks/systems/applications)
- **Impact** (who is affected and how)
- **Severity** (business services impacted)
- Contact details for the incident manager and key IMT members

**Incident log** (kept by an IMT member or delegate):

- Minutes of every IMT meeting
- All **critical decisions with the rationale**
- Actions taken, action items, next meeting times
- Every entry records **date, time and author**

### 7.8 Resolution Action Plan

The plan for resolving the incident; reviewed continuously as new evidence arrives. Key elements:

- **Containment actions**: stop the incident/threat spreading
- **Eradication actions**: remove the threat from the environment
- **Capability and capacity requirements**: people, tools, resources needed
- **Communications actions**: what, to whom, when and how

Consider: how long resolution will take, resources needed, and which systems/services will be affected during resolution.

### 7.9 Evidence preservation

Evidence supports forensic investigation and law-enforcement action.

**Types of evidence**

- Disk and RAM images
- IP addresses
- Network packet captures and flows
- Network diagrams
- Logs and configuration files
- Databases
- Investigation notes and screenshots
- Social media posts
- CCTV/audio/video
- Documents showing the **cost of remediation or lost business**

**Chain of custody practices**

- **Nominate one IMT member** to collate, record and store all evidence
- Maintain an **evidence log** (date/time, collector, description of each item)
- Store securely; **limit access**
- Record **every access**, with the reason
- **Minimise transfers** between people, and record any transfer

### 7.10 Communications

| | Internal communications | External communications |
|---|---|---|
| **Audience** | Employees | Customers, media, public, ministers/regulators |
| **Key messages** | What happened and why; what happens next; what staff must do; who to contact | What happened and why; which systems are affected; what is being done; expected resolution time; what stakeholders should do; who to contact |
| **Approval** | Communications lead **and** Incident Manager | Communications lead **and** Incident Manager (SEMT chair if the SEMT is active) |

### 7.11 Recover

Develop a **recovery plan** after containment and eradication, with business-continuity and IT-service input:

- Restore systems to normal operation
- **Continually monitor** to confirm they function normally
- **Remediate vulnerabilities** to prevent a repeat

Recovery may have to wait until any related **forensic/criminal investigation** is complete.

### 7.12 Stand down

- The **Incident Manager** advises the IMT it may stand down once the recovery plan is executed.
- If the SEMT is active, only the **SEMT chair (or deputy)** issues the stand-down instruction, after consulting the Incident Manager.
- The Incident Manager gathers all notes for the post-incident review.

### 7.13 Learn and improve

Often the **most overlooked but most important** step. A **post-incident review** asks:

- What exactly happened, and when?
- How well did staff and management perform? Were procedures followed and adequate?
- What information was needed sooner?
- Did any action hinder recovery?
- What would we do differently next time?
- How could information sharing with others improve?
- What corrective actions prevent recurrence?
- Which **precursors/indicators** should we watch for?
- What extra tools or resources are needed?

Document the outcomes, share the lessons, and record recommendations in an **action plan** (what, who, when). Then **update the CIRP**.

---

## 8. Appendix Templates

| Appendix | Purpose |
|---|---|
| **A. Situation update** | Regular status report for stakeholders |
| **B. Incident log** | Chronological record of meetings, decisions, actions |
| **C. Resolution action plan** | Containment, eradication, recovery actions with owners |
| **D. Evidence register** | Chain-of-custody log for collected evidence |
| **E. Assets and key contacts** | Critical assets and who to contact |

---

## 9. Key Takeaways

- A CIRP turns incident response from **improvisation** into a **repeatable process** with named roles.
- An **event** is any observable occurrence; an **incident** is an event that harms (or is likely to harm) **C, I or A**.
- Brute force belongs to the **Attrition** vector; the usual defences are **MFA, lockout/rate limiting, strong passwords, logging and alerting**.
- The **IMT handles the incident**; the **SEMT** gives strategic direction for serious incidents.
- Follow the five steps: **detect and analyse → contain and eradicate → communicate → recover → learn and improve**.
- **Document everything**: situation updates, incident log, and a chain-of-custody evidence register.
- The **post-incident review** is where the organisation actually gets better.

## 10. Key Terms

**CIRP** · **Cyber event** · **Cyber incident** · **CIA triad** · **Threat vector** · **Attrition** · **Brute force (T1110)** · **Password spraying** · **Credential stuffing** · **MFA** · **WAF** · **IMT** · **SEMT** · **Incident manager** · **Situation update** · **Incident log** · **Resolution Action Plan** · **Evidence register** · **Chain of custody** · **Containment** · **Eradication** · **Recovery** · **Stand down** · **Post-incident review** · **Precursor / indicator**
