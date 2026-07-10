# Network Services — Study Notes

A summary of key network services covered in this module: Web, Email, Proxy, AAA, Syslog, Load Balancing, SCADA, and Ethernet switching/routing fundamentals.

---

## 1. Web Servers & HTTP/HTTPS

A **web server** is a computer that provides web resources (text, images, video) to clients. Browsers communicate with web servers using **HTTP** (or the secure version, **HTTPS**).

### HTTP Request/Response Process

| Step | Name | Description |
|------|------|-------------|
| 1 | **Request** | The browser converts the domain name to an IP address via DNS, then sends a `GET` request to the web server asking for a specific file (e.g., `index.html`). |
| 2 | **Response** | The web server locates the requested HTML code and sends it back to the browser. |
| 3 | **Display** | The browser interprets (renders) the HTML code into the visual page layout shown on screen. |

---

## 2. Mail Servers & Email Protocols

Mail servers operate on a **store-and-forward** basis — messages pass between intermediary mail servers rather than going directly from sender to recipient.

### Key Protocols

- **SMTP (Simple Mail Transfer Protocol)** — used for *sending* email
- **POP (Post Office Protocol)** — downloads mail to a single device, typically deleting it from the server afterward
- **IMAP (Internet Message Access Protocol)** — keeps mail synced on the server; accessible/consistent across multiple devices

### Email Delivery Process

1. **Sending (SMTP)** — The sender's email client uploads the message to their mail server via SMTP; that server relays it to the recipient's mail server.
2. **Storage** — The recipient's mail server stores the message in a database.
3. **Retrieval (POP/IMAP)** — The recipient's email client connects to the mail server and retrieves the stored message using POP or IMAP.

---

## 3. Proxy Servers

A **proxy server** acts as an intermediary that performs tasks on behalf of client computers. Its most common function is **caching** — storing copies of frequently accessed web pages.

### Proxy Request Handling Process

1. **Interception** — When a user tries to access a website, the proxy intercepts the request before it leaves the internal network.
2. **Verification** — The proxy checks its cached copy of the page against the current version on the original server to see if content has changed.
3. **Delivery** — If unchanged, the proxy serves the cached copy directly, avoiding a round-trip to the remote server.

### Benefits
- **Speed** — serving from local cache increases network performance
- **Security/Privacy** — hides internal users' real IP addresses; outbound traffic appears to originate from the proxy

---

## 4. AAA (Authentication, Authorization, Accounting)

A security framework for managing network access, with three core functions:

| Function | Purpose |
|----------|---------|
| **Authentication** | Verifies who the user is |
| **Authorization** | Determines what the user is permitted to do |
| **Accounting** | Tracks what actions the user performed |

### AAA Access Process

1. **Connection** — Client connects to a network router.
2. **Credential Prompt** — Router asks the user for username and password.
3. **Verification** — Router forwards the credentials to a remote **AAA server** to confirm accuracy.
4. **Access Granted** — Once verified, the user is granted access based on permissions stored on the AAA server.

---

## 5. Syslog

**Syslog** lets network devices (routers, switches, firewalls) record system activity and send logs to a central log server, helping administrators monitor and troubleshoot the network.

### Core Functions
- **Information Collection** — gathering logs for monitoring/troubleshooting
- **Selection** — choosing which types of events to capture
- **Destination Management** — specifying where logs are sent

---

## 6. Load Balancer

High-traffic services (web, email, streaming) can overwhelm a single server. A **load balancer** sits in front of multiple servers and distributes incoming requests evenly across them.

**Benefits:** prevents overload on any single server, reduces timeouts/slow responses, ensures consistent service.

---

## 7. SCADA (Supervisory Control and Data Acquisition)

A system used in **industrial control systems (ICS)** to remotely monitor and control critical infrastructure (power plants, water treatment, etc.).

- Software gathers status data from field devices
- Manages/automates devices remotely, often via **cellular or satellite** communication

---

## 8. Network Services — Quick Reference Table

| Service | Function |
|---------|----------|
| **DHCP** | Automatically assigns IP addresses to hosts |
| **Authentication** | Typically handled via a AAA server |
| **Web** | Uses HTTP/HTTPS to display content in a browser |
| **DNS** | Translates domain names (e.g., cisco.com) into IP addresses |
| **File** | Uses FTPS, SFTP, SCP for secure file transfer |
| **Mail** | Uses SMTP (send) and POP3/IMAP (receive) |
| **Syslog** | Collects and stores system messages from network devices |
| **Proxy** | Caches web pages for faster subsequent access |

---

## 9. Ethernet Switches vs. Routers

### Switches — Communication Within the Same Network (LAN)
- Connect devices (computers, printers, routers) on the same LAN
- Devices are identified by unique **MAC addresses** (burned into the NIC)
- When a switch receives data, it checks the **destination MAC address** to determine which port to forward it to

### Routers — Communication Between Different Networks
- Devices use **IP addresses** to communicate, both within and across networks
- When a device sends data to a destination on a different network, it first sends it to its **default gateway** (the local router)
- The router consults its **routing table**:
  - If the destination is on a directly connected network → forwards data straight there
  - If not → forwards the packet to another router, continuing toward the destination

### Key Distinction
> **Switches forward data within the same network. Routers forward data between different networks.**

---

*Source: Cisco Networking Academy course material — Module 5.2.5 (Network Services)*
