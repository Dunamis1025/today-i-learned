# Networking Concepts — Study Notes

> Key summaries from practice questions. Focused on CompTIA / CCNA fundamentals.

---

## 1. IPv6 — No Broadcast

**Topic:** IPv6 address types

**Key Point:**
IPv6 does **not** support Broadcast.

| Feature | IPv4 | IPv6 |
|---|---|---|
| Broadcast | ✅ Supported | ❌ Removed |
| Multicast | ✅ Supported | ✅ Preferred |

**Why removed?**
In IPv4, broadcast sends data to **every device** on the network simultaneously — like blasting a megaphone to an entire town. This creates unnecessary traffic and network load.

IPv6 replaces broadcast with **Multicast**, which sends data only to specific groups of devices that actually need it — far more efficient.

> 💡 **Remember:** IPv6 = Unicast, Multicast, Anycast. No Broadcast.

---

## 2. Intranet vs. Internet vs. Extranet

**Topic:** Network types

**Scenario:** A branch office employee needs to access confidential pricing data from the HQ's internal server.
**Answer:** **Intranet**

| Network Type | Who Can Access | Use Case |
|---|---|---|
| **Internet** | Everyone (public) | General web browsing |
| **Intranet** | Internal employees only | Private company data, internal systems |
| **Extranet** | Specific external partners | Limited external partner access |
| **LAN** | Devices in a local physical area | Physical local network infrastructure |

**Key Point:**
An **intranet** is a private, company-internal network — essentially a "company-only internet." It keeps sensitive data (confidential documents, internal databases) secure from the outside world.

> 💡 **Remember:** If it's employees-only and confidential → **Intranet**.

---

## 3. Extended Ping on a Router

**Topic:** Network troubleshooting tools

**Scenario:** H3 can't reach H1. The admin wants to prove that Router R2's configuration is fine, by testing connectivity from the specific interface H3 uses.
**Answer:** **Extended Ping**

**What is a standard ping?**
Sends a signal ("Are you there?") from the router's **default** address to test basic connectivity.

**What is an extended ping?**
Allows you to manually specify the **source interface/address** — so you can simulate a packet originating from exactly the interface H3 uses.

If the extended ping from R2's specific interface reaches H1 successfully → R2's config is fine → problem is with H3.

| Tool | Purpose |
|---|---|
| **Ping** | Basic end-to-end connectivity test |
| **Extended Ping** | Connectivity test from a specific source interface |
| **Traceroute** | Maps the full path (hops) to the destination |
| **show cdp neighbors** | Shows directly connected neighboring devices only |
| **Telnet** | Remote management/login — not a test tool |

> 💡 **Remember:** Need to test from a *specific interface*? Use **extended ping**.

---

## 4. Presentation Layer (OSI Model)

**Topic:** OSI / TCP/IP model layers

**Question:** Which layer handles formatting, compressing, and encrypting data?
**Answer:** **Presentation Layer (Layer 6)**

**Three core functions:**

| Function | Description |
|---|---|
| **Formatting** | Converts data into a standard format both sender and receiver can read |
| **Compression** | Reduces data size for faster transmission |
| **Encryption** | Scrambles data to keep it secure during transit |

> ⚠️ **Note:** The TCP/IP model technically has 4 layers. The Presentation Layer is an OSI 7-layer concept, but educational materials often reference OSI layers when explaining these specific functions.

> 💡 **Remember:** **Presentation = Format + Compress + Encrypt** (think: "presenting" data in the right form).

---

## 5. Frame Encoding

**Topic:** Data Link Layer — Physical transmission

**Question:** Which statement correctly describes frame encoding?
**Answer:** It converts bits into a predefined code to provide a predictable pattern, helping distinguish **data bits** from **control bits**.

**Why is frame encoding needed?**
When data is sent as raw 0s and 1s, the receiver has no way to know where actual data ends and control signals (start/stop markers) begin. Frame encoding adds a structured pattern so the receiver can correctly interpret the bitstream.

| Term | Description |
|---|---|
| **Frame Encoding** | Converts bits into a pattern to separate data from control signals |
| **Modulation** | Uses one wave to modify another (e.g., radio signals) |
| **Synchronization** | Transmits data with a clock signal to align timing |
| **Signaling** | Converts binary digits into actual electrical/optical/wireless signals |

> 💡 **Remember:** Signaling = *creates* the physical signal. Encoding = *organizes* it into a recognizable structure.

---

## 6. MTU — Maximum Transmission Unit

**Topic:** Network Layer / Data Link Layer interaction

**Question:** How does the Network Layer use the MTU value?
**Answer:** The **Data Link Layer passes the MTU to the Network Layer**.

**What is MTU?**
"Maximum Transmission Unit" — the maximum size of a single data packet that can be sent across a network. Think of it as a shipping company's maximum parcel weight limit.

**How it works:**
1. The **Data Link Layer** knows the physical limits of the medium (Ethernet, Wi-Fi, etc.) and determines the MTU.
2. It **passes the MTU value up** to the Network Layer.
3. The **Network Layer** uses this value to decide whether to **fragment** (split) the data into smaller pieces before sending.

```
Data Link Layer  →  sets MTU  →  passes to Network Layer
Network Layer    →  receives MTU  →  fragments data if needed
```

> 💡 **Remember:** Data Link Layer sets the limit. Network Layer respects it (and splits data if necessary).

---

## Quick Reference Summary

| # | Topic | Key Answer |
|---|---|---|
| 1 | IPv6 missing feature | **Broadcast** (replaced by Multicast) |
| 2 | Employees-only company network | **Intranet** |
| 3 | Test from a specific router interface | **Extended Ping** |
| 4 | Formats, compresses, encrypts data | **Presentation Layer** |
| 5 | Organizes bits into data vs. control patterns | **Frame Encoding** |
| 6 | Who tells the Network Layer the MTU? | **Data Link Layer** |
