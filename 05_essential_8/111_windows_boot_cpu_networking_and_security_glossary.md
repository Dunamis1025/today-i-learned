# IT Support Study Notes

> Summary of 43 practice questions covering Windows 10 administration, networking, security, mobile devices, and customer support fundamentals.

---

## Windows 10 Boot Process & System Files

### Boot Sequence (BIOS-based, 32-bit example)
1. **POST** (Power-On Self-Test) — hardware check on power-up
2. **CMOS configuration settings loaded** — BIOS reads stored settings (boot order, date/time, etc.)
3. **MBR** (Master Boot Record) — first sector of the boot disk; identifies the boot partition
4. **VBR** (Volume Boot Record) — first sector of that partition; launches `bootmgr.exe` (Windows Boot Manager)

### After `bootmgr.exe` loads
1. `bootmgr.exe` loads the **Windows boot loader**, `winload.exe`
2. `winload.exe` executes
3. `ntoskrnl.exe` (the kernel) and `hal.dll` (Hardware Abstraction Layer) are loaded into memory
4. `ntoskrnl.exe` executes and initializes the OS/hardware
5. `winlogon.exe` loads and handles the user logon screen

**Fun fact:** `ntoskrnl.exe` = **NT OS Kernel**, with vowels stripped to fit the old 8.3 filename limit (8 chars + extension). Same pattern as `hal.dll`, `csrss.exe`, `smss.exe`.

### Repairing a corrupted MBR
- Boot from installation media → Command Prompt
- Run: **`bootrec /fixmbr`**

### Unattended installation
- **Windows SIM (System Image Manager)** creates an **answer file** (`autounattend.xml`) to automate installation settings (language, drivers, apps) across multiple PCs.
- Distinguish from: System Restore (rollback), Recovery Partition (factory reset), Disk Cloning (copying an existing disk image).

### Disk / drive prep
- **New internal hard drive**: must be **initialized** first before partitioning/formatting.
- **Full format vs. Quick format**: A full format deletes files *and* scans the disk for errors/bad sectors — better before a clean OS install. Quick format only clears the file index.
- **exFAT**: file system for USB drives that supports files **larger than 4 GB** (overcomes FAT32's 4GB single-file limit).
- **NTFS**: Windows' modern file system (successor to FAT32); supports large files, permissions, compression, journaling, and **EFS encryption**.

---

## CPU & Hardware Concepts

### Cores vs. Threads
- **Core** = a physical processing unit inside the CPU chip.
- **Thread** (in this context) = a *logical processor* created via **Hyper-Threading**, letting one core handle 2 instruction streams by filling idle gaps (e.g., while waiting on data).
- Formula (for uniform, non-hybrid CPUs): **Threads = Cores × 2**
  - Example: 4 cores → 8 threads (as in Intel i7-1065G7, 10th Gen)
  - Example: 16 cores → 32 threads
- **Modern hybrid CPUs** (Intel 12th gen+) break this simple rule:
  - **P-cores** (Performance): Hyper-Threading enabled → 2 threads/core
  - **E-cores** (Efficient): No Hyper-Threading → 1 thread/core
  - Example: i9-13900K = 8 P-cores×2 + 16 E-cores×1 = 24 cores, 32 threads

### Processor Affinity
- **Affinity** = binding a process to run only on specific CPU core(s), instead of letting the OS scheduler freely assign it.
- Found in **Task Manager → Details tab → right-click a process → Set Affinity**.
- Used for performance tuning, debugging, or real-time task guarantees.

### Windows Task Manager Tabs
| Tab | Function |
|---|---|
| Performance | Real-time CPU/memory/disk/network usage graphs |
| Startup | Enable/disable programs that auto-launch at boot |
| Services | Start/stop/restart background services |
| Details | Per-process info; includes setting processor **affinity** |

---

## Windows Features & APIs

- **Libraries**: virtually group folders from multiple different locations so they appear as one unified folder.
- **PRINT$**: a hidden administrative share (`$` suffix = hidden share) used to store/distribute **printer drivers** to admins over the network.
  - Hidden shares (`C$`, `ADMIN$`, `PRINT$`) exist to (1) prevent accidental user access, (2) reduce discoverability for attackers, (3) signal admin-only intent. They're still accessible via direct path — hiding only removes them from network browsing lists.
- **APIs matched to function**:
  - **Windows APIs** — backward compatibility, letting older-version apps run on newer Windows
  - **OpenGL** — cross-platform standard for multimedia/graphics rendering
  - **DirectX** — Microsoft's multimedia API suite (gaming, video)
  - **Java APIs** — libraries for building Java applications

---

## Networking

- **DoS (Denial of Service)**: overwhelming a server (e.g., DNS server) with massive fake traffic so legitimate users can't get through. Analogy: a shop entrance jammed by a crowd blocking real customers.
- **WWAN (Wireless Wide Area Network)**: mobile devices need an **adapter** (cellular modem/card) to link to a carrier's network via the nearest **base station / cell tower / transmitter** (these three terms overlap: base station = whole facility, cell tower = visible physical structure, transmitter = the signal-sending component inside).
- **VNC (Virtual Network Computing)**: remote screen-sharing technology; default port is **5900**.
- **Sync partnership (Offline Files)**: lets a traveling user edit files locally even without a direct connection to the company network file server; changes sync automatically once reconnected.

---

## Malware & Security

- **Culprit** = the cause of a problem (used for both people and things, e.g., "malware is the culprit").
- **Removing stubborn malware**: boot into **Safe Mode** (loads only essential drivers/services, stopping the malware from actively running) then run antimalware tools or **System Restore**.
- **Renamed system files** → sign of malware infection. Fix options: (1) restore from backup, (2) run antivirus software.
- **Trojan horse**: malware disguised as legitimate software; once installed (e.g., via email), it can **log keystrokes** and steal sensitive data.
- **Kernel panic (Linux)**: critical, unrecoverable OS error — often caused by a **corrupted driver**.
- **BIOS/UEFI password**: a password required *before* the OS even starts booting; protects hardware-level settings (boot order, etc.).
- **Sandboxing (mobile apps)**: running each app in an isolated container so malicious code can't reach the rest of the system — prevents malware from infecting the whole device.
- **DRM (Digital Rights Management)**: access-control technology to prevent unauthorized copying/distribution of software and digital content.

### Authentication
- **MFA (Multi-Factor Authentication)**: combining 2+ independent verification methods — something you know (password), something you have (token), something you are (fingerprint). Required for policies needing 3+ factors.
- **EFS (Encrypting File System)**: Windows feature to encrypt **individual files/folders** on an **NTFS** volume (vs. BitLocker, which encrypts the whole drive).
- **Local Security Policy tool**: used to configure password/account-lockout rules on a **standalone PC not joined to a domain**.

### Policy & compliance
- **Acceptable Use Policy**: governs whether employees may use company time/resources (e.g., during work hours) for personal business — relevant when an employee is caught buying personal supplies at work.
- **Redact**: to black out or replace sensitive info (like plaintext passwords) in a file before sharing it — e.g., replacing passwords with placeholders before emailing a troubleshooting file to a level-2 technician, sharing real credentials only via a separate secure channel if truly necessary.
- **Disaster recovery policies/procedures**: fall under the "**operations and planning**" category of IT documentation.

---

## Customer / Help Desk Best Practices

- **Let the customer finish talking** before asking follow-up questions — ensures full details are gathered and shows professional **courtesy** (politeness/respect).
- **Ask permission before placing a customer on hold.**
- **When dealing with an angry customer**: (1) let them explain without interrupting — this helps **defuse** (calm/de-escalate) their frustration, (2) redirect the conversation toward solving the actual problem.
- **Level-1 technician should gather**: (1) description of the problem, (2) details of recent changes to the computer, (3) contact information.
- **Unsolicited marketing emails to a past client** = policy violation. Correct approach: ask the customer if they *want* to receive info about new products/services, and check company policy on personal communication during work time.

---

## Mobile Devices

- **GPS — three key functions**:
  1. **Device tracking** — locate a lost/stolen device
  2. **Navigation** — **turn-by-turn directions** (step-by-step guidance at each turning point) from current location to a destination
  3. **Specialized search results** — location-aware results (nearby restaurants, shops, etc.)
- **Live Tiles** (Windows Phone-style home screen): dynamic tiles showing real-time content (texts, photos, news) — not just static app icons.
- **Android widgets**: often directly tied to an app; touching the widget launching the associated app is **normal behavior**, not a bug.
- **Slow mobile device performance**: often caused by a **power-intensive app running in the background**, which can **deplete** (use up/drain) CPU and memory resources.

---

## Programming Languages

- **Compiled languages** (C, C++, Rust): entire source code translated in advance via a **compiler** into a standalone executable file — must finish compiling before running; faster runtime execution.
- **Scripting/Interpreted languages** (Python, JavaScript): code is read and executed **line by line** at runtime — no separate compile step; easier/faster to modify but generally slower to execute.

---

## Vocabulary Glossary

| Word | Meaning |
|---|---|
| populated | automatically filled in (e.g., form fields with saved data) |
| opted | chose / decided (past tense of "opt") |
| deplete | to use up / drain / exhaust a resource |
| culprit | the cause of a problem (not necessarily a person) |
| redact | to black out / remove sensitive info from a document |
| courtesy | politeness, respect, consideration |
| defuse | to calm down a tense situation (often confused with "diffuse," meaning to spread out) |
| compile / compilation | translating full source code into machine-executable code in advance |
| turn-by-turn | step-by-step navigation directions at each turning point |

---


