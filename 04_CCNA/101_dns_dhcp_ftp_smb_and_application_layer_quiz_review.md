# 101 - DNS, DHCP, FTP, SMB, and Application Layer Quiz Review

## 1. Domain Name System (DNS)

### 1.1 What DNS Does
- Devices communicate using numeric **IP addresses**, but humans find names easier to remember.
- **Fully Qualified Domain Names (FQDNs)**, like `www.cisco.com`, are mapped to numeric IP addresses (e.g., `198.133.219.25`) so people don't need to memorize numbers.
- If a company changes its server's IP address, the change is transparent to users because the domain name stays the same — it's just re-linked to the new IP.

### 1.2 The 5-Step DNS Resolution Process
1. The user types an FQDN (e.g., `www.cisco.com`) into a browser's address bar.
2. The client sends a **DNS query** to its designated DNS server.
3. The DNS server matches the FQDN to its numeric IP address.
4. The DNS server sends the query response back to the client with the resolved IP address.
5. The client uses that IP address to make requests directly to the destination server.

### 1.3 DNS Message Format
DNS servers store several types of **resource records**:

| Record Type | Description |
|---|---|
| **A** | An end device's IPv4 address |
| **AAAA** | An end device's IPv6 address |
| **NS** | An authoritative name server |
| **MX** | A mail exchange record |

- When a client queries a DNS server, the server first checks its **local cache**. If the record isn't cached, it queries other servers to resolve the name.
- A DNS server stores the portion of the domain it's responsible for in a **DNS zone file**.
- All DNS messages share a single format with four sections:

| Message Section | Description |
|---|---|
| **Question** | The question for the name server |
| **Answer** | Resource records answering the question |
| **Authority** | Resource records pointing toward authority |
| **Additional** | Resource records holding additional information |

### 1.4 DNS Hierarchy
- DNS uses a **hierarchical (tree-like) system**, so no single server needs to store the entire database.
- Structure (top to bottom):
  - **Root-Level Domain**
  - **Top-Level Domains (TLD)** — e.g., `.com`, `.org`, `.au`, `.ca`
  - **Second-Level Domains** — e.g., `cisco.com`
- Each DNS server manages only its own portion of the domain space. If a server doesn't have the requested record, it forwards the request to another server for resolution — it does **not** simply return a failure message to the client.

### 1.5 The nslookup Command
- `nslookup` lets a user manually query name servers to resolve a host name (or reverse-resolve an IP into a name).
- Running `nslookup` alone immediately displays the **configured default DNS server** currently in use — this is the first and most important thing it shows.
- It can also look up **MX records** (mail servers) by running `set type=mx` before querying a domain.

### 1.6 Hands-On Lab Notes (Observe DNS Resolution)
- `ping www.icann.org` resolved to an **IPv6** address by default; `ping -4 www.icann.org` forced an **IPv4** resolution — demonstrating that one domain name can map to both address types.
- `nslookup` → `www.cisco.com` returned a **"Non-authoritative answer"** (a cached answer, not from the ultimate authoritative server), along with multiple IP addresses and a chain of **aliases** (CNAME-like redirections through CDN infrastructure, e.g., Akamai).
- `set type=mx` → `cisco.com` returned multiple mail exchanger records with different **MX preference** values. **Lower preference number = higher priority.** Multiple mail servers exist for **redundancy**.
- `ipconfig /all` confirmed the actual DNS server IP addresses configured on the local machine, matching the "Default Server" shown by `nslookup`.

---

## 2. Dynamic Host Configuration Protocol (DHCP)

### 2.1 Purpose
- DHCP automates the assignment of **IPv4 addresses, subnet masks, gateways, and other IPv4 networking parameters**.
- This is called **dynamic addressing**, as opposed to **static addressing** (where an admin manually configures each device).
- DHCP is strongly preferred on **large networks** or networks with a frequently changing user population, since manual static configuration doesn't scale.
- Addresses are assigned for a limited time called a **lease**. When the lease expires (or a DHCPRELEASE is received), the address returns to the pool for reuse.

### 2.2 Typical Deployment
- In medium-to-large networks, DHCP is usually a **dedicated PC-based server**.
- In home networks, the **home router** typically acts as the DHCP server.
- Many networks use **both** DHCP (for end-user devices) and static addressing (for network devices like gateways, switches, servers, printers).
- **DHCPv6** provides similar services for IPv6, but **does not provide a default gateway address** — that must come from the router's Router Advertisement message.

### 2.3 DHCP Operation (4-Message Exchange)
1. **DHCPDISCOVER** — client broadcasts to find any available DHCP server.
2. **DHCPOFFER** — a server responds with an offered IP address, subnet mask, DNS server, default gateway, and lease duration.
3. **DHCPREQUEST** — the client selects one offer (if multiple exist) and requests it explicitly.
4. **DHCPACK** — the server confirms the lease is finalized.
- If the offered address is no longer valid, the server sends a **DHCPNAK**, and the process restarts from DHCPDISCOVER.
- **DHCPv6** uses an analogous message set: **SOLICIT, ADVERTISE, INFORMATION REQUEST, REPLY**.

---

## 3. File Transfer Protocol (FTP)

- FTP is used to push/pull files between a client and a server.
- FTP is unique in that it establishes **two separate connections**:
  1. **Control connection** — for commands/control traffic, using **TCP port 21**.
  2. **Data connection** — for the actual file transfer, using **TCP port 20**.
- Data transfer works in **either direction**: the client can **download (pull)** from the server, or **upload (push)** to the server.
- FTP is a **client/server** protocol (not peer-to-peer), and since it runs over TCP, it **does** provide reliable data transmission.

---

## 4. Server Message Block (SMB)

- SMB is a **file-sharing protocol** describing the structure of shared network resources (files, directories, printers).
- It operates as **client/server** and **request-response**: the client sends SMB requests, the server sends SMB responses.
- SMB messages perform three main functions:
  1. Start, authenticate, and terminate sessions.
  2. Control access to files and printers.
  3. Allow an application to send/receive messages to/from another device.
- Unlike FTP (two separate connections), SMB establishes **one long-term connection**. Once established, the client can access server resources as if they were local.
- Originally Microsoft-specific, but now also supported by **UNIX, Linux, and macOS**, allowing cross-platform file/printer sharing with Windows systems.

---

## 5. Application Layer (TCP/IP Model) — Key Concepts

- In the **TCP/IP model**, the Application layer is the **closest layer to the end user** and effectively combines what the OSI model splits into Application, Presentation, and Session layers.
  - This means functions like **creating and maintaining dialogue between source and destination applications** are considered part of the TCP/IP Application layer.
- **Physical addressing** → Data Link layer (not Application layer).
- **Logical addressing** → Internet/Network layer (not Application layer).
- Protocols/standards that belong to the **Application layer**: HTTP, HTTPS, FTP, SMTP, POP, IMAP, DNS, DHCP, SMB, and also data format standards like **GIF** and **MPEG**.
- **TCP, UDP, and IP are NOT Application layer protocols** — they belong to the Transport layer (TCP/UDP) and Internet layer (IP).

### Web and Email Protocols
- **HTTP** — request/response protocol for the web; main message types: **GET** (request data), **POST** (submit data), **PUT** (upload/replace data).
- **HTTPS** — same as HTTP, but encrypted via SSL.
- **SMTP** — used to **send** email.
- **POP** — downloads mail to the client and **deletes it from the server**.
- **IMAP** — downloads a **copy** of mail while keeping the **original on the server**, enabling centralized storage/backup — better suited for small-to-medium businesses that want centralized email backup.

---

## 6. Quiz Review — Key Q&A Takeaways

| Question | Correct Answer | Key Reasoning |
|---|---|---|
| DNS record type for IPv6 | **AAAA** | A = IPv4, AAAA = IPv6, NS = name server, MX = mail server |
| DNS server outside its zone sends a failure message? | **False** | It forwards the query to another server instead of failing outright |
| What nslookup displays | **The configured default DNS server** | It shows this immediately, not cached entries or the local device's own IP |
| Record type resolving authoritative name servers | **NS** | NS = Name Server record |
| FTP connections required | **2** | Control (port 21) + Data (port 20) |
| FTP transfers happen push (client→server) and pull (server→client)? | **True** | Data transfer is bidirectional |
| FTP ports | **20 and 21** | 20 = data, 21 = control (25 = SMTP, 110 = POP3 — unrelated to FTP) |
| SMB only supported on Microsoft OS? | **False** | UNIX, Linux, and macOS also support SMB |
| Home network dynamic IPv4 addressing device | **Home router** | ISP gives the router one address; the router distributes addresses internally |
| Top-level DNS domain in `http://www.cisco.com/index.html` | **.com** | www = host, cisco = 2nd-level domain, .com = TLD |
| Two characteristics of TCP/IP Application layer | **Dialogue creation/maintenance** + **Closest to end user** | TCP/IP model merges OSI's Session layer function into Application layer |
| HTTP message to request data | **GET** | POST/PUT send data; ACK isn't an HTTP message type |
| Protocol to transfer messages server → client | **POP3** | SMTP is client/server → server (sending); POP3/IMAP are for receiving |
| File-sharing/print protocol for Microsoft apps | **SMB** | Not SMTP, DHCP, or HTTP |
| Three Application layer protocols/standards | **GIF, HTTP, MPEG** | TCP, UDP, IP are Transport/Internet layer, not Application layer |
| Why DHCP is preferred on large networks | **More efficient than static addressing** | Not about copyright, transport reliability, or DNS request volume |
| Personal computer uploading to a file server | **Client** | The uploader initiates the request; the role initiating a request is the client |
| True statement about FTP | **Client can download from or upload to server** | FTP is client/server (not P2P), always uses exactly 2 connections, and is reliable (runs over TCP) |
| Protocol to request an IPv4 address (wireless host) | **DHCP** | HTTP/ICMP/FTP/SNMP are unrelated to address assignment |
| TCP/IP layer closest to the end user | **Application** | Layer order (bottom→top): Network Access → Internet → Transport → Application |
| Protocol allowing centralized storage/backup of email | **IMAP** | POP deletes mail from server after download; IMAP keeps originals server-side |
| Protocol that uses encryption | **HTTPS** | FTP, DNS, and DHCP do not encrypt by default |
| Two tasks a local DNS server performs | **Mapping name-to-IP addresses** + **Forwarding name resolution requests between servers** | Providing IP addresses is DHCP's job, not DNS's |
