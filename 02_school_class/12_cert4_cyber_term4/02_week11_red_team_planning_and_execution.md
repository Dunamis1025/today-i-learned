# Week 11 – Red Team Planning and Execution

> **Unit:** VU23219 Manage the security infrastructure for an organisation / VU23221 Evaluate and test an incident response plan
> **Session 11, Topic 11:** Red Team Planning and Execution
> **Date:** 13 Oct 2026

---

## 1. Learning Objectives

- Define red teaming in incident response
- Develop red team scope and Rules of Engagement (ROE)
- Perform threat modelling and target selection
- Select appropriate attack vectors
- Apply risk assessment and safety controls
- Use basic penetration testing tools
- Develop a Red Team Test Plan (RTTP)

**Prerequisite knowledge:** Red / Blue / Purple team roles, cyber kill chain (7 stages), risk assessment, cyber hygiene, threat actors and threat vectors.

---

## 2. What Is Red Teaming in Incident Response?

- A **controlled, simulated cyber attack** carried out by a group (a team, not one person) following a defined method and process.
- It mimics **real attacker behaviour across the whole attack lifecycle** (the 7-stage Cyber Kill Chain), going beyond a basic vulnerability test. It is essentially ethical "critical hacking" against the organisation's network, run in a simulated environment.
- Red teams reproduce attackers' **TTPs** (tactics, techniques, procedures).

**Purpose – test how well the organisation can:**

| Capability | Question answered |
|---|---|
| **Detect** | Are threats detected, alerts triggered, logs monitored? |
| **Respond** | Does the team follow the Incident Response Plan (IRP) and escalation paths? |
| **Recover** | Can systems be restored quickly? Are backups reliable? |

**Key idea:** Hygiene and controls *prevent* attacks, risk assessment *identifies* risk, red teaming *validates* that defences and response actually work. Controls that exist "on paper" must be proven to work in practice. Attacks are a matter of **when, not if**.

---

## 3. Why Organisations Use Red Teaming

1. **Validate detection** – alerts fire correctly, logs are monitored effectively.
   - **False positive:** alert with no real attack.
   - **False negative:** real attack with no alert (more dangerous).
   - Also confirm log information is stored correctly.
2. **Test response** – teams follow the IRP; roles are split (team lead, analyst, communications, recovery); escalation to stakeholders works.
3. **Evaluate recovery** – speed of restoring normal operations, backup reliability, compliance mechanisms.
4. **Find gaps** in detection, response and recovery.
5. **Improve overall incident response readiness.**

### Alignment with organisational security goals

- **Improve security posture:** find weaknesses *before attackers do*; strengthen systems, processes **and people** (administrative controls, staff awareness/training).
- **Discover real-world gaps:** monitoring tools (IPS, IDS, SIEM), employee awareness, IRP and risk.
- **Support compliance and frameworks:** NIST, ISO require control testing, continuous improvement and incident readiness.
- **Strengthen resilience:** prepare for real attacks, reduce impact, recover faster.

Red teaming is not only technical; it checks security policy compliance and supports business goals.

---

## 4. Step 1 – Scope and Rules of Engagement (ROE)

**Before any testing:** define the **scope** and obtain **formal sign-off/approval** from the organisation. Testing outside the approved scope is illegal and unethical, and must not "escape into the wild".

**ROE** = a formal, usually **legally binding** written agreement between the organisation and the red team, so management, IT and red team operators share the same understanding. It protects all parties.

### Six core elements

| # | Element | Example |
|---|---|---|
| 1 | **Objectives & success criteria** | Detect a phishing attack within 10 minutes |
| 2 | **Scope & boundaries** | In: staff email, Active Directory. Out: patient records, critical OT systems, payment systems |
| 3 | **Permitted activities** | Phishing, social engineering, vulnerability testing |
| 4 | **Restrictions** | No encrypting real data; no attacks on critical infrastructure |
| 5 | **Legal approval & communication** | Formal approval before testing, defined communication channels, escalation procedure |
| 6 | **Legal bindingness** | Document protects all parties |

### Ethics in red teaming

Red teaming accesses systems, tests vulnerabilities and interacts with users, so without controls it can cross legal/ethical lines. Ethical testing is:

- **Approved and transparent**
- **Harmless** to systems, people and data
- **Respectful of privacy and organisational policy**

**Approval is the key ethical control** because the organisation (a) knows about the test, (b) reviews risk before execution, and (c) has clear boundaries. Missing any one makes the test potentially unethical.

---

## 5. Step 2 – Threat Modelling and Target Selection

**Threat modelling** = identify likely attackers, understand how they would attack, and determine which assets are most at risk. It helps to:

- Identify likely attackers (threat actors) and **profile** them
- Understand attack methods and pathways
- Recognise system vulnerabilities
- **Prioritise** security effort by risk

### Five key steps

| # | Step | Details |
|---|---|---|
| 1 | **Identify critical assets** | Sensitive data (financial, personal), business-critical systems, user accounts (esp. admin) |
| 2 | **Understand threat actors** | Cybercriminals (financial gain), insider threats (employees), nation-state attackers; individuals or groups; motivation |
| 3 | **Analyse attack surface** | Entry points: web applications/servers, remote access (VPN, RDP), email systems, human users (phishing targets) |
| 4 | **Identify attack paths** | e.g. phishing → stolen credentials → system access; exploit vulnerability → gain control → escalate privileges |
| 5 | **Prioritise risks** | Likelihood × impact, plus organisation's ability to respond → risk level |

---

## 6. Step 3 – Select Appropriate Attack Vectors

**Attack vector:** the path or method an attacker uses to gain unauthorised access to systems, networks or data. In red team activities these are **simulated** to test detection and response to real-world threats.

| Vector | Description |
|---|---|
| **Social engineering** | Manipulating people's psychology to gain access |
| **Phishing** | Fake emails to steal credentials |
| **Vulnerability exploitation** | Targeting unpatched systems |
| **Physical access attempts** | Gaining entry to facilities |
| **Supply chain attacks** | Exploiting third-party weaknesses |

---

## 7. Step 4 – Use Basic Penetration Testing Tools

Typical setup: **one attacking machine and one target machine**.

**Kali Linux**
- Specialised OS with a wide range of pre-installed security/penetration-testing tools
- Supports network scanning, vulnerability analysis and exploitation
- Includes **Nmap, Wireshark, Burp Suite** and more in one platform
- **Role:** the main environment where testing activities are performed

**Metasploit**
- Framework to test and exploit known vulnerabilities
- Identifies security weaknesses; uses pre-built exploit code to simulate real attacks
- Lets testers validate whether vulnerabilities can actually be exploited
- **Role:** demonstrates the real impact of vulnerabilities

**Other:** Burp Suite (web application security testing).

---

## 8. Step 5 – Develop a Red Team Test Plan (RTTP)

**RTTP** = the central document that defines how a simulated attack will be conducted. It acts as a **blueprint for execution**, guiding all stakeholders (red team, control team, management).

- Outlines **attack scenarios, techniques, timelines and controls**, keeping the test realistic yet controlled
- Clearly defines **target systems** and **"flags" (success conditions)**
- **Plan before you start.**

### RTTP structure (4 parts)

**1. Objectives and scope**
- Objectives: detect phishing attacks, identify credential compromise, detect lateral movement
- In scope: email systems, Active Directory, users and processes
- Out of scope: payment systems, life-critical OT systems
- Example: *Objective:* detect credential compromise · *Scope:* email + Active Directory · *Out of scope:* payment systems

**2. Timeline and phases**

| Phase | Activities |
|---|---|
| 1. Preparation | Planning, approvals, environment setup |
| 2. Threat intelligence | Identify realistic attack scenarios, map attacker behaviour |
| 3. Red team execution | Simulated attacks conducted, real-world techniques applied |
| 4. Closure | Reporting findings, remediation actions (Blue team also involved) |

Example timeline: **Week 1–2** planning & approvals · **Week 3–5** attack execution · **Week 6** reporting.

**3. Tools and techniques**
- Tools: Kali Linux, Metasploit, Burp Suite
- Techniques aligned with real attackers: phishing campaigns, social engineering, vulnerability exploitation, privilege escalation

**4. Risk controls and approvals**
- **Rollback plan:** restore systems if disruption occurs
- **Kill switch:** immediately stop testing if risks escalate
- **Escalation procedures:** defined emergency contacts and communication
- **Legal & management approval:** formal authorisation before testing begins

---

## 9. Summary – The Red Team Workflow

```
Red teaming tests incident response by simulating real-world attacks
   ↓
Define scope and Rules of Engagement (legal approval)
   ↓
Identify targets via threat modelling; select appropriate attack vectors
   ↓
Apply risk controls; use tools such as Kali Linux and Metasploit
   ↓
Create a structured Red Team Test Plan for controlled, measurable testing
```

---

## 10. Red / Blue / Purple Teams (applied exercise context)

| Team | Role |
|---|---|
| **Red** | Simulates threats by identifying vulnerabilities and attempting controlled exploitation |
| **Blue** | Monitors, detects and responds; investigates alerts, contains threats, strengthens defences |
| **Purple** | Evaluates both teams; facilitates collaboration, analyses the attack lifecycle, assesses response effectiveness, recommends improvements using the IRP |

**Exercise environment options**
- **Option 1 – Virtual simulation:** VirtualBox/VMware, vulnerable target (e.g. Metasploitable), Kali/Nmap (Red), Snort/Tripwire (Blue), WebEx (Purple collaboration).
- **Option 2 – Industry-aligned SOC (recommended):** Wazuh SIEM (log collection, monitoring, detection), Cydarm IR platform (ticketing, case management, evidence), firewall tools.

**Workflows**
- *Red:* scan target → exploit vulnerability → present findings to Blue/Purple.
- *Blue:* detect alerts → investigate and validate (scope, impact, affected systems) → contain/mitigate and document → report to Purple.
- *Purple:* observe and coordinate; correlate SIEM and firewall data; review response quality; recommend IRP improvements.

**Report structure:** team composition → introduction (objectives, scope, timeline) → Red team attack (methodology, threat scenarios, TTPs, breach points) → Blue team response (alert/triage, detection, containment, eradication, recovery, findings) → Purple analysis (gap analysis across people/process/technology, lessons learned, recommendations, security policy awareness & cyber hygiene) → conclusion → appendix. Insert screenshots wherever possible.

---

## 11. Key Takeaways

- Red teaming = **ethical, authorised, scoped** simulation of real attacker behaviour.
- **ROE + sign-off come first**; they are the main ethical and legal safeguard.
- Threat modelling (assets → actors → attack surface → paths → risk priority) drives target and vector selection.
- Kali Linux is the environment; Metasploit proves real impact.
- The **RTTP** ties everything together: objectives/scope, phases/timeline, tools/techniques, risk controls/approvals.
- Success is measured by the organisation's ability to **detect, respond and recover**.

## 12. Key Terms

**Red team** · **Blue team** · **Purple team** · **ROE** · **RTTP** · **Threat modelling** · **Threat actor** · **Attack surface** · **Attack path** · **Attack vector** · **TTP** · **Cyber Kill Chain** · **Kali Linux** · **Metasploit** · **SIEM** · **IRP** · **False positive / negative** · **Kill switch** · **Rollback plan** · **Flags (success conditions)**
