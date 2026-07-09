# Windows OS Troubleshooting — Study Notes

> Cisco IT Essentials — Chapter 11: Windows Operating System Troubleshooting

## 1. The Six-Step Troubleshooting Process

| Step | Name | Description |
|---|---|---|
| 1 | Identify the problem | Gather information from the customer: symptoms, recent changes, error messages. |
| 2 | Establish a theory of probable cause | List possible causes: bad settings, recent updates, malware, hardware failure. |
| 3 | Test the theory to determine cause | Verify hypotheses — log in as a different user, boot into safe mode, check drivers. |
| 4 | Establish a plan of action and implement the solution | Research using manuals, FAQs, forums, helpdesk logs; then apply the fix. |
| 5 | Verify full system functionality and implement preventive measures | Confirm everything works; take steps to prevent recurrence. |
| 6 | Document findings, actions, and outcomes | Record the problem, steps taken, and results for future reference. |

### Step 5 in Practice
Restart the computer, check event logs, Device Manager, and network connectivity. Run diagnostics, verify apps and system files work correctly.

### Step 6 in Practice
Review completed repairs with the customer, confirm the fix, and document parts used, time spent, and provide paperwork.

---

## 2. Common Windows Problems

- Computer lockups / freezes
- Unresponsive keyboard or mouse
- Boot failures ("Invalid Disk", "BOOTMGR is missing")
- Services or devices failing to start
- Blue Screen of Death (BSOD)
- Application installation failures
- System slowdowns / delayed response
- Windows Update failures
- Printing problems
- Slow boot times

## 3. Advanced Windows Problems

- **Boot errors**: "Invalid Boot Disk", "Inaccessible Boot Device", "BOOTMGR is missing"
- **Startup issues**: a service/device fails to start; computer keeps restarting without reaching the desktop
- **System errors**: BSOD, system freezes with no warning
- **Software/file issues**: missing DLL errors, failed installs, files that won't open
- **Performance/config issues**: slow search, misaligned multi-monitor setup, RAID not detected, corrupted system files, computer boots only to Safe Mode

---

## 4. Common Causes of OS Problems

- Corrupted registry
- Virus infection (damages/deletes system files → severe performance **degradation**, i.e., worsening performance)
- Failed service pack installation

*(Cable connections and CMOS battery are hardware issues; incorrect IP addressing is a network issue — not OS causes.)*

---

## 5. Key Tools & Commands

| Tool / Command | Purpose |
|---|---|
| **Task Manager** | Force-close unresponsive applications and free system resources |
| **gpresult** | Report currently applied Group Policy settings (diagnose GP issues) |
| **gpupdate** | Immediately refresh/apply Group Policy |
| **tasklist** | List running processes |
| **rstrui** | Run System Restore |
| **runas** | Run a program as a different user |
| **ping** | Test basic connectivity to an IP/hostname |
| **tracert** | Trace the full path packets take to a destination |
| **ipconfig** | Show IP address / default gateway configuration |
| **nslookup** | Test DNS name resolution (hostname ↔ IP) |

---

## 6. Restore Points

- Always create a restore point **before** making system changes.
- Acts like a "time machine" for system settings/programs — lets you roll back if changes cause problems.
- **Does NOT** back up personal files (documents, photos, etc.) — only system settings/state.

---

## 7. BSOD (Blue Screen of Death) — Likely Causes

- Device driver errors (driver = bridge between OS and hardware; corruption often crashes the system)
- RAM failure (faulty memory → data corruption → fatal errors)

*(Outdated browsers or missing antivirus rarely cause a BSOD directly.)*

---

## 8. Remote Access Tools

- **Remote Desktop**: Admin logs directly into a remote PC/server to manage/troubleshoot it, as if sitting in front of it.
- **Remote Assistance**: A user shares their screen with a support tech, who can view/control input to help resolve issues interactively.
- Both connect over the network to control applications/data on a remote machine.

## 9. VPN (Virtual Private Network)

- Used when a company has branches worldwide needing to communicate securely and share network resources.
- Encrypts data over the public internet so it functions like a private, dedicated connection.
- Remote Desktop/Assistance are for individual PC control — not for connecting entire branch networks; that's VPN's job.

---

## 10. File & System Management

### File Attributes
- **Read-only** — file can be viewed but not modified/deleted
- **Archive** — flags whether a file needs to be backed up since its last modification

*(Note: "General", "Security", "Details" are tabs in the file Properties window UI — not actual file-system attributes.)*

### Windows 10 Default Libraries
4 libraries created by default: **Documents, Music, Pictures, Videos**

### Sleep/Hibernate Password Prompt
Set via: **Control Panel → Power Options** ("Require a password on wakeup")

### 32-bit Program Files on 64-bit Windows
Installed to **C:\Program Files (x86)**
(64-bit programs go to `C:\Program Files`; "x86" refers to the legacy 32-bit architecture.)

---

## 11. Networking & Ports

| Port | Protocol | Use |
|---|---|---|
| 20 | FTP | Data transfer |
| 22 | SSH | Encrypted remote access (secure) |
| 23 | Telnet | **Unencrypted** remote access — sends data in plaintext, vulnerable to interception |
| 443 | HTTPS | Secure web traffic |
| 3389 | RDP | Windows Remote Desktop |

⚠️ Best practice: avoid Telnet (23); use SSH (22) for encrypted remote management.

---

## 12. Group Policy Troubleshooting Example

**Scenario**: User logs into Active Directory but home directory isn't redirected to the network share.
**Tool**: `gpresult` — shows which Group Policy settings are actually applied, helping diagnose conflicts or misapplied policies.

---

## Vocabulary Note
**Degradation** (noun, from *degrade*) = a worsening or decline, e.g. "severe performance degradation" = the system becoming significantly slower/less functional.
