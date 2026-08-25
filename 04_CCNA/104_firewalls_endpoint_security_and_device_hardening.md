# Network Security Study Notes — Defense-in-Depth, Device Hardening & SSH

> Summary of topics covered in CCNA-style coursework (Cisco Networking Academy, Ch. 16.3–16.4) plus hands-on Packet Tracer lab.

---

## 1. The Defense-in-Depth Approach (16.3.1)

No single security device can stop every attack, so networks are protected with **layered security controls** rather than a single line of defense.

Key devices in a layered network:

| Device | Purpose |
|---|---|
| **IPS** (Intrusion Prevention System) | Detects and blocks traffic matching known attack signatures in real time |
| **ASA Firewall** | Enforces perimeter security; filters TCP/IP-based attacks |
| **ESA/WSA** (Email/Web Security Appliance) | Inspects email and web traffic for threats |
| **DHCP Snooping** | Ensures switches only trust legitimate DHCP servers (prevents rogue DHCP) |
| **Dynamic ARP Inspection (DAI)** | Prevents ARP spoofing/poisoning attacks |

---

## 2. Keep Backups (16.3.2)

Backups are essential for recovering from compromise or data loss. Backup policy considerations:

| Consideration | Description |
|---|---|
| **Frequency** | Backups performed on a regular schedule, per policy |
| **Validation** | Regularly verify backup integrity/completeness |
| **Storage** | Store backups in a separate, secure location |
| **Security** | Protect backup files with strong passwords/encryption |

---

## 3. Upgrade, Update, and Patch (16.3.3)

New vulnerabilities are constantly discovered, so devices must be kept current with:
- Software **upgrades**
- Security **updates**
- Vulnerability **patches**

Example: Windows Update automatically manages OS-level patching.

---

## 4. Authentication, Authorization, and Accounting — AAA (16.3.4)

Modeled on a credit card analogy:

| AAA Component | Question Answered | Credit Card Analogy |
|---|---|---|
| **Authentication** | Who are you? | Verifying the card/identity |
| **Authorization** | What are you allowed to do? | Checking your spending limit |
| **Accounting** | What did you actually do? | Logging transactions/statement |

An **AAA server** is the device other network devices (routers, switches, firewalls) query to authenticate and authorize management access.

---

## 5. Firewalls (16.3.5)

A firewall **controls traffic between two or more networks** to prevent unauthorized access.

**Basic operation:**
- Traffic initiated from **inside → outside** (and its return traffic) is **permitted**
- Traffic initiated from **outside → inside** is **denied** by default

**DMZ (Demilitarized Zone) topology:**
- A middle zone between the internal network and the internet
- Houses servers that must be reachable by external users (e.g., web servers)
- Keeps the internal network isolated and protected while still allowing public services

---

## 6. Types of Firewalls (16.3.6)

| Type | Filters based on... |
|---|---|
| **Packet Filtering** | IPv4/IPv6 header info (source/destination address) |
| **Application Filtering** | Application/port in use |
| **URL Filtering** | Specific website access |
| **Stateful Packet Inspection (SPI)** | Whether incoming traffic is a legitimate response to an outbound request (most secure — unsolicited traffic treated as a potential DoS attempt) |

---

## 7. Endpoint Security (16.3.7)

An **endpoint** = any individual device connected to a network (laptop, desktop, smartphone, tablet, etc.).

Endpoints are high-risk targets because:
- They are directly operated by humans (human error)
- They are directly connected to the internet

**Mitigation:** install **antivirus software** and host-based intrusion prevention on each endpoint.

---

## 8. Passwords (16.4.2)

Guidelines for strong network device passwords:
- Minimum ~8–10+ characters
- Avoid dictionary words, names, common sequences (e.g., "qwerty")
- Use deliberate misspellings, mixed case, numbers, and symbols
- Change passwords periodically
- Never write passwords in visible/accessible locations
- **Passphrases with spaces** are considered strong and easy to remember

| Weak Password Examples | Why Weak |
|---|---|
| Dictionary words | Easy to guess via dictionary attack |
| Names of people/pets | Predictable, socially guessable |
| Birthdays | Easily discoverable |

---

## 9. Additional Password Security (16.4.3)

Techniques beyond just choosing a good password:

| Technique | Command Example | Purpose |
|---|---|---|
| Encrypt stored passwords | `service password-encryption` | Prevents plaintext passwords in config files |
| Enforce minimum length | `security password min-length 10` | Rejects short passwords |
| Block brute-force login attempts | `login block-for 180 attempts 4 within 120` | Locks out login for 180s after 4 failed attempts in 120s |
| VTY session timeout | `exec-timeout 6` | Auto-logout after idle time (minutes) |

---

## 10. Enable SSH (16.4.4)

- **Telnet** sends data in **plaintext** — vulnerable to interception/eavesdropping
- **SSH (Secure Shell)** encrypts remote management sessions — the modern standard

**SSH configuration workflow:**
1. Set hostname
2. Set domain name (`ip domain-name`) — required before generating crypto keys
3. Generate RSA key pair (`crypto key generate rsa`, e.g. 1024-bit)
4. Create local user account (`username <name> secret <password>`)
5. Restrict VTY lines to SSH only (`transport input ssh`)
6. Set VTY login method to local database (`login local`)
7. Test connection from a client

---

## 11. Disable Unused Services (16.4.5)

Default-enabled but unused services are potential attack surfaces ("open doors"). Best practice: identify open ports/services and disable anything not required (e.g., HTTP, CDP if unneeded).

---

## 12. Hands-On Lab: Packet Tracer — Configure Secure Passwords and SSH

**Topology:**

| Device | Interface | IP Address | Subnet Mask | Default Gateway |
|---|---|---|---|---|
| RTA (Router) | G0/0 | 172.16.1.1 | 255.255.255.0 | N/A |
| PCA (PC) | NIC | 172.16.1.10 | 255.255.255.0 | 172.16.1.1 |
| SW1 (Switch) | VLAN 1 | 172.16.1.2 | 255.255.255.0 | 172.16.1.1 |

### Router (RTA) Configuration Steps
```
enable
configure terminal
hostname RTA
interface g0/0
 ip address 172.16.1.1 255.255.255.0
 no shutdown
 exit
service password-encryption
security password min-length 10
enable secret <strong_password>
no ip domain-lookup
ip domain-name CCNA.com
username admin secret <strong_password>
crypto key generate rsa        ! 1024 bits
login block-for 180 attempts 4 within 120
line vty 0 4
 transport input ssh
 login local
 exec-timeout 6
 end
copy running-config startup-config
```

Verified SSH access from PCA:
```
C:\> ssh -l admin 172.16.1.1
Password: ****
RTA>
```
✅ Successful SSH login confirmed encrypted remote access was working.

### Switch (SW1) Configuration Steps
Same general process, plus disabling unused ports:
```
hostname SW1
interface vlan 1
 ip address 172.16.1.2 255.255.255.0
 no shutdown
 exit
ip default-gateway 172.16.1.1
interface range f0/2-24, g0/2
 shutdown              ! disable all unused ports, keep only F0/1 and G0/1 active
exit
service password-encryption
enable secret <strong_password>
no ip domain-lookup
ip domain-name CCNA.com
username admin secret <strong_password>
crypto key generate rsa        ! 1024 bits
line vty 0 15                  ! NOTE: switch has 16 VTY lines (0-15), not 5 like the router
 transport input ssh
 login local
 exec-timeout 6
 end
copy running-config startup-config
```

### Troubleshooting Notes (Key Lessons Learned)

1. **`login block-for` not supported on this switch IOS image.**
   Attempting `login block-for 180 attempts 4 within 120` on SW1 repeatedly returned `% Invalid input detected`. Verified with `login ?` → command not recognized. This is a known Packet Tracer switch IOS limitation, not a user error — this feature is router-only on some IOS images.

2. **Switch VTY line range differs from router.**
   Initial `line vty 0 4` only configured 5 of the switch's 16 VTY lines (0–15). Packet Tracer's "Check Results" scoring flagged VTY Line 15 as failing (Login/Transport Input/Timeout all unset). 
   **Fix:** re-run the VTY block using `line vty 0 15` to cover the full range.
   
   **Takeaway:** Always confirm the actual number of VTY lines available on a given device (`line vty ?`) rather than assuming router and switch platforms match.

3. **Result:** After correcting the VTY range, Packet Tracer reported:
   > "Congratulations Guest! You completed the activity."

---

## 13. Related Lab (Not Yet Completed): "Configure Network Devices with SSH"

A parallel lab exists that assumes **physical Cisco hardware** (Cisco 4221 router, Cisco 2960 switch) and a real terminal client (**Tera Term**) rather than Packet Tracer.

**Topology:**

| Device | Interface | IP Address |
|---|---|---|
| R1 | G0/0/1 | 192.168.1.1 |
| S1 | VLAN 1 | 192.168.1.11 |
| PC-A | NIC | 192.168.1.3 |

**Differences from the Packet Tracer lab:**
- Console password (`cisco`) and privileged EXEC password (`class`) are set explicitly
- A **login banner** (unauthorized access warning) is configured
- VTY lines allow **both Telnet and SSH** (`transport input telnet ssh`), not SSH-only
- Includes using the **switch's built-in SSH client** to SSH *from* S1 *into* R1 (`ssh -l admin 192.168.1.1`), plus session suspend/resume via `Ctrl+Shift+6, x`

**Since real hardware isn't available**, this lab can be replicated in Packet Tracer using the same commands/logic as the completed lab above (Section 12), adjusting IP addressing and the Telnet+SSH VTY policy accordingly. Planned for a future session.

---

## Quick-Reference Command Cheat Sheet

```
! Password hardening
service password-encryption
security password min-length 10
enable secret <password>
username <user> secret <password>

! SSH setup
no ip domain-lookup
ip domain-name <domain>
crypto key generate rsa

! Brute-force protection (router only, in this PT image)
login block-for <seconds> attempts <n> within <seconds>

! Restrict remote access to SSH
line vty 0 4        ! (router: check actual range)
 transport input ssh
 login local
 exec-timeout <minutes>

! Disable unused switch ports
interface range f0/2-24, g0/2
 shutdown

! Save config
copy running-config startup-config
```

---
*Notes compiled from Cisco Networking Academy CCNA coursework (Ch. 16.3–16.4) and a completed Packet Tracer lab session.*
