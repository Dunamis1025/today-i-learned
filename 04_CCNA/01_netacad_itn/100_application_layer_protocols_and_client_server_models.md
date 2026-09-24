# Module 15: Application Layer

## Module Objective
Explain the operation of application layer protocols in providing support to end-user applications.

---

## 15.1 Application Layer Protocols

### 15.1.1 Application Layer

- In both the OSI and TCP/IP models, the **application layer** is the layer closest to the end user. It provides the interface between the network and the applications running on a host.
- **OSI model**: splits this functionality into three separate layers — Application (L7), Presentation (L6), Session (L5).
- **TCP/IP model**: combines all three into a single **Application** layer.
- Key application layer protocols: **DNS, HTTP, SMTP, POP3, IMAP, DHCP, FTP, Telnet**.

### 15.1.2 Presentation and Session Layer

**Presentation layer** — three primary functions:
1. **Formatting** — presents data in a compatible format for the destination device.
2. **Compressing** — compresses data so it can be efficiently decompressed by the destination.
3. **Encrypting** — encrypts data for transmission and decrypts it on receipt.

Standard formats handled at this layer:
- Video: MPEG (Motion Picture Experts Group)
- Images: JPEG (Joint Photographic Experts Group), GIF (Graphics Interchange Format)
- Documents/graphics: PNG (Portable Network Graphics)

**Session layer** — manages dialogues between source and destination applications:
- Creates, maintains, and ends dialogues between applications.
- Manages the exchange of information needed to initiate dialogues.
- Determines whether a session can be resumed after a long interruption.

### 15.1.3 TCP/IP Application Layer Protocols

| Category | Protocol | Port(s) | Function |
|---|---|---|---|
| Name System | **DNS** | TCP/UDP 53 | Translates domain names (e.g. cisco.com) into IP addresses |
| Host Config | **BOOTP** | UDP client 68, server 67 | Lets a diskless workstation discover its IP, a BOOTP server's IP, and a boot file (superseded by DHCP) |
| Host Config | **DHCP** | UDP client 68, server 67 | Dynamically assigns reusable IP addresses |
| Email | **SMTP** | TCP 25 | Sends email — client→server and server→server |
| Email | **POP3** | TCP 110 | Retrieves email from server, downloads to local client |
| Email | **IMAP** | TCP 143 | Accesses email while keeping it stored on the server |
| File Transfer | **FTP** | TCP 20–21 | Reliable, connection-oriented, acknowledged file transfer |
| File Transfer | **TFTP** | UDP client 69 | Simple, connectionless, best-effort file transfer with less overhead than FTP |
| Web | **HTTP** | TCP 80, 8080 | Exchanges text, images, sound, video, and other multimedia on the web |
| Web | **HTTPS** | TCP/UDP 443 | Encrypts HTTP communications and authenticates the website |

**Exam tip**: know the ports cold — DNS=53, DHCP=67/68, SMTP=25, POP3=110, IMAP=143, FTP=20/21, HTTP=80, HTTPS=443.

---

## 15.2 Peer-to-Peer

### 15.2.1 Client-Server Model

- The client sends a data request to the server; the server responds.
- Data storage is **centralized**, making access control and backups easier to manage.
- Clients may need authentication to access server data; some services (e.g. FTP) require a dedicated server.
- Example: web browser (client) ↔ web server.

### 15.2.2 Peer-to-Peer (P2P) Networks

- Data is accessed from a peer device **without a dedicated server**.
- Every device can act as **both client and server simultaneously**.
- No central management device — security enforcement is harder.
- Example: Peer 1 (Print Client / File Server), Peer 2 (Print Server / File Client), a peer with a directly connected printer.

### 15.2.3 Peer-to-Peer Applications

- A P2P **application** lets a single device act as both client and server within the same communication (e.g. instant messaging — both sides send and receive simultaneously).
- Some P2P apps use a **hybrid model**: resources are decentralized, but a **centralized index** points to where resources are located.

### 15.2.4 Common P2P Applications

- Common P2P networks: **BitTorrent, Direct Connect, eDonkey, Freenet**.
- Many are based on the **Gnutella protocol**, which lets users share **whole files** and locate resources shared by other Gnutella peers (clients: BitTorrent, BitComet, DC++, Deluge, eMule).
- **BitTorrent**-style apps allow users to share **pieces of many files** with multiple peers at the same time, using a torrent file that tracks which peers hold which pieces.
- ⚠️ Copyright: downloading/distributing copyrighted files without permission can lead to criminal charges and civil lawsuits.

---

## 15.3 Web and Email Protocols

### 15.3.1 HTTP and HTML — How a Web Page Loads

Example: entering `http://www.cisco.com/index.html`

1. **Browser parses the URL** into three parts: `http` (protocol), `www.cisco.com` (server name), `index.html` (requested filename).
2. **DNS lookup + request**: browser resolves the server name to an IP via a name server, then sends an HTTP **GET** request for the file.
3. **Server responds**: sends back the HTML code for the page (e.g. `HTTP/1.1 200 OK` plus the page's HTML content).
4. **Browser renders**: deciphers the HTML and displays the formatted page in the browser window.

### 15.3.2 HTTP and HTTPS

- **HTTP** is a request/response protocol. Three common message types:
  - **GET** — client requests data (e.g. an HTML page).
  - **POST** — uploads data files to the server (e.g. form data).
  - **PUT** — uploads/replaces resources or content on the server (e.g. an image).
- HTTP is flexible but **not secure** — requests and responses are sent in plaintext and can be intercepted.
- **HTTPS** secures communication using **authentication and encryption**, applying **TLS** (or its predecessor **SSL**) to encrypt data before it's transported across the network.

### 15.3.3 Email Protocols — Overview

- Email is a **store-and-forward** service: messages are stored in databases on mail servers, then forwarded and retrieved across the network.
- Flow: Sender → local mail server (via SMTP) → recipient's mail server (via SMTP across the internet) → recipient (via IMAP or POP3).
- Email uses **separate protocols for sending vs. retrieving**:
  - **Sending**: always **SMTP**.
  - **Retrieving**: either **POP3** or **IMAP**.

### 15.3.4 SMTP, POP, and IMAP — Details

**SMTP (Simple Mail Transfer Protocol)**
- Requires a message header (properly formatted sender/recipient addresses) and a message body.
- Client SMTP process connects to server SMTP process on **port 25**.
- Server delivers to a local account, or **forwards** to another mail server.
- **Spools** messages if the destination server is offline/busy; retries periodically; returns as undeliverable after expiration.

**POP (Post Office Protocol)**
- Retrieves mail: **downloads to client and deletes from server** by default.
- Server passively listens on **TCP port 110**; client connects, server greets, commands/responses are exchanged, then the connection closes.
- No centralized copy remains on the server — **not recommended** for businesses needing centralized backup.
- **POP3** is the most common version.

**IMAP (Internet Message Access Protocol)**
- Downloads only a **copy** of messages; the **original stays on the server** until manually deleted.
- Supports a **file hierarchy** on the server that's mirrored on the client; deletions sync between client and server.
- Better suited for multi-device access and centralized backup needs.

**Comparison table**

| | SMTP | POP3 | IMAP |
|---|---|---|---|
| Purpose | Sending | Retrieving | Retrieving |
| Port | 25 | 110 | 143 |
| Message kept on server? | N/A | ❌ Deleted after download | ✅ Kept until manually deleted |
| Multi-device sync | N/A | Difficult | Easy |
| Best for | Always used | Single device, personal use | Multiple devices, backup needs |

---

## Quiz Review — Key Takeaways

1. The **Application layer** is concerned with protocols that exchange data between programs running on hosts.
2. **MKV, GIF, JPG** are Presentation-layer standards (data formatting), not Application-layer protocols.
3. **Presentation, Session, and Application** (OSI) together map to the single Application layer in TCP/IP.
4. Protocols vs. formats — **DNS and SMTP** are Application-layer *protocols*; PNG and QuickTime are Presentation-layer *formats*.
5. Session layer function = "exchange of information to initiate dialog between peers" (not formatting or compression — those are Presentation layer).
6. P2P model does **not** require a dedicated server; every peer can be both client and server.
7. **BitTorrent** allows sharing pieces of many files simultaneously; **Gnutella** allows sharing whole files; **Hybrid** describes a model (centralized index + decentralized resources), not an app.
8. **POST** uploads data files to a web server; **GET** requests data; **PUT** uploads/replaces resources.
9. **HTTP** establishes the browser-to-server connection; **SMTP** sends email to a mail server.
10. **IMAP** downloads a copy of messages while leaving the original on the server (vs. POP3, which deletes after download).
