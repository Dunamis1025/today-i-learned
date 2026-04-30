# 09. Network Addressing and Protocols Summary

---

## 1. IP vs MAC Addressing

### Network Layer (IP Address)
- Logical address
- Identifies the final destination
- Used for end-to-end communication
- IPv4 = 32 bits
- IPv6 = 128 bits

---

### Data Link Layer (MAC Address)
- Physical address
- Identifies device on local network
- Used for local delivery
- 48 bits (12 hexadecimal digits)

---

### Key Idea
👉 IP = Logical (Who & Where)  
👉 MAC = Physical (How to deliver)

---

## 2. Same vs Different Network

### Same Network
- Devices communicate directly
- Uses destination MAC address
- No router required

---

### Different Network
- Must use default gateway (router)
- Packet is sent to gateway first

👉 "Different network = go to gateway"

---

## 3. Subnet Mask

### Purpose
Determines:
- Network portion
- Host portion

---

### Rule
👉 Left side = Network  
👉 Right side = Host  

---

### Example
IP: 192.168.1.10  
Mask: 255.255.255.0  

→ Network: 192.168.1  
→ Host: 10  

---

## 4. Frame Structure (Data Link Layer)

### Order of Addresses

Frame format:

[ Destination MAC ] → [ Source MAC ] → [ Data ]

👉 Destination comes first

---

## 5. MAC Address Behavior

### Key Concept
MAC addresses change at every hop

---

### Why?
Each network segment has different devices

---

### Result
- Source MAC = current sender
- Destination MAC = next hop

👉 NOT end-to-end

---

## 6. Communication Basics

### Three Elements

- Sender (Source)
- Receiver (Destination)
- Channel

---

## 7. What is a Protocol?

A protocol is a set of rules that defines how communication happens.

---

### Protocol Defines

- Who communicates
- How data is formatted
- When data is sent
- How delivery is confirmed

---

## 8. Protocol Requirements

- Encoding
- Formatting
- Encapsulation
- Size
- Timing
- Delivery options

---

### Encoding

Encoding = convert data into transmittable form  
Decoding = reverse process

---

## 9. Message Timing

Includes:

- Flow control
- Response timeout
- Access method

---

## 10. Delivery Methods

- Unicast → 1:1
- Multicast → 1:Group
- Broadcast → 1:All

---

## 11. Protocol Functions

Protocols provide:

- Addressing
- Reliability
- Flow control
- Sequencing
- Error detection
- Application interface

---

## 12. Protocol Types

### Security Protocols

- SSH
- SSL
- TLS

👉 Provide:
- Authentication
- Integrity
- Encryption

---

### Routing Protocols

- OSPF
- BGP

👉 Used to find best path

---

### Network Services

- DHCP → Assign IP
- DNS → Resolve domain names

---

## 13. Protocol Suite

### Definition

A protocol suite is a group of related protocols working together.

---

### TCP/IP Suite

Used in modern networks

Layers:
- Application
- Transport
- Internet

---

### Features

- Open standard
- Widely adopted

---

## 14. Communication Process

### Server
Encapsulates data → sends

### Client
Decapsulates data → displays

---

## 🔥 Final Key Summary

👉 IP = Logical / End-to-End  
👉 MAC = Physical / Local  
👉 Subnet mask = Defines boundary  
👉 Frame = Destination MAC → Source MAC  
👉 Different network = Use gateway  
👉 MAC changes every hop  
👉 Protocol = Rules of communication  
👉 TCP/IP = Standard protocol suite
