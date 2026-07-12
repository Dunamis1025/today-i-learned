# Computer Security & Networking Study Notes

## 1. Securing a Workstation

### Layers of Protection
- **BIOS/UEFI**: Prevents the OS from loading or settings from being changed without a password. Blocks attackers from booting from an external USB to steal files.
- **Login**: Prevents unauthorized local access to the computer.
- **Network**: Prevents unauthorized access to network resources.

### Windows Sign-in Options
- **Password**: Traditional text-based authentication.
- **Windows Hello**: Faster, more convenient sign-in using a PIN, fingerprint, or facial recognition.
  - PIN setup is required before fingerprint/face recognition can be configured.
  - Fingerprint requires a fingerprint reader; face recognition requires a compatible camera.
- **Picture Password**: Unlock by performing specific gestures on a chosen image.
- **Dynamic Lock**: Automatically locks the PC when a paired device (e.g., phone) moves out of Bluetooth range.

### Local Password Management
- Managed via **Control Panel > User Accounts**.
- Enable **screen saver + "On resume, display logon screen"** to force re-authentication after inactivity.

### Password Best Practices
| Rule | Guideline |
|---|---|
| Length | Minimum 8 characters |
| Complexity | Avoid common/guessable words; mix character types and spaces |
| Variety | Unique password per site/device — never reuse |
| Secrecy | Never write down or share passwords |

### Single Sign-On (SSO)
- One authentication grants access to multiple linked services (e.g., Microsoft account → OneDrive, Outlook).
- **Pros**: Convenience — no repeated logins across services.
- **Cons**: Single point of failure — one compromised account exposes all linked services.
- Other real-world example: Google account → Gmail, Drive, YouTube.

---

## 2. Windows Local Security Policy (`secpol.msc`)

Used on **standalone computers** (not part of an Active Directory domain) to enforce security settings individually.

### Account Policies → Password Policy
| Setting | Function |
|---|---|
| Enforce password history | Blocks reuse of a set number of previous passwords |
| Maximum password age | Forces password change after X days |
| Minimum password age | Minimum time before a password can be changed again (stops rapid cycling to bypass history) |
| Minimum password length | Minimum required character count |
| Password complexity requirements | Must exclude account name; must include 3 of 4: uppercase, lowercase, numbers, symbols |
| Store passwords using reversible encryption | **Should always stay disabled** — equivalent to storing plaintext passwords |

### Account Lockout Policy
Protects against **brute-force**, **dictionary**, and **rainbow table** attacks (attacks that guess or use precomputed password/hash tables).

| Setting | Function |
|---|---|
| Account lockout threshold | Number of failed attempts allowed before lockout |
| Account lockout duration | How long the account stays locked (e.g., 30 min) |
| Reset account lockout counter after | Time after which the failed-attempt counter resets to zero |

### Local Policies
- **Audit Policy**: Logs successful/failed login events (e.g., "Audit account logon events").
- **User Rights Assignment**: Controls what actions specific users/groups can perform.
- **Security Options**: Additional settings such as inactivity timeouts and custom logon banners.

### Exporting/Importing Policies
Useful for applying identical settings across multiple standalone machines:
1. `Action > Export Policy` → save as `.inf` file.
2. Copy file to target machine.
3. `Action > Import Policy` → apply instantly.

### Example Company Policy (Lab Scenario)
- Passwords: min 8 chars, changed every 90 days, min 1 day between changes, no reuse of last 8 passwords, 3-of-4 complexity.
- Lockout: 5 failed attempts → locked for 5 minutes.
- Auditing: all events enabled.
- Auto logout after 30 min inactivity.
- Custom logon warning banner required.

---

## 3. Users and Groups Management

### Tools
- **User Account Control (UAC)**: Manages account creation/deletion and warns before privilege-elevating actions (malware prevention).
- **Local Users and Groups Manager**: Detailed local account/group management, including permissions.

### Default Built-in Accounts
- **Administrator**: Full control, disabled by default.
- **Guest**: Temporary use, profile deleted on logoff, disabled by default.

### Default Groups
| Group | Permissions |
|---|---|
| Administrators | Full system control |
| Users | Run applications, use printers — no system-wide changes |
| Guests | Very limited, temporary access |

**Best practice**: Use a standard **Users** account for daily tasks; only use Administrator credentials when necessary (reduces malware/trojan risk).

### Folder Permission Management
- Set via **Properties > Security tab**.
- Permissions can be **Allowed** or **Denied** per user/group.
- **Disable inheritance** to stop a folder from inheriting parent folder permissions, allowing precise custom control.
- Accounts can be **disabled** (blocks login, preserves data) instead of deleted (harder to reverse) — safer for departing employees.

### Active Directory (Domain Environment)
- A centralized database managing all users, computers, and services across an organization.
- **Domain accounts** (unlike local accounts) can log in from any computer joined to the domain.
- Managed via **Active Directory Users and Computers**.
- Key tasks: create accounts, force password change at first login, unlock locked accounts, disable/delete accounts, manage security groups.

---

## 4. Windows Firewall

A firewall inspects incoming/outgoing traffic and blocks unauthorized external access while allowing safe outbound traffic.

### DMZ (Demilitarized Zone)
- Isolated network segment for public-facing servers (web, mail).
- External users can only reach the DMZ — the real internal network stays protected.

### Basic Firewall Controls
- **Allowed Apps list**: Grant/deny specific applications network access.
- ⚠️ Too many exceptions = larger attack surface = weaker security.
- Network profiles: **Private (home)**, **Public (café/airport)**, **Domain (work)** — each applies a different security strictness level.

### Windows Defender Firewall with Advanced Security
| Feature | Purpose |
|---|---|
| Inbound Rules | Control traffic coming into the PC (by port, protocol, program, user) |
| Outbound Rules | Control traffic leaving the PC |
| Connection Security Rules | Enforce encryption/authentication between two computers |
| Monitoring | View currently active rules and real-time traffic status |

### Lab Insight
- Disabling "File and Printer Sharing" blocks other PCs from accessing shared folders.
- ICMP (ping) settings can be customized to control whether the PC responds to network discovery/ping requests.

---

## 5. SOHO Router (Home/Small Office) Firewall Features

| Feature | Function |
|---|---|
| NAT (Network Address Translation) | Hides internal private IPs behind one public IP |
| Port Forwarding | Routes specific incoming traffic to a specific internal device (e.g., hosting a web server) |
| Port Blocking | Closes unnecessary/risky ports |
| MAC Address Filtering | Only allows approved device hardware addresses onto the network |
| Website Filtering | Blocks access to known malicious/unwanted sites |
| Port Triggering | Temporarily opens ports only while a specific app is actively using them (more secure than permanent forwarding) |
| UPnP | Auto-configures port forwarding for convenience — **security risk**, exploitable by malware; recommended to disable |
| Firmware Updates | Manufacturer-issued updates improving performance and patching vulnerabilities |

### Firewall Implementation Types
- **Packet Filter**: Allows/blocks based on IP/port rules.
- **Stateful Packet Inspection (SPI)**: Tracks full connection state to detect unsafe traffic.
- **Application Layer**: Filters based on specific applications.
- **Proxy**: Relays traffic on behalf of users, hiding internal network structure.

---

## 6. Web Security

### Multi-Factor Authentication (MFA)
- Combines password + a second factor (e.g., SMS code) for stronger login security.

### Browser Extensions & Plugins
- **Extensions**: Add browser functionality — only install from trusted/official sources.
- **Plugins**: Handle multimedia content — mostly deprecated due to high security risk.
- Best practices: install only from official stores, keep updated, use built-in password managers.

### TLS & Digital Certificates
- **TLS (Transport Layer Security)**: Encrypts data in transit and verifies website authenticity.
- Users should check certificate validity in the browser; installing untrusted certificates is a major risk.

### Browser Privacy Tools
- **Ad Blockers**: Filter out unwanted ads.
- **Pop-up Blockers**: Prevent unrequested windows from opening automatically.
- **Clearing browsing history**: Manually deletes visited sites, cookies, cached files.
- **InPrivate/Incognito Mode**: Temporary session — automatically discards history/cookies/site data when the window closes.

### Microsoft Edge-Specific Features
- **SmartScreen Filter**: Detects phishing sites and malicious downloads automatically.
- **ActiveX Filtering**: Blocks legacy ActiveX controls (largely obsolete, high security risk).

---

## 7. Device & OS Security Maintenance

### Auto-Play / Auto-Run
- Older "Auto-Run" auto-executed files from USB/CD — heavily exploited by malware.
- Modern "Auto-Play" lets users choose the action; **best practice: disable entirely**.

### Patches & Service Packs
- Manufacturers regularly release **patches** (small fixes) and **service packs** (larger update bundles) to close security vulnerabilities.
- Keeping systems updated via Windows Update is one of the most effective defenses against attacks.

### Permissive vs. Restrictive Settings
| Type | Description |
|---|---|
| Permissive | All ports/access open by default — easy setup, high vulnerability |
| Restrictive | Everything blocked except explicitly allowed — harder to configure, much more secure |

---

## 8. Encryption & Cryptographic Concepts

### Hash Encoding (Integrity)
- Creates a unique **message digest** (numeric fingerprint) via a one-way mathematical function.
- Any change to the original data produces a completely different hash.
- Cannot be reversed to reveal the original message.
- Algorithms: **SHA** (current standard), **MD5** (older, being phased out).

### Symmetric Encryption (Confidentiality)
- Same key used to encrypt and decrypt.
- Both sender and receiver must share the identical secret key.
- Examples: **AES** (modern standard), **3DES** (older).

### Asymmetric Encryption (Public/Private Key Pair)
- **Public key**: freely distributed, used to encrypt.
- **Private key**: kept secret, used to decrypt.
- **Use case 1 – Confidential messaging**: Anyone encrypts with the recipient's public key; only the recipient's private key can decrypt.
- **Use case 2 – Digital signatures**: Sender encrypts (signs) with their own private key; anyone can verify using the sender's public key, proving authenticity.
- **Use case 3 – Smart cards**: A private key + digital certificate stored on a hardware token authenticates the user by decrypting a server-issued challenge.
- Most popular algorithm: **RSA**.

---

## 9. Wireless Network Security

### Key Terms
| Term | Meaning |
|---|---|
| SSID | The visible name of a wireless network |
| WPA/WPA2/WPA3 | Encryption/authentication standards for secure Wi-Fi access |
| UPnP | Auto-configuration feature; convenient but a known security risk |
| Firmware | Router's internal OS/software, periodically updated by the manufacturer |
| Firewall | Filters incoming/outgoing traffic to protect the network |

### Wireless Configuration Best Practices
- **Antenna placement**: Position for optimal coverage; avoid trying to cover excessive area with one device.
- **Signal power**: Avoid setting too high (causes interference) — auto/moderate settings are often best.
- **Change default admin credentials** immediately upon setup.
- **Use static IPs** where possible instead of DHCP for tighter control.
- **Change the default SSID** (default reveals router brand/model).
- **Disable SSID broadcast** for an extra layer of obscurity (not full security, but reduces casual discovery).

### Wireless Authentication Methods (Weakest → Strongest)
1. **Open**: No password — anyone can connect.
2. **Shared Key**: Older, weak authentication method.
3. **WEP**: Original standard; encryption key doesn't change — easily cracked.
4. **WPA**: Improved via TKIP (key changes per packet).
5. **WPA2**: Current standard; uses **AES** encryption — strong security.
6. **WPA3**: Latest standard with further security enhancements.

> **Rule of thumb**: Always use WPA2 or higher when configuring a wireless network.

### WPS (Wi-Fi Protected Setup)
- Convenient one-button or PIN-based pairing method.
- **Security flaw**: vulnerable to brute-force PIN attacks.
- **Best practice**: disable WPS entirely.

---

## Quick Reference: True/False Concepts Covered

- Account & password policies help prevent brute-force attacks — **True**
- Local Security Policy settings can be exported/imported between hosts — **True**
- Audit Policy logs both successful and failed login attempts — **True**
- PIN alone enables facial/fingerprint recognition — **False** (PIN is a separate numeric method; biometrics are separate Windows Hello features)
- Local passwords are managed under Personalization — **False** (managed under User Accounts)
