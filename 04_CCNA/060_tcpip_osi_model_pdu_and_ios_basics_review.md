# Network Fundamentals Study Notes
> Cisco IOS / TCP-IP / OSI Model — Study Summary

---

## 1. Cisco IOS — Password Protection

**Q: Which modes and interfaces can be protected with passwords? (Choose 3)**

| Protected Area | Description |
|---|---|
| **Privileged EXEC mode** | Requires password when entering admin mode via `enable` command |
| **VTY interface** | Requires password for remote access via Telnet / SSH |
| **Console interface** | Requires password when physically connecting via console cable |

> **Key point:** Console = physical access, VTY = remote access, Privileged EXEC = admin-level protection.

---

## 2. Remote Management of a Layer 2 Switch

**Q: Which interface allows remote management of a Layer 2 switch?**

**Answer: Switch Virtual Interface (SVI)**

- Layer 2 switches cannot assign IP addresses to physical ports
- SVI is a **logical interface** — assign an IP here to enable remote management
- Console port = physical only (not remote)
- Regular Ethernet ports = data traffic only, not management

---

## 3. Encrypting Passwords in Configuration Files

**Q: What command prevents unencrypted passwords from displaying in plain text?**

```
(config)# service password-encryption
```

- Encrypts all plain-text passwords (console, VTY, etc.) stored in running-config
- `enable secret` only protects the privileged EXEC password — not all passwords

---

## 4. Open Standard Protocols

**Q: What is an advantage of using open standard protocols?**

**Answer:** A client and server running **different operating systems** can successfully exchange data.

| Type | Description |
|---|---|
| **Open Standard** | Publicly available, free to use, vendor-neutral (e.g., HTTP, TCP/IP, OSPF, SMTP) |
| **Proprietary** | Vendor-specific, limited compatibility (e.g., older EIGRP — Cisco only) |

> **Why it matters:** The internet works globally because open standards allow any device/OS to communicate with each other.

---

## 5. TCP/IP Encapsulation Process

**Q: Which statement accurately describes TCP/IP encapsulation when sending data?**

**Answer:** Segments are sent **from the Transport Layer to the Internet Layer.**

### Encapsulation Flow (Top → Down)

```
Application Layer   →   Data
       ↓
Transport Layer     →   Segment  (data is divided into segments)
       ↓
Internet Layer      →   Packet   (IP address added)
       ↓
Network Access Layer →  Frame    (MAC address added)
       ↓
                        Bits     (converted to electrical/optical signals)
```

---

## 6. TCP/IP vs OSI Model — Layer Mapping

**Core concept:** Both models describe the same networking behavior — just with different levels of granularity.

| TCP/IP (4 Layers) | OSI (7 Layers) | PDU |
|---|---|---|
| **Application Layer** | 7 — Application | Data |
| | 6 — Presentation | Data |
| | 5 — Session | Data |
| **Transport Layer** | 4 — Transport | **Segment** |
| **Internet Layer** | 3 — Network | **Packet** |
| **Network Access Layer** | 2 — Data Link | **Frame** |
| | 1 — Physical | **Bits** |

### Key Takeaways

- TCP/IP **Application** = OSI layers 5 + 6 + 7 (merged into one)
- TCP/IP **Transport** = OSI **Transport** (same name, same PDU)
- TCP/IP **Internet** = OSI **Network** (internet ≈ network, same concept)
- TCP/IP **Network Access** = OSI **Data Link + Physical** (two layers merged into one)

> ⚠️ **Common confusion:** "Network" appears in both models but refers to **different layers**
> - OSI **Network** Layer (Layer 3) ↔ TCP/IP **Internet** Layer
> - TCP/IP **Network Access** Layer ↔ OSI **Data Link + Physical**
>
> This is because TCP/IP and OSI were developed **independently by different organizations.**

---

## 7. PDU (Protocol Data Unit) — Layer Reference

> PDU names are **model-agnostic** — they apply to both TCP/IP and OSI based on the layer's function.

| PDU Name | TCP/IP Layer | OSI Layer |
|---|---|---|
| **Data** | Application | Application / Presentation / Session (7, 6, 5) |
| **Segment** | Transport | Transport (4) |
| **Packet** | Internet | Network (3) |
| **Frame** | Network Access | Data Link (2) |
| **Bits** | Network Access | Physical (1) |

### Memory tip
```
Data → Segment → Packet → Frame → Bits
```
Think of it as **wrapping layers** — each lower layer adds a new envelope around the data.

---

## 8. Returning to Previous CLI Level

**Q: Which command returns a user to the previous level in the command hierarchy?**

**Answer: `exit`**

| Command | Behavior |
|---|---|
| `exit` | Goes **one level up** in the hierarchy |
| `end` / `Ctrl-Z` | Jumps directly to **top-level (privileged EXEC)** |
| `Ctrl-C` | Cancels the current operation |

```
Router(config-if)# exit
Router(config)#          ← moved back one level
```

---

*Study notes compiled from Cisco CCNA / Networking Fundamentals coursework.*
