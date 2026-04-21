# Network Attacks: DDoS, DNS, Zero-Day & WLAN Security

> **Course:** Test Concepts and Procedures for Cyber Security (CSOC Blue Room)
> **Topic:** Network attack types, DNS vulnerabilities, Zero-day exploits, WLAN security, Penetration Testing

---

## 1. TCP 3-Way Handshake

Before two computers communicate, they establish a connection through a 3-step process:

| Step | Direction | Signal | Meaning |
|------|-----------|--------|---------|
| 1 | Client → Server | SYN | "Can I talk to you?" |
| 2 | Server → Client | SYN-ACK | "Yes, I'm available!" |
| 3 | Client → Server | ACK | "Great, let's talk!" |

- **SYN** = Synchronize — the first signal sent to initiate a connection
- Once all 3 steps complete, a **TCP SYN is established**

---

## 2. DDoS Attack (SYN Flood)

### How it works
A **Distributed Denial of Service (DDoS)** attack overwhelms a server by exploiting the TCP handshake:

1. Attacker sends thousands of SYN requests to the server
2. Server opens a channel for each request and waits
3. Attacker never sends the final ACK (goes silent)
4. Server keeps all channels open — memory fills up
5. Server crashes 💥

### Why it's dangerous
- Servers are designed **not to lose requests**, so every pending connection is stored in memory
- When memory is full, it moves to the database — same problem
- All resources are consumed waiting for responses that will never come

### Real purpose of DDoS
> DDoS isn't just about crashing the main server.
> When the main server goes down, a **backup server** kicks in.
> Backup servers are less secure (lower-grade infrastructure in the DMZ).
> This gives attackers an opportunity to send malicious files or packets to the weaker backup server.

### Mitigation
| Method | Description |
|--------|-------------|
| **Rate Limiting** | Sets a TTL (Time To Live) on each open channel. If no response within X seconds (e.g. 15 sec), the channel closes automatically and resources are freed |
| **IPS (Intrusion Prevention System)** | Detects abnormal traffic patterns and blocks them automatically |
| **HTTPS / TLS** | Modern server technology that helps counter these attacks |

---

## 3. DNS (Domain Name System)

### What is DNS?
DNS translates human-readable URLs into IP addresses.

> `google.com` → `142.250.x.x`

Think of it as the **internet's phone book**.

- **IPv4** = 32-bit, 4 blocks (e.g. `192.168.1.1`)
- **IPv6** = 128-bit, 6 blocks (e.g. `2001:0db8:...`)

### DNS Lookup Process
When you type a URL in your browser:

```
1. Browser cache        — Has this URL been visited before?
2. OS hosts file        — Does the OS have a URL-to-IP mapping stored?
3. Modem/Router         — Passes request to ISP
4. ISP DNS cache        — ISP checks its own cached records
5. Root Name Server     — Top-level DNS server (first outer layer)
6. TLD Name Server      — Handles domains like .com, .gov, .edu, .au
                          (13 different TLD servers exist for .com alone)
7. Authoritative NS     — Holds the actual IP address for the domain
8. Response sent back   — IP address returned to client → connection made
```

### DNS Vulnerabilities
Each stage above stores data temporarily (cached), and **that cache can be manipulated**:
- Malicious software installed via phishing email can read and alter browser cache/cookies
- OS memory (hosts file) can be tampered with
- ISP DNS cache can be poisoned

> Note: **Cookie data itself is encrypted**, but the **memory location where cookies are stored is NOT encrypted** — making it an easy target for malicious software.

---

## 4. DNS Attack Types

| Attack | Description | Number |
|--------|-------------|--------|
| **DNS Hijacking** | Redirects DNS requests to malicious servers without user consent by changing DNS configuration | 1 |
| **DNS Spoofing** | Injects malicious data into a DNS server's cache to redirect users to fraudulent websites | 2 |
| **NXDOMAIN Attack** | Floods a DNS server with requests for non-existent domains to exhaust its resources | 3 |
| **DNS Tunnelling** | Uses DNS queries to exfiltrate data from a compromised system — bypasses firewalls because DNS traffic is never blocked | 4 |
| **DNS Amplification** | Exploits open DNS servers to overwhelm a target with amplified traffic | 5 |

### Why DNS Tunnelling is hard to stop
> Firewalls **never block DNS traffic** because doing so would make websites extremely slow to load.
> Attackers exploit this by hiding malicious data inside DNS packets — the firewall sees the DNS header and lets it through automatically.

### DNS Spoofing — Real Attack Scenario

```
1. Attacker creates ANZ1.com (fake ANZ bank site, looks identical)
2. Injects fake IP into DNS cache: "ANZ.com = attacker's server"
3. User types ANZ.com in browser
4. DNS returns attacker's IP instead of real one
5. User lands on fake site, enters login credentials
6. Attacker captures credentials
7. User sees "login failed" and retries on real site — never notices
8. Without MFA → account is immediately compromised
```

### DNS Attack Mitigations
| Attack | Defense |
|--------|---------|
| DNS Spoofing | **DNSSEC** — adds digital signatures to DNS responses to verify authenticity |
| DNS Tunnelling | **Monitor DNS traffic for anomalies** — detect unusual patterns in DNS queries |

---

## 5. Zero-Day Vulnerabilities

### Definition
A **Zero-day vulnerability** is a security flaw that:
- Was **unknown to the developer**
- Is **exploited by attackers before a patch is released**
- By the time it's discovered, "zero days" remain to fix it

### Notable Examples

**Stuxnet (2010)**
- Widely considered the world's first cyber weapon
- Created by the US and Israel to target Iran's nuclear facilities
- Exploited **4 unknown Windows Zero-day vulnerabilities simultaneously**
- Infected uranium enrichment centrifuges via USB
- Caused centrifuges to spin too fast → **~1,000 centrifuges physically destroyed**
- Iran initially believed it was mechanical failure
- Delayed Iran's nuclear program by several years

**Flash Player CVE-2015-0313**
- Zero-day exploit targeting web browsers
- Attackers embedded malicious code in online advertisements
- Simply visiting a website with the ad would trigger infection — **no click required**
- Adobe patched it after the fact, but many users were already compromised
- Led to a significant drop in Flash Player's reputation
- Adobe Flash was completely discontinued in 2020

### CVE (Common Vulnerabilities and Exposures)
- A **public database** that tracks known cybersecurity vulnerabilities
- Format: `CVE-YEAR-NUMBER` (e.g. `CVE-2015-0313`, `CVE-2017-0144`)
- Where to find it:
  - **www.cve.org** (official CVE database)
  - **nvd.nist.gov** (NIST National Vulnerability Database — more detailed)

---

## 6. WLAN Security Vulnerabilities

### Hardware Vulnerabilities
| Vulnerability | Risk | Fix |
|--------------|------|-----|
| **Default hardware configurations** | Out-of-the-box devices use default admin/password — easily guessed | Change credentials immediately |
| **Outdated firmware** | Unpatched security vulnerabilities remain exploitable | Update firmware regularly |

### Software Vulnerabilities
| Vulnerability | Risk | Fix |
|--------------|------|-----|
| **WEP encryption** | Extremely weak — can be cracked in minutes with modern tools | Upgrade to WPA3 |
| **Weak access control** | Makes it easy for unauthorized users to intercept and decrypt data | Use strong encryption + access control |

### Encryption Protocol Evolution
```
WEP  (1997) — Extremely weak, avoid completely
 ↓
WPA  (2003) — Better, but still vulnerable
 ↓
WPA2 (2004) — Currently widely used
 ↓
WPA3 (2018) — Latest and most secure ✅
```

---

## 7. OWASP & Application Layer Security

### OWASP (Open Web Application Security Project)
- A non-profit organization that publishes the **Top 10 most critical web application vulnerabilities**
- Provides guidelines to help developers build secure web applications
- Latest version: **OWASP Top 10 — 2021**

### Common OWASP Vulnerabilities
| Vulnerability | Description | Mitigation |
|--------------|-------------|------------|
| **SQL Injection** | Malicious SQL code injected into database queries to steal or destroy data | Input validation + Prepared Statements |
| **XSS (Cross-Site Scripting)** | Malicious scripts injected into web pages to steal cookies/session tokens | Input sanitization, Content Security Policy |

### TCP/IP Application Layer Protocols
Protocols used at the Application Layer (Layer 4 of TCP/IP model):
- **HTTP/HTTPS** — web browsing
- **SMTP** — email
- **DNS** — domain name resolution
- **FTP** — file transfer

---

## 8. OSINT (Open-Source Intelligence)

- Collects and analyses **publicly available information** for security analysis
- Sources: social media, news, public records, search engines
- Used by both **attackers** (to research targets) and **defenders** (to find exposed data)
- Google search is a basic form of OSINT
- Does NOT require proprietary software — many free tools available

---

## 9. Penetration Testing (Pen Testing)

### PTES (Penetration Testing Execution Standard)
A standard framework that outlines the steps of ethical hacking:

```
1. Pre-engagement         — Define scope, rules, legal agreements
2. Intelligence Gathering — Collect info about target (OSINT etc.)
3. Threat Modeling        — Identify potential attack paths
4. Vulnerability Analysis — Find weaknesses
5. Exploitation           — Actively attempt to breach the system ← core phase
6. Post Exploitation      — Assess damage, maintain access for testing
7. Reporting              — Document all findings
```

### Legal and Ethical Rules
- Must operate **strictly within the agreed scope**
- Exceeding scope = **violation of ethical hacking guidelines** = illegal
- Written permission is always required before testing
- Any vulnerabilities found must be reported

---

## 10. Virus Detection: Heuristics vs Signature

| Method | How it works | What it detects |
|--------|-------------|-----------------|
| **Signature-based** | Compares files against a database of known virus signatures | Known viruses only |
| **Heuristics-based** | Analyses behavioural patterns of files | Known AND unknown/new viruses |

### How Heuristics Works in Practice
> A malware sample downloads data, collects keystrokes, and transmits at 9:00 AM (to blend into heavy network traffic).
> Heuristics detects this suspicious behaviour pattern → flags it → quarantines the file.

### Tools that use Heuristics
- Norton, McAfee, and other major antivirus programs use heuristics alongside signature-based detection

### Connection to Zero-Day
> Zero-day attacks use unknown malware → signature-based detection **cannot catch them**
> Heuristics-based detection **can** catch them by identifying suspicious behaviour

---

## Quick Reference: Attacks vs Defenses

| Attack | Defense |
|--------|---------|
| DDoS / SYN Flood | Rate Limiting + IPS |
| DNS Spoofing | DNSSEC |
| DNS Tunnelling | Monitor DNS traffic for anomalies |
| SQL Injection | Input validation + Prepared Statements |
| Weak WLAN encryption (WEP) | Upgrade to WPA3 |
| Zero-day exploits | Heuristics-based antivirus |
| Phishing / Malware delivery | MFA + email filtering |
