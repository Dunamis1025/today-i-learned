# Network Core Concepts Summary  
(VU23213 – Network Fundamentals for Cyber Security)

This document summarises key networking concepts I studied while working on the Metasploitable Case Study and IPv4/IPv6 configuration in Packet Tracer.

---

## 1. What is a Network?

A network is a group of connected devices (nodes) that communicate with each other.  
Examples of nodes include PCs, laptops, routers, switches, printers, and servers.

---

## 2. What is a Subnet?

A subnet (sub-network) is a smaller division of a larger network.

For example:

192.168.40.0/24 → Large network  
192.168.40.0/26 → Smaller subnet

Subnetting improves:
- Security
- Performance
- Network management

---

## 3. What is a Subnet Identifier?

In IPv6, when using /64, the first 64 bits represent the network portion.

Example:

2001:db8:acad:A::/64  
2001:db8:acad:B::/64  

The fourth block (A, B, etc.) is used to identify different subnets.

---

## 4. IPv6 Address Structure

An IPv6 address has 128 bits and is divided into 8 blocks.

Example:

2001:db8:acad:A::1

Rules:
- Leading zeros can be removed (0db8 → db8)
- Consecutive 0000 blocks can be replaced once with ::

---

## 5. Why is /64 Common in IPv6?

Most IPv6 LAN networks use /64 because of SLAAC.

SLAAC (Stateless Address Auto Configuration) allows devices to automatically generate their own IPv6 address without DHCP.

The first 64 bits = network prefix  
The last 64 bits = interface ID

---

## 6. What is DHCP?

DHCP stands for Dynamic Host Configuration Protocol.

It automatically assigns:
- IP address
- Subnet mask
- Default gateway
- DNS server

Home routers typically act as DHCP servers.

---

## 7. What is SLAAC?

SLAAC allows devices to self-configure an IPv6 address using:
- The network prefix advertised by a router
- Their own interface information

No DHCP server is required.

---

## 8. What is Link-Local Address (FE80::)?

FE80::/10 is reserved for link-local addresses.

- Used only within the local network
- Not routable to the internet
- Often used as default gateway in IPv6

Example:
FE80::1

---

## 9. What is Multicast?

Multicast is a communication method where data is sent to a specific group instead of all devices.

Types of communication:

- Unicast → one-to-one
- Broadcast → one-to-all (IPv4 only)
- Multicast → one-to-group

IPv6 does not use broadcast.  
Instead, it uses multicast (e.g., ff02::1).

---

## 10. What is a Node?

A node is any device connected to a network.

Examples:
- PC
- Router
- Switch
- Server
- Access Point

---

## Reflection

Through this study, I developed a clearer understanding of how IPv4 and IPv6 networks are structured, how subnetting improves network segmentation, and how automatic address assignment works using DHCP and SLAAC.

This foundation supports further cybersecurity studies, including network segmentation, monitoring, and attack simulation.
