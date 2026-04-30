

---

## 1. Same Network Communication

### Key Concept
When two devices are on the same network, data is sent directly using MAC addresses.

---

### Address Roles

#### Network Layer (IP Address)
- Source IP: 192.168.1.110
- Destination IP: 192.168.1.9

👉 Identifies the final destination

---

#### Data Link Layer (MAC Address)
- Source MAC: AA-AA-AA-AA-AA-AA
- Destination MAC: CC-CC-CC-CC-CC-CC (FTP Server)

👉 Identifies the actual device within the same network

---

### Result
- Data is sent directly via a switch
- No router is required

---

## 2. Remote Network Communication

### Key Concept
When devices are on different networks, data must be sent through a router (default gateway).

---

### Address Roles

#### Network Layer (IP Address) – DOES NOT CHANGE
- Source IP: 192.168.1.110
- Destination IP: 172.16.1.99

👉 The final destination remains constant

---

#### Data Link Layer (MAC Address) – CHANGES
- Source MAC: AA-AA-AA-AA-AA-AA
- Destination MAC: 11-11-11-11-11-11 (Router R1)

👉 The frame is sent to the default gateway first

---

### Result
- Data is sent to the router first
- The router forwards the packet to the next hop

---

## 3. Key Differences

| Category | Same Network | Remote Network |
|----------|------------|----------------|
| Destination IP | Final device | Final device |
| Destination MAC | Final device MAC | Gateway MAC |
| Path | Direct | Via router |
| Routing | Not required | Required |

---

## 4. Important Concepts

### IP Address
👉 Identifies the final destination  
👉 Does not change during transmission  

---

### MAC Address
👉 Identifies the next hop  
👉 Changes at each hop  

---

## 5. Hop-by-Hop Communication

Data moves step by step through routers until it reaches the destination.

---

### Example
- PC → Router → Router → Server

👉 Data "hops" from one device to another

---

## 6. Simple Analogy

### IP Address
👉 Final home address  

---

### MAC Address
👉 Delivery step at each stage  

---

## 7. Key Insight

👉 IP address stays the same  
👉 MAC address changes at every hop  

---

## 8. Why This Matters

- Fundamental concept in networking
- Essential for cybersecurity understanding
- Required for:
  - ARP
  - Routing
  - NAT

---
