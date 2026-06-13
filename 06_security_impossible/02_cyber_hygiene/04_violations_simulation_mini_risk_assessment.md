# Mini Risk Assessment – Information Security Violations Simulation (Part 2)

## Overview

This lab is a hands-on cybersecurity exercise that builds on a Part 1 simulation, in which two real security violations were observed:

1. An **unauthenticated SMB file share** (`\\127.0.0.1\ConfidentialShare`) that exposed sensitive files without any login required.
2. **Unauthorized external email disclosure** — confidential data was emailed from an internal address (`john@snapshipdelivery.com`) to an untrusted external domain (`ghost@darknet.com`).

Part 2 builds a structured **Mini Risk Assessment** in four steps, aligned with **ISO/IEC 27001** and **NIST SP 800-30** frameworks:

1. Asset Identification and Valuation
2. Threat and Vulnerability Analysis
3. Risk Analysis / Risk Register
4. Recommended Mitigation Principles

---

## Step 1: Asset Identification and Valuation

**Goal:** Identify what needs protecting and rank assets by how much damage their compromise would cause.

### Asset Categories

| Category | Description | Examples |
|---|---|---|
| **High-Value** | Core to operations; compromise causes severe financial, legal, or reputational damage | Email server, web server, database server, internet-facing router |
| **Medium-Value** | Needed for daily work, but smaller "blast radius" if compromised | Staff workstations/laptops, admin PCs, meeting room equipment |
| **Low-Value** | Minimal sensitive data, high public exposure | Reception/front-desk computer |
| **Restricted** | Security/monitoring systems themselves; must be tightly controlled | CCTV systems |

### Valuation Criteria
- Business impact if compromised
- Sensitivity of data handled
- Operational dependency
- Regulatory/privacy obligations
- Level of exposure to unauthorized access

### Key Asset Register Findings (from the office network diagram)

- **Email / Web / Database Servers (Server Room)** → High-Value: core repositories of confidential, financial, and operational data.
- **Internet-facing Router** → High-Value: all traffic passes through it; compromise risks the entire network.
- **IT/Admin Room workstations & hub** → Medium-Value: daily operations, limited blast radius.
- **Staff workstations/laptops** → Medium-Value: supports productivity, individually less critical than servers.
- **Meeting room router, laptops, screen** → Medium-Value: confidential discussions occur here, but limited scope.

---

## Step 2: Threat and Vulnerability Analysis

**Goal:** For each asset, determine *how* it could be improperly accessed, *what controls are missing*, and *who* could exploit the gap — linking back to evidence from Part 1.

### Key Concepts
- **Threat** = anything that could cause harm
- **Vulnerability** = the weakness a threat exploits

### Threat & Vulnerability Register (Summary)

| Asset | Threat | Vulnerability | Possible Exploiter | Linked Part 1 Evidence |
|---|---|---|---|---|
| File/Database Server | Unauthorized Access | Shared folder accessible with no authentication; excessive file permissions | Internal user / external attacker if exposed | Payroll, HR, Budget, Roadmap files openly accessible without login |
| File/Database Server | Insider Misuse | No reliable logging of file access ("Date Accessed" not updated) | Insider/employee | File access metadata didn't update after opening |
| Corporate Email Server | Data Exfiltration | No outbound email monitoring or DLP | Insider or compromised account | Email sent from internal address to `ghost@darknet.com` |
| Corporate Email Server | Insider Misuse | No policy enforcement/security awareness | Insider/employee | Email content showed awareness of wrongdoing ("avoid drawing unnecessary attention") |
| Core Network Devices (Router/Hubs) | Network Compromise | No monitoring → lateral movement possible | External attacker / insider with network access | High-value devices have no monitoring controls |
| Server Room | Physical Intrusion | Weak access control → tailgating possible | Unauthorized visitor/staff | Server Room houses all High-Value servers |
| Employee Workstations | Unauthorized Access | Excessive permissions, no least-privilege | Insider/employee | Confidential files accessible from a standard workstation |

### Identified Risk Themes
1. **Unauthorized Access** — weak permission management on file servers
2. **Data Exfiltration** — no email monitoring/DLP
3. **Physical Intrusion** — poor server room access control
4. **Network Compromise** — unmonitored routers/hubs allow lateral movement
5. **Insider Misuse** — lack of logging, oversight, and accountability

---

## Step 3: Risk Analysis (Risk Register)

**Goal:** Prioritize which risks matter most by combining:

- **Asset Value** (how important is it?)
- **Likelihood of Threat** (how likely is an attack?)
- **Potential Impact** (how bad would it be?)

### Risk Rating Formula
> **Risk Rating = Likelihood × Impact**

Impact is typically categorized as **Low / Medium / High**, based on:
- Financial loss
- Legal/regulatory consequences
- Operational disruption
- Reputational damage

### Top-Priority Assets Requiring Immediate Protection

1. **File Server** — contains payroll/HR/strategy data; already shown to be exposed → very high impact if breached.
2. **Email System** — primary channel for data exfiltration; no outbound controls → high likelihood + high impact.
3. **Core Network Devices** — gateway to all other systems; compromise enables lateral movement across the network.

### Root Causes Identified
- **Weak access controls** — no authentication/authorization on shares, excessive permissions
- **Limited monitoring/logging** — no detection capability for data exfiltration or insider activity
- **Lack of procedural enforcement** — no data classification policy, no external-sharing approval process, low staff awareness

> **Key insight:** The focus shifts from individual incidents to **root causes** — technical fixes alone aren't enough; procedural and physical controls are also required.

---

## Step 4: Recommended Mitigation Principles

A **layered defense** combining technical, physical, and administrative/human controls:

### 1. Technical Controls
- **Least Privilege + Role-Based Access Control (RBAC)** — users only access what their role requires
- **Network Segmentation** — isolate sensitive infrastructure
- **Logging & Monitoring** — enable logs for file access, email, and network traffic for detection/investigation
- **Data Loss Prevention (DLP)** — monitor and block unauthorized transmission of sensitive data

### 2. Physical Controls
- Restrict access to server rooms via secure entry systems, CCTV, and visitor logs

### 3. Administrative / Human Controls
- Regular **security awareness training** so staff understand data-handling responsibilities and the consequences of improper sharing

### Overall Outcome
- A layered defense addresses **technical weaknesses, physical exposure, and human error** simultaneously.
- **Proactive risk review + continuous monitoring** reduce the likelihood of breaches, operational disruption, and reputational damage.
- Foundational principle: **you can't protect what you haven't identified** — asset identification + threat analysis underpin the entire security program.

---

## Quick Reference: Glossary of Key Terms

| Term | Meaning |
|---|---|
| **Asset** | Anything of value to the organization (data, systems, hardware) |
| **Threat** | A potential cause of harm |
| **Vulnerability** | A weakness that a threat can exploit |
| **Risk** | The combination of a threat exploiting a vulnerability on an asset |
| **Likelihood** | Probability that a threat will occur |
| **Impact** | Severity of consequences if a risk materializes |
| **Risk Rating** | Likelihood × Impact |
| **Least Privilege** | Granting users only the minimum access needed for their role |
| **RBAC** | Role-Based Access Control |
| **DLP** | Data Loss Prevention — tools that detect/block unauthorized data transmission |
| **Tailgating** | Following an authorized person through a secure entry without credentials |
| **Data Exfiltration** | Unauthorized transfer of data out of an organization |
| **Lateral Movement** | An attacker moving from one compromised system to others within a network |

---

## End-to-End Summary

1. **Identify assets** → know what you have and how important each piece is.
2. **Find vulnerabilities** → figure out how each asset could be attacked and by whom.
3. **Assess risk** → rank issues by Likelihood × Impact to prioritize action.
4. **Mitigate** → apply least privilege, DLP, monitoring, physical security, and training to build layered defenses.

This mirrors the real-world workflow used by security consultants and analysts: **Assess → Analyze → Determine → Mitigate**, following standards like ISO/IEC 27001 and NIST SP 800-30.
