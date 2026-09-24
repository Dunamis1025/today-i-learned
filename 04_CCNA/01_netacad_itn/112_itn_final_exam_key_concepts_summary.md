# 112 — ITN Final Exam: Key Concepts Summary

> Comprehensive review notes based on the CCNA: Introduction to Networks (ITN) course final exam (60 questions, scored 98%). Organized by topic for quick reference and future review before SRWE/ENSCA.

---

## 1. Layer 2 vs Layer 3 Addressing

- **IP addresses (Layer 3) are end-to-end**: they never change between the original source and the final destination, no matter how many routers the packet passes through.
- **MAC addresses (Layer 2) change at every hop**: each time a frame crosses a router, the source/destination MAC addresses are rewritten for the next segment.
- When a host sends data to a device on a **different subnet**, the frame's destination MAC address is the **default gateway's** interface MAC — not the final destination's MAC.
- When the outgoing interface is **serial** (not Ethernet), the router **removes the Ethernet header entirely** and encapsulates with a new Layer 2 protocol (e.g., HDLC/PPP), since serial links don't use MAC addresses.

## 2. ARP (Address Resolution Protocol)

- Used to resolve an **IP address → MAC address** mapping within a local network.
- If the destination is on a **remote network**, the host ARPs for the **default gateway's MAC**, not the final destination's MAC.
- ARP requests are sent as **broadcasts** (FF-FF-FF-FF-FF-FF) and reach every device in the same broadcast domain (but not across routers).
- If a device recognizes its own IP in the request, it replies with a **unicast ARP reply**.
- If no device responds, the packet is **discarded** (not broadcast as data).

## 3. Default Gateway

- Acts as the **exit point** to networks outside the local subnet.
- A misconfigured or missing default gateway **does not affect local (same-subnet) communication** — local hosts still resolve each other via ARP/switching.
- It **does** prevent communication with hosts on **other networks**.

## 4. Transport Layer (OSI Layer 4)

- Core function: **multiplexing** — using **port numbers** to direct data to the correct process/application (e.g., separating multiple browser tabs on one host).
- Actual multimedia payload (video/audio content) belongs to the **Application layer**, not the transport header. The transport header only carries control info: source/destination ports, sequence numbers, ACK numbers, window size.
- **TCP sliding window**: a flow-control mechanism — lets the receiver tell the sender to slow down the transmission rate (not about ordering or retransmission triggers).
- **TCP vs UDP**:
  - TCP: connection-oriented, reliable, higher overhead (used when reliability matters).
  - UDP: connectionless, lower overhead, used for time-sensitive traffic like RTP (voice/video).
- Source port = identifies the sending application/session on the local host; destination port = identifies the receiving application/service on the server.

## 5. Network Layer (OSI Layer 3)

- Provides: (1) unique logical addressing for end devices, (2) routing packets to hosts on other networks.
- **TTL (Time To Live)**: decremented by 1 at each router hop; when it reaches 0, the packet is discarded and an ICMP **Time Exceeded** message is sent back to the source — this prevents infinite routing loops.
- When a router matches a destination to a **directly connected** route, it simply **switches the packet out that interface** (no next-hop lookup needed).

## 6. Data Link Layer (OSI Layer 2) & Ethernet Sublayers

- Function: exchange of **frames** over a shared local medium.
- **LLC (Logical Link Control) sublayer**: communicates between upper-layer software and the NIC hardware; uses the frame's **Type field** to identify the Layer 3 protocol (enables IPv4/IPv6 to share the same physical medium).
- **MAC sublayer**: handles addressing, frame structure, and media access control.
- Frame fields:
  - **FCS (Frame Check Sequence)** → error detection.
  - **Destination/Source MAC** → addressing.
  - **802.2 header** → LLC sublayer info.
  - Preamble/SFD → marks frame start.

## 7. IP Addressing — IPv4 & Subnetting

- Subnet mask determines block size: block size = 2^(host bits).
- To find usable host range: network address + 1 → broadcast address − 1.
- When multiple subnets must share **one mask**, size the mask to fit the **largest** required subnet.
- When choosing the smallest mask for N hosts, pick the smallest block size ≥ N + 2 (network + broadcast).
- Standard reserved ranges:
  - **127.0.0.0/8** → loopback (e.g., 127.0.0.1)
  - **169.254.0.0/16** → link-local (APIPA)
  - **240.0.0.0+** → experimental (Class E)
  - Public addresses → globally routable, not in private ranges.

## 8. IPv6 Addressing

- Address structure: **Global Routing Prefix** (assigned by ISP) + **Subnet ID** (org-defined subnets) + **Interface ID** (equivalent to IPv4 host portion, typically last 64 bits).
- To calculate available subnets: 2^(64 − prefix length). E.g., a /56 block → 2^8 = **256** subnets without touching the interface ID space.
- `ipv6 unicast-routing` (global config command) enables IPv6 routing → interfaces begin sending **ICMPv6 Router Advertisement (RA)** messages.
- Well-known multicast addresses:
  - **FF02::1** → all-nodes on the local link.
  - **FF02::2** → all-routers on the local link.

## 9. IP Protocol Characteristics

- IP is **connectionless** (no dedicated end-to-end connection required) and **media-independent** (works over Ethernet, serial, wireless, etc.).
- IP does **not** guarantee delivery, retransmit lost packets, or reassemble out-of-order data — those are TCP responsibilities.

## 10. TCP/IP Model vs OSI Model Mapping

- TCP/IP **Application layer** = OSI **Application + Presentation + Session** layers.
- TCP/IP **Internet layer** = OSI **Network layer** — provides routing across an internetwork.
- TCP/IP **Transport layer** = OSI **Transport layer**.
- TCP/IP **Network Access layer** = OSI **Data Link + Physical** layers.
- Top-layer (Application) protocol examples: **DNS, POP, SMTP, FTP, HTTP**.
- Transport-layer protocols: **TCP, UDP**.
- Internet-layer protocol: **IP**.
- Network Access-layer protocol example: **Ethernet**.

## 11. Application Layer Protocols

- **DNS**: resolves domain names to IP addresses.
- **DHCP**: automatically assigns IP configuration; server listens on **UDP port 67**, client uses **UDP port 68**.
- **SMTP**: sends email from client→server and server→server (not for receiving mail — that's POP3/IMAP).
- **FTP**: file transfer (ports 20/21).
- **SSH**: encrypted remote access (port 22); Telnet is unencrypted (port 23).

## 12. Physical Layer / Cabling

- **UTP (Unshielded Twisted Pair)**: no metal shielding; wires are **twisted into pairs** to cancel out electromagnetic interference and reduce **crosstalk** (signal leakage between adjacent wire pairs inside the same cable).
- **Attenuation**: loss of signal strength as distance increases (different from crosstalk, latency, or amplification).
- **EMI (Electromagnetic Interference)** and **RFI (Radio Frequency Interference)**: external interference sources (e.g., electrical equipment, fluorescent lights) — distinct from crosstalk, which is internal to the cable.
- Connectors:
  - **RJ-45** → Ethernet UTP.
  - **RJ-11** (4 or 6 pin) → telephone lines.
  - **LC / SC** → fiber optic connectors (LC = small form factor, common in data centers; SC = square, push-pull, legacy).
  - **BNC (Bayonet Neill–Concelman)** → coaxial cable, twist-lock connector.
- Common causes of UTP signal degradation: **improper termination**, **low-quality cable/connectors**.

## 13. Wireless Network Design Considerations

Three key concerns when designing a wireless network:
- **Coverage area**
- **Interference**
- **Security**
(Not primary concerns: extensive cabling — that's a wired-network issue; packet collision is handled by the wireless MAC protocol itself.)

## 14. Network Characteristics (Reliability Pillars)

- **Fault tolerance**: network continues operating despite a failure (e.g., automatic failover to a secondary ISP connection).
- **Quality of Service (QoS)**: prioritizing traffic to maintain performance for time-sensitive applications (e.g., video conferencing).
- **Security**: authentication, encryption, access control (e.g., username/password login).
- **Scalability**: ability to grow to support more users/devices.

## 15. Security Fundamentals

- **AAA framework**:
  - **Authentication** → verifying identity (who you are).
  - **Authorization** → determining what an authenticated user is permitted to do (e.g., read-only vs edit rights).
  - **Accounting** → logging/tracking user activity.
- **Malware types**:
  - **Virus**: attaches to files, needs user action to spread.
  - **Worm**: self-replicates and spreads across a network automatically, often causing network slowdowns/high bandwidth usage.
  - **Trojan horse**: disguised as legitimate software; performs hidden malicious actions (e.g., silently disabling a firewall).
- Security solutions typically **corporate-only** (less common at home): **Intrusion Prevention Systems (IPS)**, **VPNs**. (Strong passwords and antivirus are common in both home and corporate settings.)
- **VPN (Virtual Private Network)**: a tunneling protocol that gives remote users secure access into an organization's private network over a public network.

## 16. Cisco Device CLI / IOS Basics

- Prompt levels: `Switch>` (User EXEC) → `Switch#` (Privileged EXEC, via `enable`) → `Switch(config)#` (Global Config, via `configure terminal`).
- `configure terminal` only works from **Privileged EXEC mode** — entering it directly from User EXEC causes "Invalid input detected."
- `show startup-config` → displays the **saved configuration in NVRAM**.
- `show running-config` → displays the **current active configuration in RAM**.
- Fastest way to test a login banner: **exit privileged EXEC and press Enter** (re-triggers the login prompt) — no need to reboot.
- `transport input ssh` on VTY lines → restricts remote access to SSH only, meaning **all remote management traffic is encrypted**.

## 17. Windows CLI Troubleshooting Tools

- `ipconfig` → view IP configuration (Windows equivalent question to Cisco's `show ip interface brief`, but ipconfig is correct for a **PC**, not a Cisco device).
- `nslookup` → test/verify DNS resolution.
- `ping` → test basic connectivity (e.g., to the local router/gateway).
- `tracert` → trace the hop-by-hop path to a destination; useful for diagnosing where connectivity breaks down.
- `arp -a` → view the local ARP cache.
- Typical first troubleshooting steps for "local access works, but no Internet access": check IP/DNS config (`ipconfig`), test DNS (`nslookup`), and test connectivity to the local gateway (`ping`).

## 18. Protocol Analysis Best Practices

When assessing traffic flow patterns with a protocol analyzer:
- Capture during **peak utilization times** to get a representative sample.
- Capture on **multiple/different network segments**, not just one area — avoids a biased or incomplete picture.

## 19. Open Standards

- Advantage of open-standard protocols: they **encourage competition and promote choice** among vendors (not monopolization or vendor lock-in).
- Open standards are actively **regulated by standards organizations** (e.g., IETF, IEEE) — not "unregulated."

## 20. Network Communication Protocol Requirements

Protocols define rules that govern how messages are transmitted successfully across a network, including:
- **Message encoding**
- **Message size**
- **Delivery options** (unicast / multicast / broadcast)
- (Not protocol-defined: physical media selection, connector specs, or end-device installation — these are physical/hardware concerns.)

---

## Quick-Reference Cheat Sheet

| Concept | Key Fact |
|---|---|
| MAC address | 48 bits, OUI + unique ID, never changes, Layer 2 header |
| IP address | 32 (IPv4) / 128 (IPv6) bits, network + host portions, changes per network, Layer 3 header |
| DHCP ports | Server = UDP 67, Client = UDP 68 |
| TTL = 0 | Packet discarded, ICMP Time Exceeded sent |
| ARP target (remote dest.) | Default gateway's MAC, not final destination's MAC |
| /26 subnet | Block size 64, 62 usable hosts |
| /29 subnet | Block size 8, 6 usable hosts |
| /56 IPv6 block | 256 possible /64 subnets |
| UTP protection method | Twisting wire pairs (not shielding) |
| Crosstalk | Internal cable interference between adjacent pairs |
| EMI / RFI | External interference (electrical equipment / radio sources) |

---

*Last updated: based on ITN Course Final Exam review (98%, September 2026).*
