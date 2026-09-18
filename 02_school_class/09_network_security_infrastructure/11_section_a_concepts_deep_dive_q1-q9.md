# VU23218 – Section A Knowledge Questions: Concepts Deep Dive (Q1–Q9)

> Certificate IV in Cyber Security (22603VIC) | Holmesglen Institute
> This is a companion to `01_vu23218_section_a_study_notes.md`. Where that file summarises the *answers*, this file captures the deeper **"why/how"** explanations worked through during a review session for Q1–Q9 — the mental models and low-level mechanics behind each concept, not just the final answer text.

---

## Q1. NGFW — Application Awareness and Control

- A classic firewall filters on **IP + port + protocol only** (Layer 3/4). It doesn't know *which* application is generating the traffic on port 80/443 — Facebook and BitTorrent look identical to it.
- An NGFW performs **deep packet inspection** up to **Layer 7 (application layer)**, so it can identify the actual application/website and apply policy per-application rather than per-port.
- This is combined with IPS and malware/threat detection in one platform, giving NGFWs much finer-grained control than a classic firewall.

---

## Q2. Serial Link, DCE/DTE, and Clock Rate — Why They Exist

**Serial vs Ethernet**
- Ethernet (used for LAN/switch connections) is a **short-distance** technology with speed/timing already built into the standard — no manual clock configuration needed.
- Serial links simulate a **WAN connection** (e.g. company router ↔ ISP router over a long-distance line). Historically this used real modems over telephone lines.

**What a clock signal actually does**
- Digital communication requires both ends to agree on *when* each bit starts/ends. The **clock signal** is the timing pulse that tells the receiving side "read the next bit now."
- In a real WAN setup, the **modem (DCE – Data Communication Equipment)** generated this clock signal; the router (**DTE – Data Terminal Equipment**) just followed it.

**Why "back-to-back"**
- In a classroom, there is no real modem or long-distance line — two routers are connected directly with a short serial cable, "back to back." Since there's no modem to provide the clock, **one of the two routers must be manually configured to act as the DCE** and generate the clock itself.
- The DCE end of the cable is physically marked (small clock icon on the connector in Packet Tracer). Only the DCE side needs `clock rate` configured; the DTE side does not.
- `clock rate 64000` = 64,000 bits per second. The number itself isn't special — it's just a commonly used lab default; what matters is that *some* rate is set on the DCE side, or the link stays down.

**In real-world practice:** clock rate configuration is rarely done by network engineers in production — the ISP's equipment normally acts as the DCE and provides clocking on a leased line. This lab exercise simulates that role using a second router purely for learning purposes.

---

## Q3. VPN Types and IPsec — Mental Model

- **Remote-Access VPN** = one person, one device, one encrypted tunnel to the office (like an individual badge).
- **Site-to-Site VPN** = the routers at two whole sites maintain a permanent tunnel; every device at both ends can talk without installing anything (like merging two buildings into one).
- **AH vs ESP (both IPsec protocols):**
  - AH = "notarised envelope" — proves who sent it and that it wasn't altered, but the contents are still readable if intercepted (no encryption).
  - ESP = "sealed and notarised envelope" — does everything AH does **plus encrypts the payload**, so intercepted data is unreadable. This is why ESP is used far more often than AH in practice.

---

## Q4. MFA — Why Each Component Was Chosen

| Term | What it is | Why it matters |
|---|---|---|
| **SIM swapping** | An attacker convinces the mobile carrier to transfer a victim's phone number to a SIM card the attacker controls, e.g. by claiming the phone was lost. | Once successful, SMS-based OTP codes go straight to the attacker's phone — this is why SMS-based MFA is considered weak. |
| **TOTP** (Time-based One-Time Password) | A code that regenerates every 30–60 seconds, calculated locally on the device from a shared secret + current time — never transmitted over SMS/network. | Immune to SIM swapping because it never relies on the phone number/carrier. |
| **FIDO2 / YubiKey** | A physical hardware key (USB/NFC) that must be physically present and touched to complete login. | Strongest factor — even a fully phished password is useless without physical possession of the key, making remote takeover essentially impossible. |
| **IdP (Identity Provider)**, e.g. Azure AD/Entra ID, Okta | A centralised service that manages user identities for multiple systems (VPN, apps, NAC) from one place. | Without it, each system (VPN gateway, NAC, apps) would need separate accounts/MFA policies — a management and security nightmare. With it: one account, one MFA policy, centrally monitored/revoked. |
| **VPN gateway** | The "front door" server/appliance that all remote VPN connections must pass through before reaching the internal network. | Integrating it with the IdP means VPN logins are also covered by centralised MFA policy. |
| **Network Access Control (NAC)** | Controls access at the network edge (e.g. switch port), separate from VPN. | Also benefits from IdP integration for consistent identity/MFA enforcement across both wired/local and remote access paths. |

---

## Q5. NAC and Monitoring Tools — Extra Detail

- **"Port-based" in 802.1X** means authentication happens at the level of an individual physical/wireless **switch port** — not once for the whole building, but separately for every single port a device could plug into.
- **Protocol layers** (relevant to how Wireshark works): network data is wrapped in multiple layers before transmission — Application → Transport → Network → Data Link/Physical. Wireshark can "peel back" each layer of a captured packet to inspect it, which is what lets an analyst trace a problem down to its root cause (e.g. seeing the raw TCP/IP headers, not just the top-level content).
- **Compliance** (as in "Endpoint Compliance" for Posture Assessment) = the state of meeting a defined set of rules/standards (e.g. AV enabled + OS patched). A device is either *compliant* (allowed on the network) or *non-compliant* (blocked/quarantined).

---

## Q6. EPP → EDR → XDR → DLP as Layered Defence

This is best understood as **increasing scope of visibility**, plus one separate control:

1. **EPP** — first line of defence on a single endpoint. Uses **signature matching** (comparing files against known-malware "mugshots") and **heuristic analysis** (flagging suspicious *behaviour* even for never-seen-before malware, which is how zero-day threats can be partially caught).
2. **EDR** — assumes EPP can be bypassed. Continuously records what's happening on **one device** and helps security teams investigate + isolate/clean it if something suspicious appears.
3. **XDR** — assumes EDR alone isn't enough when an attacker hits **multiple fronts at once** (e.g. email + network + a compromised cloud workload simultaneously — a "multi-vector attack"). XDR correlates signals from endpoints, network, servers, email, and **cloud workloads** (i.e. apps/services running on rented cloud infrastructure like AWS/Azure, not just on-premises servers) into a single view, so a coordinated attack across several channels can be spotted as one event instead of several unrelated alerts.
4. **DLP** — a fundamentally different kind of control. EPP/EDR/XDR all defend against **inbound** attacks; DLP defends against **outbound** data leakage — like a safe protecting what's already inside, rather than a wall keeping intruders out. It watches data in three states (in transit, at rest, in use) and blocks sensitive files from leaving the organisation.

---

## Q7. RC4 vs AES — The Underlying Mechanics

- **Stream cipher (RC4):** encrypts data **one bit at a time, continuously**, as it flows — like items being wrapped individually on a conveyor belt as they pass by. This makes it lightweight and fast.
- **Block cipher (AES):** groups data into fixed-size **blocks** and encrypts each block as a whole unit — more computation per operation, but much stronger security.
- **Key stream:** RC4 generates a long sequence of pseudo-random-looking numbers (the key stream) from the encryption key. Encryption is done by **XOR-ing** the plaintext with this key stream.
- **XOR (eXclusive OR):** a bitwise operation where the result is `1` only if the two input bits are *different* ("exclusive" = excludes the case where both are the same, unlike a normal OR). Its key property for cryptography: applying the **same** key stream via XOR twice returns the original value — `plaintext XOR keystream = ciphertext`, and `ciphertext XOR keystream = plaintext` again. This makes XOR ideal and very fast for stream cipher encryption/decryption.
- **RC4's fatal flaw:** researchers found the key stream isn't truly random — it contains **statistical patterns**. With enough captured traffic, an attacker can analyse these patterns and recover the encryption key. This is why **WEP** and **early TKIP** (both RC4-based) are considered completely broken today.
- **WLAN** = Wireless LAN — the general term for Wi-Fi-based local networks (as opposed to a wired LAN).
- **WPA2 / WPA3** = the current Wi-Fi security standards, both built on **AES** (block cipher) rather than RC4 — this is why they replaced WEP/TKIP.

---

## Q8. Cryptography vs Cryptanalysis + CIA Triad

**Analogy used:** Cryptography is like being a **locksmith** — designing strong locks (ciphers) that (ideally) no one can open without the correct key. Cryptanalysis is the opposite role — an analyst (or attacker) trying to find a weakness in the lock and open it *without* the key, by exploiting flaws or implementation errors. Both sit within the broader field of **cryptology**.

**CIA Triad** (unrelated to the US intelligence agency — just a shared acronym):
| Objective | Meaning | Typical approach |
|---|---|---|
| **Confidentiality** | Only authorised people can read the data | Encryption (e.g. AES) for data in transit and at rest |
| **Integrity** | Data hasn't been secretly altered | Hash functions (SHA-256) or digital signatures |
| **Availability** | Authorised users can access data/systems when needed | Redundancy, regular backups, DoS/DDoS defences |

---

## Q9. Symmetric vs Asymmetric — Why Both Exist

- **Symmetric encryption** uses **one identical secret key** for both encrypting and decrypting — fast and efficient for large volumes of data, but creates a **key distribution problem**: how do you safely get the same secret key to the other party without it being intercepted in transit?
- **Asymmetric encryption** solves this using **two mathematically linked keys**: a **public key** (can be freely shared — like handing out an open padlock) used to encrypt, and a **private key** (kept secret, never shared) used to decrypt. Because the public key can be distributed openly, there's no secure-channel problem — but the underlying maths is far more complex, making asymmetric encryption noticeably slower than symmetric encryption.
- **Examples:**
  - Symmetric: **AES**, **DES**, **3DES**
  - Asymmetric: **RSA**, **ECC**, **Diffie-Hellman** (key exchange)

*(In practice, many real systems — e.g. HTTPS/TLS — use asymmetric encryption only to securely exchange a symmetric key, then switch to fast symmetric encryption for the actual data. This is a natural extension worth remembering even though it wasn't explicitly asked in Q9.)*

---

*Notes compiled during a concept-review session for VU23218 Assessment Task 2, Section A, with AI assistance used to explain underlying mechanics and build analogies for concept clarification — per the assessment's "Guided Use" AI policy. The final written answers submitted for assessment were composed and understood in the learner's own words; this file documents the conceptual reasoning behind them.*
