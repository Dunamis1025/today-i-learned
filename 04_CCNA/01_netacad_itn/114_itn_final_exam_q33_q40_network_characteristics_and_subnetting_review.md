# 114. ITN Final Exam Review: Q33–Q40

**Course:** CCNA: Introduction to Networks (ITN) – Final Exam practice (60 questions)
**Scope of this note:** Questions 33–40
**Progress:** 40 of 60 completed

## Results at a Glance

| Q | Topic | Result | Key Takeaway |
|---|---|---|---|
| 33 | Benefit of cloud computing | Correct | Cloud extends capabilities without new infrastructure, personnel, or software |
| 34 | Network characteristics in a scenario | Wrong | Match each sentence to a characteristic: security, QoS, fault tolerance |
| 35 | Traffic types that use RTP | Correct | RTP = real-time traffic: voice and video |
| 36 | Protocol analyzer best practices | Wrong | Capture at peak times and on different network segments |
| 37 | Bad UTP termination | Correct | Untwisted length is too long |
| 38 | Networking model for a shared printer | Wrong | Peer-to-peer (P2P), not point-to-point |
| 39 | Subnet mask for 40 devices | Correct | /26 = 255.255.255.192 |
| 40 | Fifth subnet of a /29 network | Wrong | Count from subnet zero: (N − 1) × 8 |

---

## Q33. Benefit of Cloud Computing in Networking

**Correct answer:** Network capabilities are extended without requiring investment in new infrastructure, personnel, or software.

**Key concept:** Cloud computing is a rental service. Instead of buying servers, hiring IT staff, and installing software, a company rents these from a cloud provider. This saves money and time, and the company can scale up right away.

**Analogy:** Instead of building your own power plant at home, you buy electricity from a power company.

**Why the other options are incorrect (each one describes a different concept):**

| Description | Concept |
|---|---|
| End users use personal tools to access a business network | **BYOD** (Bring Your Own Device) |
| Everyday appliances connect to other devices and become "smart" | **IoT** (Internet of Things) |
| Existing electrical wiring is used to connect devices to the network | **Powerline networking** |

**Study tip:** Memorize each term together with its description. Questions like this pair a concept with its definition.

**Vocabulary:** *integrated* = built into something (e.g., "technology is integrated into everyday appliances").

---

## Q34. Network Characteristics in a Scenario

**Scenario:** An employee logs in remotely with a username and password. During an important video conference, the connection to the company ISP fails. The secondary connection activates within seconds, and nobody notices.

**Correct answers (choose three):** security, quality of service, fault tolerance

**Finding clues in the scenario:**

| Clue in the scenario | Characteristic |
|---|---|
| "appropriate username and password" | **Security** (authentication is a key element) |
| "important for the video quality to be excellent" | **Quality of service (QoS)** |
| "the connection to the company ISP failed. The secondary connection, however, activated within seconds" | **Fault tolerance** |

**Why the other options are incorrect:**

- **Integrity:** The scenario does not mention data being kept unchanged during transmission.
- **Powerline networking:** This is a technology, not a network characteristic. It appeared as an option in Q33.
- **Scalability:** The scenario does not mention the network growing.

### The Four Fundamental Network Characteristics (Cisco)

| Characteristic | Meaning |
|---|---|
| **Fault tolerance** | The network keeps working when a component fails, thanks to backup paths or connections |
| **Scalability** | The network can grow (more users and devices) without a drop in performance |
| **Quality of Service (QoS)** | Time-sensitive traffic, such as voice and video, gets priority |
| **Security** | The network and its data are protected from unauthorized access and threats |

**Study tip:** Match each sentence in the scenario to one characteristic, one by one.

---

## Q35. Traffic Types That Use RTP

**Correct answers (choose two):** voice, video

**Key concept:** RTP (Real-Time Transport Protocol) is, as the name suggests, a protocol for transmitting data in real time. It is used for traffic that must be delivered immediately without delay.

**Why the other options are incorrect:**

| Option | Reason |
|---|---|
| Web | Uses HTTP/HTTPS. A slightly late page load is not a big problem |
| Peer to peer | Users exchange files with each other. Real-time delivery is not necessary |
| File transfer | Uses protocols such as FTP. Arriving intact matters more than arriving fast |

**Analogy:**

- **Phone call (real time):** a 0.5-second delay on every sentence makes the conversation uncomfortable, so speed matters. → RTP
- **File download (not real time):** a slight delay is fine, but a corrupted file is not, so accuracy matters. → FTP

**Connection to Q34:** Real-time traffic is sensitive to delay, so QoS gives it higher priority.

---

## Q36. Assessing Traffic Patterns with a Protocol Analyzer

**Correct answers (choose two):**

1. Capture traffic during peak utilization times to get a good representation of the different traffic types.
2. Perform the capture on different network segments.

**Key concept:** A protocol analyzer (for example, **Wireshark**) captures network traffic and shows which types of traffic are flowing and how much of each. The goal is to understand how the network is actually being used.

**Why these two are correct:**

- **Peak utilization times:** You can see a wide variety of traffic types, and observe both normal and high-load conditions.
- **Different network segments:** Traffic characteristics differ by department and section. Checking only one part misses the whole picture.

**Why the other options are incorrect:**

| Option | Reason |
|---|---|
| Capture on the weekends | Most employees are off, so traffic is low and does not represent normal usage |
| Only the data center | Traffic in other segments is missed |
| Only WAN traffic | There is also a lot of LAN traffic, so the WAN alone is not the whole picture |

**Exam tip:** If an answer option contains the word **"only"**, be suspicious. It often narrows the scope too much.

---

## Q37. Bad UTP Cable Termination

**Exhibit:** An RJ-45 connector with the wires untwisted for a long distance from the cable jacket to the connector.

**Correct answer:** The untwisted length of each wire is too long.

**Key concept:**

- A UTP cable contains **eight copper wires** twisted together in **pairs** (twisted pair).
- Twisting reduces **EMI** and **crosstalk**.
- When terminating, keep the untwisted section as short as possible (**at most about 1.3 cm / 0.5 inch**). If you untwist too much, the protection is lost, signal quality drops, and crosstalk increases.

**Why the other options are incorrect:**

| Option | Reason |
|---|---|
| Wires are too thick for the connector | The wire thickness is fine |
| Wrong type of connector | RJ-45 is correct for UTP |
| Woven copper braid should not have been removed | Braid exists only in **STP** cables; this cable is UTP |

### Crosstalk vs. EMI

| Term | Source | Example |
|---|---|---|
| **Crosstalk** (누화) | Interference from **inside** the cable, from a neighboring wire | The signal on one wire leaks into another |
| **EMI** | Interference from **outside** the cable | Motors, fluorescent lights |

**How crosstalk happens:** A signal traveling through a copper wire creates a weak electromagnetic field around it. When wires are close together, this field affects the neighboring wire and creates noise.

**Results:** corrupted data → more retransmissions → slower speed → unstable connection in severe cases.

**How twisting helps:** The electromagnetic fields of the two wires in a pair **cancel each other out**.

**Analogy:** Thin apartment walls let you hear your neighbor's TV.

---

## Q38. Networking Model for a Shared Printer

**Scenario:** A wired laser printer is attached to a home computer and shared so that other computers on the home network can use it.

**Correct answer:** peer-to-peer (P2P)

**Key concept:** In a peer-to-peer model, computers share resources with each other **without a dedicated server**. "Peer" means an equal partner. Every computer can act as both a client and a server.

**Why the other options are incorrect:**

| Option | Meaning |
|---|---|
| **Point-to-point** | A direct one-to-one link between two devices (a *connection type*, e.g., two routers joined by one cable) |
| **Master-slave** | One device (master) controls another (slave). No control relationship exists here |
| **Client-based** | Not a standard networking term |

### Comparison Table

| Term | Key Point | Category |
|---|---|---|
| Point-to-point | Direct 1:1 connection between two devices | Connection type |
| Peer-to-peer | Equal computers sharing resources | Network model |
| Client-server | A server provides resources; clients request them | Network model |

**Lesson learned:** Similar-sounding terms (point-to-point vs. peer-to-peer) belong to different categories. Ask, "Is this a connection type or a network model?"

---

## Q39. Subnet Mask for 40 Devices

**Question:** What subnet mask is needed if an IPv4 network has 40 devices and address space is not to be wasted?

**Correct answer:** 255.255.255.192 (/26)

**Key concept:** Choose the **smallest** subnet that can still hold all the devices.

**Formula:** Usable host addresses = 2ⁿ − 2, where n is the number of host bits. We subtract 2 because the network address and the broadcast address cannot be assigned to devices.

| Subnet mask | Prefix | Host bits | Usable addresses | Enough for 40? |
|---|---|---|---|---|
| 255.255.255.0 | /24 | 8 | 254 | Yes, but wastes the most |
| 255.255.255.128 | /25 | 7 | 126 | Yes, but wastes too many |
| **255.255.255.192** | **/26** | **6** | **62** | **Yes, wastes the fewest** |
| 255.255.255.224 | /27 | 5 | 30 | No |
| 255.255.255.240 | /28 | 4 | 14 | No |

**Steps to solve:**

1. Check the number of devices (40).
2. Find the smallest n where 2ⁿ − 2 ≥ 40, so n = 6.
3. Prefix = 32 − 6 = /26.
4. /26 = 255.255.255.192.

**Memorizing mask values (last octet):** Each value turns on one more bit from the left.

- 128
- 128 + 64 = 192
- 128 + 64 + 32 = 224
- 128 + 64 + 32 + 16 = 240
- 128 + 64 + 32 + 16 + 8 = 248

---

## Q40. Fifth Subnet of a /29 Network

**Scenario:** The LAN of LBMISS uses 192.168.10.0, subnetted with a **/29** prefix. The technician uses the **fifth subnet** for a new building (**subnet zero is the first subnet**). By company policy, the router interface gets the **first usable host address** and the workgroup server gets the **last usable host address**.

**Correct answer:**

- **IP address:** 192.168.10.38
- **Subnet mask:** 255.255.255.248
- **Default gateway:** 192.168.10.33

**Step-by-step solution:**

1. **/29 mask:** /29 = 255.255.255.**248** (3 host bits).
2. **Block size:** 2³ = 8 addresses per subnet, so 8 − 2 = 6 usable hosts.
3. **List the subnets** (subnet zero is the first):

| Order | Subnet | Range |
|---|---|---|
| 1st (subnet 0) | 192.168.10.0 | .0 – .7 |
| 2nd | 192.168.10.8 | .8 – .15 |
| 3rd | 192.168.10.16 | .16 – .23 |
| 4th | 192.168.10.24 | .24 – .31 |
| **5th** | **192.168.10.32** | **.32 – .39** |
| 6th | 192.168.10.40 | .40 – .47 |

4. **Fifth subnet = 192.168.10.32**
   - Network address: .32
   - Broadcast address: .39
   - Usable range: **.33 – .38**
5. **Apply the company policy:**
   - Router (first usable) = **.33** → the server's **default gateway**
   - Server (last usable) = **.38** → the server's **IP address**

**Why my answer was wrong:** I chose .41 / .46 (mask 248), which belongs to the **6th** subnet (.40 – .47). I calculated 5 × 8 = 40, but subnet zero is the first subnet, so the fifth subnet starts at 4 × 8 = 32.

**Formula:** Subnet start = **(N − 1) × block size**

**Why the other options are incorrect:**

- **.65 / .76:** Out of range, and the server and gateway are not in the same subnet.
- **Mask 255.255.255.240:** This is /28, not /29.
- **.254 / mask 255.255.255.0:** This is /24, so the network is not subnetted.

**Exam tips:**

1. Check the mask first. /29 = 248 eliminates the wrong masks quickly.
2. Calculate the subnet start: (N − 1) × 8.
3. First usable = start + 1. Last usable = next subnet start − 2.
4. If the question says "subnet zero is the first subnet," subtract 1 from the subnet number.
5. The **default gateway** is the router interface address in the same subnet.

**Key vocabulary:**

| Term | Meaning |
|---|---|
| Refer to the exhibit | Look at the attached diagram |
| subnetted | Divided into subnets |
| to accommodate | To make room for |
| subnet zero | The first subnet (starts at .0) |
| usable host address | An address that can be assigned to a device (excludes network and broadcast addresses) |
| default gateway | The router address a device uses to reach other networks and the Internet |

---

## Summary of Lessons Learned

1. **Scenario questions:** Match each sentence to a concept, one by one.
2. **Similar terms:** Identify the category first (connection type vs. network model; technology vs. characteristic).
3. **"Only" in an option** is often a warning sign.
4. **Subnetting:** Always check whether counting starts at zero, and use (N − 1) × block size.
5. **Real-time traffic (voice, video)** uses RTP and benefits from QoS.
6. **Twisted pairs** cancel electromagnetic fields, so keep the untwisted length short when terminating.

## Expressions to Practice (English Speaking/Writing)

- *as the name suggests*
- *cancel each other out*
- *act as both A and B*
- *be sensitive to ~*
- *It is more important to A than B*
- *end in ~ / at least ~ / at most ~*
- *a wide variety of ~*
- *the first usable host address / the last usable host address*

## Next Steps

- Continue with Q41–Q60 using the same method: solve, understand the concept, explain it in Korean, then explain it in English.
- After the exam review, start SRWE/ENSA self-study (video lectures + Packet Tracer labs).
- Target: pass the CCNA exam in mid-January 2027.
