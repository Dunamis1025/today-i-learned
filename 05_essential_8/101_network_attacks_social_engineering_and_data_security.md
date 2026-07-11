# Network Security — Study Notes

## 1. Network Attacks

### Reconnaissance Phase (Attack Steps)
1. **Information query** — gather basic info about the target.
2. **Ping sweep** — check which devices are active on the network.
3. **Port scan** — identify open ports on active hosts.
4. **Vulnerability scanner** — search for known security weaknesses.
5. **Exploitation tools** — attack the discovered vulnerabilities.

### Types of TCP/IP Attacks
| Attack | Description |
|---|---|
| **DoS** (Denial of Service) | Overwhelms a system with traffic from one source, making it unavailable. |
| **DDoS** (Distributed DoS) | Same as DoS but launched from multiple sources simultaneously. |
| **DNS Poisoning** | Corrupts DNS records to redirect users to malicious sites. |
| **Man-in-the-Middle (MitM)** | Intercepts communication between two parties to eavesdrop/modify data. |
| **Replay** | Captures valid transmissions and resends them later to impersonate a user. |
| **Spoofing** | Fakes an IP/MAC address to gain unauthorized access. |
| **SYN Flood** | Floods a server with fake connection requests to exhaust resources. |

### Zero-Day vs Zero-Hour
- **Zero-day**: the day a vulnerability is discovered by the vendor (before a patch exists).
- **Zero-hour**: the moment the exploit is actually used in an attack.
- Networks stay vulnerable during the gap between discovery and patch release → requires rapid response and constant monitoring.

### Defense-in-Depth (Layered Security)
| Tool | Function |
|---|---|
| **VPN** | Encrypted tunnel for secure remote access to the internal network. |
| **Firewall** | Filters traffic between internal/external networks, blocks unauthorized access. |
| **IPS** (Intrusion Prevention System) | Monitors traffic in real time and blocks detected attacks instantly. |
| **AAA Server** | Authenticates users and manages access permissions. |
| **ESA/WSA** | Filters malicious email (ESA) and web traffic (WSA) — spam, malware, phishing. |
| **Device Hardening** | Strengthens security settings on routers/switches to prevent tampering. |

---

## 2. Social Engineering

Attacks the "human" element instead of technology.

| Technique | Description |
|---|---|
| **Phishing** | Fake email from a trusted org to steal info or install malware. |
| **Spear Phishing** | Phishing tailored to a specific researched individual. |
| **Whaling** | Spear phishing aimed at executives/high-level targets. |
| **Baiting** | Leaves an infected device (e.g., USB) as bait; victim plugs it in. |
| **Pretexting** | Fabricates a scenario to justify requesting sensitive info. |
| **Impersonation** | Pretends to be someone else (new employee, vendor, etc.) to gain trust. |
| **Shoulder Surfing** | Watches over someone's shoulder to see passwords/data. |
| **Tailgating** | Follows an authorized person into a secure area without credentials. |
| **Dumpster Diving** | Searches trash for discarded confidential documents. |
| **Quid Pro Quo / Something for Something** | Offers a fake benefit (gift, survey reward) in exchange for info. |
| **Spam** | Mass unsolicited emails, often carrying malicious links. |

### Practice Quiz Answers (from official image)
| Scenario | Answer |
|---|---|
| USB found in parking lot, plugged in → malware installed | Baiting |
| Config file copy found in trash | Dumpster diving |
| "HVAC technician" requests access to secure area | **Impersonation** |
| Clicked bank-impersonation email link → malware | Phishing |
| Fake bank asks for personal/financial info to "verify identity" | **Pretexting** |
| Coworker watches supervisor log in | Shoulder surfing |
| Survey email offering a free T-shirt for personal info | **Something for Something (Quid pro quo)** |
| Mass malicious links sent to random people | Spam |
| Targeted phishing attack aimed at a CEO | Spear phishing |
| "Forgot my badge" follows you into secure building | Tailgating |

> Note: earlier draft answers for HVAC/bank/T-shirt scenarios were corrected above based on the official answer key.

### Protecting Against Social Engineering
- Educate employees on risks; verify identities before granting access.
- Dispose of confidential documents per policy.
- Never share usernames/passwords.
- Don't store passwords insecurely.
- Don't open emails from unknown sources.
- Don't post work info on social media.
- Never reuse passwords.
- Always lock/log out when away from your desk.
- Report suspicious activity immediately.

---

## 3. Security Policy & Physical Security

### Categories of Security Policy
- **Identification & Authentication** — who can access the system.
- **Password Policy** — rules for creating/managing passwords.
- **Acceptable Use Policy** — how resources may be used.
- **Remote Access Policy** — safe external connections to the network.
- **Network Maintenance Policy** — device management/repair procedures.
- **Incident Handling Policy** — how to respond to security incidents.

### Physical Security
- **Access Control**: restrict entry to buildings, restricted zones, and equipment rooms.
- **Locking Mechanisms**: automatic locks, secured doors.
- **Authentication of Visitors**: checkpoints, visitor logs, photo ID badges.
- **Advanced Tracking**: smart cards / RFID badges log who accessed where and when.

### Mantrap
A small room with two doors that prevents tailgating — the first door must fully close and lock before the second door can open.

### Securing Hardware
- Install network equipment in restricted, secured areas; protect cabling with conduits.
- Restrict switch port access to authorized personnel; lock ports via software.
- Use USB locks/security cables for equipment in public areas.
- Use **EMM** (Enterprise Mobility Management) software to manage/secure mobile devices and separate corporate data from unauthorized apps.

### Lock Types
| Lock | Description |
|---|---|
| Biometric | Fingerprint, voiceprint, retina scan |
| Conventional | Traditional lock, separate from the door handle |
| Deadbolt | Requires the key to be used directly in the handle |
| Token-based | Requires a smart card or RFID proximity key |
| Electronic | Requires a PIN or code combination |

---

## 4. Data Protection

### Why Data Matters
Loss of data can cause: brand/reputation damage, loss of competitive advantage, customer attrition, revenue loss, legal penalties.

### Core Protections
- **Backups** — regular, combining full + incremental; must be password-protected and periodically validated for restorability; stored at an approved secure off-site location.
- **File/Folder Permissions** — apply the **Principle of Least Privilege** (users get only the access they need); permissions can be inherited/propagated to subfolders.
  - Permission inheritance rules:
    - Moved within same volume → keeps original permissions.
    - Copied within same volume → inherits new permissions.
    - Moved/copied to a different volume → inherits new permissions.
- **Encryption (EFS)** — Windows' Encrypting File System encrypts files so only the encrypting user account can access them. Enable via right-click → Properties → Advanced → "Encrypt contents to secure data." Encrypted items show in **green** in File Explorer.
- **DLP (Data Loss Prevention)** — software that identifies confidential data and automatically blocks policy-violating transfers (e.g., to removable media or email).

---

## 5. BitLocker & BitLocker To Go

BitLocker encrypts an entire drive so data can't be read without the correct password/key.

### BitLocker To Go (removable drives, e.g. USB)
1. Control Panel → BitLocker Drive Encryption → select the removable drive → Turn on BitLocker.
2. Set a password (or smart card).
3. Save/print the **recovery key** (critical backup if password is lost).
4. Choose to encrypt: **used space only** vs **entire drive** (entire drive is safer — it also wipes traces of previously deleted files).
5. Choose **Compatible mode** if you'll use the drive on multiple/older systems; New encryption mode if only on the latest Windows.
6. Start encrypting.
7. To decrypt: BitLocker menu → Turn off BitLocker.

### BitLocker on the OS/system drive
1. Requires a **TPM (Trusted Platform Module)** — a security chip on the motherboard that stores encryption keys, certificates, and passwords securely.
2. If no TPM is available/enabled: use `gpedit.msc` (Local Group Policy Editor) → Administrative Templates → Windows Components → BitLocker Drive Encryption → Operating System Drives → **"Require additional authentication at startup"** → Enable → allows software-based encryption without TPM.
3. Set a password, save the recovery key, choose encryption scope and mode, run the BitLocker system check, then restart.
4. After setup, the password must be entered at every boot before Windows loads.

### Lab Q&A
- **Q: Why is it important to save a BitLocker recovery key?**
 A: It's the only way to unlock/access your data if you forget your password or lose your smart card.
- **Q: What is the function of a TPM in relation to BitLocker?**
 A: A hardware security chip that stores the disk encryption key, tying the encrypted disk's use to that specific computer.

---

## 6. Data Destruction

Simply deleting files or reformatting a drive is **not enough** — remnants of the data physically remain on the media and can be recovered with the right tools. To truly eliminate confidential data, stronger methods are required:

| Method | Description |
|---|---|
| **Data Wiping Software** | Overwrites the entire drive with meaningless data multiple times, making original data unrecoverable. |
| **Degaussing** | Uses a powerful magnetic field to erase the magnetic recording on a hard drive. Expensive equipment, but can process large volumes quickly. |
| **Physical Destruction** | Shredding, grinding, or hammering the drive to pieces. This is the primary method for **SSDs**, since they use flash memory (not magnetic) — degaussing has no effect on them. |

### Recycling vs. Destruction
- **Recycling**: a drive that's been thoroughly wiped can be reformatted and reused elsewhere.
- **Destruction**: for highly sensitive data, physical destruction via a professional service is the safest option — request a **Certificate of Destruction** as proof.

### Formatting Types
- **Low-level format**: done at the factory; marks the physical sector locations on the disk.
- **Standard (high-level) format**: performed by the OS; creates the logical file system so it can organize/manage files.

### Matching Exercise (Answers)
| Term | Description |
|---|---|
| **Standard format** | Creates the file system and boot sector on a disk. |
| **Degaussing wand** | Handheld magnetic tool used to erase data on hard drive platters. |
| **Data wiping software** | Repeatedly overwrites data to make it unrecoverable. |
| **Electromagnetic degaussing device** | Machine generating a powerful magnetic field to destroy data almost instantly. |
| **Low-level format** | Marks physical disk locations at the factory during manufacturing. |
