# Network Fundamentals – Study Notes
> Based on Cisco NetAcad coursework. Gemini-provided answers verified and corrected where needed.

---

## 1. Communication Process Elements

When data is transmitted across a network, it goes through several distinct steps:

| Step | Description | Analogy |
|------|-------------|---------|
| **Encoding** | Converting information into a suitable form for transmission (e.g., converting data into electrical/optical signals — 0s and 1s) | Translating a letter into Morse code before sending |
| **Formatting** | Properly identifying the address of the sender and receiver so the message reaches the right destination | Writing "From" and "To" addresses on an envelope |
| **Encapsulation** | Wrapping data with necessary header/trailer information (addresses, error-checking, etc.) at each layer | Putting a letter inside an envelope, sealing it, and adding a stamp |

> ⚠️ **Gemini Error Caught:** Gemini incorrectly answered **Encapsulation** for both the "encoding" question and the "formatting" question. The correct answers are:
> - *Converting information into proper form for transmission* → **Encoding**
> - *Identifying sender/receiver address* → **Formatting**

---

## 2. Message Timing Components

**Message Timing** refers to rules that control *when* and *how fast* data is sent between devices.

The three core components are:

### ✅ Flow Control
- Regulates the rate of data transmission so the sender doesn't overwhelm the receiver.
- Analogy: Telling a fast speaker to slow down so you can keep up.

### ✅ Access Method
- Determines *who gets to transmit* when multiple devices share the same network medium.
- Prevents collisions by deciding the order of transmission.
- Analogy: Raising your hand in class before speaking so only one person talks at a time.

### ✅ Response Timeout
- Defines how long a sender waits for an acknowledgment before giving up or retrying.
- Analogy: If you send a text and get no reply in 5 minutes, you assume it wasn't delivered.

> ⚠️ **Gemini Error Caught:** Gemini listed **Retransmit time** instead of **Access method** as one of the three components. The correct third component is **Access method**.

---

## 3. Data Delivery Methods

When a network device sends data, it can use one of three delivery methods:

| Method | Target | Analogy |
|--------|--------|---------|
| **Unicast** | One specific device | 1-on-1 direct message (DM) |
| **Broadcast** | All devices on the network | School-wide announcement over the intercom |
| **Multicast** | A specific group of devices (not all) | A group chat — only members receive the message |

**Key Rule:** *"One or more end devices, but NOT all"* → **Multicast**

---

## 4. Network Protocols & Models

### What is a Protocol?
A **protocol** is a set of agreed-upon rules that govern how devices communicate.
- Think of it as a **common language** — without it, devices from different manufacturers can't understand each other.

### What is a Reference Model?
A **reference model** (e.g., OSI, TCP/IP) is a **blueprint** that visualizes how communication is broken into layers, making it easier to understand and troubleshoot.

---

## 5. Cisco Device Memory Types

| Memory | Volatile? | Stores | Notes |
|--------|-----------|--------|-------|
| **RAM** | ✅ Yes (wiped on reboot) | Running configuration (`running-config`) | Active workspace; lost when powered off |
| **NVRAM** | ❌ No (persistent) | Startup configuration (`startup-config`) | Survives reboots |
| **Flash** | ❌ No (persistent) | IOS operating system image | Like a hard drive for the OS |
| **ROM** | ❌ No (read-only) | Bootstrap / POST instructions | Basic boot instructions, can't be changed by user |

### Key Commands
```bash
# Copy startup config into RAM (make it the running config)
copy startup-config running-config

# Save running config to NVRAM (make it the startup config)
copy running-config startup-config
```

---

## 6. Network Services

### DHCP (Dynamic Host Configuration Protocol)
- **Function:** Automatically assigns an IP address to each device that joins the network.
- **Analogy:** A ticket dispenser at a deli counter — you walk in, grab a number (IP), and you're ready to go.
- Without DHCP, every device would need a manually configured IP address.

---

## 7. Testing Connectivity with Ping

The `ping` command tests whether two devices can communicate over a network.

### How it works:
1. Device A sends an **echo request** to Device B.
2. Device B replies with an **echo reply**.
3. If replies are received → connection is working ✅

### Important Notes:
- **First ping often times out** — this is normal. The network needs a moment to establish the path (ARP resolution).
- **Always test in both directions** (A→B and B→A).
  - If A→B works but B→A fails → likely a **firewall issue**, not a cable/network issue.
  - Windows Firewall blocks ICMP echo requests by default.

### Example (from lab):
```
PC-A> ping 192.168.1.2   # Ping Switch S1
PC-A> ping 192.168.1.3   # Ping Switch S2
PC-A> ping 192.168.1.11  # Ping PC-B
PC-B> ping 192.168.1.10  # Reverse test back to PC-A
```

---

## 8. Subnetting Basics

### What is a Subnet Mask?
A subnet mask filters which part of an IP address is the **network** portion and which is the **host** portion.
- `255` in the mask → **keep** that octet (network part)
- `0` in the mask → **zero out** that octet (host part → becomes 0)

### Example:
```
IP Address:    10.1.100.50
Subnet Mask:   255.255.0.0

Network Address: 10.1.0.0
(Keep 10.1, zero out 100.50)
```

---

*Last updated based on Cisco NetAcad – Protocols and Models module*
