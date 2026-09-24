# 113. Data Link Layer, Router Frame Handling, ARP, TCP/UDP, IP Characteristics, and `show ip interface brief`

> CCNA ITN quiz review covering Questions 27-32.
> Topics: Data link layer role, how a router rewrites Layer 2 headers, ARP table, TCP vs. UDP common features, characteristics of IP, and reading `show ip interface brief`.

---

## Table of Contents

1. [Q27 - Main characteristic of the data link layer](#q27---main-characteristic-of-the-data-link-layer)
2. [Q28 - What R1 does with the Ethernet frame header](#q28---what-r1-does-with-the-ethernet-frame-header)
3. [Q29 - Which protocol builds the ARP table](#q29---which-protocol-builds-the-arp-table)
4. [Q30 - Two characteristics shared by TCP and UDP](#q30---two-characteristics-shared-by-tcp-and-udp)
5. [Q31 - Two characteristics of IP](#q31---two-characteristics-of-ip)
6. [Q32 - `show ip interface brief` output](#q32---show-ip-interface-brief-output)
7. [Big Picture Cheat Sheet](#big-picture-cheat-sheet)
8. [Useful English Vocabulary](#useful-english-vocabulary)

---

## Q27 - Main characteristic of the data link layer

**Question:** What is one main characteristic of the data link layer?

**Correct answer:** *It shields the upper layer protocol from being aware of the physical medium to be used in the communication.*

### Why it is correct

The data link layer (Layer 2) acts as a **translator between the Network layer (Layer 3) and the Physical layer (Layer 1)**.

Upper-layer protocols such as IP do not need to care whether data travels over an Ethernet cable, Wi-Fi, or fiber-optic cable. The data link layer packages the data into a **frame** suited to each medium. Even if the medium changes, the upper layers keep working as before.

### Why the other options are wrong

| Option | Belongs to |
|---|---|
| Converts a stream of data bits into a predefined code | Physical layer (Layer 1) - encoding |
| Generates electrical or optical signals that represent 1s and 0s | Physical layer (Layer 1) |
| Accepts Layer 3 packets and decides the path to a remote network | Network layer (Layer 3) - routing |

### Memory tips

- **Layer 1 (Physical):** signals, bits, cables
- **Layer 2 (Data Link):** frames, MAC addresses, shielding the upper layers from the medium
- **Layer 3 (Network):** packets, IP addresses, path selection (routing)

> Path selection = Layer 3, signals = Layer 1, shielding from the medium = Layer 2.

---

## Q28 - What R1 does with the Ethernet frame header

**Scenario:** PC1 (192.168.10.8/24) sends a packet to PC2 (192.168.11.5/24). R1 and R2 are connected through serial links (S0/0/0), and routing is configured between them. What will R1 do with the Ethernet frame header attached by PC1?

**Correct answer:** *Remove the Ethernet header and configure a new Layer 2 header before sending it out S0/0/0.*

### Key concept: IP address vs. MAC address (parcel analogy)

| | IP address (Layer 3) | MAC address / Layer 2 header |
|---|---|---|
| Analogy | Final destination address on the parcel | Shipping label for the current leg only |
| Changes along the path? | **No** - stays the same from source to destination | **Yes** - rebuilt at every hop |

Example: sending a parcel from Australia to Korea. First it goes to the local post office (Keysborough), then Melbourne, then Incheon International Airport, and finally Bucheon. The final address never changes, but each leg has a different destination.

### Step-by-step packet journey

1. **PC1 builds a frame.**
   - Inside: IP packet (destination IP = 192.168.11.5).
   - Outside: Ethernet header (destination MAC = R1's G0/0 MAC address).
   - PC2 is on a different network, so PC1 sends the frame to its **default gateway (R1)**.
2. **R1 receives the frame on G0/0.**
   - Layer 1: receives bits.
   - Layer 2: checks that the frame is addressed to its own MAC, then **removes the Ethernet header** (de-encapsulation).
3. **R1 decides the path at Layer 3.**
   - Reads the destination IP (192.168.11.5) in the IP header.
   - Looks it up in the **routing table** and finds that the packet must leave via **S0/0/0**.
4. **R1 builds a new Layer 2 header.**
   - S0/0/0 is a **serial link**, not Ethernet, so it needs a serial Layer 2 header (e.g., HDLC or PPP).
   - This is **encapsulation**. Layer 1 then sends it out as bits.
5. **R2 repeats the same process** and delivers the packet to PC2.

### Inside a router

```
[Receive: G0/0]                       [Send: S0/0/0]

Layer 1: receive signal               Layer 1: transmit signal
   ↓                                     ↑
Layer 2: remove Ethernet header       Layer 2: add NEW Layer 2 header
   ↓                                     ↑
Layer 3: read IP -> routing table -> decide outgoing interface
```

A router is called a **Layer 3 device** because its decision is made at Layer 3, but it has **Layers 1 to 3** on every interface. It decides at Layer 3, then passes the packet down and attaches a new Layer 2 header.

### Why the other options are wrong

| Option | Why it is wrong |
|---|---|
| Open the header and use it to determine whether data is sent out S0/0/0 | The path is decided by the **IP header (Layer 3)**. The Ethernet header has no routing information; it is checked and discarded. |
| Nothing, because the router has a route | A router always removes the old Layer 2 header and builds a new one. |
| Open the header and replace the destination MAC with a new one | The outgoing link is serial, so the **entire header format changes**. It is not just a MAC swap. |

### Key points

- The destination **IP address never changes**.
- The **Layer 2 header (MAC address) is created anew at every hop**.
- **Layer 3 (IP)** decides where the packet goes.
- The Ethernet header is a **temporary cardboard box for one hop**: the router removes it, checks the IP, decides the path, and wraps the packet in a new box.

---

## Q29 - Which protocol builds the ARP table

**Question:** Refer to the exhibit (output with *Internet Address*, *Physical Address*, and *Type* columns). Which protocol was responsible for building the table?

**Correct answer:** **ARP** (Address Resolution Protocol)

### Why ARP

The output comes from the `arp -a` command on Windows, which shows the **ARP table (ARP cache)**.

- **Internet Address** = IP address (Layer 3)
- **Physical Address** = MAC address (Layer 2)

So the table is a **mapping from IP addresses to MAC addresses**, and ARP is the protocol that builds it.

### How ARP builds the table

1. The PC wants to send data to 192.168.1.254 but does not know its MAC address.
2. The PC **broadcasts an ARP request**: "If your IP is 192.168.1.254, please tell me your MAC address."
3. The target device sends back an **ARP reply** with its MAC address.
4. The PC stores the result in its ARP table as a **dynamic** entry.

### Dynamic vs. static entries

| Type | Meaning | Example |
|---|---|---|
| **Dynamic** | Learned through ARP during real communication; removed after a period of time | `192.168.1.254 -> 64-0f-29-0d-36-91` |
| **Static** | Registered automatically (not learned by ARP requests) | Broadcast `ff-ff-ff-ff-ff-ff`, multicast `01-00-5e-...` |

### Why the other options are wrong

| Protocol | What it actually does |
|---|---|
| **ICMP** | Error reporting and ping (Layer 3). Builds no mapping table. |
| **DNS** | Translates domain names into IP addresses. Unrelated to MAC addresses. |
| **DHCP** | Automatically allocates IP addresses. Does not build an IP-to-MAC table. |

**Why DHCP is confusing:** DHCP deals with IP addresses (and uses MAC addresses to identify clients), but its role is to *lend an IP address*. Finding the MAC that belongs to an IP is ARP's job. They are separate protocols that work together in practice.

### Memory tips

- **ARP:** IP address -> MAC address
- **DNS:** domain name -> IP address
- **DHCP:** automatic IP address allocation
- **ICMP:** error reporting and ping

> If you see IP addresses and MAC addresses paired in a table, think ARP.

---

## Q30 - Two characteristics shared by TCP and UDP

**Correct answers:** **Port numbering** and **use of checksum**

Both TCP and UDP are **Layer 4 (transport layer)** protocols.

### 1. Port numbering

Both protocols use port numbers to identify which application the data belongs to.

- HTTP uses **TCP port 80**.
- DNS uses **UDP (and TCP) port 53**.

This is why a browser, a messenger, and a game can run at the same time on one computer without their data getting mixed up.

### 2. Use of checksum

Both have a **checksum field in the header**. The sender calculates a small value from the data, and the receiver recalculates it. If the values differ, the data was corrupted in transit.

- **UDP:** discards the corrupted data (no recovery).
- **TCP:** detects the problem and **retransmits** to ensure reliable delivery.

> Note: in IPv4, the UDP checksum is technically optional (mandatory in IPv6). For exam purposes, treat checksum as shared by both.

### Why the other options are wrong

| Option | Reason |
|---|---|
| Ability to carry digitized voice | VoIP normally uses **UDP**. TCP retransmissions add latency, which hurts real-time voice. Not shared. |
| 3-way handshake | **TCP only** (SYN, SYN-ACK, ACK). UDP sends with no connection setup. |
| Default window size | **TCP only** (flow control). UDP has no window size. |
| Connectionless communication | **UDP only**. TCP is connection-oriented. |

### TCP vs. UDP comparison

| Feature | TCP | UDP |
|---|---|---|
| Port numbering | Yes | Yes |
| Checksum | Yes | Yes |
| 3-way handshake | Yes | No |
| Window size (flow control) | Yes | No |
| Connection type | Connection-oriented | Connectionless |
| Reliability (retransmission, sequencing) | Yes | No |
| Main uses | Web, email, file transfer | Voice, video, games, DNS |

> Common features = basic Layer 4 functions (ports + checksum). TCP-only features = reliability functions. UDP is faster and lighter than TCP.

---

## Q31 - Two characteristics of IP

**Correct answers:**

- *Operates independently of the network media*
- *Does not require a dedicated end-to-end connection*

IP (Internet Protocol) is a **Layer 3** protocol. Its main job is to look at the destination IP address and forward the packet.

### Three core features of IP

1. **Connectionless:** no connection is established before transmission.
2. **Best effort:** IP tries its best but does **not guarantee delivery**.
3. **Media independent:** it works over Ethernet, Wi-Fi, fiber, or serial links alike.

### Option: Operates independently of the network media

An IP packet has the same format whether it travels over Ethernet, serial, or Wi-Fi. The **Layer 2 data link layer** packages the packet into a frame suited to each medium, so IP (Layer 3) does not have to care about the medium. This is the same principle as Q27: *the data link layer shields the upper layers from the medium.*

### Option: Does not require a dedicated end-to-end connection

- **End-to-end:** from the source device (PC1) to the destination device (PC2).
- **Dedicated:** reserved only for one user.

| | Old landline telephone | IP |
|---|---|---|
| Path | A whole line is reserved for the two people during the call | No reserved path |
| Analogy | Private road | Shared public roads (routers); each packet finds its own way |

Sending a parcel is similar: you don't need to phone the receiver beforehand; you just send it.

### Why is IP designed without connections?

Setting up a connection sounds useful, but it costs speed and efficiency:

- It is slower, because preparation is needed before transmission.
- Routers would have to **remember the state of every connection**, which makes them heavy (billions of transmissions happen at once).
- If a dedicated path breaks, the communication is cut. Without a fixed connection, packets can be **rerouted** through another path.
- A dedicated path stays occupied even when idle.

So IP is designed to be **as simple and light as possible**.

### Why does IP not guarantee delivery?

Because each layer has its own role (**division of labor**):

- **IP (Layer 3) = postman:** reads the address, finds the route, and delivers.
- **TCP (Layer 4) = registered-mail service:** checks arrival, reorders packets, retransmits lost ones.

If every communication carried guarantee functions, everything would be slower. Some traffic, such as VoIP or online games, values speed over reliability. So IP does only the fundamentals: **if a guarantee is needed, TCP is added on top; if not, UDP is used.**

### Why the other options are wrong

| Option | Reason |
|---|---|
| Guarantees delivery of packets | IP is best effort. Guarantees are **TCP's** job. |
| Re-assembles out-of-order packets into the correct order | Sequencing is done by **TCP**. IP does not care about order. |
| Retransmits packets if errors occur | Retransmission is done by **TCP**. IP does not retransmit. |

### IP vs. TCP (and UDP)

| Feature | IP | TCP |
|---|---|---|
| Layer | Layer 3 | Layer 4 |
| Connection | Connectionless | Connection-oriented |
| Delivery | Best effort | Guaranteed |
| Reassembly | No | Yes |
| Retransmission | No | Yes |
| Media independent | Yes | Not applicable |

**IP and UDP are similar:** both are connectionless and best effort. The difference is that IP works at Layer 3 and finds paths using **IP addresses**, while UDP works at Layer 4 and distinguishes applications using **port numbers**.

### Grammar note: media vs. medium

- **medium** = singular (Ethernet is a medium).
- **media** = plural (Ethernet, Wi-Fi, and fiber are media).
- "Network media" is a standard term, and "media independent" is a common expression.

> Guarantee, sequencing, and retransmission = TCP's job. IP is just a postman doing his best on public roads.

---

## Q32 - `show ip interface brief` output

**Question:** Refer to the exhibit. What three facts can be determined from the viewable output of `show ip interface brief`? (Choose three.)

**Exhibit summary:**

| Interface | IP-Address | Status | Protocol |
|---|---|---|---|
| FastEthernet0/1 | unassigned | **up** | **up** |
| FastEthernet0/2, 0/3, 0/5, 0/6, ..., 0/23, 0/24 | unassigned | down | down |
| **Vlan1** | **192.168.11.3** | **up** | **up** |

**Correct answers:**

1. *The default SVI has been configured.*
2. *The switch can be remotely managed.*
3. *One device is attached to a physical interface.*

### How to read the columns

| Column | Meaning |
|---|---|
| Interface | Interface name |
| IP-Address | Assigned IP address |
| Status | **Layer 1** state (cable/device connected) |
| Protocol | **Layer 2** state (line protocol working) |

### Why each answer is correct

- **The default SVI has been configured.**
  An SVI (Switch Virtual Interface) is a virtual interface inside the switch. A Layer 2 switch does not put IP addresses on physical ports; it puts one on an SVI instead. **VLAN 1 is the default VLAN**, so `Vlan1` is the default SVI, and it has the IP 192.168.11.3.
- **The switch can be remotely managed.**
  Vlan1 has an IP address and is **up/up**, so an admin can connect to 192.168.11.3 (via SSH or Telnet) from another device. Switches receive IP addresses **for management purposes**.
- **One device is attached to a physical interface.**
  **Status up = something is connected.** Only FastEthernet0/1 is up/up, so exactly **one device** is attached.

### Why the other options are wrong

| Option | Reason |
|---|---|
| Passwords have been configured on the switch | This command shows only IP and status. Use `show running-config` to see passwords. |
| Two physical interfaces have been configured | All physical ports show `unassigned` (no IP), and only one is up. |
| Two devices are attached to the switch | Only Fa0/1 is up, so only **one** device is connected. |

### Note on the "Method: manual" column

Physical switch ports show `manual` even without an IP address by default. It does **not** mean the ports were configured.

### Memory tips

- `show ip interface brief` shows **IP addresses and up/down status**.
- It does **not** show passwords or detailed settings (use `show running-config`).
- **up/up = connected**, **down/down = not connected**.
- **Vlan1 with an IP and up/up = the switch can be remotely managed.**

---

## Big Picture Cheat Sheet

### OSI layers covered in this review

| Layer | Name | Data unit | Key items |
|---|---|---|---|
| 4 | Transport | Segment / datagram | TCP, UDP, port numbers, checksum |
| 3 | Network | Packet | IP address, routing, best effort, connectionless |
| 2 | Data Link | Frame | MAC address, ARP mapping, shields upper layers from the medium |
| 1 | Physical | Bits | Signals, encoding, cables |

### Protocol quick reference

| Protocol | Job |
|---|---|
| **ARP** | IP address -> MAC address |
| **DNS** | Domain name -> IP address |
| **DHCP** | Automatic IP address allocation |
| **ICMP** | Error reporting and ping |
| **IP** | Addressing and routing, best effort |
| **TCP** | Reliable, connection-oriented delivery |
| **UDP** | Fast, lightweight, connectionless delivery |

### Key one-liners

- The router **strips the Layer 2 header, reads the IP, picks the path, and wraps a new Layer 2 header**.
- **IP addresses stay the same end to end; MAC addresses change at every hop.**
- **Guarantee, sequencing, and retransmission = TCP.** IP just does its best.
- **Ports + checksum = what TCP and UDP share.**
- **Vlan1 (SVI) with an IP and up/up = remotely manageable switch.**

---

## Useful English Vocabulary

| Term | Meaning |
|---|---|
| encapsulation / de-encapsulation | Adding / removing headers as data moves down / up the layers |
| hop | One leg of the path between two devices |
| default gateway | The router a host uses to reach other networks |
| outgoing interface | The interface a router sends a packet out of |
| connectionless / connection-oriented | No setup before sending / setup and tracking before sending |
| best effort | Tries to deliver but gives no guarantee |
| dedicated end-to-end connection | A reserved path from source to destination |
| media / medium | Plural / singular of transmission channel |
| SVI | Switch Virtual Interface (virtual interface for switch management) |
| checksum | Value used to detect corrupted data |
| retransmit | Send again after loss or error |
| trade-off | Giving up one benefit to gain another |
