# Day 06: Ethernet LAN Switching (Part 2) — Frame Sizing, ARP, Ping, and MAC Address Table Management

> Detailed English summary of Jeremy's IT Lab CCNA 200-301 video **"Free CCNA | Ethernet LAN Switching (Part 2)"** — based on the user's Gemini-generated Korean notes, expanded, translated, and gap-filled with additional explanations. Continues directly from `09_day05_ethernet_lan_switching_part1.md` and `10_day05_ethernet_frame_fields_qa_deep_dive.md`. Video: https://www.youtube.com/watch?v=5q1pqdmdPjo

---

## 1. Ethernet Frame — Deeper Look at Sizing

### Preamble/SFD are transmitted with every frame, but aren't "the header" in the strict sense

- The Preamble and SFD are sent alongside every Ethernet frame and are necessary for the frame to be received correctly, but strictly speaking they are **not counted as part of the official Ethernet header** in size calculations. They exist purely to prepare the receiver (clock synchronization + "frame starts now" signal) — they carry no addressing or protocol information themselves.
- This is why frame-size figures (below) are usually quoted **excluding** the Preamble (7 bytes) and SFD (1 byte) — a total of 8 bytes that sits "outside" the officially measured frame size.

### Header + Trailer = 18 bytes

| Field | Size |
|-------|------|
| Destination MAC | 6 bytes |
| Source MAC | 6 bytes |
| Type/Length | 2 bytes |
| **Header subtotal** | **14 bytes** |
| FCS (Trailer) | 4 bytes |
| **Header + Trailer total** | **18 bytes** |

> **Added clarification:** this 18-byte figure is what Day 05's notes called the "5 header fields + 1 trailer field," just added together numerically (14 + 4 = 18), excluding Preamble/SFD as explained above.

### Minimum frame size and the minimum payload

- **Minimum Ethernet frame size: 64 bytes** (excluding Preamble/SFD) — this was mentioned in Day 05 as well, but this video explains *why* that number matters practically.
- Since the header+trailer overhead is fixed at 18 bytes, the **minimum size of the actual data (payload/encapsulated packet) must be**:

```
64 bytes (minimum frame) − 18 bytes (header + trailer) = 46 bytes (minimum payload)
```

### Padding

- If the data you actually want to send is **smaller than 46 bytes** (e.g., a tiny 34-byte packet), Ethernet cannot send a frame that small — it would fall below the 64-byte minimum and be treated as a corrupt "runt" frame by the receiver.
- To fix this, the sending device adds **padding**: extra bytes filled entirely with `0`s, appended after the real data, just to reach the 46-byte payload minimum.
  - Example: a 34-byte packet needs **12 bytes of padding** (34 + 12 = 46) to make the total frame reach exactly 64 bytes.
- **Why a minimum size exists at all** (added context, not explicit in the notes): Ethernet's original collision-detection mechanism (CSMA/CD, used on old shared/half-duplex Ethernet) required frames to be long enough that a collision could still be detected by the sender before it finished transmitting. A frame that was too short could finish sending before a collision signal made it back, making the collision invisible to the sender. The 64-byte minimum was calculated to guarantee this on maximum-length legacy Ethernet segments. Modern switched, full-duplex networks don't have collisions in the same way, but the 64-byte minimum remains part of the Ethernet standard for compatibility.

### Key EtherType Values (Type field, recap + additions)

| Protocol | EtherType (hex) | EtherType (decimal) |
|----------|--------------------|------------------------|
| IPv4 | `0x0800` | 2048 |
| **ARP** | **`0x0806`** | 2054 |
| IPv6 | `0x86DD` | 34525 |

> **Added clarification:** all three values are comfortably above the 1536 threshold discussed in Day 05, confirming they're interpreted as "Type" (protocol identifier), not "Length." ARP's EtherType (`0x0806`) is new information not covered in the Day 05 notes — it's essential to know since ARP (covered next) is carried directly inside an Ethernet frame, without being wrapped in an IP packet at all (ARP operates between Layer 2 and Layer 3, and is often called a "Layer 2.5" protocol for this reason).

---

## 2. ARP (Address Resolution Protocol)

### What ARP does

**ARP resolves a known Layer 3 address (IP address) into the corresponding Layer 2 address (MAC address).**

> **Added clarification — why this is needed at all:** a switch forwards frames using MAC addresses, not IP addresses (Day 05). But applications and humans work with IP addresses ("ping 192.168.1.10"). Before a device can actually put a frame on the wire, it needs to fill in the Destination MAC Address field of the Ethernet header — and the only address it started out knowing was the destination's *IP* address. ARP is the mechanism that bridges this gap: "I know your IP address, now tell me your MAC address so I can actually address a frame to you."

### The Two ARP Messages

| Message | Direction | Purpose |
|---------|-----------|---------|
| **ARP Request** | **Broadcast** (`FF:FF:FF:FF:FF:FF`) — sent to *every* host on the local network | "Who has this IP address? Please tell me [your MAC address]." |
| **ARP Reply** | **Unicast** — sent directly back only to the device that asked | "I have that IP address — here is my MAC address." |

- **Why the request is a broadcast:** the sender doesn't know *who* has the target IP address yet, so it has no specific MAC address to send the request to — broadcasting to everyone is the only way to reach the right device without already knowing where it is.
- **Why the reply is a unicast:** once the device that owns the target IP address hears the broadcast request, it already knows exactly who asked (the request contains the requester's own IP and MAC address), so it can reply directly to that one device instead of broadcasting the answer to everyone.

> **Added clarification — the full ARP request/reply cycle, step by step:**
> 1. PC-A wants to send a packet to PC-B (PC-A knows PC-B's IP address, but not its MAC address).
> 2. PC-A broadcasts an ARP Request onto the LAN: *"Who has IP 192.168.1.20? Tell 192.168.1.10 (me)."*
> 3. Every device on the LAN receives this broadcast frame and inspects it, but only the device that actually owns 192.168.1.20 (PC-B) responds.
> 4. PC-B sends an ARP Reply directly back to PC-A (unicast): *"192.168.1.20 is at MAC address AA:BB:CC:DD:EE:FF."*
> 5. PC-A now stores this IP-to-MAC mapping in its own ARP table and can finally build and send the actual Ethernet frame to PC-B.

### ARP Table

- A table that stores the **learned mappings between IP addresses and MAC addresses**, so a device doesn't have to run the ARP request/reply process again for every single packet it sends to the same destination.
- **On Windows/macOS/Linux hosts:** view with the command `arp -a`
- **On Cisco IOS devices (routers):** view with the command `show arp`

> **Added clarification — ARP entries also age out:** similar to a switch's MAC address table, ARP table entries are not kept forever. Operating systems typically expire dynamic ARP entries after a few minutes of inactivity (the exact timeout varies by OS — e.g., Windows typically uses a shorter timer, around 2–10 minutes depending on version/reachability, while Cisco IOS devices default to a 4-hour ARP cache timeout). This isn't identical to the switch's 5-minute MAC address aging timer covered in Day 05 — they are two *separate* tables (ARP table = IP-to-MAC on a host/router; MAC address table = MAC-to-port on a switch) with independent aging behavior.

---

## 3. Ping and ICMP

### What Ping does

**Ping** is a network utility used to test **reachability** between two devices and measure the **round-trip time (RTT)** — how long it takes for a message to go to the destination and a reply to come back.

### How Ping Works

- Ping uses the **ICMP (Internet Control Message Protocol)** protocol, specifically two message types:
  - **ICMP Echo Request** — sent to the target
  - **ICMP Echo Reply** — sent back by the target if it's reachable

> **Added clarification — where ICMP fits in the stack:** ICMP operates at Layer 3 (it's carried directly inside an IP packet, just like TCP or UDP would be, but ICMP is used for diagnostics/control messages rather than carrying application data). This is different from ARP, which operates below IP entirely (directly inside an Ethernet frame with its own EtherType, `0x0806`) rather than being carried inside an IP packet.

### Ping vs. ARP — Unicast, Not Broadcast

- Unlike ARP, a ping (ICMP Echo Request) is **not broadcast** — it's sent **directly to a specific host**.
- Because of this, **the sending device must already know the destination's MAC address before it can send the ping** — which means an ARP Request/Reply exchange typically has to happen *first*, immediately before the actual ping packets are sent.

### Cisco IOS Default Ping Behavior

- By default, Cisco IOS sends **5 ICMP Echo Requests**, each **100 bytes** in size, when you run the `ping` command.
- **Why the first ping often fails (shown as `.` instead of `!` in the output):** the device doesn't yet know the destination's MAC address, so it has to pause and run the ARP Request/Reply process first. This takes just long enough that **the very first ping attempt often times out** while ARP is still resolving, and shows as a failure (`.`). Once the MAC address is learned and cached in the ARP table, the remaining 4 pings succeed instantly and show as `!`.

> **Added clarification — reading Cisco's ping output symbols:**
>
> | Symbol | Meaning |
> |--------|---------|
> | `!` | Success — Echo Reply received |
> | `.` | Timeout — no reply received in time (often the very first ping, due to the ARP delay described above) |
> | `U` | Destination unreachable |
>
> A typical successful Cisco ping output looks like: `.!!!!` — one timeout followed by four successes — which is the exact pattern the ARP-delay explanation describes.

---

## 4. Cisco Switch MAC Address Table Management

### Viewing the Table

```
Switch# show mac address-table
```
(On older/some IOS versions, the equivalent command is `show mac-address-table` — with a hyphen. Newer IOS uses the space-separated form shown above.)

### Table Fields

| Field | Meaning |
|-------|---------|
| **VLAN** | Which VLAN this MAC address entry belongs to (VLANs are a Layer 2 network segmentation feature — likely to be covered in more depth later in the SRWE portion of CCNA) |
| **MAC Address** | The learned MAC address |
| **Type** | Whether the entry is **Dynamic** (learned automatically, as covered in Day 05) or **Static** (manually configured by an administrator and does not age out) |
| **Ports** | Which switch interface/port that MAC address was learned on |

> **Added clarification — Dynamic vs. Static entries:** Day 05 covered dynamic learning (the switch watches Source MAC addresses to build the table automatically). This video adds that entries can also be **static** — manually entered by a network administrator with a command like `mac address-table static <MAC> vlan <VLAN-ID> interface <interface>`. Static entries are useful for security (locking a specific MAC address to a specific port so no other device can use that port) and they **never age out**, unlike dynamic entries.

### Aging (Recap + Confirmation from Day 05)

- If a switch receives **no traffic from a given MAC address for 5 minutes**, that entry is **automatically removed** from the dynamic MAC address table. This matches exactly what was covered in Day 05's notes on Basic Device Security and Day 05's Ethernet LAN Switching Part 1 video.

### Manually Clearing MAC Address Table Entries

| Command | Effect |
|---------|--------|
| `clear mac-address-table dynamic` | Removes **all** dynamically learned MAC address entries from the table |
| `clear mac-address-table dynamic address <MAC-address>` | Removes only the entry for **one specific MAC address** |
| `clear mac-address-table dynamic interface <interface-ID>` | Removes all dynamic entries that were learned on **one specific port/interface** |

> **Added clarification — why you'd ever want to manually clear the table:** in real-world troubleshooting, if a device has physically moved to a different switch port, or its network card has been replaced (new MAC address), the switch's old table entry can point traffic to the wrong (now-stale) port until the 5-minute aging timer naturally clears it. Manually clearing the relevant entry (or the whole table) forces the switch to re-learn the correct mapping immediately, rather than waiting for the timeout — useful during labs, troubleshooting, or right after reconfiguring a network.

---

## 5. Quick Summary

- The Preamble and SFD travel with every frame but aren't counted as part of the "official" header; the header (14 bytes: Dest MAC + Src MAC + Type/Length) plus the trailer (FCS, 4 bytes) together total **18 bytes**.
- Minimum frame size is 64 bytes, so the minimum payload size is **64 − 18 = 46 bytes**; anything smaller gets **zero-padding** added to reach 46 bytes.
- Key EtherType values: IPv4 = `0x0800`, ARP = `0x0806`, IPv6 = `0x86DD` — all well above the 1536 "Type vs. Length" threshold from Day 05.
- **ARP** resolves a known IP address into its MAC address, using a **broadcast Request** ("who has this IP?") and a **unicast Reply** ("I do, here's my MAC"). Results are cached in an ARP table (`arp -a` on hosts, `show arp` on Cisco IOS).
- **Ping** uses **ICMP Echo Request/Reply** to test reachability and measure round-trip time. Because ping is unicast (not broadcast), the sender needs the destination's MAC address *first* — which is why the very first ping often fails (`.`) while ARP resolves, before subsequent pings succeed (`!`).
- Cisco switches manage their MAC address table with `show mac address-table` (fields: VLAN, MAC Address, Type [Dynamic/Static], Ports), aging out dynamic entries after 5 minutes of inactivity, and can be manually cleared with `clear mac-address-table dynamic` (optionally scoped to one address or one interface).

---

## 6. Command / Concept Cheat Sheet

| Command / Term | Purpose |
|-----------------|---------|
| `arp -a` | View the ARP table on a Windows/macOS/Linux host |
| `show arp` | View the ARP table on a Cisco IOS device |
| `ping <IP address>` | Send ICMP Echo Requests to test reachability and measure RTT (Cisco IOS default: 5 requests, 100 bytes each) |
| `show mac address-table` | View a Cisco switch's MAC address table (VLAN, MAC, Type, Ports) |
| `clear mac-address-table dynamic` | Remove all dynamic MAC address table entries |
| `clear mac-address-table dynamic address <MAC>` | Remove one specific MAC address entry |
| `clear mac-address-table dynamic interface <ID>` | Remove all dynamic entries learned on one interface |
| ARP Request | Broadcast (`FF:FF:FF:FF:FF:FF`) — "Who has this IP address?" |
| ARP Reply | Unicast — "I have it, here's my MAC address" |
| ICMP Echo Request/Reply | The two message types used by ping |
| Padding | Zero-filled bytes added to a payload smaller than 46 bytes, to meet Ethernet's 64-byte minimum frame size |

---

## 7. Review Questions (for self-testing / Anki)

| Question | Answer |
|----------|--------|
| Are the Preamble and SFD counted as part of the official Ethernet header size? | No — they're sent with every frame but excluded from standard header/frame size calculations |
| What is the combined size of the Ethernet header and trailer (excluding Preamble/SFD)? | 18 bytes (14-byte header + 4-byte FCS trailer) |
| What is the minimum Ethernet frame size (excluding Preamble/SFD)? | 64 bytes |
| What is the minimum payload (encapsulated packet) size? | 46 bytes (64 − 18) |
| What happens if the payload is smaller than 46 bytes? | Zero-filled padding bytes are added to reach the 46-byte minimum |
| What is the EtherType value for ARP? | `0x0806` |
| What is the EtherType value for IPv4? | `0x0800` |
| What is the EtherType value for IPv6? | `0x86DD` |
| What does ARP do? | Resolves a known IP (Layer 3) address into its corresponding MAC (Layer 2) address |
| Is an ARP Request a broadcast or unicast message? | Broadcast (`FF:FF:FF:FF:FF:FF`) |
| Is an ARP Reply a broadcast or unicast message? | Unicast — sent directly to the original requester |
| Where can you view the ARP table on a Windows/Mac/Linux computer? | `arp -a` |
| Where can you view the ARP table on a Cisco IOS device? | `show arp` |
| What does Ping use to test reachability? | ICMP Echo Request and Echo Reply messages |
| Is a ping message broadcast like ARP? | No — it's unicast, sent directly to one specific host |
| Why does the first ping in a Cisco `ping` command sequence often fail? | Because the device doesn't yet know the destination's MAC address and must first complete an ARP Request/Reply exchange, which delays/times out the first Echo Request |
| How many ICMP Echo Requests does Cisco IOS send by default, and what size? | 5 requests, 100 bytes each |
| What command shows a Cisco switch's MAC address table? | `show mac address-table` |
| What four fields appear in the MAC address table output? | VLAN, MAC Address, Type, Ports |
| What are the two possible values for the "Type" field in the MAC address table? | Dynamic and Static |
| How long before an inactive dynamic MAC address entry is removed? | 5 minutes |
| Does a static MAC address entry ever age out automatically? | No |
| What command removes all dynamic MAC address table entries? | `clear mac-address-table dynamic` |
| What command removes only one specific MAC address entry? | `clear mac-address-table dynamic address <MAC-address>` |
| What command removes all dynamic entries learned on one specific interface? | `clear mac-address-table dynamic interface <interface-ID>` |

---

## My Study Log

- [x] Watched "Ethernet LAN Switching (Part 2)" video (Jeremy's IT Lab)
- [x] Had Gemini summarize the video content (Korean)
- [x] Had this summary translated, expanded, and gap-filled in English
- [ ] Reviewed Day 06 Anki flashcards
- [ ] Packet Tracer lab for ARP/Ping/MAC address table (if available)

### Notes / Confusing Points

- (add your own notes here)
