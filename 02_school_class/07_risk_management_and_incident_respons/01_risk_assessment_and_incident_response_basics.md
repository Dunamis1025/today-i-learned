# Cyber Security Risk Management & Incident Response — Study Notes

## 1. Risk Assessment: Purpose

The primary purpose of conducting a risk assessment for organizational assets and systems is to **identify, analyse, and mitigate potential threats**. It is the process of discovering what security risks exist within a company's assets and systems, analyzing how severe those risks are, and preparing countermeasures in advance to prevent damage.

## 2. Risk Assessment Process (Correct Order)

1. **Risk Identification** — Determine what risks exist.
2. **Risk Analysis** — Understand how serious those risks are.
3. **Risk Evaluation** — Prioritize the risks and decide whether/how to address them.
4. **Risk Mitigation** — Implement measures to reduce or eliminate the risks.

## 3. Key Security Plans & Policies

| Plan / Policy | Description |
|---|---|
| **Cyber Security Risk Management Plan** | Outlines how cyber security risks are identified, assessed, treated, and reviewed. |
| **Incident Response Plan (IRP)** | Describes how the organisation detects, responds to, and recovers from cyber security incidents. |
| **Disaster Recovery Plan (DRP)** | Focuses on restoring IT systems, applications, and data following a cyber incident or disaster. |
| **Acceptable Use Policy (AUP)** | Defines how users are permitted to access and use organisational systems and data. |
| **Access Control Policy** | Defines rules for granting, reviewing, and revoking user access based on roles and permissions. |
| **Business Continuity Plan (BCP)** | Ensures critical business operations continue during and after a major disruption. |

## 4. Prioritizing Cyber Risks

The most important action for accurately identifying and prioritizing cyber risks is:
**Identifying critical assets, threats, and vulnerabilities, then assessing likelihood and impact.**

This means: figure out what's most valuable (assets), what could attack it (threats), and where the weaknesses are (vulnerabilities) — then estimate how likely an incident is and how severe its impact would be.

## 5. Penetration Testing

The primary objective of a basic penetration test on a simulated enterprise security system is:
**To identify vulnerabilities and weaknesses in security controls without causing damage.**

It's a safe, controlled way to find security holes a real attacker could exploit — without actually breaking systems or disrupting operations.

## 6. Incident Response Plan (IRP) — Purpose in a Malware Scenario

**Scenario:** Suspicious network activity suggests malware infection; staff can't access critical systems; concerns about data integrity and service disruption.

**Purpose of the IRP:** To ensure proper handling and recovery from the security incident — following a documented plan (roles, communication procedures, containment steps, recovery actions) to respond quickly, minimize damage, and restore normal operations.

## 7. Security Testing Tools

| Tool | Purpose |
|---|---|
| **Metasploit** | Framework used to exploit and test vulnerabilities in systems and networks. |
| **Nmap** | Scans networks to discover hosts, open ports, and running services. |
| **Nessus** | Performs automated vulnerability scanning and risk reporting. |
| **Kali Linux** | A penetration testing OS bundled with multiple security testing tools. |

## 8. Reducing Human-Error Incidents

**Scenario:** Repeated incidents from phishing clicks, password sharing, unauthorized USB use — despite existing technical controls.

**Most effective strategy:** Implement regular cyber security awareness training, supported by phishing simulations and clear security guidance. Technical controls alone aren't enough — employees need ongoing education and practice to recognize threats and follow security rules.

## 9. Cyber Hygiene Best Practice

**Best practice:** Regularly updating software and antivirus tools.

Just like washing hands for personal hygiene, keeping software and antivirus up to date is a fundamental habit that protects against newly discovered threats.

## 10. Incident Response Team (IRT) Role — Ransomware Scenario

**Scenario:** Ransomware encrypts several critical servers; IRT is activated with tasks like isolating systems, analyzing logs, communicating with management, preserving evidence, and coordinating recovery.

**Best description of IRT's role:** Coordinating technical response actions, communication, evidence handling, and recovery activities. The IRT manages technical defense/recovery, stakeholder communication, and proper evidence collection all at once.

## 11. Red / Blue / Purple Team Roles

- **Red Team** — Simulates attacks (acts like hackers to test defenses).
- **Blue Team** — Detects and responds to incidents (defends the system).
- **Purple Team** — Shares lessons learned between Red and Blue teams to improve overall security.

## 12. Continual Improvement of an IRP

**Scenario:** After a simulated phishing incident, review finds: alerts detected late, unclear inter-team communication, and slower-than-expected recovery.

**Best continual improvement action:** Updating detection thresholds, clarifying communication roles, and testing the revised IRP in future exercises. Real improvement means directly fixing the weaknesses found during practice, then re-testing in future drills to confirm effectiveness.

---

## Quick Summary Table

| Topic | Key Takeaway |
|---|---|
| Risk Assessment | Identify → Analyse → Mitigate potential threats |
| Risk Process Order | Identification → Analysis → Evaluation → Mitigation |
| IRP | Enables organized, fast incident handling & recovery |
| DRP | Restores IT/data after incident or disaster |
| BCP | Keeps critical operations running through disruption |
| Pen Testing | Finds vulnerabilities safely, without causing damage |
| Awareness Training | Reduces human-error-driven incidents |
| Cyber Hygiene | Routine habits (updates, patching) prevent basic attacks |
| Red/Blue/Purple Teams | Attack / Defend / Share & Improve |
| Continual Improvement | Fix gaps found in drills, retest revised plans |
