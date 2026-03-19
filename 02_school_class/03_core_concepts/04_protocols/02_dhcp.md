# DHCP (Dynamic Host Configuration Protocol)

DHCP is a network protocol that automatically assigns IP addresses and other network configuration settings to devices on a network.

Instead of manually configuring each device, DHCP allows devices to connect to a network and receive the necessary settings automatically.

---

# Why DHCP is Important

Without DHCP, network administrators must manually assign IP addresses to every device.

Problems without DHCP:

- Time-consuming configuration
- High risk of human error
- IP address conflicts (duplicate IPs)
- Difficult to manage large networks

With DHCP:

- Automatic IP assignment
- Efficient network management
- Reduced configuration errors
- Scalable for large environments

---

# What DHCP Provides

When a device connects to a network, DHCP provides:

- IP Address
- Subnet Mask
- Default Gateway
- DNS Server Address
- Lease Time (how long the IP is valid)

---

# DHCP Process (DORA)

DHCP uses a 4-step process called **DORA**:

## 1. Discover

The client broadcasts a message to find available DHCP servers.

- Message: DHCP Discover
- Type: Broadcast

## 2. Offer

The DHCP server responds with an available IP address.

- Message: DHCP Offer
- Contains: IP address, subnet mask, gateway, DNS

## 3. Request

The client requests the offered IP address.

- Message: DHCP Request
- Sent to the selected DHCP server

## 4. Acknowledge

The server confirms and assigns the IP address.

- Message: DHCP Acknowledgement (ACK)

---

# DHCP Lease

A DHCP lease is the period during which a device can use an assigned IP address.

- Temporary assignment
- Must be renewed before expiration
- Prevents IP exhaustion

Example:

- Lease time: 24 hours
- Device must renew before expiration

---

# DHCP Renewal Process

There are two key stages:

## T1 (50% of lease time)

- Client tries to renew with the original DHCP server

## T2 (87.5% of lease time)

- Client broadcasts to any DHCP server if original server is unavailable

---

# DHCP Allocation Methods

## 1. Dynamic Allocation

- IP is assigned automatically from a pool
- Most common method

## 2. Automatic Allocation

- DHCP assigns a permanent IP to a device

## 3. Manual Allocation (Reservation)

- Admin assigns a specific IP based on MAC address

---

# DHCP Components

## DHCP Server

- Assigns IP addresses
- Manages IP pool

## DHCP Client

- Requests IP address
- Example: PC, smartphone, laptop

## DHCP Relay Agent

- Forwards DHCP requests between different networks (subnets)

---

# DHCP Ports and Protocol

- Protocol: UDP
- Port 67 → Server
- Port 68 → Client

---

# Advantages of DHCP

- Simplifies network management
- Reduces human error
- Prevents IP conflicts
- Supports large networks
- Automatically updates configurations

---

# Disadvantages of DHCP

- Dependency on DHCP server
- Single point of failure (if no redundancy)
- Possible security risks (rogue DHCP server)

---

# DHCP Security Risks

## Rogue DHCP Server

An unauthorized DHCP server that provides incorrect network settings.

Risks:

- Redirect traffic
- Man-in-the-Middle attack
- Network disruption

## DHCP Starvation Attack

Attacker floods DHCP server with requests to exhaust IP pool.

---

# DHCP Security Solutions

- DHCP Snooping (switch feature)
- Port security
- Network segmentation
- Monitoring and logging

---

# DHCP vs Static IP

| Feature | DHCP | Static IP |
|--------|------|----------|
| Configuration | Automatic | Manual |
| Management | Easy | Difficult |
| Scalability | High | Low |
| Use Case | Home, office networks | Servers, printers |

---

# Real-World Example

When you connect your phone to Wi-Fi:

1. Your phone sends a DHCP Discover
2. Router replies with DHCP Offer
3. Phone sends Request
4. Router sends ACK

Your phone now has:

- IP address
- Internet access
- Network configuration

---

# Summary

DHCP is essential for modern networks.

It automates IP address assignment, reduces errors, and allows efficient network management.

Understanding DHCP is critical for:

- Network engineers
- Cybersecurity professionals
- IT support roles

---

# Key Takeaways

- DHCP = automatic IP assignment
- Uses DORA process
- Works over UDP (ports 67/68)
- Uses lease system
- Can be vulnerable without security controls
