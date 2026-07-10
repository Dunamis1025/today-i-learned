# Networking Fundamentals: Hosts, DHCP, DNS, and Network Services

## 1. Hosts: Servers and Clients

Every computer connected to a network that participates in communication is called a **host** (or end device). Hosts fall into two main roles:

- **Server** — A computer that provides a specific service (web pages, file storage, email, etc.). A single physical server can run multiple server applications simultaneously, offering several services at once.
- **Client** — A computer (user device) that consumes the services a server provides.

### Common Server/Client Pairs

| Type | Server Role | Client Role |
|---|---|---|
| File Server | Stores files centrally | Accesses files via apps like Windows Explorer |
| Web Server | Hosts website data | Accesses pages via browsers (Chrome, Firefox) |
| Email Server | Manages mail data | Sends/receives mail via apps like Outlook |

---

## 2. DHCP (Dynamic Host Configuration Protocol)

Every device on a network needs a unique **IP address** to communicate. **DHCP** is the service that assigns these addresses automatically, so users don't have to configure them manually — a device just connects, and DHCP hands out the network settings needed to get online.

DHCP servers (run by ISPs, network admins, or home routers) lease IP addresses to devices from a predefined address pool.

### 2.1 DHCP Operation — The 4-Step Process (DORA)

When a device joins a network, it obtains an IP configuration through four steps:

1. **Discover** — The client broadcasts: *"Is there a DHCP server that can give me an IP configuration?"*
2. **Offer** — A DHCP server responds: *"I can offer you this IP configuration."*
3. **Request** — The client replies: *"I accept this offer and want to use it."*
4. **Acknowledge (ACK)** — The server confirms: *"Confirmed — you're cleared to use this configuration for the specified lease time."*

After this exchange, the client can communicate on the network until its lease expires.

### 2.2 Duplicate Address Detection (via ARP)

Before actually using the assigned IP, the client sends an **ARP** message asking the network, *"Is anyone already using this address?"*
- No reply → the client begins using the IP.
- A reply received → there's a conflict, and the client must restart the DHCP process to get a different address.

### 2.3 DHCP Lease & Renewal

- An IP address is essentially **rented**, not owned permanently.
- Before the lease expires, the client sends a **DHCPREQUEST** asking to renew it.
- If approved, the server replies with a **DHCPACK**, extending the lease for the same address.
- If a device goes offline and the lease expires without renewal, the server reclaims the address for other devices to use.

### 2.4 DHCP Reservations

Some devices (servers, printers) need a **fixed, unchanging IP address**. Administrators pre-register the device's unique **MAC address** in the DHCP server's configuration, mapping it to a specific IP. Every time that device connects, the server recognizes its MAC address and always assigns the same reserved IP.

### 2.5 Why Wireshark Comes Up Here

**Wireshark** is a network analysis tool that captures and displays real-time traffic flowing across a network. It's relevant to DHCP because:

- The 4-step DORA process happens almost instantly and is invisible to the user. Wireshark lets you actually **see the packets** — their order and contents — as they're exchanged.
- It provides **empirical proof** that DHCP's theoretical steps are real, observable events happening at the packet level, not just an abstract concept.

---

## 3. DNS (Domain Name System)

DNS acts as a **translator** between human-friendly domain names (e.g., `www.cisco.com`) and the numeric IP addresses (e.g., `198.133.219.25`) that computers actually use to locate each other. If a server's IP address changes, DNS updates the mapping behind the scenes — users keep using the same name without noticing anything changed.

### 3.1 DNS Resolution Process

1. **Request** — User types a domain name (e.g., `www.cisco.com`) into a browser.
2. **Matching** — The DNS server checks its records for an entry matching that name.
3. **Query** — The client asks the DNS server: *"What's the IP address for this name?"*
4. **Response** — The DNS server returns the matching IP address.
5. **Connection** — The client uses that IP address to connect directly to the target server and load the content.

### 3.2 DNS Resource Records (RRs)

DNS servers store domain-to-IP (and other) mappings as **resource records**. If a server doesn't have the requested record, it queries a higher-level DNS server to find the answer.

| Record Type | Purpose |
|---|---|
| **A** | Maps a domain name to an IPv4 address |
| **AAAA** | Maps a domain name to an IPv6 address |
| **MX** | Specifies the mail server(s) for a domain, with priority values for redundancy |
| **TXT** | Holds extra text info, commonly used for security/anti-spam purposes |

### 3.3 Spam Management via DNS (TXT-based Security)

Because attackers often abuse DNS to send spam pretending to be from a legitimate domain, three TXT-record-based mechanisms help verify sender legitimacy:

- **SPF (Sender Policy Framework)** — Lists the servers officially authorized to send mail for a domain. Receivers check this list and can reject/flag mail from unauthorized servers.
- **DKIM (DomainKeys Identified Mail)** — Uses cryptographic digital signatures to verify the sender's identity and confirm the message wasn't altered in transit. Stronger than SPF alone.
- **DMARC (Domain-based Message Authentication, Reporting & Conformance)** — Builds on SPF and DKIM by defining a policy for what receivers should do with messages that fail those checks (reject, quarantine, etc.).

---

## 4. Print Servers

A print server lets multiple users share a single printer efficiently. Its core functions:

- **Client Access** — Provides the connection users need to reach the shared printer.
- **Job Administration (Spooling)** — Queues incoming print jobs in order and sends them to the printer one at a time as it becomes available.
- **Feedback** — Reports printer status to users (e.g., paper jam, low ink, job completed).

---

## 5. File Servers (FTP)

File servers use **FTP (File Transfer Protocol)** to let clients upload/download files to/from a server.

- **Connection Process** — FTP requires **two separate connections**: one for control commands/replies, and one for the actual file data transfer.
- **Security Concerns** — Standard FTP is not secure. Safer alternatives include:
  - **FTPS** — Encrypts the FTP session.
  - **SFTP** — Uses SSH (Secure Shell) to securely transfer files.
  - **SCP** — Also uses SSH, providing a secure method to copy files across a network.

---

## Quick Reference Summary

| Concept | One-Line Takeaway |
|---|---|
| Host | Any networked computer; either a server or a client |
| DHCP | Auto-assigns IP addresses via Discover → Offer → Request → ACK |
| ARP (in DHCP) | Confirms the assigned IP isn't already in use |
| DHCP Lease | IPs are "rented" and must be renewed periodically |
| DHCP Reservation | Fixed IP tied to a device's MAC address |
| Wireshark | Tool to observe real network traffic, used here to prove DHCP works as described |
| DNS | Translates domain names ↔ IP addresses |
| DNS Records (A/AAAA/MX/TXT) | Different types of name-to-resource mappings |
| SPF/DKIM/DMARC | Email authentication layers to prevent spam/spoofing |
| Print Server | Shares one printer among many users via queued jobs |
| File Server (FTP/FTPS/SFTP/SCP) | Transfers files between client and server, securely or not |
