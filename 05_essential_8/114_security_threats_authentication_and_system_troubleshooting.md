# IT Essentials / CompTIA-Style Study Notes

A consolidated summary of concepts covered in today's practice questions, organized by topic.

---

## 1. Malware & Security Threats

| Threat | Key Characteristic |
|---|---|
| **Virus (in a VM)** | Isolation means a virus inside a virtual machine does **not** automatically infect the host OS or other VMs. |
| **Spyware** | Goal is to **covertly** collect personal data / monitor activity — not primarily to evade antivirus. |
| **Rootkit** | Hides its own files/processes from antivirus software by manipulating OS-level functions — this is its defining trait. |
| **Worm** | Self-replicates and spreads across networks on its own. |
| **Trojan** | Disguises itself as legitimate software to trick users into installing it. |
| **Phishing** | Uses fraudulent emails/messages to trick people into revealing personal info. |
| **Social engineering** | Exploits human trust/psychology rather than technical flaws (e.g., impersonating a cleaner to gain physical access). Prevention: escort visitors, verify ID of unknown persons. |
| **DDoS attack** | Massive, simultaneous traffic from multiple external sources overwhelms a server — distinct from bandwidth shortage (which is a static capacity issue) or a virus (which is local/internal). |

### Malware Remediation Steps
1. **Disconnect the workstation from the network immediately** (most urgent — stops the attacker/malware from communicating).
2. Boot into **Safe Mode** to investigate/clean without interference.
3. Run **SFC (System File Checker)** — ideally in Safe Mode — to repair corrupted/missing system files, e.g., fixing "missing or corrupt DLL" errors.
4. After cleaning: **delete all System Restore points** (they may contain saved copies of the malware), then create a **new clean restore point**.
5. Back up data **before** running any repair/removal tool, since the process itself carries risk.

### Data Destruction / Disposal
- **Simple delete/format** ≠ secure erase (recoverable with common tools).
- **Data wipe with specialized software** (overwrite with 0s/random data): best option when the device must remain **functional** (e.g., donating computers).
- **Physically shattering the drive platters**: guarantees destruction but destroys the hardware — not suitable if the device needs to be reused/donated.

---

## 2. Authentication & Access Control

- **Multifactor Authentication (MFA):** combines 2+ independent proofs of identity (e.g., username + password + OTP sent to phone). Example: Gmail sending a verification code to a smartphone.
- **Principle of Least Privilege:** users get only the minimum access needed for their specific task — limits damage from mistakes or breaches.
- **Strong password guidelines:** at least 8 characters; mix letters, numbers, and symbols.
- **Weak-password breach fix:** the root-cause solution is to **enforce a security policy** (mandating password complexity/rotation) — not physical security, patching, or AV scans, since those don't address user-chosen weak passwords.
- **Remote wipe:** admin can erase all data on a lost/stolen mobile device remotely — the strongest way to make business data completely inaccessible (stronger than passcode lock, sandboxing, or remote lock, which don't destroy the data).
- **Biometric security devices:** voice recognition, retina scanner, fingerprint reader.
- **File permissions:** "Read" permission lets a user view/open a file but not save changes — a classic cause of "can open but can't save edits."

---

## 3. Networking

- **DDoS vs. bandwidth vs. virus vs. replay attack:** a sudden spike in TCP requests from many different internet locations is the signature of a **DDoS attack**, not a capacity or single-host issue.
- **Port 80:** standard HTTP web traffic port. If ping (ICMP) succeeds but web browsing fails, the likely cause is **Windows Firewall blocking port 80**.
- **Port 3389:** used by RDP (Remote Desktop Protocol).
- **Port 22:** used by SSH.
- **Port 23:** used by Telnet.
- **RDP (Remote Desktop Protocol)** — two key traits:
  - Connects over **TCP port 3389**.
  - Uses an **encrypted session** (protects screen data & keystrokes in transit).
  - Note: RDP clients now exist for macOS/Linux/mobile, not just Windows; it's graphical, not command-line (that's SSH/Telnet's job).
- **Telnet client:** used to remotely configure legacy devices that only support **plain-text (unencrypted)** sessions.
- **VPN (Virtual Private Network):** encrypts traffic to create a secure private tunnel — used to (a) protect confidential data over open/public Wi-Fi, and (b) let remote offices around the globe communicate/share resources privately.
- **SD-WAN advantages over traditional WAN:** better network consistency/reliability; integrated & automated security features.
- **MAC address filtering:** allows only pre-approved device MAC addresses to connect to a wireless network — blocks unauthorized devices.
- **Reducing Wi-Fi radio power:** shrinks signal range to stay within the building, blocking outside unauthorized connections while still letting on-site guests connect easily.
- **Wi-Fi security upgrade (WEP → WPA2):** WEP is old/weak and easily cracked; WPA2 is the modern, secure standard. Combine with MAC filtering for stronger defense against unauthorized external access.
- **Smartphone auto-connecting to Wi-Fi:** if "auto-connect to available networks" is enabled, the phone silently detects & joins nearby open Wi-Fi (e.g., a mall coffee shop) without any user action.
- **Rapid battery drain while driving:** caused by **roaming among cell towers** — frequent handovers force the radio to work harder. (Lack of Wi-Fi merely shifts traffic to cellular data; it doesn't itself cause rapid drain.)

---

## 4. Operating Systems & System Tools

- **Shell:** interprets user commands and passes them to the OS kernel (the "translator" between user input and the OS core). Different from CLI (the *environment*, not the interpreting component) and the kernel (the OS core itself).
- **PnP (Plug and Play):** Windows 10 process responsible for detecting new hardware, installing drivers, and assigning system resources automatically.
- **NTFS:** default file system for a fresh Windows 10 install — supports large files, security permissions, encryption, better recovery than FAT32/FAT16/HPFS.
- **32-bit OS on x64 hardware:** runs correctly (backward compatible) — but still capped at ~4GB RAM addressing, cannot use all installed RAM, and has weaker security than 64-bit.
- **64-bit processor architecture (2 correct facts):**
  - Has **additional registers** to handle larger (64-bit) memory addresses.
  - **Supports both 32-bit and 64-bit operating systems** (backward compatible).
  - (It is *not* limited to 4GB RAM — that's the 32-bit limitation.)
- **Program Files locations (64-bit Windows 10):**
  - 64-bit apps → `C:\Program Files`
  - 32-bit apps → `C:\Program Files (x86)`
- **System Restore points:**
  - Should always be created **before** making system changes (safety net).
  - The action is **reversible** (can undo a restore).
  - Restore points do **not** back up personal data files (documents, photos) — only system/program settings. Use separate backups (external drive/cloud) for personal files.
- **Clean OS install scenarios (when no backup exists):** existing OS is corrupted beyond repair; a brand-new replacement hard drive is installed.
- **SFC (System File Checker):** scans and repairs/replaces corrupted critical OS files.
- **Chkdsk (Check Disk):** scans a hard disk for errors and repairs them — used after abrupt power loss caused data loss/corruption.
- **Safe Mode in Windows 10:** no longer started via F8 by default — hold **Shift** and click **Restart** in the Power menu to reach the advanced startup/recovery options.
- **ReadyBoost:** lets Windows use an external flash drive (USB) as a hard-drive cache to boost performance when RAM is limited.
- **Task Manager:** best tool to forcibly release system resources from an unresponsive/frozen application ("End Task").
- **Disk states (Windows Disk Management):**
  - **Missing:** dynamic disk corrupted, powered off, or disconnected.
  - **Online (Errors):** I/O errors detected on a dynamic disk.
  - **Initializing:** basic disk being converted to dynamic.
  - **Foreign:** dynamic disk moved in from another Windows computer.
  - **Not Initialized:** disk lacks a valid signature.
  - **Offline:** dynamic disk corrupted or unavailable.
  - **Healthy:** volume functioning properly.
  - **Unreadable:** basic/dynamic disk with hardware failure, corruption, or I/O errors.
- **Group Policy commands:**
  - `gpupdate` — forces immediate sync/application of updated Group Policy settings.
  - `gpresult` — shows which Group Policy settings are currently applied (diagnostic/verification).
- **PXE (Preboot Execution Environment):** boots a PC over the network to install/reinstall an OS without local media — used when a hard drive is empty or the OS needs replacing.
- **pwd (Linux/macOS CLI):** prints the current working directory path.
- **Linux/macOS file system terms:**
  - **Swap file system:** disk space that holds inactive RAM content when memory is full.
  - **ext4:** modern Linux file system supporting larger files/volumes.
  - **Journaling:** logs changes before applying them, minimizing corruption risk from power loss.
  - **MBR:** stores partition/organization info at the start of a disk.
- **Scripting language file extensions:**
  - `.ps1` → PowerShell
  - `.js` → JavaScript
  - `.bat` → Windows Batch File
  - `.sh` → Linux Shell Script
  - `.py` → Python
- **Bool (Boolean) data type:** represents true/false conditions in programming.

---

## 5. Mobile Devices

- **Bluetooth pairing failure (keyboard fails, mouse works):** likely causes are the keyboard being **too far away** or its **battery being dead** (Bluetooth itself is confirmed working since the mouse connects fine).
- **App-caused device freeze right after install:** likely because the **app is not compatible with the device** (OS version/hardware mismatch).
- **App crashes across multiple different programs:** points to a **virus infection** (a single app crashing would suggest an app-specific bug instead).
- **Slow app response while multitasking (e.g., GPS fitness app + email app):** caused by **insufficient RAM** — running apps compete for limited memory.
- **Rapid battery drain while driving:** roaming between cell towers (see Networking section).
- **Auto Wi-Fi connection:** device setting to auto-join available networks (see Networking section).

---

## 6. Cloud, Data & Privacy

- **Photos leaked online after being taken on a smartphone:** likely cause — the **cloud service account was hacked** (photos auto-backup to cloud; a compromised account exposes them).
- **Junk/spam mail flooding a new personal laptop:** likely cause — **no antivirus/anti-spam software installed** to filter it.
- **Certificate Revocation List (CRL):** a list of security certificates that are no longer valid/trustworthy. If a browser's CRL data is outdated, it may throw a security-certificate warning even for a trusted site.
- **Offline Files (Sync Center, Windows 10):** creates a local storage location to hold files synced from a network share, allowing offline editing that syncs back once reconnected.
- **Enterprise software licenses:** typically allow a company to use the software **campus/company-wide** across many machines.

---

## 7. Hardware & Peripherals

- **64-bit processors:** backward compatible with 32-bit OS; more registers for larger memory addresses (see OS section).
- **USB-spread virus prevention:** configure antivirus to **automatically scan removable media** when connected (more effective than changing passwords, destroying the drive, or just enabling the firewall, which targets network traffic, not physical media).

---

## 8. IT Support Roles, Procedures & Professionalism

- **Level 1 technician tasks:** gathering customer info to open a work order, prioritizing calls, escalating tickets (basic intake/triage).
- **Level 2 technician tasks:** gathering **diagnostic information** from the customer's computer; **remotely updating drivers/software** (deeper technical remediation).
- **Handling an angry customer:** let them finish explaining without interrupting; then redirect the conversation toward solving the problem.
- **Technician already knows the issue before customer finishes talking:** still **wait politely** for the customer to finish (builds trust, avoids misunderstanding).
- **Unsolicited marketing emails to a former client (policy violation):** technician should have (1) asked if the customer wanted such information, and (2) checked company policy on personal/promotional communication with customers.
- **Migrating files/profiles from old to new Windows 10 PC:** Microsoft recommends **PCmover Express** (by Laplink) for individual users — *User State Migration Tool* is for enterprise-scale IT admin use.
- **Suspected illegal activity found on a computer:** document immediately — (1) why the technician accessed the computer, (2) evidence of the suspected activity, (3) the computer's exact physical location (important for any later investigation).
- **Administrator account:** should be reserved for system management tasks only — not for everyday use, since a mistake or infection under this account could severely damage the whole system.

---

## Quick Vocabulary Glossary (from today's reading discussions)

| Word | Meaning |
|---|---|
| grinds to a halt | comes to a complete stop (like machinery jamming from friction) |
| indicative (of) | suggestive/serving as a sign (of) |
| definitive | conclusive, decisive |
| merely | just, only |
| covertly | secretly, without being noticed |
| fraudulent | deceptive, meant to trick/defraud |
| counterparts | the corresponding equivalent items being compared |
| subsequent | occurring afterward |
| extensive | broad, wide-ranging |
| intervening | stepping in / acting directly (here: "without manually intervening" = without manual action) |
| abrupt | sudden, unexpected |
| revocation | the act of cancelling/invalidating something |
| rendering (something + adjective) | making something become a certain state |

---

*Prepared as a study reference — organized from IT Essentials–style practice questions (malware, networking, OS troubleshooting, mobile devices, security, and IT support procedures).*
