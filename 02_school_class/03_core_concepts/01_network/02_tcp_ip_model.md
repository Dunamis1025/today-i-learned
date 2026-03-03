# TCP/IP Model

## 1. What is the TCP/IP Model?

The **TCP/IP Model** is a networking model that explains how data is transmitted across the internet.

It was designed based on real-world internet communication and is the **actual architecture used by the modern internet**.

TCP/IP stands for:

- **TCP (Transmission Control Protocol)**
- **IP (Internet Protocol)**

The model consists of **four layers**, each responsible for a specific part of network communication.

---

# 2. TCP/IP Model Layers

| Layer | Role |
|------|------|
| Application | Provides network services to user applications |
| Transport | Handles end-to-end communication between devices |
| Internet | Responsible for logical addressing and routing |
| Network Access | Handles physical network transmission |

---

# 3. Layer Explanation

## 1️⃣ Application Layer

The **Application Layer** is where users interact with network services.

It provides protocols that applications use to communicate over the network.

Examples:

- Web browsing
- Email services
- File transfers

Common protocols:

- HTTP / HTTPS
- FTP
- SMTP
- DNS

Example:

```
Browser → HTTP Request → Web Server
```

---

## 2️⃣ Transport Layer

The **Transport Layer** manages how data is delivered between devices.

Main responsibilities:

- Segmenting data
- Managing data delivery
- Error checking
- Ensuring proper communication between hosts

Two main protocols are used here.

### TCP (Transmission Control Protocol)

Characteristics:

- Connection-oriented
- Reliable
- Ensures correct data order
- Performs error recovery

Used for:

- Web browsing
- Email
- File downloads

---

### UDP (User Datagram Protocol)

Characteristics:

- Connectionless
- Faster transmission
- Less reliability
- No delivery guarantee

Used for:

- Online gaming
- Video streaming
- VoIP

---

## 3️⃣ Internet Layer

The **Internet Layer** is responsible for determining where data should go.

It uses **IP addresses** to route packets between networks.

Main protocols:

- IP (Internet Protocol)
- ICMP
- ARP

Example:

```
IP Address → Determines destination of data packets
```

---

## 4️⃣ Network Access Layer

The **Network Access Layer** handles the actual transmission of data over the physical network.

Responsibilities include:

- MAC addressing
- Frame transmission
- Physical network communication

Common technologies:

- Ethernet
- WiFi

---

# 4. Data Transmission Flow Example

Example: Opening a website

```
Application Layer
HTTP Request created

↓
Transport Layer
TCP Segment created

↓
Internet Layer
IP Packet created

↓
Network Access Layer
Frame transmitted through the network
```

---

# 5. TCP/IP Model vs OSI Model

| OSI Model | TCP/IP Model |
|-----------|-------------|
| Application | Application |
| Presentation | Application |
| Session | Application |
| Transport | Transport |
| Network | Internet |
| Data Link | Network Access |
| Physical | Network Access |

Key differences:

- **OSI Model has 7 layers**
- **TCP/IP Model has 4 layers**
- TCP/IP is **used in real-world internet communication**

---

# 6. Key Concepts to Remember

Important points to remember:

1. The **TCP/IP Model explains how the internet works**.

2. It consists of **four layers**:

```
Application
Transport
Internet
Network Access
```

3. Important protocols:

Application → HTTP, DNS  
Transport → TCP, UDP  
Internet → IP  
Network Access → Ethernet

4. **TCP**

- Reliable
- Connection-oriented
- Guarantees delivery

5. **UDP**

- Faster
- Connectionless
- No delivery guarantee

---

# Summary

The **TCP/IP Model** is the foundational networking model used for internet communication.

It consists of **four layers**, each responsible for a specific function in data transmission.

Data moves through the layers from:

```
Application → Transport → Internet → Network Access
```

This layered structure allows devices across the internet to communicate efficiently and reliably.
