# 03_message_delivery_and_timing

## 📘 Message Delivery and Timing

Today I studied how messages are sent across a network and why rules about message format, size, timing, and delivery method are important.

---

## 1. Network Messages Follow Rules

A message sent over a computer network must follow specific rules so it can be delivered and processed correctly.

This is similar to sending a letter:
- The message needs a proper format
- The sender and receiver must be identified
- The message must be prepared in a form that the network can understand

---

## 2. IP Works Like an Envelope

Internet Protocol (IP) works like an envelope in a letter system.

It helps identify:
- the **source** of the packet
- the **destination** of the packet

In IPv6, the packet header contains fields such as:
- Version
- Traffic Class
- Flow Label
- Payload Length
- Next Header
- Hop Limit
- Source IP Address
- Destination IP Address

The IPv6 header size is **40 bytes**.

---

## 3. Long Messages Are Broken into Smaller Pieces

When a long message is sent across a network, it cannot always be sent as one large block.

Instead, it is broken into smaller pieces called **frames**.

This is necessary because:
- networks have strict size rules
- frames that are too large or too small may not be delivered
- each frame carries part of the original message
- each frame also contains addressing information

At the destination, the frames are put back together to rebuild the original message.

---

## 4. Message Timing

Message timing is very important in network communication.

There are **three main components** of message timing:

### Flow Control
Flow control manages how much data can be sent and how fast it can be delivered.

This prevents the sender from sending data too quickly for the receiver to handle.

### Response Timeout
A device does not wait forever for a reply.

If no response is received within a certain time, the device follows a rule or takes another action.

### Access Method
Access method decides when a device can send data.

This is important because if two devices send at the same time, a collision can happen.

In wireless networks, the device checks whether the medium is available before transmitting.

---

## 5. LAN and WLAN

### LAN
**LAN** stands for **Local Area Network**.

It is a network used in a limited area such as:
- home
- office
- school

A LAN often uses wired connections.

### WLAN
**WLAN** stands for **Wireless Local Area Network**.

It is basically a wireless version of a LAN, such as Wi-Fi.

---

## 6. Delivery Methods

There are three main ways that data can be delivered across a network.

### Unicast
Data is sent to **one single device**.

Example:
- one sender → one receiver

### Multicast
Data is sent to **a specific group of devices**.

Example:
- one sender → selected devices only

### Broadcast
Data is sent to **all devices on the network**.

Example:
- one sender → everyone on the local network

---

## 7. Key Quiz Answers

### Q1. What is the process of converting information into the proper form for transmission?
**Answer: Encoding**

### Q2. Which step of the communication process properly identifies the address of the sender and receiver?
**Answer: Encapsulation**

### Q3. Which three are components of message timing?
**Answers:**
- Flow control
- Access method
- Response timeout

### Q4. Which delivery method sends information to one or more end devices, but not all devices?
**Answer: Multicast**

---

## 8. What I Learned

Today I learned that network communication is not just about sending data.

It also requires:
- proper formatting
- correct addressing
- controlled timing
- correct delivery methods
- breaking large messages into smaller frames

These rules make communication reliable and organized across networks.

---


이 내용을 통해 네트워크 통신은 단순히 데이터를 보내는 것이 아니라,  
정확한 규칙과 구조 위에서 작동한다는 점을 이해했다.
