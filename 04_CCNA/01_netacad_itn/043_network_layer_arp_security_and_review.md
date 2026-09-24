# Networking Fundamentals – Study Notes

> Topics covered: MTU, MAC Address Table, Password Security, ARP, Banner Config, Data Link Layer

---

## 1. MTU (Maximum Transmission Unit) & the Network Layer

**Key Concept:** MTU is the maximum size of data that can be sent in a single network transmission.

**How it works:**
- The **Data Link Layer** (Layer 2) knows the physical limits of the medium (e.g., Ethernet, Wi-Fi)
- The **Data Link Layer passes the MTU value up to the Network Layer** (Layer 3)
- The Network Layer uses this value to **fragment (split)** packets so they fit within the limit

**Analogy:** The Data Link Layer is like a road inspector who tells the Network Layer dispatcher: *"This road only allows vehicles up to X size."* The dispatcher then ensures all packages are sized correctly.

**✅ Correct Answer:** The MTU is passed to the network layer by the data link layer.

---

## 2. How a Switch Builds Its MAC Address Table

**Key Concept:** A switch learns which device is on which port by inspecting **incoming frames**.

**How it works:**
- When a frame arrives, the switch reads the **source Layer 2 (MAC) address** from the frame header
- It records: `Source MAC Address → Port Number`
- This builds the MAC address table over time

**What the switch does NOT use:**
- ❌ Destination MAC address
- ❌ IP addresses (Layer 3) — switches operate at Layer 2

**Analogy:** A receptionist notes down *who came in* and *which door they used* — so later, they know exactly where to route a response.

**✅ Correct Answer:** The source Layer 2 address of incoming frames.

---

## 3. Password Security – Dictionary Attacks

**Key Concept:** Even long passwords based on common phrases are weak due to **dictionary attacks**.

**The Example:** `WhatAreyouwaiting4`
- Looks strong (long, has a number)
- Actually based on the common phrase *"What are you waiting for?"*
- Hackers use automated tools with **wordlists/dictionaries** of common phrases → cracked easily

**What makes a strong password:**
- Truly **random** characters (letters, numbers, symbols)
- Not based on any dictionary word, common phrase, or quote
- Alternatively: a very long, unique passphrase that doesn't appear anywhere

**✅ Correct Answer:** It is weak since it is a word/phrase easily found in the dictionary.

---

## 4. ARP (Address Resolution Protocol) – Type Field 0x806

**Key Concept:** The NIC identifies ARP packets using the **Type field** in the Ethernet frame header.

**How it works:**
- Every Ethernet frame has a `Type` field in its header
- The value `0x806` is the **reserved identifier for ARP**
- When the NIC reads `0x806`, it routes the frame's data to the **ARP process**

**Why not the broadcast MAC (FF-FF-FF-FF-FF-FF)?**
- `FF:FF:FF:FF:FF:FF` explains *why all devices receive* the ARP request (broadcast)
- But the **Type field** is what tells each NIC *what to do with it* (pass it to ARP)

**Analogy:** The Type field is like a category label on mail — `0x806` means *"Hand this to the ARP department."*

**✅ Correct Answer:** The type field `0x806` appears in the header of the Ethernet frame.

---

## 5. Verifying a Banner Message on Cisco Devices

**Key Concept:** Banner messages (MOTD) appear **before login**, so you must log out to test them.

**How it works:**
- The banner is displayed at the start of a new connection/login attempt
- While already logged in, you **cannot** see the banner
- To verify: **exit privileged EXEC mode** → press `Enter` → triggers a new login screen → banner appears

**Why not reboot?**
- Rebooting (Options 1 & 4) would work but takes too long — not the *fastest* method
- Exiting config mode (Option 3) only drops you back to the prompt, doesn't log you out

**✅ Correct Answer:** Exit privileged EXEC mode and press Enter.

---

## 6. Data Link Layer (OSI Layer 2) – Two Key Services

**Key Concept:** The Data Link Layer has two primary responsibilities.

### ✅ Service 1: Encapsulation
- Takes **Layer 3 packets** from the Network Layer
- Wraps them into **frames** for physical transmission
- Analogy: Putting a letter (packet) into an envelope (frame) with addressing info

### ✅ Service 2: Media Access Control (MAC) + Error Detection
- **MAC:** Manages *who sends data and when* to prevent collisions on shared media
- **Error Detection:** Checks if data was corrupted during transmission (e.g., using CRC)

**What Layer 2 does NOT do:**
| Task | Actual Layer |
|------|-------------|
| Fragment packets by MTU | Layer 3 – Network Layer |
| Determine routing path | Layer 3 – Network Layer |
| Build MAC address table | Switch function (device-specific, not a general Layer 2 service) |

**✅ Correct Answers:** Encapsulation of Layer 3 packets into frames + Media Access Control & Error Detection.

---

## Quick Reference Summary

| Topic | Key Point |
|-------|-----------|
| MTU | Passed from Data Link Layer → Network Layer |
| MAC Table | Built from **source** MAC of **incoming** frames |
| Password Security | Common phrases = weak (dictionary attack risk) |
| ARP Identification | Type field `0x806` in Ethernet header |
| Banner Verification | Exit privileged EXEC mode + press Enter |
| Data Link Layer | Encapsulation + MAC control & error detection |

---

*Study notes based on Cisco Networking Academy / CCNA fundamentals.*
