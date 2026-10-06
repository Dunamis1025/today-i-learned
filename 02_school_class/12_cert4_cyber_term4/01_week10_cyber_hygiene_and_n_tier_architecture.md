# Session 10 – Implementing Cyber Hygiene Best Practices & Processes

- **Unit:** VU23219 – Manage Security Infrastructure (Term 4, Week 1 of the term block)
- **Date:** 6 October 2026 (Tuesday, 1:30 pm class)
- **Topic:** Topic 10 – Cyber hygiene tasks, prioritisation, workflows, automation, monitoring
- **Hands-on:** n-tier architecture walkthrough, ELK (Kibana) log search, Sprint 2 FTP misconfiguration guided exercise

---

## 1. Big Picture

Cyber hygiene is **not a one-off activity**. It is a continuous, operational cycle that sits inside the security lifecycle:

**Identify → Protect → Detect → Respond → (repeat)**

- Regular updates reduce known vulnerabilities.
- Strong access control prevents unauthorised use.
- Continuous monitoring enables fast detection and response.
- Ignoring hygiene leads to unmanaged systems, weak controls, breaches, ransomware and data loss.

> Key sentence from the slides: *Cyber hygiene is not about **knowing** security; it is about **consistently doing** the right tasks at the right time.*

### Why is "Identify" the first step?

- You cannot protect or respond to what you do not know exists.
- Analogy: a doctor cannot treat an undiagnosed illness; surgery needs a diagnosis first.
- Flow: **identify threats/vulnerabilities → risk assessment → appropriate controls → incident response plan (IRP)**.
- Identification covers assets, architecture, threats and vulnerabilities. This links directly to the IRP and to Assessment 2.

---

## 2. Understanding Infrastructure: n-tier Architecture

To identify threats you must first understand how the system is built. The subject is *security infrastructure*, so network/security architecture must always be understood. "n-tier" (multi-tier) architecture is a common interview topic.

### 2.1 The three tiers

| Tier | Role | Examples from the diagram |
|---|---|---|
| **Presentation tier (Tier 1)** | What users interact with; the client-facing side | Public users, supplier LAN, DMZ with web servers between firewalls |
| **Business logic tier (Tier 2)** | Application/business processing in the service data centre | Web/app servers behind a switch on the data-centre LAN |
| **Data tier (Tier 3)** | Persistent data storage | Database servers on the DB data-centre LAN |

"n" simply means there can be many servers/tiers, not just three.

### 2.2 Request flow (online banking example)

1. User on a phone/laptop (café, truck, anywhere) sends a request.
2. Request passes the **firewall** into the **DMZ web servers** (Presentation tier).
3. A **switch** connects the LAN to the data-centre servers.
4. **Web/application servers** (Business Logic tier) process the request in code.
5. The application queries the **database** (Data tier) through an API (JDBC/ODBC).
6. Results travel back up the chain to the user. Every step is logged.

The user only ever sees the **front end (GUI)**; everything else happens behind it.

### 2.3 Key concepts

- **Web server = software**, not hardware. Examples: **Apache** (free), **Microsoft IIS** (paid). It runs at the **application layer** (OSI Layer 7) and processes requests and sets up connections to the back-end database.
- **Without web servers nobody can access the internet-based service.** Cloud (e.g. AWS) is built on top of the internet and still depends on servers; no provider can guarantee 100% security.
- **API (Application Programming Interface):** a bridge that lets different software (web server ↔ database, written in different languages) talk to each other. It is a tool used by web servers, not the same thing as a web server.
  - **JDBC** (Java Database Connectivity) and **ODBC** (Open Database Connectivity) are database-connection APIs; different names, same purpose.
- **Database types** differ mostly in syntax; the purpose (store and retrieve data) is the same. Online banking, shopping and email all use this same structure.
- **Router** = gateway, works at **OSI Layer 3 (Network layer)**.
- **Switch** connects devices within a LAN.
- **Application server vs web server:** the web server handles/forwards requests (simple role); the application server executes the business logic (e.g. a bank app processing a balance check or bill payment).

### 2.4 Redundancy, load balancing and DDoS

- Two web servers (and two on each tier) exist for:
  - **Redundancy/backup:** if one fails, the other takes over automatically (fault tolerance).
  - **Load balancing:** requests are distributed across servers. Banks have millions of users and large platforms have billions; one server is not enough.
- **Load balancer analogy:** a supermarket staff member directing customers to open checkouts. It sends traffic to healthy, available servers and removes failed ones.
- Each server has a processing limit (e.g. 5,000 requests/second). Beyond that it goes down. Attackers exploit this with **DDoS (Distributed Denial of Service)**: many machines flood the server with requests.
- Two servers at 5,000 req/s each with load balancing can handle roughly 10,000 req/s.

### 2.5 Security implications

- If an attacker passes the web server/firewall/DMZ they reach the **internal LAN**, then the application servers and the database (where the data lives). This is the "disaster" scenario and a cyber-security failure.
- Defence in depth: **firewalls, IDS, IPS** and other devices make this hard; each tier needs its own protection and vulnerability checks.
- Understanding the structure shows **where assets are, where firewalls/DMZ sit, and where data lives** – the basis of the Identify step.

---

## 3. Recap from Week 9: Security Awareness and Culture

- Awareness programs train staff (e.g. do not click phishing links that download malware).
- Benefits: **accurate incident reporting**, **response readiness**, **improvement** of security activities.
- **Culture** here means *organisational security culture*, i.e. employee habits:
  - Lock the screen when leaving the desk.
  - Log off / shut down at the end of the day.
  - Do not click phishing links.
- Tools alone do not make an organisation safe; habits must become culture.

### Why policies must keep being updated

1. **People change** (new joiners/leavers need current rules).
2. **Incident response changes** – after an incident, new policies are written and differences from the old policy are documented.
3. Policy documents and **change history** matter for **audits** (regular external audits, e.g. by government bodies).

### What does an auditor check first?

Answers discussed: policy documents, IRP, how controls are implemented, incident reporting, awareness training. The missing key answer was:

> **A recognised framework, e.g. NIST or ISO 27001.**

- **NIST** – National Institute of Standards and Technology (Cybersecurity Framework).
- **ISO/IEC 27001** – international information security standard.
- Auditors are not impressed by "we have firewalls and backup servers" alone; they look for adherence to an **industry standard** built on decades of experience.
- Analogy: TCP/IP is a standard; without standards systems cannot interoperate.
- In practice organisations combine frameworks and pick the best parts of each. The policy states "we use the NIST framework", steps are defined from it, and the architecture diagram demonstrates it.

---

## 4. Learning Objectives for Topic 10

After this session you should be able to:

1. **Identify and prioritise operational cyber hygiene tasks** – recurring tasks such as patch cycles, backups, access reviews; prioritise by **risk, frequency and business impact**, using **ASD** (Australian Signals Directorate) and **NIST** guidance.
2. **Perform system- and user-level hygiene activities** – verify patches, review logs, check endpoint health; identify phishing attempts and unsafe user habits.
3. **Develop and implement workflows** – schedules, role assignment, tracking; daily/weekly/monthly routines; record and verify completion.
4. **Automate** – scheduled updates, backups, scripts; choose tasks that gain efficiency and consistency from automation.
5. **Monitor, validate and improve** – use logs, reports and alerts to confirm tasks completed.

---

## 5. 10.1.1 The Six Categories of Cyber Hygiene Tasks

| # | Category | Typical tasks | Risk if missed |
|---|---|---|---|
| 1 | **Data protection & backup management** | Regular secure backups; **restore tests** to verify integrity; recovery process availability | Data loss, no recovery |
| 2 | **Identity & access management** | Access reviews, credential management, least privilege | Unauthorised access |
| 3 | **Vulnerability & patch management** | Patch/update cycles, vulnerability checks | Known vulnerabilities exploited |
| 4 | **Continuous monitoring & threat detection** | Log review, alerts, SIEM (Wazuh, ELK) | Late detection |
| 5 | **Security awareness & user behaviour monitoring** | Training, phishing identification | Human-error incidents |
| 6 | **System maintenance & configuration management** | Hardening, config baselines, maintenance | Misconfiguration, drift |

**Exam tip:** a backup is only meaningful if you **validate it by restoring**.

---

## 6. 10.1.2 Prioritising Cyber Hygiene Tasks

Not all tasks are equally important; time and resources are limited.

### 6.1 Three factors

- **Risk** – how dangerous is it if the task is not done?
- **Frequency** – how often must it be done to stay effective?
- **Business impact** – how important is it to operations?

Examples:
- **Backup verification** – high risk and high impact → **daily** check.
- **Access rights review** – medium risk, not urgent → **monthly**.

### 6.2 Risk Assessment Matrix (RAM)

- **Y-axis:** Likelihood – very unlikely, unlikely, possible, likely, very likely.
- **X-axis:** Impact – negligible, minor, moderate, significant, severe.
- Cell colour = risk level: green (low), yellow (medium), orange (medium-high), red (high).
- Priority ≈ **likelihood × impact**; handle the red cells first.
- Example: a firewall that successfully blocks a virus = low risk. If it can no longer block it, risk rises towards high – the organisation has left a risk unmanaged.
- This is directly usable for **Assessment 2 Part A (risk assessment)**.

### 6.3 Business impact examples

- **Backup failure on a critical server → critical impact** (data loss, downtime).
- **Missed update on a non-critical device → lower impact** (unless that device is tied to a significant risk).
- Focus: **prioritise tasks that support core business operations.**
- Good prioritisation combines risk + frequency + business impact so resources are used efficiently and security work matches real organisational priorities.

---

## 7. System- and User-Level Checks

### 7.1 Log review (first thing a security analyst does)

- Hackers try to reach services through **open ports (TCP)**; open ports are attack paths.
- Always check **system logs**.
- Examples:
  - **Task Manager (Windows)** – abnormal CPU/memory use can signal compromise; Linux has equivalents.
  - **Application history** – find unknown programs that ran.
  - **PID (process ID):** every running process has one; end suspicious processes with **End task** (Windows) or `kill <PID>` (Linux).
  - **Logins:** who logged in (teacher/student accounts, groups) and who is still connected.
  - **USB scenario:** even if the system blocks a virus on a USB, logs show who moved which file and when.
  - Logs reveal tools such as **nmap** scans and unauthorised access attempts.

### 7.2 Patch verification

- **Windows:** Settings → Windows Update → Update history ("You're up to date").
- **Linux:** `sudo apt list --upgradable` to list packages that can be upgraded.

### 7.3 Common things to check

Failed updates, pending critical patches, system logs, unusual IP addresses, unusual login attempts and alerts.

---

## 8. Workflows and Automation

### Workflows
- Define schedules, roles and tracking; use daily/weekly/monthly routines; record completion and verify it.
- Cyber hygiene can look boring but is a repeated cycle of identify, protect, monitor, control.

### Automation
- Set up once and it runs by itself – e.g. antivirus, Word auto-save.
- **Not everything can be automated;** pick tasks where automation improves efficiency and consistency.
- **Backups are the classic example:** databases such as Oracle and MySQL have automated backup features configured by a **DBA (Database Administrator)** via GUI (date/time) or a small SQL script. Banks typically back up after business hours; some use **mirror servers** for continuous real-time backup.

### Monitor, validate, improve
- Automation is not "set and forget": review **logs, reports and alerts** to confirm tasks were completed (e.g. did last night's backup succeed?), then improve.
- Cycle: **automate → verify results → improve.**

---

## 9. Assessment 2 Overview

| Part | Content | Type |
|---|---|---|
| **A** | Organisational **risk assessment** | Individual (mostly submitted in September) |
| **B** | Write an **Incident Response Plan (IRP)** for NovaStyle | Group |
| **C** | **Red / Blue / Purple team** activity (SOC-style) | Group |

- Part B due near the end of term (instructor mentioned Week 16 – verify in the assessment document).
- AI use is **guided**: allowed for research/concept checking, but the final answer must show your own application and understanding.

### Part B requirements
1. Choose **one incident** from the recent-incidents list (e.g. phishing, DDoS, SQL injection); define the **Incident Response Team (IRT)** and write the IRP (Victorian Government template recommended, not mandatory).
2. **Roles and responsibilities** for each IRT member – specific and realistic for the incident type.
3. **Communication and escalation:** how the incident is reported, who is notified first, who approves the response, how information flows to team, management and stakeholders.
4. **Business impact:** operational disruption, financial loss, reputational damage.
5. **Step-by-step response actions**, including evidence collection.

Tips: course diagrams may be reused with explanation; the score depends on how well you **organise and explain** the response.

---

## 10. Hands-on: Wazuh / ELK and Sprint 2

### 10.1 Tools
- **Wazuh** and **ELK (Kibana)** both collect, store and visualise logs (SIEM). Knowing them is highly valuable for a security analyst.
- Lab access is through a **VPN** (SoftEther client) from outside campus. Credentials are shared by the instructor in class chat and are intentionally **not recorded here**.
- Wazuh's web interface was refused for many students (likely a **firewall issue**, passed to IT); **ELK worked**.

### 10.2 Troubleshooting notes
- `ERR_CONNECTION_REFUSED` with a successful **ping** = route is fine but the service/port refuses connections (server/firewall side), not a client or browser problem.
- `NET::ERR_CERT_AUTHORITY_INVALID` on an internal lab server is expected (self-signed certificate); only proceed on trusted internal lab hosts.
- Empty Discover results: check the **Data view** (use the `wazuh-alerts-4.x-*` view, not Logstash monitoring metrics) and widen the **time range**.

### 10.3 ELK / Kibana walkthrough
- **Discover:** time-series histogram plus documents; searching `nmap` over Sep 13–27 returned **21 "Nmap scan detected" alerts**. Expanding a document shows timestamp, agent ID/IP/name, rule description and `full_log`.
- **Security → Alerts:** example alert **"SOC-S4 – FTP-server-file download"**, severity **High**, risk score **73**, status Open; notes and assignees can be added, severity can be tuned in the rule configuration.
- **Observability → Alerts:** statuses **Active** (condition still met) vs **Recovered** (resolved); rules fire when a **threshold** (e.g. > 1000 documents) is exceeded.
- **JSON = JavaScript Object Notation:** key/value format used for configuration and data (instructor described it as used for system configuration).
- ELK also offers dashboards and machine-learning features.

### 10.4 Sprint 2 guided exercise – FTP misconfiguration

A Linux file server has an FTP misconfiguration. Teams work without seeing each other's activity.

- **Red team (Kali Linux):** `nmap` scan → find services allowing access without a password → **anonymous FTP** login → retrieve files/credentials → **SSH** in.
- **Blue team (SOC analyst, ELK + Wazuh):** monitor dashboards → investigate source/scope → assess whether access succeeded → document in **Cydarm** as a formal incident → close the case. Logs can take **5–10 minutes** to appear.
- **Purple team debrief:** compare attacker actions with defender detections, find what was missed, and identify the one change that would have prevented the attack.
- **MITRE ATT&CK mapping:** **T1078** Valid Accounts, **T1083** File and Directory Discovery, **T1021.004** Remote Services: SSH.
- This is effectively practice for **Assessment 2 Part C**.

---

## 11. Key Takeaways / Likely Exam Points

1. Cyber hygiene = continuous cycle (**Identify → Protect → Detect → Respond**).
2. **Identify first:** you cannot protect or respond to unknown assets/threats.
3. Auditors first look for a **recognised framework (NIST, ISO 27001)**, then policy, IRP and controls.
4. n-tier: **Presentation / Business Logic / Data**; web server = **software** (Apache, IIS) at the application layer; **API** (JDBC/ODBC) connects web/app servers to databases; router = **Layer 3**.
5. Redundancy and load balancing protect against failure and DDoS.
6. Prioritise by **risk + frequency + business impact**; use the **risk matrix (likelihood × impact)**.
7. **Validate backups by restoring**; automate suitable tasks; verify with logs/reports/alerts.
8. Logs are the evidence of "what happened"; review them regularly.
9. Tools (ELK, Wazuh) show which attacks are happening; without them you are blind.
10. Most failures come from **people and process**, not just technology.

---

## 12. Action Items

- [ ] Group discussion: choose the incident for **Part B (IRP)**.
- [ ] Read Sprint 2 guided learning: *Before You Start → Red Team → Blue Team → Purple Debrief*.
- [ ] Retry Wazuh once IT resolves the firewall issue; keep ELK screenshots as evidence.
- [ ] Review Topic 10 slides (six categories, prioritisation criteria).
