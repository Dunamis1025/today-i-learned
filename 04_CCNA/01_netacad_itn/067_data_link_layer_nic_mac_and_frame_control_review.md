# Data Link Layer — Study Notes

---

## 1. NIC Frame Checks (Q8)

When a NIC receives a frame, it performs two checks before passing data up to the data link layer:

| Check | Description |
|---|---|
| **Frame Check Sequence (FCS)** | The NIC runs a CRC calculation on the incoming frame and compares it to the FCS field value. If they don't match → frame is **discarded** (data corruption detected). |
| **Minimum Frame Size** | Ethernet requires frames to be at least **64 bytes**. Frames smaller than this are called **"runt" frames** — treated as damaged or incomplete → **discarded**. |

---

## 2. Data Link Layer Frame Header Fields (Q9)

**Key characteristic:** Frame header fields **vary depending on the protocol** being used.

- Ethernet (wired) and Wi-Fi 802.11 (wireless) have completely different frame structures.
- Each protocol defines its own header fields based on what information it needs to transmit data correctly.

**Why the other options are wrong:**

| Wrong Option | Reason |
|---|---|
| Frame headers contain Layer 3 addresses | IP addresses belong to the **packet header** (Layer 3), not the frame header (Layer 2). |
| Frame headers include user application info | Application data sits inside the **data payload**, not the header. |
| All protocols include flow control and logical connection fields | Not true — standard **Ethernet does not** include these fields. |

---

## 3. Media Arbitration & Full-Duplex (Q10)

**Arbitration** = the process of managing and resolving conflicts over who gets to use a shared communication medium and when.

| Mode | Arbitration Needed? | Why |
|---|---|---|
| **Full-duplex** | ❌ No | Sending and receiving use **physically separate paths** → collisions are impossible. |
| **Half-duplex** | ✅ Yes | Devices share the same path for both directions → collisions can occur → arbitration required. |

> Full-duplex eliminates the need for arbitration because the transmit and receive signals never interfere with each other.

---

## 4. Services Provided by the Data Link Layer (Q11)

**Two correct services:**

1. **Packages various Layer 3 PDUs into a frame format** compatible with the network interface.
   - Takes data coming down from the Network Layer and wraps it into a frame the physical hardware can understand.

2. **Manages the access of frames to the network media.**
   - Acts as a traffic controller — determines when and how devices are allowed to place frames onto the physical medium to prevent collisions.

**Why the other options are wrong:**

| Wrong Option | Reason |
|---|---|
| Provides reliable delivery | Reliable delivery is handled by **Layer 4 (Transport Layer)**, not Layer 2. |
| Defines end-to-end addressing | End-to-end addressing (e.g., IP) is a **Layer 3 (Network Layer)** function. |
| Ensures data priority by application | Traffic prioritization is managed by **upper-layer protocols or QoS mechanisms**. |
| Maintains path between source and destination | Path determination is a **Layer 3** function. |

---

## 5. Media Access Control (MAC) Methods (Q12)

**Three correct statements about MAC:**

1. **Ethernet utilizes CSMA/CD** — In older Ethernet (hub-based), devices use Carrier Sense Multiple Access with Collision Detection to detect and recover from collisions.

2. **MAC provides placement of data frames onto the media** — The MAC sublayer controls how frames are placed onto the physical transmission medium.

3. **Data link layer protocols define the rules for access to different media** — Different physical media (copper, fiber, wireless) require different access rules; the data link layer defines them.

**Why the other options are wrong:**

| Wrong Option | Reason |
|---|---|
| 802.11 uses CSMA/CD | Wireless (802.11) uses **CSMA/CA** (Collision *Avoidance*) — detecting collisions while transmitting is not feasible wirelessly. |
| Controlled access reduces performance due to collisions | Controlled access (e.g., Token Passing) **prevents collisions entirely** by ensuring only one device transmits at a time — it is actually efficient. |
| Contention-based access is deterministic | **False.** Contention-based access is **non-deterministic** — there is no guarantee when a device gets to transmit. *Deterministic* describes controlled access methods where transmission is strictly scheduled. |

---

## Key Vocabulary

| Term | Definition |
|---|---|
| **FCS (Frame Check Sequence)** | A field used to detect errors in a received frame via CRC calculation. |
| **Runt frame** | A frame smaller than the minimum required size (64 bytes); treated as damaged and discarded. |
| **Validity** | Whether a frame meets the correct format and rules required by the protocol. |
| **Arbitration** | The mechanism that controls which device gets to use a shared medium and when. |
| **Deterministic** | A system where transmission timing is fixed and predictable in advance. |
| **Non-deterministic** | A system where there is no guarantee of when a device will get to transmit. |
| **Full-duplex** | Simultaneous two-way communication using separate paths for send and receive. |
| **Half-duplex** | Two-way communication, but only one direction at a time on a shared path. |
| **CSMA/CD** | Collision Detection — used in wired Ethernet; detects collisions after they occur. |
| **CSMA/CA** | Collision Avoidance — used in Wi-Fi (802.11); tries to avoid collisions before they occur. |
| **MAC (Media Access Control)** | Sublayer of the data link layer that controls how devices access the shared medium. |
| **PDU (Protocol Data Unit)** | The unit of data at a given layer (Layer 2 PDU = Frame, Layer 3 PDU = Packet). |
