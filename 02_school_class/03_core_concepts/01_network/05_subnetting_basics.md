# Subnetting Basics

## What is Subnetting?

Subnetting is the process of dividing a large IP network into smaller networks called **subnets**.

Instead of using one large network for all devices, subnetting creates smaller and more manageable networks.

Example:

A company network might be divided into separate subnets for:
- Office computers
- Servers
- Security cameras
- Guest Wi-Fi

Each subnet becomes its own smaller network.

---

## Why Subnetting is Important

Subnetting provides several advantages:

### 1. Better Network Management
Smaller networks are easier to manage and troubleshoot.

### 2. Improved Security
Different departments or systems can be separated into different networks.

Example:
- Finance network
- HR network
- Guest network

If one subnet is compromised, other networks remain protected.

### 3. Reduced Network Congestion
Broadcast traffic stays inside its own subnet instead of spreading across the entire network.

This improves overall network performance.

### 4. Efficient Use of IP Addresses
Subnetting allows administrators to allocate IP addresses more efficiently.

---

## Basic Concept of Subnetting

An IP address consists of two parts:

Network portion
Host portion


Example:


192.168.1.25


If the subnet mask is:


255.255.255.0


Then:


Network: 192.168.1
Host: 25


Devices in the same network share the same **network portion**.

---

## What is a Subnet Mask?

A **subnet mask** determines which part of an IP address belongs to the network and which part belongs to the host.

Example:


IP Address: 192.168.1.25
Subnet Mask: 255.255.255.0


This means:


Network portion: 192.168.1
Host portion: 25


---

## CIDR Notation

CIDR (Classless Inter-Domain Routing) is a shorter way to represent a subnet mask.

Example:


255.255.255.0 = /24


The number after the slash indicates how many bits are used for the network portion.

Examples:


/24 = 255.255.255.0
/25 = 255.255.255.128
/26 = 255.255.255.192


---

## Example of Subnetting

Suppose we start with this network:


192.168.1.0 /24


This network contains:


256 total addresses


But we can divide it into smaller subnets.

Example:

### Two /25 subnets


192.168.1.0 – 192.168.1.127
192.168.1.128 – 192.168.1.255


Each subnet contains:


128 IP addresses


---

### Four /26 subnets


192.168.1.0 – 192.168.1.63
192.168.1.64 – 192.168.1.127
192.168.1.128 – 192.168.1.191
192.168.1.192 – 192.168.1.255


Each subnet contains:


64 IP addresses


---

## Important Subnet Addresses

Every subnet contains three important types of addresses:

### 1. Network Address

The first IP address in the subnet.

Example:


192.168.1.0


This identifies the subnet itself.

It **cannot be assigned to a device**.

---

### 2. Host Addresses

The usable IP addresses assigned to devices.

Example:


192.168.1.1
192.168.1.2
192.168.1.3
...


---

### 3. Broadcast Address

The last IP address in the subnet.

Example:


192.168.1.255


It is used to send messages to **all devices in the network**.

It also **cannot be assigned to a device**.

---

## Example Calculation

Network:


192.168.1.0 /24


Subnet mask:


255.255.255.0


Addresses:


Network address: 192.168.1.0
First usable host: 192.168.1.1
Last usable host: 192.168.1.254
Broadcast address: 192.168.1.255


Usable hosts:


254 devices


Because:


256 total − 2 reserved (network + broadcast)


---

## Simple Way to Remember Subnetting

Always identify these four things:

1. Network address
2. First usable IP
3. Last usable IP
4. Broadcast address

These are the key values used when designing networks.

---

## Why Subnetting Matters in Cybersecurity

Subnetting is important for cybersecurity because it allows networks to be segmented.

Network segmentation helps:

- limit attack spread
- isolate sensitive systems
- control network traffic
- improve monitoring

For example:


Office network
Server network
Security camera network
Guest Wi-Fi network


If an attacker enters one subnet, segmentation can prevent access to other networks.

---

## Summary

Subnetting divides a large network into smaller networks.

Key concepts include:

- IP address structure
- subnet masks
- CIDR notation
- network address
- host addresses
- broadcast address

Subnetting improves network management, performance, security, and efficient IP address allocation.

Understanding subnetting is a fundamental skill for networking and cybersecurity professionals.
