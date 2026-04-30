# 07. IP, MAC, and Same Network Communication

## 1. IP Address Basics

An IP packet always contains two addresses:

- **Source IP Address**: The IP address of the sending device (original source)
- **Destination IP Address**: The IP address of the receiving device (final destination)

🔑 Key Point:
- These addresses **do not change** from source to destination
- It does not matter if the destination is local or remote

---

## 2. Structure of an IP Address

An IP address consists of two parts:

### (1) Network Portion (Prefix)
- Identifies the network (like a “neighborhood”)
- Devices in the same network share this part

### (2) Host Portion (Interface ID)
- Identifies a specific device within the network
- Must be unique for each device

---

## 3. Subnet Mask

- Determines which part is **network** and which part is **host**
- Example:
  - IP: 192.168.1.110
  - Subnet Mask: 255.255.255.0
  → Network: 192.168.1
  → Host: 110

---

## 4. Same Network Communication

### Example:
- PC1: 192.168.1.110
- Server: 192.168.1.9

👉 Both share the same network portion: **192.168.1**

🔑 Result:
- They are in the **same network**
- No router is needed
- Communication happens directly

---

## 5. IP vs MAC Address

### IP Address (Network Layer)
- Logical address
- Used for **end-to-end delivery**
- Remains the same across the network

### MAC Address (Data Link Layer)
- Physical address (NIC)
- Used for **local delivery**
- Changes at each hop (if routed)

---

## 6. Encapsulation

Data is wrapped step by step:

1. Data
2. + IP Header → Packet
3. + MAC Header → Frame

🔑 Final transmission unit = **Frame**

---

## 7. Key Concept (Very Important)

When devices are in the same network:

- IP network portion is the same
- Data is sent using **MAC address directly**
- No router is involved
- A switch delivers the frame

💡 Analogy:
- Same network = same apartment building
- IP = building address
- MAC = room number

---

## 8. Summary

- IP = “Which network and which device”
- MAC = “Which physical device right now”
- Same network → direct communication
- Different network → router required
