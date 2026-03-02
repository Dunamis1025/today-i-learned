# OSI Model (Open Systems Interconnection Model)

## 1. What is the OSI Model?

The OSI model is a 7-layer conceptual framework used to understand how data travels through a network.

It helps us:
- Understand how different networking functions work
- Troubleshoot network problems
- Compare networking technologies

It is a theoretical model, not a real protocol stack.

---

## 2. The 7 Layers (Top → Bottom)

7️⃣ Application  
6️⃣ Presentation  
5️⃣ Session  
4️⃣ Transport  
3️⃣ Network  
2️⃣ Data Link  
1️⃣ Physical  

Mnemonic:
**All People Seem To Need Data Processing**

---

## 3. Layer-by-Layer Explanation

### 7. Application Layer
- Interface between user and network
- Provides network services to applications
- Examples: HTTP, FTP, SMTP, DNS

This is where users interact with network services.

---

### 6. Presentation Layer
- Data formatting
- Encryption / Decryption
- Compression

Example: SSL/TLS encryption happens here conceptually.

---

### 5. Session Layer
- Manages sessions between devices
- Opens, maintains, and closes connections
- Keeps login sessions active

Example: Maintaining a logged-in state on a website.

---

### 4. Transport Layer
- End-to-end communication
- Reliability and flow control
- Port numbers

Protocols:
- TCP (reliable, connection-oriented)
- UDP (fast, connectionless)

---

### 3. Network Layer
- Logical addressing
- Routing between networks
- Determines best path

Protocol:
- IP (Internet Protocol)

Devices:
- Routers operate here

---

### 2. Data Link Layer
- Physical addressing (MAC address)
- Error detection within local network
- Frames

Devices:
- Switches operate here

---

### 1. Physical Layer
- Physical transmission of bits
- Cables, voltage, signals

Examples:
- Ethernet cables
- Fiber optic cables

---

## 4. OSI vs TCP/IP (Quick Comparison)

- OSI = 7 layers (theoretical model)
- TCP/IP = 4 layers (practical implementation)
- TCP/IP combines some OSI layers

Mapping:

Application + Presentation + Session → TCP/IP Application  
Transport → TCP/IP Transport  
Network → TCP/IP Internet  
Data Link + Physical → TCP/IP Network Access  

---

## 5. Why This Model Matters

Understanding the OSI model helps to:

- Diagnose network issues
- Identify which layer a problem belongs to
- Communicate clearly in technical discussions

Example:
If ping works but website does not load → likely Application layer issue.
If no IP address assigned → likely Network layer issue.

---

Note: These notes were written after reviewing learning materials and reorganised in my own words for understanding and revision purposes.
