# 🌐 TCP/IP Model Overview

This document summarizes the core concepts of the TCP/IP 4-layer model, including protocols, roles, and data flow.

---

# 📌 1. Application Layer

Provides services directly to users.

## 🔹 Name System
- **DNS (Domain Name System)**
  - Translates domain names (e.g., cisco.com) into IP addresses.

## 🔹 Host Configuration
- **DHCPv4**
  - Automatically assigns IPv4 addresses.
- **DHCPv6**
  - Automatically assigns IPv6 addresses.
- **SLAAC**
  - Allows devices to configure IPv6 addresses without DHCP.

## 🔹 Email Protocols
- **SMTP**
  - Sends emails between clients and servers.
- **POP3**
  - Downloads emails from server to client.
- **IMAP**
  - Accesses and manages emails on the server.

## 🔹 File Transfer
- **FTP**
  - Reliable, connection-oriented file transfer.
- **SFTP**
  - Secure file transfer using SSH encryption.
- **TFTP**
  - Simple, fast, connectionless transfer with low overhead.

## 🔹 Web Services
- **HTTP**
  - Transfers web data (text, images, video).
- **HTTPS**
  - Secure version of HTTP (encrypted).
- **REST**
  - API-based web service architecture.

---

# 📌 2. Transport Layer

Determines how data is transmitted.

## 🔹 TCP (Transmission Control Protocol)
- Connection-oriented
- Reliable (acknowledgments, retransmission)
- Slower but accurate
- Used in HTTP, FTP, Email

## 🔹 UDP (User Datagram Protocol)
- Connectionless
- No delivery guarantee
- Faster, low overhead
- Used in streaming, gaming, VoIP

## 💡 Analogy
- TCP = Registered mail (safe)
- UDP = Normal mail (fast)

---

# 📌 3. Internet Layer

Handles addressing and routing.

## 🔹 IP Protocols
- **IPv4**
  - 32-bit address
- **IPv6**
  - 128-bit address
- **NAT**
  - Translates private IP → public IP

## 🔹 Messaging
- **ICMPv4**
  - Error reporting (e.g., ping)
- **ICMPv6**
  - Same as ICMPv4 for IPv6
- **ICMPv6 ND**
  - Neighbor discovery & duplicate detection

## 🔹 Routing Protocols
- **OSPF**
  - Fast path selection (link-state)
- **EIGRP**
  - Cisco protocol using multiple metrics
- **BGP**
  - Used between ISPs (global routing)

---

# 📌 4. Network Access Layer

Handles physical transmission.

## 🔹 Address Resolution
- **ARP**
  - Maps IP address → MAC address

## 🔹 Data Link Protocols
- **Ethernet**
  - Wired network standard
- **WLAN**
  - Wireless network (Wi-Fi)

---

# 📦 Encapsulation Process

Data is wrapped layer by layer:

1. **User Data**
2. **TCP Segment** (Port number)
3. **IP Packet** (IP address)
4. **Ethernet Frame** (MAC address)

---

# 🔄 Communication Flow

- Server → Encapsulation → Network → Client
- Client → Decapsulation → Display data

---

# 📊 PDU (Protocol Data Unit)

- Transport Layer → **Segment**
- Internet Layer → **Packet**
- Network Access Layer → **Frame**

---

# 🚀 Key Takeaways

- Each layer has a specific role
- Data is encapsulated step by step
- Protocols differ by purpose (speed vs reliability)
- TCP/IP model = foundation of networking
