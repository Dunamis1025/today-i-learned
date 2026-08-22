# TCP/UDP Congestion, Sockets, and Module Quiz Review

## 1. TCP Reliability Recap: Sequence Numbers, ACKs, and Retransmission

TCP is a reliable, connection-oriented protocol that uses **sequence numbers** and **acknowledgements (ACKs)** to guarantee delivery.

- The source sends a segment and starts a **timer**.
- The destination, upon receiving a segment, sends back an ACK requesting the *next* expected segment (e.g., after receiving segment 1, it sends ACK 2).
- If the timer expires before an ACK arrives, the source assumes the segment was lost and **retransmits only that segment** (not the entire message), then restarts the timer.
- This retransmit-on-timeout mechanism is what allows TCP to reliably reconstruct an entire file/image/video even when individual segments are lost in transit.

## 2. TCP Flow Control — Congestion Avoidance

- **Congestion** occurs when an overloaded router discards packets. When TCP segments never arrive, the destination never sends an ACK for them.
- The **source** detects the lack of expected ACKs and infers that the network is congested.
- Blind retransmission during congestion is dangerous: it adds retransmitted segments on top of new traffic, creating a feedback loop that makes congestion worse (a "spiral").
- **TCP's response:** the *source* voluntarily reduces the amount of unacknowledged data it sends before waiting for an ACK. This is a self-throttling decision made by the sender based on observed ACK behavior — **not** an explicit command from the destination.
- **Key distinction:**
  - *Flow Control* → uses **Window Size**, and the **window size itself is determined by the destination** (based on its buffer capacity).
  - *Congestion Avoidance* → the **source** reduces the number of bytes it sends before receiving an ACK. This is a separate mechanism from the destination-controlled window size.
- Detailed congestion algorithms/timers (e.g., slow start) are beyond the scope of this course.

## 3. UDP Overview

### 3.1 Low Overhead vs. Reliability
- UDP is **connectionless** — no handshake before sending data.
- Small datagram header → very little overhead/management traffic.
- Ideal for applications where **speed matters more than perfect reliability** (e.g., VoIP). A brief pause to resend a lost packet would harm real-time communication more than the lost data itself.

### 3.2 UDP Datagram Reassembly
- Like TCP, UDP datagrams may take different paths and arrive out of order.
- **UDP does not track sequence numbers**, so it has no mechanism to reorder datagrams.
- UDP simply reassembles data **in the order received** and forwards it to the application — it does **not** reorder to match the original transmission order.
- **Lost datagrams are never resent** by UDP.
- If order matters to the application, the **application itself** must handle detecting/reordering sequence.

### 3.3 UDP Server Processes
- UDP server applications use well-known/registered port numbers (e.g., DNS = port 53, RADIUS = port 1812).
- UDP forwards each datagram to the correct application based on the **destination port number** in the datagram header.
- Multiple services can run on one server simultaneously, distinguished only by port.

### 3.4 UDP Client Processes
- The client **dynamically/randomly selects a source port** (e.g., 49152, 51152) for the conversation.
- The destination port is the server's well-known/registered port.
- The same port pair is used throughout the transaction.
- **When the server responds, source and destination ports are reversed**:
  - Request: Source = client's random port, Destination = server's well-known port
  - Response: Source = server's well-known port, Destination = client's original source port

## 4. Sockets and Port Ranges

- A **socket** = combination of an **IP address + port number** (e.g., `192.168.1.1:80`). It uniquely identifies one endpoint of a conversation (source socket and destination socket exist per connection).
- **Well-known ports**: range **0–1023** (e.g., HTTP=80, DNS=53, FTP=21).
- **Registered ports**: 1024–49151 (e.g., RADIUS=1812).
- **Dynamic/private ports**: 49152–65535 (used by clients as random source ports).
- Port numbers (not IP addresses alone) are what let a server distinguish *which service* a request is for, and let it track multiple simultaneous conversations from multiple clients.

## 5. TCP vs. UDP — Key Feature Comparison

| Feature | TCP | UDP |
|---|---|---|
| Connection setup | Yes (3-way handshake) | No |
| Reorders segments to original order | Yes | No (reassembles in order *received* only) |
| Resends lost data | Yes | No |
| Uses ACKs | Yes | No |
| Overhead | High | Low |
| Typical uses | HTTP, FTP, Email (SMTP/POP3) | DNS, DHCP, SNMP, TFTP, VoIP, video streaming |

**Important nuance:** Both TCP and UDP identify individual conversations/applications (via ports) and both reassemble data in the order it was received. What only TCP does: **acknowledging received data** and **retransmitting unacknowledged data**.

## 6. TCP Three-Way Handshake (confirmed via Packet Tracer lab)

| Step | Direction | Src Port | Dst Port | Seq | Ack | Flags |
|---|---|---|---|---|---|---|
| 1 | Client → Server | 1027 | 80 | 0 | 0 | **SYN** |
| 2 | Server → Client | 80 | 1027 | 0 | 1 | **SYN, ACK** |
| 3 | Client → Server | 1027 | 80 | 1 | 1 | **ACK** |

- Only **SYN** and **ACK** flags are used across the handshake to establish connectivity.
- After the handshake, the same port pair is reused for the actual HTTP request/response (visible as a differently-colored PDU layered on top of the TCP control PDUs in Packet Tracer).
- In the simulation, inbound/outbound source and destination ports are always mirror images of each other (e.g., outbound Src 1027/Dst 80 ↔ inbound Src 80/Dst 1027).

## 7. Packet Tracer Lab: "TCP and UDP Communications" — Key Takeaways

**Part 1 (traffic generation + multiplexing):**
- Generated HTTP, FTP, DNS, and Email traffic from separate clients simultaneously.
- Observed PDUs of different colors crossing the same switch — this is called **multiplexing**: multiple independent conversations sharing one physical link, one PDU per direction at a time.
- Different colors in the Event List = different protocols.

**Part 2 (protocol inspection):**
- Filtered Event List to isolate HTTP/TCP traffic, then FTP/TCP, then DNS/UDP.
- Confirmed TCP segments carry Source Port, Destination Port, Sequence Number, Acknowledgement Number, and Flags — DNS (UDP) segments do **not** carry sequence/ack numbers at all.
- HTTP took time to appear because the 3-way handshake must complete before actual HTTP data can be exchanged.

## 8. Module Quiz Review (Transport Layer) — Answer Key & Reasoning

| # | Question (summarized) | Correct Answer | Why |
|---|---|---|---|
| 1 | Field used to reassemble segments into original order | **Sequence Number** | Tracks order and detects missing segments |
| 2 | Field used for flow control | **Window Size** | Controls how much data can be sent before an ACK |
| 3 | What happens when sender senses congestion | **Sending host reduces bytes sent before ACK** | Source self-throttles, not the destination |
| 1 (retake) | Connection-oriented session establishment mechanism | **TCP 3-way handshake** | SYN → SYN-ACK → ACK sets up the session |
| 2 | Complete range of well-known ports | **0–1023** | Standard reserved range |
| 3 | Definition of a socket | **Source or destination IP + port number combo** | e.g., `192.168.1.1:80` |
| 4 | How a server manages multiple client requests | **Each request = unique IP + port combo** | Enables distinguishing simultaneous requests |
| 5 | What happens if part of an FTP message is lost | **Only the lost part is re-sent** | FTP uses TCP, which retransmits selectively |
| 6 | Best-suited apps for UDP | **Applications sensitive to delay** | Speed prioritized over reliability (careful: "sensitive to packet loss" implies needing TCP, not UDP) |
| 7 | TCP's congestion response | **Source decreases data sent before receiving ACK** | Source-side self-throttling, distinct from destination-set window size |
| 8 | Two operations TCP does but UDP doesn't (multi-select) | **Retransmitting unacknowledged data** + **Acknowledging received data** | Both TCP and UDP identify conversations/apps and reassemble in received order — only TCP does ACK + retransmission |
| 9 | Purpose of source port number | **Track multiple conversations between devices** | Allows distinguishing simultaneous sessions |
| 10 | Two flags used in 3-way handshake (multi-select) | **SYN** + **ACK** | RST/URG/FIN/PSH are unrelated to connection establishment |
| 11 | Mechanism allowing continuous segment streaming while receiving ACKs | **Sliding window** | Enables throughput without waiting for each individual ACK |
| 12 | Client action when using UDP | **Client randomly selects a source port number** | UDP has no handshake, ISN, or window size (those are TCP-only) |
| 13 | Two protocols that prefer UDP for speed/low overhead (multi-select) | **VoIP** + **DNS** | FTP and HTTP/POP3 use TCP for reliability |
| 14 | Which value represents a socket | **192.168.1.1:80** | IP + port combo; MAC address, port-only, or IP-only don't qualify |
| 15 | A responsibility of transport layer protocols | **Tracking individual conversations** | NAT/routing = network layer; network access = physical/data link layer |

## 9. Common Pitfalls Identified This Session

- Confusing **"sensitive to packet loss"** (needs reliability → TCP) with **"sensitive to delay"** (needs speed → UDP).
- Assuming UDP "does not reassemble data at all" — it does reassemble, just **without reordering** to the original sequence.
- Assuming FTP uses UDP because it's a simple request — FTP actually requires **TCP** for reliable file transfer.
- Confusing **Flow Control (Window Size, destination-controlled)** with **Congestion Avoidance (source reduces bytes sent, source-controlled)**.
- Mixing up transport layer responsibilities (tracking conversations) with network layer (routing, NAT) or physical/data link layer (network access) responsibilities.

---
*Compiled from Cisco NetAcad CCNA course material (TCP/UDP Communications module), Packet Tracer lab activity ("14.8.1 Packet Tracer - TCP and UDP Communications"), and the accompanying Module Quiz — Transport Layer.*
