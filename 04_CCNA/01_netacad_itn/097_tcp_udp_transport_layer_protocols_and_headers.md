# TCP & UDP — CCNA Study Notes

## 1. Overview

TCP and UDP are the two **transport layer protocols** in the TCP/IP suite. Choosing between them depends on whether an application needs **reliability** (TCP) or **speed with minimal overhead** (UDP).

---

## 2. TCP (Transmission Control Protocol)

### 2.1 Key Features
TCP is a **connection-oriented** protocol that provides reliable data delivery through the following mechanisms:

- **Establishing a Session** — Devices negotiate and establish a connection before exchanging traffic. This session establishment negotiates the amount of traffic that can be forwarded at a given time, and the communication between the hosts can be closely managed.
- **Ensuring Reliable Delivery** — If a segment is lost or corrupted in transit, TCP can detect this and retransmit the lost or corrupted data.
- **Providing Same-Order Delivery** — Because segments may arrive out of order, TCP reassembles segments into the proper (original) order at the destination.
- **Supporting Flow Control** — When resources on a host are overwhelmed (limited memory or processing power), TCP requests that the sending device reduce the rate of data flow, preventing the need for retransmission due to overwhelmed resources.

TCP is a **stateful protocol** — it keeps track of the state of the communication session (what has been sent, what has been acknowledged) from establishment to termination.

### 2.2 TCP Header

- Total overhead: **20 bytes** (added when encapsulating application layer data)
- Fields:

| Field | Size (bits) | Description |
|---|---|---|
| Source Port | 16 | Identifies the source application by port number |
| Destination Port | 16 | Identifies the destination application by port number |
| Sequence Number | 32 | Used for data reassembly purposes |
| Acknowledgment Number | 32 | Indicates the next byte of data expected from the source; confirms data received |
| Header Length ("Data Offset") | 4 | Indicates the length of the TCP segment header |
| Reserved | 6 | Reserved for future use |
| Control Bits (Flags) | 6 | Indicate the purpose and function of the TCP segment |
| Window | 16 | Indicates the number of bytes that can be accepted at one time (flow control) |
| Checksum | 16 | Used for error checking the segment header and data |
| Urgent | 16 | Indicates if the contained data is urgent |

### 2.3 Applications That Use TCP
Used when **reliability is more important than speed** (data integrity cannot be sacrificed):

- **FTP** (File Transfer Protocol)
- **HTTP** (Web)
- **SMTP** (Email)
- **SSH** (Remote access)

TCP sits between these applications and the **IP layer** — applications hand their data stream to TCP, which handles segmentation, reliability, flow control, and reordering before passing it down to IP.

---

## 3. UDP (User Datagram Protocol)

### 3.1 Key Features
UDP is a **lightweight, best-effort** transport protocol. It provides the same basic data segmentation and reassembly as TCP, but **without reliability or flow control**. It is usually described in terms of what it does *not* do compared to TCP:

- Data is **not** reconstructed in the order it was sent — it is used in the order it is received.
- **No retransmission** — any segments that are lost are not resent.
- **No session establishment** — there is no handshake before data is sent.
- **No flow control** — the sender is not informed about the receiver's resource availability.

UDP is a **stateless protocol** — neither the client nor the server tracks the state of the communication session. If reliability is required, it must be handled by the application itself, not the transport layer.

> UDP is well suited to applications where data needs to flow quickly, and video/voice applications can tolerate some data loss with minimal or no noticeable effect.

### 3.2 UDP Header

- Total overhead: **8 bytes** (much simpler than TCP because it has far fewer fields)
- The units of communication in UDP are called **datagrams** (or segments), sent on a best-effort basis by the transport layer protocol.
- Fields:

| Field | Size (bits) | Description |
|---|---|---|
| Source Port | 16 | Identifies the source application by port number |
| Destination Port | 16 | Identifies the destination application by port number |
| Length | 16 | Indicates the length of the UDP datagram header |
| Checksum | 16 | Used for error checking of the datagram header and data |

### 3.3 Applications That Use UDP
Three categories of applications are best suited to UDP:

1. **Live video and multimedia applications** — Can tolerate some data loss but require little or no delay (e.g., **VoIP**, video streaming/video conferencing).
2. **Simple request-and-reply applications** — A host sends a request and may or may not receive a reply (e.g., **DNS**, **DHCP**).
3. **Applications that handle reliability themselves** — Flow control, error detection, acknowledgment, and error recovery are not required from the transport layer, or are handled by the application (e.g., **SNMP**, **TFTP**).

> **Note:** Although DNS and SNMP use UDP by default, DNS switches to TCP if a request or response is larger than 512 bytes. Similarly, network administrators may configure SNMP to use TCP in certain situations.

---

## 4. TCP vs. UDP — Side-by-Side Comparison

| Category | TCP | UDP |
|---|---|---|
| Connection type | Connection-oriented | Connectionless |
| Reliability | Reliable (retransmission, error recovery) | Best-effort (no retransmission) |
| Ordering | Guaranteed (reassembled in order) | Not guaranteed |
| Flow control | Yes | No |
| Header size | 20 bytes | 8 bytes |
| State | Stateful | Stateless |
| Speed | Slower (more overhead) | Faster (minimal overhead) |
| Data unit name | Segment | Datagram |
| Typical apps | FTP, HTTP, SMTP, SSH | VoIP, DNS, DHCP, SNMP, TFTP |

### Shared Header Fields (present in both TCP and UDP)
- **Source Port**
- **Destination Port**
- **Checksum**

### TCP-Only Fields (all related to reliability functions)
- Sequence Number, Acknowledgment Number, Control Bits, Window, Header Length, Reserved, Urgent

---

## 5. FTP vs. TFTP (Common Point of Confusion)

| Category | FTP | TFTP |
|---|---|---|
| Transport protocol | TCP | UDP |
| Reliability | High | Low |
| Authentication | Requires username/password | No authentication |
| Functionality | Full-featured (list files, navigate directories, upload/download) | File transfer only (minimal functionality) |
| Port | 20, 21 | 69 |
| Typical use case | Uploading website files, large file transfers | Transferring firmware/config files for network devices (e.g., router/switch boot process) |

---

## 6. Practice Questions Covered

**Q: Which two applications would use the UDP transport layer protocol?**
✅ **VoIP** and **TFTP**
(FTP and HTTP use TCP; ICMP is a separate protocol used for diagnostics, not a transport layer protocol.)

**Q: Which two fields are the same in a TCP and UDP header?**
✅ **Source port number** and **Destination port number**
(Sequence Number and Control Bits are TCP-only; "Well-known port number" is a port range concept, not a header field.)

---

## 7. Quick Reference Summary

- **TCP = reliable, slower, heavier header (20 bytes)** — used when data integrity matters more than speed.
- **UDP = best-effort, faster, lighter header (8 bytes)** — used when speed matters more than perfect delivery, or when the application handles reliability itself.
- Both protocols share only 3 header fields: **Source Port, Destination Port, Checksum.**
- TCP's extra fields all exist to support its reliability features (ordering, acknowledgment, flow control).
