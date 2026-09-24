# Module 16: Network Security Fundamentals

**Course:** Cisco NetAcad
**Topic:** Network Security Fundamentals — Threats, Vulnerabilities, Malware, and Network Attacks

---

## 16.0 Module Overview

**Objective:** Configure switches and routers with device hardening features to enhance security.

**Four topics covered:**
1. Security Threats and Vulnerabilities
2. Network Attacks
3. Network Attack Mitigation
4. Device Security

---

## 16.1 Security Threats and Vulnerabilities

### 16.1.1 Types of Threats

| Threat Type | Description |
|---|---|
| **Information theft** | Breaking into a system to obtain confidential information |
| **Data loss / manipulation** | Breaking into a system to destroy or alter data records |
| **Identity theft** | Stealing personal information to impersonate someone (financial fraud, etc.) |
| **Disruption of service** | Preventing legitimate users from accessing services |

### 16.1.2 Types of Vulnerabilities

**Technological vulnerabilities**
- Weaknesses in TCP/IP protocol design
- Operating system weaknesses
- Network equipment weaknesses

**Configuration vulnerabilities**
- Unsecured user accounts
- Weak or easily guessed passwords
- Misconfigured internet services
- Insecure default settings

**Policy vulnerabilities**
- Lack of a written security policy
- Organizational politics obstructing security
- Lack of authentication continuity
- Lack of proper access controls
- No disaster recovery plan

### 16.1.3 Physical Security

**Four classes of physical threats:**
1. Hardware threats — physical damage to servers, routers, cabling
2. Environmental threats — temperature/humidity extremes
3. Electrical threats — voltage spikes, power loss, insufficient power
4. Maintenance threats — poor handling of components, lack of spare parts, poor labeling

**Three-step mitigation plan:**
1. Lock up equipment (secure physical access)
2. Monitor and log all entry/access to facilities
3. Use security cameras for surveillance

---

## 16.2 Network Attacks

### 16.2.1 Types of Malware

| Type | Key Characteristics |
|---|---|
| **Virus** | Requires a host file and human action (execution) to spread |
| **Worm** | Standalone software; self-propagates automatically without human interaction |
| **Trojan Horse** | Disguised as legitimate software; tricks user into executing it; does not self-replicate; typically creates a backdoor for attackers |

### 16.2.2 Reconnaissance Attacks

Attackers gather information about the target in a sequential process:
1. **Internet queries** — WHOIS lookups, public info gathering on target
2. **Ping sweeps** — identify which IP addresses are active (tools: `fping`, `gping`)
3. **Port scans** — identify which services/ports are open on active hosts

### 16.2.3 Access Attacks

| Attack Type | Description |
|---|---|
| **Password attacks** | Brute-force attacks, Trojan horse-based credential theft, packet sniffers capturing credentials |
| **Trust exploitation** | Abusing a trusted relationship within a network to gain unauthorized access |
| **Port redirection** | Using a compromised host to pass traffic through a firewall that would otherwise be blocked |
| **Man-in-the-Middle (MITM)** | Attacker positions between two communicating parties to intercept/alter traffic (4-step process) |

### 16.2.4 DoS and DDoS Attacks

- **DoS (Denial of Service):** Attack originates from a single source, overwhelming a target system/service
- **DDoS (Distributed Denial of Service):** Attack originates from multiple sources simultaneously, typically a **botnet** of "zombie" machines controlled via a **Command-and-Control (CnC)** server

---

## Quiz Results Summary

### Quiz 1 — Threat Types (8 questions)
**Result: 8/8 correct**
Topics: information theft, identity theft, disruption of service, data loss/manipulation, and identifying non-applicable threat categories.

### Quiz 2 — Scenario-Based Threat/Attack Classification (6 questions)
**Result: 4/6 correct**

| # | Scenario Category | Answered | Correct? | Correct Answer |
|---|---|---|---|---|
| 1 | DoS | DoS | ✅ | DoS |
| 2 | Weak password ("file") scenario | Reconnaissance | ❌ | Access attack |
| 3 | Trojan horse | Malware | ✅ | Malware |
| 4 | USB baiting scenario | Access attack | ❌ | Malware |
| 5 | Flooded print server | Access attack | ❌ | DoS |
| 6 | Port scanning | Reconnaissance | ✅ | Reconnaissance |

**Key takeaways from mistakes:**
- A weak/guessable password being exploited = **Access attack**, not Reconnaissance (Reconnaissance is only the *information-gathering* phase, not exploitation).
- Baiting via infected USB drives = **Malware** delivery method, not a direct Access attack.
- Overwhelming a server/service with traffic (even without deep info theft) = **DoS**, not Access attack — the goal (disruption) defines the category, not the target type.

---

## SANS Lab Assignment — "Research Network Security Threats"

**Source:** Cisco NetAcad Lab PDF, done informally for self-study (not for submission)

**Structure (3 parts):**
1. Explore the SANS Institute website
2. Identify a recent threat via the SANS `@RISK` newsletter archive
3. Research and present a specific real-world attack in depth:
   - Name of attack
   - Type of attack
   - Dates of attack activity
   - Systems/organizations affected
   - How it worked (mechanism)
   - Mitigation/response measures
   - References/sources

**Progress so far:**
- Explored SANS "Free Resources" and "Newsletters" pages (NewsBites, @RISK, OUCH!)
- Reviewed the @RISK newsletter archive, opened **Vol. 26, Issue 32 (Aug 20, 2026)**
- Reviewed newsletter highlights: Apple iOS/macOS patch (108 vulnerabilities fixed), an actively-exploited macOS-only Screen Sharing (VNC-based) vulnerability, a Linux kernel process accounting feature, and a list of high-severity recent CVEs (Microsoft IKE, SharePoint, macOS auth bypass, VMware vCenter — several in CISA's Known Exploited Vulnerabilities catalog)
- **Part 3 (deep-dive on a specific attack) not yet started** — next session will pick a specific attack case study to research in depth

---

## Next Steps
- [ ] Complete Part 3 of the SANS lab: select and research one specific attack in depth
- [ ] Continue Module 16: **16.3 Network Attack Mitigation**
- [ ] Continue Module 16: **16.4 Device Security**
