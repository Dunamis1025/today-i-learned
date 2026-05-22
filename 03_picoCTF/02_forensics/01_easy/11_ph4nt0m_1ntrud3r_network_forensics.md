# CTF Writeup: Ph4nt0m 1ntrud3r

> **Category:** Network Forensics  
> **Difficulty:** Easy  
> **Tools Used:** Wireshark, tshark, Python, CyberChef

---

## Table of Contents
1. [Challenge Overview](#1-challenge-overview)
2. [Key Concepts](#2-key-concepts)
3. [What is a PCAP File?](#3-what-is-a-pcap-file)
4. [Understanding Network Packets](#4-understanding-network-packets)
5. [Reading a Hex Dump](#5-reading-a-hex-dump)
6. [Solution Walkthrough](#6-solution-walkthrough)
7. [Lessons Learned](#7-lessons-learned)

---

## 1. Challenge Overview

**Title:** Ph4nt0m 1ntrud3r (Phantom Intruder)

**Scenario:**  
Someone has breached the system and stolen sensitive data. Your mission is to analyze a PCAP (network traffic capture) file to trace how the attack happened and recover the hidden flag.

**Hints given:**
- *"Filter your packets"* → You need to isolate the relevant packets from the noise
- *"Attacks were done in a timely manner / Time is essential"* → The **order of timestamps** is the key to solving this challenge

---

## 2. Key Concepts

### Intent
In security, **intent** means "what is the attacker trying to do?"  
When analyzing traffic, you don't just look at raw data — you try to understand the attacker's goal.

> Example: If someone repeatedly requests `admin.php` or `config.php`, their intent is clearly to access restricted files.

### Beacon
A **beacon** is a periodic, automated signal sent from an infected machine to the attacker's server (called a C2 — Command and Control server).

Think of it like a heartbeat. The infected system checks in every X seconds asking:
> "Any new orders for me?"

Because beacons happen at **regular intervals**, they create a rhythmic pattern in network logs — which is how security teams detect compromised systems.

### Decipher
To **decipher** means to convert encoded or hidden data into human-readable form.

Attackers often encode their commands to avoid detection. For example:
```
d2hvYW1p  →  (Base64 decode)  →  whoami
```

---

## 3. What is a PCAP File?

A **PCAP (Packet Capture)** file is a recording of all network traffic that occurred over a period of time.

Think of it like a CCTV recording, but for network data instead of video. Tools like **Wireshark** and **tshark** can open and analyze these files.

| Tool | Type | Use Case |
|------|------|----------|
| Wireshark | GUI | Visually browse and filter packets |
| tshark | CLI (Terminal) | Automate extraction and filtering |

---

## 4. Understanding Network Packets

Every packet is like a **shipping box**:

```
┌─────────────────────────────────┐
│  IP Header (20 bytes)           │  → Sender/Receiver IP address
├─────────────────────────────────┤
│  TCP Header (20 bytes)          │  → Port numbers, connection state
├─────────────────────────────────┤
│                                 │
│  Payload  ← THE ACTUAL DATA     │  → What the attacker sent/received
│                                 │
└─────────────────────────────────┘
```

- **IP Header:** Always 20 bytes. Contains source and destination IP addresses.
- **TCP Header:** Always 20 bytes. Contains port numbers and connection info.
- **Payload:** Everything after the first 40 bytes. This is the real content — where the flag fragments were hidden.

> **Rule of thumb:** Skip the first 40 bytes → the rest is payload.

---

## 5. Reading a Hex Dump

When you click a packet in Wireshark, the bottom-right panel shows a **hex dump** — the raw bytes of the packet expressed as hexadecimal numbers.

```
0000  45 00 00 30 00 01 00 00  40 06 f8 72 c0 a8 00 02
0010  c0 a8 01 02 00 14 00 50  00 00 00 00 00 00 00 00
0020  50 02 20 00 73 c6 00 00  68 57 69 55 76 71 51 3d
```

### How to read it:

- **Left column** (`0000`, `0010`, `0020`): The byte offset (position) of the first byte on that line, in hexadecimal.
  - `0000` = starts at byte 0
  - `0010` = hex 10 = decimal **16**, so starts at byte 16
  - `0020` = hex 20 = decimal **32**, so starts at byte 32
- **Each line has exactly 16 bytes.**

### Counting the bytes:

```
0000  45 00 00 30 00 01 00 00  40 06 f8 72 c0 a8 00 02
       1  2  3  4  5  6  7  8   9 10 11 12 13 14 15 16   ← IP Header starts

0010  c0 a8 01 02 00 14 00 50  00 00 00 00 00 00 00 00
      17 18 19 20 21 22 23 24  25 26 27 28 29 30 31 32
      ↑IP Header ends↑ ↑TCP Header starts↑

0020  50 02 20 00 73 c6 00 00  68 57 69 55 76 71 51 3d
      33 34 35 36 37 38 39 40  41 42 43 44 45 46 47 48
                               ↑ Payload starts here! ↑
```

So bytes 41–48 (`68 57 69 55 76 71 51 3d`) are the payload.

### Converting hex to ASCII:

Each hex value maps to a character:
```
68 = h
57 = W
69 = i
55 = U
76 = v
71 = q
51 = Q
3d = =
```
→ **`hWiUvqQ=`**

This looks like Base64. One packet = one Base64 fragment.

> **Tip:** In Wireshark, you don't need to do this manually. Expand "Transmission Control Protocol" in the bottom-left panel and click **"TCP payload"** — the payload bytes will be highlighted automatically in the hex dump.

---

## 6. Solution Walkthrough

### Step 1: Open the PCAP file

```bash
# In terminal (CLI):
tshark -r myNetworkTraffic.pcap
```

Or open directly in Wireshark (GUI).

### Step 2: Observe the packets

- Only **2 IP addresses** appear: `192.168.0.2` (attacker) and `192.168.1.2` (victim server)
- All **22 packets** are sent from port 20 → port 80
- No HTTP traffic — this is **raw TCP**
- Each packet carries a short payload that looks like Base64

### Step 3: Recognize the pattern

The hint said "Time is essential."  
All 22 packets were sent at almost the **same second**, but with different **microsecond** timestamps.  
The attacker deliberately scrambled the packet order — so sorting by timestamp (microseconds) reveals the correct sequence.

### Step 4: Extract and sort payloads by timestamp

```python
import struct, base64

with open('myNetworkTraffic.pcap', 'rb') as f:
    f.read(24)  # Skip global header
    packets = []
    while True:
        ph = f.read(16)
        if len(ph) < 16:
            break
        ts_sec, ts_usec, incl_len, orig_len = struct.unpack('<IIII', ph)
        data = f.read(incl_len)
        packets.append((ts_sec, ts_usec, data))

# Sort by timestamp (microseconds matter!)
packets.sort(key=lambda x: x[0] + x[1]/1e6)

flag = ""
for ts_sec, ts_usec, raw in packets:
    ihl = (raw[0] & 0x0f) * 4          # IP header length
    tcp_data_offset = (raw[ihl + 12] >> 4) * 4  # TCP header length
    payload = raw[ihl + tcp_data_offset:]        # Extract payload
    b64 = payload.decode('ascii', errors='replace')
    decoded = base64.b64decode(b64).decode('latin-1')
    flag += decoded

print(flag)
```

### Step 5: Result

Sorted payloads decoded in order:

| Order | Timestamp (μs) | Base64 | Decoded |
|-------|---------------|--------|---------|
| 1 | 250762 | `hWiUvqQ=` | (noise) |
| ... | ... | ... | ... |
| 16 | 254664 | `cGljb0NURg==` | `picoCTF` |
| 17 | 254895 | `ezF0X3c0cw==` | `{1t_w4s` |
| 18 | 255124 | `bnRfdGg0dA==` | `nt_th4t` |
| 19 | 255446 | `XzM0c3lfdA==` | `_34sy_t` |
| 20 | 255667 | `YmhfNHJfZQ==` | `bh_4r_e` |
| 21 | 255903 | `NWU4Yzc4ZA==` | `5e8c78d` |
| 22 | 256121 | `fQ==` | `}` |

**Flag: `picoCTF{1t_w4snt_th4t_34sy_tbh_4r_e5e8c78d}`**

---

## 7. Lessons Learned

### What this challenge actually tested:
1. **Can you open and navigate a PCAP file?**
2. **Can you identify that the data is in the TCP payload, not HTTP?**
3. **Can you figure out that timestamp ORDER is the key?**

### Core takeaways:

| Concept | What I learned |
|---------|---------------|
| PCAP | A recording of raw network traffic |
| Payload | The actual data inside a packet, after the headers |
| Hex dump | Raw bytes of a packet shown as hexadecimal numbers |
| Base64 | An encoding method that turns binary data into readable text (ends in `=` or `==`) |
| Timestamp | Each packet has a precise time — microsecond order can matter |
| tshark | CLI version of Wireshark, great for automating extraction |

### Key insight for similar challenges:
> When packets arrive at nearly the same time but in scrambled order, always check the **microsecond** part of the timestamp. The correct sequence is hidden there.

### Tools used:
- **Wireshark** — visual packet analysis
- **tshark** — command-line packet extraction
- **Python (struct, base64)** — parse PCAP and decode payloads
- **CyberChef** — quick encoding/decoding in browser

---

*Written after solving Ph4nt0m 1ntrud3r on picoCTF.*
