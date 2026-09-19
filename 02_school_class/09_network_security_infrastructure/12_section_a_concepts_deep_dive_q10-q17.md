# VU23218 – Section A Concept Notes (Q10–Q17)

**Unit:** VU23218 Implement network security infrastructure for an organisation
**Scope:** Study notes on the concepts behind Knowledge Questions Q10–Q17
**Method:** For each question I worked through the concept in plain language, re-explained it in my own words, then wrote and refined the English.

---

## Q10 – Network-based Intrusion Prevention System (NIPS)

### a) IDS vs IPS functions
| | IDS (Intrusion Detection System) | IPS (Intrusion Prevention System) |
| --- | --- | --- |
| Placement | Out-of-band (receives a copy of traffic) | In-line (traffic passes through it) |
| Action | Passive: detects, logs, alerts the administrator | Active: drops packets, resets connections, blocks source IP |

### b) Updating the signature database
- A **signature** is like a fingerprint of a known attack pattern; the signature database is the list IDS/IPS compares traffic against.
- Attackers constantly create new methods, so the database must be updated regularly.
- **Automatic:** scheduled downloads from the vendor's server. **Manual:** administrator uploads the update package to the management console.
- Good practice: check that an update does not start blocking legitimate traffic.

### c) Strengths and weaknesses
- **IDS strengths:** out-of-band, so a failure does not affect network traffic; false positives only raise alerts.
- **IDS weaknesses:** detects but does not block; the network stays exposed until an administrator responds.
- **IPS strengths:** real-time protection by blocking attacks before damage occurs.
- **IPS weaknesses:** in-line placement can add latency; false positives can block legitimate traffic; an in-line device failure can become a single point of failure.

### d) How AI/ML helps
- Signature-based detection cannot catch attacks that are not yet in the list.
- **Anomaly detection:** ML learns a baseline of normal behaviour, then flags deviations (e.g. a large data transfer at midnight).
- **Zero-day detection:** ML analyses structural features of traffic to identify patterns linked to brand-new attacks with no signature.

---

## Q11 – Vigenère Cipher (manual decryption)

**Task:** Decrypt a ciphertext using the repeating key `CISCOCCNAS` (repeat mode, not case sensitive) with the Vigenère table.

**Key ideas**
- Unlike a Caesar cipher (same shift for every letter), Vigenère shifts each letter by a **different amount decided by the key letter** (C = 2, I = 8, S = 18 …).
- **Repeat mode:** the key is repeated to match the length of the message. Spaces are skipped; the key only advances on letters.
- **Table method:** find the key letter in the left column → move along that row to the ciphertext letter → go up to the top header → that is the plaintext letter.
- **Formula:** `P = (C − K) mod 26`

**Worked start:** key C, cipher `k` → `i`; key I, cipher `t` → `l`; key S, cipher `g` → `o`.
**Result:** *"i love to study network security at holmesglen institute"*

---

## Q12 – Hardening network infrastructure devices and keeping AV updated

### Five hardening actions
1. **Change default credentials** – replace default usernames/passwords with strong, unique ones.
2. **Disable unnecessary services and ports** – turn off unused protocols; avoid Telnet/HTTP (they send data in plain text) and use SSH/HTTPS.
3. **Apply firmware/OS patches regularly** – firmware is the built-in software that runs a device (e.g. Cisco IOS); patches close known vulnerabilities.
4. **Restrict management access** – only trusted management IPs, a dedicated management VLAN, or a secure VPN; block everything else (whitelist approach).
5. **Enable logging and monitoring** – system logs and audit trails to trace who did what, and when.

### Why keep anti-virus (AV) updated
- AV compares files against a signature database of known malware (like a police "wanted list").
- New malware variants, ransomware and zero-day exploits appear daily; an outdated database cannot recognise them.
- An updated AV has the latest threat definitions and can **detect, quarantine and block** modern attacks.
- Related: EPP/EDR/XDR add behaviour-based analysis on top of traditional signature-based AV.

---

## Q13 – Two security vulnerabilities of a proxy server

**Proxy server:** an intermediary between a client and the internet; it sends requests and receives responses on the client's behalf (like a company mailroom) and can inspect, log and block traffic.

### 1. Man-in-the-Middle (MitM) and decryption risks
- **Risk:** if the proxy handles unencrypted traffic or mismanages SSL/TLS inspection certificates, an attacker can pose as the proxy, then eavesdrop, intercept or alter data.
- **Mitigation:** enforce strict HTTPS (SSL/TLS) end to end; securely manage the proxy's certificates and trust store.
- **Notes:** SSL/TLS encrypts data in transit (SSL is the old name, TLS the current version). The "S" in HTTPS stands for *Secure*. SSL/TLS inspection means the proxy decrypts traffic temporarily to scan it, which is why certificate management matters.

### 2. Open proxy / unauthorised relay abuse
- **Risk:** a proxy without access control can be used by outsiders to hide their real IP while launching attacks or sending spam; the organisation's proxy then looks like the source.
- **Mitigation:** apply an ACL to allow only authorised internal subnets/IPs (whitelist), and require user authentication (username/password, MFA).

---

## Q14 – WLAN: relationship between OSI Physical and Data Link layers

| Layer | PDU | Role in WLAN |
| --- | --- | --- |
| Layer 2 – Data Link | Frame | Creates frames, handles MAC addresses, controls how devices access the shared medium (e.g. CSMA/CA in Wi-Fi) |
| Layer 1 – Physical | Bits | Converts bits into radio signals and transmits them through the air (and back) |

- Layer 2 uses MAC = **Media Access Control**: the address decides *who* receives, access control decides *when* a device may transmit. In a WLAN all devices share the same medium (the air), so a rule is needed to decide who sends first.
- **Sending:** upper-layer data → Data Link adds a header (MAC addresses) and a trailer (FCS, Frame Check Sequence) → **frame (L2 PDU)** → Physical converts bits to radio signals → transmitted.
- **Receiving:** Physical picks up radio signals → **bit stream (L1 PDU)** → passed up → Data Link groups bits into frames (framing), checks errors with the FCS, and processes MAC information.
- In a WLAN, the switching role is typically performed by an access point (AP).

---

## Q15 – WLAN security checklist for a small business

1. **Change default credentials** on routers/APs.
2. **Use WPA3**; if devices do not support it, use **WPA2 with AES/CCMP**. Do not use TKIP (old, based on the weak RC4 cipher).
3. **Separate guest and company networks** so visitors or infected devices cannot reach business data.
4. **Disable WPS and remote management.** WPS checks an 8-digit PIN in two 4-digit halves, so it can be cracked in about 11,000 attempts at most, bypassing a strong password. Remote management over the internet should be off so settings change on-site only.
5. **Change the default SSID** (to avoid revealing brand/model) and optionally use MAC filtering/ACLs. These are **weak protections** (SSIDs can be discovered, MAC addresses can be spoofed) – items 1–4 are the core.

**Terms:** SSID = Service Set Identifier (the Wi-Fi name); AES = the encryption algorithm, CCMP = the Wi-Fi protocol that uses AES and also checks message integrity.

---

## Q16 – Three methods to access a Cisco device CLI

| Method | How it works | Restrict and secure |
| --- | --- | --- |
| **Console (physical)** | Console cable (USB-to-RJ45 or rollover) + terminal emulation software, directly at the device | Locked, climate-controlled server room/rack; strong console password; idle timeout |
| **SSH (remote, in-band)** | Encrypted remote CLI over an IP network | Disable Telnet; enforce SSH v2; strong local auth or AAA (TACACS+/RADIUS); trusted IPs or management VLAN; ACLs |
| **AUX port (out-of-band)** | Modem + telephone line as an emergency path when the main network is down; modern equivalent is a dedicated management port or console server | Strong password; restrict dial-in to authorised numbers/networks; disable when not in use |

**Terms:** CLI = Command Line Interface; **AAA** = Authentication (who), Authorization (what they can do), Accounting (what they did); TACACS+/RADIUS = protocols for talking to a central AAA server; **out-of-band** = a management path separate from the normal data network; **in-band** = management over the normal network (SSH).

---

## Q17 – Zone-Based Firewall (ZBF / ZPF)

**Concept:** A Cisco router feature that groups interfaces into security **zones** (inside, outside, DMZ) and inspects traffic as it moves **between zones**, instead of applying rules interface by interface like a traditional ACL.
- **Default rules:** traffic between different zones is **denied** unless a policy explicitly allows it; traffic within the same zone is allowed.
- **`inspect`** is stateful: replies to connections started from the inside are automatically allowed back; connections started from the outside are not.

### Configuration flow (Cisco IOS)
```
! 1. Create zones
zone security IN_ZONE
zone security OUT_ZONE

! 2. Choose the traffic (class-map)
class-map type inspect match-any IN_TO_OUT_CLASS
 match protocol tcp
 match protocol udp
 match protocol icmp

! 3. Choose the action (policy-map)
policy-map type inspect IN_TO_OUT_POLICY
 class type inspect IN_TO_OUT_CLASS
  inspect

! 4. Define the direction (zone-pair) and attach the policy
zone-pair security IN_TO_OUT source IN_ZONE destination OUT_ZONE
 service-policy type inspect IN_TO_OUT_POLICY

! 5. Assign interfaces to zones
interface gigabitEthernet0/0
 zone-member security IN_ZONE
interface serial0/3/0
 zone-member security OUT_ZONE
```

### Verification (Packet Tracer)
| Test | Result | Meaning |
| --- | --- | --- |
| Before ZPF: PC0 → PC1 | Reply received | Baseline connectivity works |
| After ZPF: PC0 → PC1 (Inside → Outside) | Reply received (0% loss on retry) | Outbound traffic permitted by the inspect policy; return traffic allowed automatically |
| After ZPF: PC1 → PC0 (Outside → Inside) | 100% loss | No zone-pair policy for that direction, so default-deny blocks unsolicited inbound traffic |

**Note:** The single timeout on a first ping is normal (ARP resolution). It also appeared before the firewall was configured, so it is not caused by the firewall.

---

## Cross-topic connections
- **Signature databases** appear in IDS/IPS (Q10), anti-virus (Q12), and TKIP/AES contrasts show the same "weak vs strong cipher" theme as RC4 vs AES.
- **Whitelist / default-deny** thinking links Q12 (management access), Q13 (proxy ACL), Q15 (WPS/remote management off) and Q17 (ZBF).
- **Encrypted vs plain text:** Telnet/HTTP vs SSH/HTTPS (Q12, Q16) and SSL/TLS (Q13).
- **Layered defence:** no single control is enough (Q15 SSID/MAC filtering are only extra layers).
