# Network Security — Part 3: Secure Administrative Access & Subnetting

**Course:** VU23218 — Implement Network Security Infrastructure
**Topic:** Control Administrative Access for Routers + IPv4 Subnetting Fundamentals

---

## 1. Why Edge Routers Matter

- An **edge router** sits at the boundary between a private network and an external network (e.g. the internet), so it's often the **first target for attackers**.
- With only **one router** at home, that single device plays **both the edge and internal role** at the same time.
- Router functions can be summarized with **C.O.O.L.**:
  - **C**onnectivity — bridges local devices to the internet
  - **O**utbound — manages traffic leaving the private network
  - **O**ptimization — routes traffic efficiently to reduce lag
  - **L**ine of defense — firewalls/filtering to protect internal systems

### Edge Router Security Approaches
1. **Single Router** — one router connects LAN to internet; all security policies live on it.
2. **Defense-in-Depth** — multiple security layers before traffic reaches the LAN (edge router → firewall → internal router).
3. **DMZ (Demilitarized Zone)** — a buffer zone between trusted and untrusted networks for public-facing servers (web, email, DNS, FTP, proxy servers) so a breach there doesn't expose the internal LAN.

### Three Areas of Router Security
1. **Physical** — secure locked room, restricted access, UPS/backup power.
2. **Operating System** — max available memory (mitigates DoS attacks), latest stable OS version, secure config/image backups.
3. **Router Hardening** — restrict access, disable unused ports/interfaces and unnecessary default services (attackers can use them to gather info).

---

## 2. Secure Administrative Access — Core Tasks

To secure administrative access to a device:
- Restrict device accessibility
- Log and account for all access
- Authenticate access
- Authorize actions
- Present legal notification (banner)
- Ensure confidentiality of data

### AAA Concept (Authentication, Authorization, Accounting)
- **Authentication** — verifying username/password match (stored as a **hash**, not plaintext).
- **Authorization** — determining what an authenticated user is *allowed* to do, based on role.
- **Accounting/Logging (syslog)** — recording who accessed what, when, and what they changed/deleted, for traceability.

### Local vs Remote Access
- **Local access** — physical connection via console cable; required for **initial configuration** (no GUI exists yet).
- **Remote access** — Telnet, **SSH**, HTTP, HTTPS, SNMP once basic config is in place. Telnet is avoided in favor of SSH (Telnet sends data in plaintext).

---

## 3. Password Security

### Weak vs Strong Passwords
- Weak: dictionary words, names, birthdays, simple word+number combos (e.g. `secret`, `smith`, `bob1967`).
- Strong: random alphanumeric + symbols (e.g. `12^h u4@1p7`).

### Key Commands
```
security passwords min-length 8      ! enforce minimum password length
enable secret <password>             ! encrypted privileged-mode password
username <name> secret <password>    ! local user account (hashed)
service password-encryption          ! encrypts remaining plaintext passwords (weak, type 7)
no ip domain-lookup                  ! stops router from treating typos as domain names (avoids delay)
ip domain-name <domain>              ! required before generating SSH keys
login block-for <secs> attempts <n> within <secs>   ! brute-force protection
```

### Password Encryption Types (Cisco IOS)
| Type | Meaning |
|---|---|
| 0 | No encryption (plaintext) |
| 5 | MD5 hash (stronger, used by `enable secret`) |
| 7 | Weak encryption (Cisco's own algorithm via `service password-encryption`, easily reversible online) |
| 8 / 9 | Newer, stronger — scrypt (9) and PBKDF2 w/ SHA-256, 256-bit (8); recommended over MD5 today |

### Hashing (why "reset" not "retrieve")
- A password is never stored as-is — it's converted via a **one-way hash function** (e.g. MD5, SHA-1) into a fixed-length string.
- Hashing ≠ encryption: it **cannot be reversed** to get the original string back.
- This is why a forgotten password can only be **reset**, never retrieved — the system only stores the hash, not the original.
- **Same password + same algorithm = same hash.** This is a weakness (identical passwords produce identical hashes), which is why **salting** is used: a random value is added to each password before hashing, so even identical passwords produce different hashes.
- Old password reuse is blocked the same way: the system hashes the new input and compares it against stored *old* hashes — it never needs to know the original password.

---

## 4. Configuring SSH — 6 Steps

```
Router(config)# hostname R1
R1(config)# ip domain name span.com
R1(config)# crypto key generate rsa general-keys modulus 1024
R1(config)# username Bob secret cisco
R1(config)# line vty 0 4
R1(config-line)# login local
R1(config-line)# transport input ssh
```

1. **Configure a unique device hostname** — required before key generation (the key name is derived from hostname + domain).
2. **Configure the IP domain name** — combined with hostname to form the key's unique name (e.g. `R1.span.com`).
3. **Generate RSA keys** — `crypto key generate rsa`. RSA uses a public/private key pair: the public key is shared, the private key stays on the router, enabling encrypted SSH sessions (unlike Telnet, which sends everything in plaintext). `modulus` sets key strength (larger = stronger but slower).
4. **Verify/create a local database entry** — `username <name> secret <password>`.
5. **Authenticate against the local database** — `login local` tells the line to check credentials against the local user database.
6. **Enable VTY inbound SSH sessions** — `transport input ssh` restricts the line to SSH only (blocks Telnet).

### Additional SSH/Login Hardening
```
login block-for 120 attempts 3 within 60   ! block login for 120s after 3 failed attempts in 60s
exec-timeout 5 30                          ! auto-logout after 5 min 30 sec of inactivity
show ip ssh                                ! verify SSH settings
ip ssh time-out <seconds>                  ! set SSH auth response timeout
```

### Banners
```
banner motd | exec | login <delimiter> message <delimiter>
```
- Displays a legal warning message on login (protects the organization legally).
- Example: *"This equipment is privately owned and access is logged. Disconnect immediately if you are not an authorized user. Violators will be prosecuted to the fullest extent of the law."*

---

## 5. Defense-in-Depth — Full Layered Security Model

| Layer | Examples |
|---|---|
| Physical controls | Door locks, fences, rack locks, cameras |
| Technical controls | Firewalls, DMZ, hashing/salting passwords, authentication, IPS, VPN access, card/badge access, anti-virus/anti-malware |
| Administrative controls | Policies & procedures, onboarding/offboarding, backup media handling |

- No single security component is enough — real security is a **mixture of many layers**.
- Card/badge access protects **physical** entry; IPS + VPN gateway protects **remote technical** access from outside.

---

## 6. IPv4 Addressing & Subnetting Fundamentals

### Classful Address Ranges
| Class | Public Range | Default Mask | Typical Use |
|---|---|---|---|
| A | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 (/8) | Very large networks (ISPs, huge corps) |
| **127.x.x.x** | — | — | **Reserved for loopback** (not usable) |
| B | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 (/16) | Medium-large networks (universities, mid-size business) |
| C | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 (/24) | Small LANs (small business, home) |
| D | 224.0.0.0 – 239.255.255.255 | — | Multicast (not for host assignment) |
| E | 240.0.0.0 – 255.255.255.255 | — | Reserved for research/experimental |

### Private (RFC 1918) Ranges
| Class | Private Range |
|---|---|
| A | 10.0.0.0 – 10.255.255.255 |
| B | 172.16.0.0 – 172.31.255.255 |
| C | 192.168.0.0 – 192.168.255.255 |

- Private IPs are reserved for internal use only and are never routed on the public internet — this is why the same ranges (e.g. `192.168.1.1` for home routers) can be reused worldwide without conflict.
- **172.16.1.x used in this lab is a Class B private address.**

### Network Portion vs Host Portion
- The subnet mask determines which part of an IP address is the **network** (fixed, identifies the subnet) and which part is the **host** (variable, identifies individual devices).
- Rule: wherever the mask has consecutive `255`s (all 1-bits), that portion of the IP is the network; the rest is the host.
  - `/16` (255.255.0.0) → first 2 octets = network, last 2 = host
  - `/24` (255.255.255.0) → first 3 octets = network, last 1 = host
- Devices with the same network portion are on the same subnet and can communicate directly; a different network portion means a different subnet (requires a router to communicate).

### Why 172.16.1.x Uses a /24 Mask (Not the Class B Default /16)
- Class B's default mask (/16) allows 65,534 hosts per network — far more than needed for a small lab/office.
- By adding an extra `255` (going from /16 to /24), 8 bits are **"borrowed" from the host portion and given to the network portion**.
- This shrinks the network to 254 usable hosts but allows the same address space to be split into many smaller, more manageable subnets — this is the whole point of **subnetting**: avoid wasting IP address space and organize networks by actual need (e.g. a department of 5 people doesn't need a /24, let alone a /16).
- Subnetting is **classless** (CIDR) — the address's original class doesn't restrict what mask an admin can actually apply.

### Subnetting Math (example: 200.15.10.0)
- Default mask /24 → New mask /28 (borrowed 4 bits)
- Number of subnets = 2^(borrowed bits) = 2^4 = **16 subnets**
- Number of usable hosts per subnet = 2^(remaining host bits) − 2 = 2^4 − 2 = **14 hosts**
  (the −2 accounts for the network address and broadcast address, which aren't assignable to hosts)
- Increment value = 256 − subnet mask octet value (determines where each new subnet starts)

---

## 7. Practical Lab — Configure Secure Passwords and SSH (Packet Tracer)

**Topology:** PCA (PC) — RTA (Router) — SW1 (Switch)

### Part 1: Router (RTA) Basic Security — Full Command Sequence
```
enable
configure terminal
hostname RTA
interface gigabitEthernet 0/0/0
 ip address 172.16.1.1 255.255.255.0
 no shutdown
 exit

service password-encryption
security passwords min-length 10
enable secret cisco12345
no ip domain-lookup
ip domain-name netsec.com
username Admin1 secret Admin12345

crypto key generate rsa
  ! modulus: 1024

login block-for 180 attempts 4 within 120

line vty 0 4
 transport input ssh
 login local
 exec-timeout 6
 end

copy running-config startup-config
```

### Part 2: Switch (SW1) Basic Security
- Same security steps as the router (hostname, password encryption, min-length, domain settings, username/secret, RSA keys, SSH-only VTY, exec-timeout, save config).
- **Additional switch-specific hardening — disable unused ports:**
```
interface range F0/2-24, G0/2
 shutdown
```
- This directly applies the "Router/Device Hardening" principle: disable unused physical interfaces so they can't be used as an attack entry point.

### Common Pitfalls Encountered
- `security password min-length 10` (singular) fails — must be **`security passwords`** (plural).
- Typos in commands can trigger a DNS lookup attempt (causing delays) unless `no ip domain-lookup` is set first.
- Packet Tracer auto-fills a classful default subnet mask (e.g. 255.255.0.0 for a 172.x address) — this must be manually overridden to match the addressing table (255.255.255.0).

---

## 8. Quick Reference — Command Cheat Sheet

```
! Basic device hardening
hostname <name>
enable secret <password>
security passwords min-length <n>
service password-encryption
no ip domain-lookup
ip domain-name <domain>
username <name> secret <password>
banner motd # <message> #

! Console / AUX / VTY lines
line console 0
 password <password>
 login
 exec-timeout <min> <sec>

line aux 0
 password <password>
 login
 exec-timeout <min> <sec>

line vty 0 4
 password <password>       ! or login local for AAA
 login local
 transport input ssh
 exec-timeout <min> <sec>

! AAA
aaa new-model
aaa authentication login default local

! SSH
crypto key generate rsa general-keys modulus 1024
ip ssh version 2
show ip ssh

! Brute-force protection
login block-for <seconds> attempts <n> within <seconds>

! Save configuration
copy running-config startup-config
```
