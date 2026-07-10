# Networking Notes: TCP/IP Transport Layer (TCP vs. UDP)

*Topics: 5.1.2.7, 5.2.1.2–5.2.1.6 — Internet connection types, Transport Layer protocols, and port numbers*

---

## 1. Internet Connection Types (5.1.2.7)

| Type | Definition |
|---|---|
| **Cellular** | Uses towers distributed across a coverage area to provide seamless access to phone and internet services. |
| **Mobile Hotspot** | A cell phone configured to let other devices connect via Wi-Fi. |
| **Satellite** | Popular in rural areas lacking DSL or cable providers. |
| **Broadband** | Uses different frequencies to send multiple signals over the same medium. |
| **DSL** | Digital phone service that can also provide internet access. |
| **Fiber** | Uses light to transfer data; increasingly popular for home/business internet. |
| **Tethering** | The process of connecting another device to a cell phone so it can access the internet. |
| **Cable** | Uses coaxial cables to deliver TV, internet, and voice services. |

---

## 2. The TCP/IP Protocol Suite — Overview

- Network communication is governed by the **TCP/IP Protocol Suite**, organized into **4 layers**: Network Access, Internet, Transport, and Application.
- The **Transport Layer** decides *how* data gets delivered, and offers two main protocols: **TCP** and **UDP**.
- The application determines which protocol to use, depending on whether reliability or speed matters more.

---

## 3. TCP (Transmission Control Protocol)

**Priority: Reliability & Accuracy**

- Breaks data into **segments**, each with a **sequence number**, so the receiver can reassemble them in the correct order.
- The receiver sends an **acknowledgment (ACK)** confirming data was received.
- If no ACK arrives in time, the sender assumes the data was lost and **retransmits** it.
- This verification process adds **overhead** (extra processing/delay), making TCP somewhat slower than UDP.
- **Analogy:** A tracked/registered mail package — the sender can confirm it arrived safely.

**Common use cases:** Web browsing (HTTP), email (SMTP/POP), file transfers (FTP) — anywhere data integrity is critical.

---

## 4. UDP (User Datagram Protocol)

**Priority: Speed**

- A lightweight, "fire-and-forget" protocol — **no acknowledgments, no sequence tracking, no retransmission**.
- Delivers data on a **best-effort basis**: as fast as possible, with no guarantee of arrival.
- Called "unreliable" not because it's bad, but because there's no feedback loop confirming delivery — if data is lost, it's simply gone.
- Much lower overhead than TCP, making it significantly faster.
- **Analogy:** Ordinary (non-registered) mail — you send it and hope for the best, with no delivery confirmation.

**Common use cases:** Live video/audio streaming, VoIP (internet calls), DNS queries — anywhere speed matters more than perfect accuracy.

---

## 5. Quick Comparison

| Feature | TCP | UDP |
|---|---|---|
| Reliability | Reliable (guaranteed delivery) | Unreliable (best-effort) |
| Order | Data reassembled in correct order | No ordering guarantee |
| Acknowledgment | Yes | No |
| Retransmission of lost data | Yes | No |
| Overhead | High | Low |
| Speed | Slower | Faster |
| Typical uses | Web, email, file transfer | Streaming, VoIP, DNS |

> **Note:** Some application-layer protocols use only UDP, some can use both TCP and UDP (e.g., DNS — UDP for quick queries, TCP for larger transfers), but **all** application-layer protocols must use one of the two — none use neither.

---

## 6. Port Numbers — How TCP/UDP Track Conversations

Port numbers let a computer manage **multiple simultaneous connections** without mixing up data, by acting as an addressing system on top of IP.

- **Source Port:** A number the client's OS assigns to identify the specific application/window/process that originated a request (e.g., a particular browser tab).
- **Destination Port:** A "well-known" number identifying the target service on the remote server (e.g., **port 80** for HTTP).

### How it works, step by step:
1. **Client → Server:** Browser sends a request using a unique source port (e.g., `1024`) to the server's destination port (`80`, for HTTP).
2. **Server → Client:** The server replies from its own source port `80`, and sends the response **to the client's original source port** — now used as the destination port (`1024`).
3. **Client identifies the data:** The client checks the incoming destination port (`1024`) to know exactly which browser window/tab the data belongs to.

### Multiple connections at once:
- Opening a second browser tab/window (e.g., to a different website) gets a **new source port** (e.g., `1555`).
- Even though both requests target port 80 on their respective servers, responses come back addressed to different ports (`1024` vs. `1555`), so the client can route each response to the correct tab.

**Summary:** Port numbers function like a routing label — "who sent this, and who should receive it" — allowing many internet conversations to happen at once without confusion.
