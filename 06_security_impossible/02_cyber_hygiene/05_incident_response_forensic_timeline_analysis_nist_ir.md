# Incident Response and Executive Reporting Using NIST-IR
> Security Impossible – Cyber Range Lab Study Notes

---

## 📌 Lab Overview

| Item | Detail |
|------|--------|
| **Lab Title** | Incident Response and Executive Reporting Using NIST-IR |
| **Platform** | Security Impossible – Cyber Range |
| **Duration** | 60 minutes |
| **Difficulty** | Intermediate |
| **Focus Area** | Digital Forensics & Incident Response (DFIR) |

### Objective
Train in forensic timeline analysis using **Hayabusa** and **Timeline Explorer**, and produce a structured **NIST-aligned Incident Response (IR) report** based on Windows Event Log evidence.

### Learning Outcomes
- Generate forensic timelines from Windows Event Logs using Hayabusa
- Analyse large-scale event data using Timeline Explorer
- Identify post-exploitation attacker behaviour from logs
- Correlate events into a coherent incident timeline
- Produce a concise NIST Incident Response report

---

## 🛠️ Tools Used

### Hayabusa
- A **Windows Event Log fast forensics tool** by Yamato Security
- Detects malicious activity using **Sigma rules**
- Generates **timeline-based CSV outputs** for investigation
- Command-line tool (`.exe`)

### Timeline Explorer
- Used to **analyse CSV timelines**
- Supports **grouping, filtering, and keyword search**
- Identifies patterns indicative of attacker behaviour

---

## 📋 Key Concepts

### NIST-IR (Incident Response Framework)
Defined by the **National Institute of Standards and Technology (NIST)**, documented in **NIST Special Publication 800-61**.

| Phase | Description |
|-------|-------------|
| **Preparation & Detection** | Identify the incident, affected hosts, severity |
| **Analysis** | Reconstruct the attack timeline and technical findings |
| **Containment** | Stop the spread — isolate hosts, block malicious activity |
| **Eradication & Recovery** | Remove all traces, reimage systems, patch vulnerabilities |
| **Post-Incident Activity** | Document lessons learned, improve defences |

### MITRE ATT&CK Framework
A globally recognised knowledge base of adversary **Tactics, Techniques, and Procedures (TTPs)**. Used to map observed attacker behaviour to known attack patterns.

### Timeline-Based Incident Response
Reconstructing attacker activity in **chronological order** using log evidence.
- Event correlation improves detection accuracy
- Timeline analysis reveals attack chains
- Windows logs provide critical forensic evidence
- Structured reporting improves response quality

---

## 🔬 Step-by-Step Lab Procedure

### Step 1 — Disable Windows Defender Real-Time Protection
> Required to prevent lab tools from being blocked (isolated lab environment only)

1. Open **Windows Security**
2. Go to **Virus & threat protection**
3. Click **Manage settings**
4. Toggle **Real-time protection → Off**

⚠️ *Never disable this in a real production environment.*

---

### Step 2 — Update Hayabusa Detection Rules

```powershell
# Open PowerShell as Administrator
cd 'C:\Users\MALAB\Desktop\Lab Files\'

# Update detection rules
.\hayabusa-2.16.0-win-x64.exe update-rules
```

**Expected result:**
```
Updated Sigma rules: 2266
Rules updated successfully.
```

> This downloads the latest **Sigma rules** — the "wanted list" of known attack patterns.

---

### Step 3 — Generate Forensic Timeline from EVTX Logs

```powershell
.\hayabusa-2.16.0-win-x64.exe csv-timeline -d .\sample-evtx\ -o Lab-output.csv
```

**Wizard options:**
- Select **Option 2: Core (3,909 rules)** — includes medium, high, and critical severity
- Include **Sysmon rules: Yes**

**Results Summary:**
| Metric | Value |
|--------|-------|
| Total events analysed | 46,309 |
| Events matched | 6,118 |
| Data reduction | 86.79% |
| Output file | `Lab-output.csv` (14.3 MB) |

**Top Alerts Detected:**
- Metasploit SMB Authentication
- Suspicious Service Installation Script
- PowerShell Script Installed as Services
- Failed Logon — Incorrect Password (3,884)
- Potentially Malicious PwSh (235)
- Proc Injection (104)
- Suspicious Service Name (80)

---

### Step 4 — Analyse Suspicious Activity in Timeline Explorer

Load `Lab-output.csv` into Timeline Explorer and search for the following:

#### 🔍 Search 1: `PowerShell`
**Findings (1,992 results):**
- `Windows Defender Exclusions Added - PowerShell` — attacker disabled AV detection
- `Malicious PowerShell Commandlets` — malicious commands executed
- `HackTool - CrackMapExec PowerShell Obfuscation` — hacking tool usage
- `Change PowerShell Policies to an Insecure Level` — security policy weakened
- `Potentially Malicious PwSh` — suspicious PowerShell execution
- **Event ID 4104** — PowerShell Script Block Logging
- **`-ExecutionPolicy Bypass`** — security policy bypassed

#### 🔍 Search 2: `lsass`
**Findings (201 results):**
- `Reconnaissance Activity` — system information gathering
- `AD Privileged Users or Groups Reconnaissance` — admin account enumeration
- `Password Policy Enumerated` — password policy exfiltration
- **Event ID 4661** — sensitive object access attempts
- Primary target: `WIN-77LTAPHIQ1R.example.corp`

#### 🔍 Search 3: `psexec`
**Findings:**
- `PsExec Service Execution` — remote execution across multiple hosts
- `PsExec Service Child Process Execution as LOCAL SYSTEM` — highest privilege execution
- `PsExec/PAExec Escalation to LOCAL SYSTEM` — privilege escalation
- `PsExec Lateral Movement` — movement across the network
- Affected hosts: `srvdefender01`, `PC01`, `MSEDGEWIN10`, `fs03vuln`

#### 🔍 Search 4: `NTLM`
**Findings (7,165 results):**
- `Pass the Hash Activity 2` — attacker used captured password hashes to authenticate
- **Event ID 4624** — successful network logon
- **Logon Type 3 (NETWORK)** — remote authentication
- Target accounts: Administrator accounts across multiple systems
- Affected hosts: `srvdefender01`, `rootdac1`, `mssql01`, `MSEDGEWIN10`, `fs03vuln`

---

## 🔑 Key Event IDs Reference

| Event ID | Source | Description |
|----------|--------|-------------|
| **4104** | PowerShell | Script Block Logging — records executed PS commands |
| **4624** | Security | Successful logon |
| **4625** | Security | Failed logon |
| **4657** | Security | Registry value modification |
| **4661** | Security | Sensitive object access |
| **4688** | Security | New process creation |
| **7045** | System | New service installed |
| **1** | Sysmon | Process creation |
| **10** | Sysmon | Process access (e.g. lsass access) |
| **13** | Sysmon | Registry value set |
| **17/18** | Sysmon | Pipe created/connected |

---

## 🧩 Attack Chain Reconstructed

```
[1] Initial Access & Execution
    └── PowerShell executed with NT AUTHORITY\SYSTEM privileges
        └── Event ID 4688 / 4104
        └── ExecutionPolicy Bypass

[2] Persistence Established
    └── Malicious services created via registry modifications
        └── Event ID 7045 (Service Install) / 4657 (Registry Modification)
        └── HKLM\SYSTEM\CurrentControlSet\Services

[3] Credential Access
    └── Suspicious access to lsass.exe (password store)
        └── Sysmon Event ID 10 (Process Access)
        └── Tools: Mimikatz

[4] Lateral Movement
    └── PsExec-based remote execution across multiple hosts
        └── Event ID 4688 / 7045
        └── Pass-the-Hash authentication (Event ID 4624, Logon Type 3)

[5] Defence Evasion
    └── Renamed binaries executed from temp/user-writable directories
        └── Paths: C:\Windows\Temp\, C:\Users\*\AppData\
        └── Windows Defender exclusions added via PowerShell
```

---

## 🛡️ NIST Incident Response Mini Report Summary

### Incident Identification
| Field | Detail |
|-------|--------|
| **Incident Type** | Credential Access, Persistence, Lateral Movement |
| **Detection Method** | Windows Event Log analysis via Hayabusa timeline correlation |
| **Severity** | Medium to High |

### High-Confidence Infected Hosts
- `srvdefender01.offsec.lan`
- `mssql01.offsec.lan`
- `IE10Win7`
- `fs03vuln.offsec.lan`
- `FS03.offsec.lan`
- `fs02.offsec.lan`
- `fs01.offsec.lan`

### Additional Impacted Hosts
- `rootdc1.offsec.lan` *(Domain Controller — increases severity)*
- `jump01.offsec.lan` *(Likely used for lateral movement)*
- `MSEDGEWIN10`, `PC01.example.corp`, `MSEDGEWIN10`

### Containment Actions
- Isolated affected hosts from the network
- Disabled and removed malicious services and scheduled tasks
- Blocked identified malicious hashes, binaries, and execution paths
- Reset credentials for compromised user and service accounts

### Eradication & Recovery
- Removed all identified persistence mechanisms
- Reimaged compromised hosts where integrity could not be verified
- Applied missing security patches and system updates
- Enabled **PowerShell Script Block Logging** and **Sysmon monitoring**
- Monitored systems post-recovery for signs of reinfection

### Lessons Learned
- Comprehensive endpoint logging is critical for accurate incident reconstruction
- Service creation and registry modification events are strong indicators of persistence
- **LSASS access must be tightly monitored** due to its role in credential theft
- Timeline-based log correlation significantly improves visibility into attack progression

---

## 📚 Terminology Glossary

| Term | Definition |
|------|-----------|
| **SIFT** | SANS forensic Linux distro for DFIR investigations |
| **Metasploit** | Open-source penetration testing framework |
| **Flagging** | Submitting a captured flag string in CTF competitions |
| **Anomalous** | Abnormal or irregular — deviating from expected behaviour |
| **Containment** | Stopping an attack from spreading further |
| **Remediation** | Fixing the problem and restoring systems to a clean state |
| **Persistence** | Attacker techniques to maintain access (survive reboots/detection) |
| **Evasion** | Techniques to avoid detection by security tools |
| **Pass-the-Hash** | Using captured password hashes to authenticate without knowing the plaintext password |
| **Lateral Movement** | Attacker moving from one system to others within the network |
| **lsass.exe** | Windows process responsible for authentication — primary target for credential theft |
| **PsExec** | Sysinternals tool for remote execution — commonly abused by attackers |
| **Sigma Rules** | Open standard for writing detection rules for log analysis |
| **EVTX** | Windows Event Log file format |
| **TTPs** | Tactics, Techniques, and Procedures — how attackers operate |

---

*Study notes compiled from Security Impossible Cyber Range — NIST-IR Lab*
