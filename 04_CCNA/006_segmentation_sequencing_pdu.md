# 06. Segmentation, Sequencing, and PDU

## 1. Segmentation

Segmentation is the process of breaking large data into smaller, manageable pieces for transmission.

- Large data (e.g., video, email attachments) is divided into smaller units.
- Each piece is sent separately across the network.
- Similar to sending a long letter using multiple envelopes.

### Why Segmentation?

- Prevents one device from monopolizing the network
- Allows multiple communications at the same time (Multiplexing)
- Improves efficiency by retransmitting only lost segments

---

## 2. Multiplexing

Multiplexing allows multiple communications to share the same network simultaneously.

- Different data streams are interleaved
- Network resources are used more efficiently

---

## 3. Sequencing

When data is segmented, packets may arrive out of order.

### Problem:
- Packets can take different routes
- They may arrive in the wrong order

### Solution:
- Each segment is assigned a **sequence number**

### Role of TCP:
- TCP ensures segments are:
  - Delivered to the correct destination
  - Reassembled in the correct order

### Analogy:
- Like numbering pages in a book sent in separate envelopes

---

## 4. PDU (Protocol Data Unit)

A PDU is the name given to data at each layer of the network.

As data moves down the protocol stack, it is encapsulated and renamed.

### Encapsulation:
- Each layer adds its own header information
- Data is wrapped layer by layer

---

## 5. PDU Names by Layer

| Layer              | PDU Name   |
|-------------------|-----------|
| Application       | Data      |
| Transport (TCP)   | Segment   |
| Network           | Packet    |
| Data Link         | Frame     |

---

## 6. Key Concept Summary ⭐

- Segmentation improves speed and efficiency
- Multiplexing allows multiple communications simultaneously
- Sequencing ensures correct order using TCP
- PDU = data format at each layer
- Encapsulation = adding headers at each layer

---
