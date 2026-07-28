# VU23218 – Implement Network Security Infrastructure for an Organisation
## Section A – Knowledge Questions: Study Notes (Q1–Q17)

> Certificate IV in Cyber Security (22603VIC) | Holmesglen Institute
> These notes summarise the key concepts covered while working through the 17 knowledge questions in Assessment Task 2, Section A.

---

## Q1. Next-Generation Firewall (NGFW)

**Core idea:** An NGFW extends a traditional stateful firewall by adding deeper inspection capabilities.

- Traditional firewalls filter based on **IP address, port, and protocol** (Layer 3/4) only.
- NGFWs add: **Intrusion Prevention System (IPS)**, **Deep Packet Inspection (DPI)**, and **malware/threat detection**, all in one platform.
- **Key differentiator not found in classic firewalls:** **Application Awareness and Control** — inspection at **Layer 7 (application layer)**, allowing the firewall to identify the actual application (e.g. Facebook, BitTorrent) rather than just a port/protocol, and to control access at the application level.

---

## Q2. Configuring Two Routers over a Serial Link (Cisco CLI)

**Concept:** A serial link is a WAN-style physical connection. One side is **DCE** (Data Communication Equipment, provides clocking) and the other is **DTE** (Data Terminal Equipment).

**Key configuration steps:**
1. Add a serial interface module (e.g. HWIC-2T) to routers that don't have one built in.
2. Connect the two routers with a **Serial DCE cable**.
3. Configure IP addresses on both serial interfaces (same subnet).
4. On the **DCE side only**, set the `clock rate` (e.g. `64000`) — this is required or the link will not come up.
5. `no shutdown` on both sides.

**Verification:**
- `show ip interface brief` → interface status should read **up/up** on both routers.
- `ping <remote serial IP>` → should succeed (100% success rate).

**Common pitfall:** If `clock rate` is missing or mistyped on the DCE side, the link stays **down/down** even though IP addressing is correct.

---

## Q3. VPN – Remote-Access vs Site-to-Site, IPsec, Commercial VPNs

**a) Remote-Access vs Site-to-Site VPN**
- **Remote-Access VPN:** Individual users connect to the corporate network from outside using a VPN client app on their device.
- **Site-to-Site VPN:** Connects two entire networks (e.g. branch office ↔ HQ) via routers/gateways that maintain a permanent tunnel — no client software needed on individual PCs.

**b) Two main IPsec protocols**
- **AH (Authentication Header):** Provides integrity and authentication only — **no encryption**, so data can still be read if captured.
- **ESP (Encapsulating Security Payload):** Provides integrity + authentication **plus encryption** (confidentiality). Because of this, ESP is far more widely used than AH.

**c) Commercial VPN comparison**
| | Advantages | Disadvantages |
|---|---|---|
| **ExpressVPN** | Very fast, reliable, easy to use across platforms, strong custom protocol (Lightway) | More expensive than competitors |
| **NordVPN** | Extra security features (Threat Protection, Double VPN), good value on long-term plans | Desktop app can feel cluttered/busy with extra features |

---

## Q4. Implementing MFA as an IT Security Manager

Passwords alone are vulnerable (theft, guessing, phishing), so MFA implementation follows a structured process:

1. **Assess risks & define policy** — identify which resources need MFA (especially remote workers, admins).
2. **Choose secure MFA factors** — avoid SMS (vulnerable to SIM-swapping); prefer authenticator apps (TOTP) and hardware keys (FIDO2/YubiKey) for admins.
3. **Pilot test & gradual rollout** — test with a small group (e.g. IT team) first to catch technical issues and user friction before a company-wide rollout.
4. **Integrate with an Identity Provider (IdP)** — e.g. Azure AD/Entra ID or Okta, to centrally manage credentials and MFA policy.
5. **User training & support** — teach staff why/how to use MFA, and provide support for lost devices/reset requests.

---

## Q5. Network Access Control & Monitoring Tools

**a) Two examples of Network Access Control (NAC):**
1. **802.1X Port-Based Authentication** — a device must authenticate (username/password or certificate) before a switch port grants network access.
2. **Posture Assessment (Endpoint Compliance)** — checks a device's security health (AV running, patches up to date) before allowing connection; non-compliant devices are blocked or quarantined.

**b) Three network monitoring tools:**
1. **Wireshark** — open-source packet analyzer; captures traffic in real time and inspects packets down to the protocol layer.
2. **Nagios** — monitors host/service status (up/down, CPU, alerts); notifies admins of outages or performance drops.
3. **Zabbix** — enterprise monitoring platform; tracks performance metrics, bandwidth, and device health via visual dashboards.

*(Screenshots: live Wireshark capture taken directly; Nagios/Zabbix dashboards sourced from official product demo pages, cited as such.)*

---

## Q6. Endpoint Security Concepts

| Term | Role |
|---|---|
| **EPP** (Endpoint Protection) | First line of defence — blocks known malware/ransomware before execution (signature matching, heuristics). |
| **EDR** (Endpoint Detection & Response) | Handles what happens *if* EPP is bypassed — continuously monitors endpoint activity, detects suspicious behaviour, investigates, and responds (isolate/clean). |
| **XDR** (Extended Detection & Response) | Extends EDR by correlating data across **multiple layers** (endpoints, network, servers, email, cloud) to detect complex, multi-vector attacks. |
| **DLP** (Data Loss Prevention) | Protects sensitive data (in transit, at rest, in use) from being leaked or improperly shared outside the organisation. |

---

## Q7. RC4 vs AES (WLAN Encryption)

| | RC4 | AES |
|---|---|---|
| **Type** | Stream cipher | Block cipher |
| **Strength** | Lightweight, very fast — good for low-power devices | High security; core of WPA2/WPA3 |
| **Weakness** | Statistical patterns in keystream allow key recovery → WEP/early TKIP completely broken | More computationally demanding than RC4 |

**Conclusion:** AES is far more secure and should always be preferred; RC4-based WEP is now obsolete.

---

## Q8. Cryptography vs Cryptanalysis + CIA Triad

**a)** 
- **Cryptography** = designing systems/algorithms to protect data (the "defence" side).
- **Cryptanalysis** = analysing/breaking cryptographic systems to recover hidden information without the key (the "attack/analysis" side).

**b) Three primary objectives of securing communications (CIA Triad):**
1. **Confidentiality** → achieved via encryption (e.g. AES) in transit and at rest.
2. **Integrity** → achieved via hash functions (SHA-256) or digital signatures.
3. **Availability** → achieved via redundancy, backups, and DoS/DDoS defences.

---

## Q9. Symmetric vs Asymmetric Algorithms

- **Symmetric:** Same secret key for encryption and decryption. Fast, efficient for large data — but key distribution is a challenge.
- **Asymmetric:** Public key (encrypt) + private key (decrypt) pair. Solves key exchange problem but is computationally slower.

| Symmetric examples | Asymmetric examples |
|---|---|
| AES | RSA |
| DES | ECC |
| 3DES | Diffie-Hellman (key exchange) |

---

## Q10. NIPS – IPS/IDS, Signature Updates, AI/ML Detection

**a) Functions:**
- **IDS** — passive; monitors and alerts, does not block.
- **IPS** — active; monitors in real time and blocks/drops/resets malicious traffic.

**b) Signature database updates:** Download the latest threat definitions from the vendor's server, either via scheduled automatic updates or manual upload to the management console.

**c) IPS vs IDS strengths/weaknesses:**
- **IDS:** Out-of-band → a failure or false positive doesn't disrupt traffic, but it can't stop an attack in real time.
- **IPS:** In-line → can stop attacks immediately, but introduces latency and a false positive can block legitimate traffic.

**d) AI/ML in threat detection:**
- **Anomaly detection** — learns normal baseline behaviour, flags deviations (e.g. large midnight data transfer).
- **Zero-day detection** — analyses structural features of traffic to catch new attacks with no existing signature.

---

## Q11. Vigenère Cipher Decryption

**Ciphertext:** `k tgxs vq ftmfg fghyqek kgkmtwva nt zqtegginrn apalkhwvr`
**Key (repeating):** `CISCOCCNAS`

**Method:** For each ciphertext letter, find the key letter's row in the Vigenère table, locate the ciphertext letter within that row, then read the corresponding column header (top row) to get the plaintext letter.

**Decrypted result:**
> **"I LOVE TO STUDY NETWORK SECURITY AT HOLMESGLEN INSTITUTE"**

*(A few worked examples — e.g. Row C → find K → read I; Row I → find T → read L; Row S → find G → read O — are shown in the table screenshot as evidence of the manual process; not every single letter needs to be shown by arrows, but the full decrypted sentence must be provided.)*

---

## Q12. Infrastructure Hardening & AV Updates

**Five actions to enhance network device security:**
1. Change default usernames/passwords.
2. Disable unnecessary services/ports (e.g. Telnet, HTTP) in favour of secure alternatives (SSH, HTTPS).
3. Apply regular firmware/OS patches.
4. Restrict management access (trusted IPs, dedicated management VLAN/VPN).
5. Enable logging and monitoring/audit trails.

**Why keep AV updated:** Malware evolves daily; without updated signatures, AV cannot recognise new viruses, ransomware, or zero-day exploits.

---

## Q13. Proxy Server Vulnerabilities

1. **Man-in-the-Middle / decryption risks** — unencrypted traffic or poorly managed SSL/TLS inspection certificates let attackers intercept data.
   - *Mitigation:* Enforce HTTPS everywhere; securely manage trust stores/certificates.
2. **Open proxy / unauthorized relay abuse** — a misconfigured proxy with no access control can be abused by external attackers to hide their IP.
   - *Mitigation:* Strict ACLs limiting proxy use to authorised subnets/IPs; require user authentication.

---

## Q14. WLAN – Physical & Data Link Layer Relationship

- **Data Link Layer (L2):** Framing, MAC addressing, controls how devices access the network.
- **Physical Layer (L1):** Handles actual hardware-level transmission (radio waves).

**PDU exchange process:**
- **Sending:** Data Link wraps data into a frame (L2 PDU) → Physical Layer converts frame to bits → bits become radio waves for transmission.
- **Receiving:** Physical Layer catches radio waves → converts back to bit stream (L1 PDU) → rebuilds into a frame → passes up to Data Link Layer for error checking and MAC processing.

---

## Q15. WLAN Security Checklist for a Small Business

1. Change default credentials on routers/access points.
2. Upgrade to **WPA3** encryption (minimum WPA2-Enterprise/Personal).
3. Separate guest Wi-Fi from the corporate network entirely.
4. Disable **WPS** and remote management over the internet.
5. Change default SSID and use MAC filtering/ACLs as an extra layer where practical.

---

## Q16. Methods to Access Cisco Device CLI

1. **Console connection** (physical cable) — secure via locked server room + strong console password + idle timeout.
2. **SSH** — secure remote CLI access; disable Telnet, enforce SSHv2, use AAA (TACACS+/RADIUS), restrict to trusted IPs/management VLAN, apply ACLs.
3. **AUX port** (out-of-band dial-up/modem, or modern equivalent management port) — secure via strong authentication, restrict to authorised numbers/segments, disable when unused.

---

## Q17. Zone-Based Firewall (ZPF) — Explanation, Configuration & Verification

**Definition:** A Zone-Based Firewall groups router interfaces into security **zones** (e.g. inside, outside, DMZ) and inspects traffic as it moves **between zones**, rather than applying rules per-interface like a traditional ACL. **By default, all inter-zone traffic is denied unless a policy explicitly allows it**; traffic within the same zone is allowed by default.

**Configuration steps (Cisco IOS CLI):**
```
! 0. Enable the security technology package (required on some IOS images)
license boot module c2900 technology-package securityk9

! 1. Create the zones
zone security IN_ZONE
zone security OUT_ZONE

! 2. Define traffic to inspect
class-map type inspect match-any IN_TO_OUT_CLASS
match protocol tcp
match protocol udp
match protocol icmp

! 3. Define the action (inspect = stateful allow + track return traffic)
policy-map type inspect IN_TO_OUT_POLICY
class type inspect IN_TO_OUT_CLASS
inspect

! 4. Link zones with the policy (one direction only!)
zone-pair security IN_TO_OUT source IN_ZONE destination OUT_ZONE
service-policy type inspect IN_TO_OUT_POLICY

! 5. Assign interfaces to zones
interface gigabitEthernet0/0
zone-member security IN_ZONE

interface serial0/3/0
zone-member security OUT_ZONE
```

**Lab topology used:** `PC0 (192.168.10.10) — Router0 (ZPF applied) === serial link === Router1 — PC1 (192.168.20.10)`

**Verification (Packet Tracer):**
- **Before ZPF applied:** PC0 ↔ PC1 ping succeeds in both directions (baseline connectivity confirmed).
- **After ZPF applied:**
  - `PC0 → PC1` (IN_ZONE → OUT_ZONE): **ping succeeds (0% loss)** — traffic matches the configured zone-pair/inspect policy.
  - `PC1 → PC0` (OUT_ZONE → IN_ZONE): **ping fails completely (100% loss)** — no zone-pair exists for this direction, so it is blocked by the firewall's default-deny behaviour.

This before/after, both-directions test is the key piece of evidence that the Zone-Based Firewall is actually enforcing policy, not just configured but inactive.

---

## General Notes on Packet Tracer Practicals (Q2 & Q17 Lab)

- Router model used: **Cisco 2911**.
- Serial ports require adding an **HWIC-2T** module (Physical tab → power off → drag module into slot → power on).
- Serial cable: the **DCE cable icon has a small clock symbol**; the DCE end requires `clock rate`, the DTE end does not.
- **IOS "security" technology package** may need to be activated with `license boot module c2900 technology-package securityk9` + `write memory` + `reload` before `zone security` commands will work (`% Unrecognized command` otherwise).
- **File handling lesson learned:** Packet Tracer `.pkt` files should be opened via **File → Open** from inside an already-running Packet Tracer instance, not by double-clicking the file in File Explorer — double-clicking caused the file to appear blank/empty on this system. Save frequently with `Ctrl+S` during long configuration sessions.

---

*Notes compiled while working through VU23218 Assessment Task 2, Section A, with AI assistance used for concept clarification, structure, and review — per the assessment's "Guided Use" AI policy. All final answers were written and verified in the learner's own words.*
