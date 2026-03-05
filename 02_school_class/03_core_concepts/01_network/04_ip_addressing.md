# IP Addressing (IPv4 & IPv6) — Simplified Notes

An IP address is a unique identifier used to locate a device on a network.

A simple analogy is a postal system:

- **IP address** = the street address of a house (which device)
- **Port** = the apartment or room number (which service)
- **MAC address** = the hardware ID of the device inside the house (used within local networks)

---

# 1. IPv4 Basic Structure

IPv4 addresses are **32 bits long** and written in four decimal numbers separated by dots.

Example:

192.168.1.10

Each section ranges from **0 to 255** (8 bits per section).

Total structure:

8 bits + 8 bits + 8 bits + 8 bits = **32 bits**

An IPv4 address has two main parts:

- **Network portion** – identifies which network the device belongs to
- **Host portion** – identifies the specific device within that network

The boundary between these two parts is determined by the **Subnet Mask or CIDR notation**.

---

# 2. What is CIDR?

CIDR stands for **Classless Inter-Domain Routing**.

Originally, IP addresses were divided into fixed classes (Class A, B, and C).  
However, this approach wasted many IP addresses.

CIDR was introduced to allow networks to be divided more flexibly and efficiently.

In simple terms:

CIDR specifies **how many bits of the IP address belong to the network portion**.

---

## CIDR Notation

CIDR uses a slash followed by a number.

Examples:

192.168.1.10/24  
10.0.5.20/16

The number after the slash indicates how many bits represent the **network portion**.

Example:

/24 means:

- First **24 bits = network**
- Remaining **8 bits = hosts**

---

## Why CIDR is Important

CIDR helps with three main things:

1. **Reduces IP address waste**  
   Networks can be allocated based on actual size requirements.

2. **Improves routing efficiency**  
   Large blocks of IP addresses can be summarized.

3. **Simplifies subnetting**  
   Network sizes can be easily expressed.

---

## Understanding CIDR Quickly

IPv4 addresses have **32 bits total**.

Host bits are calculated as:

Host bits = 32 − CIDR value

Example:

/24  
Host bits = 8

Possible addresses:

2^8 = 256

Usable hosts:

256 − 2 = **254**

(The two reserved addresses are the Network Address and Broadcast Address.)

---

## Example CIDR Sizes

/24 → 256 total addresses → 254 usable hosts  
/26 → 64 total addresses → 62 usable hosts  
/27 → 32 total addresses → 30 usable hosts

---

## Block Size Concept

CIDR also determines the **block size** of the network.

Common increments:

/24 → increments of 256  
/25 → increments of 128  
/26 → increments of 64  
/27 → increments of 32

Example:

192.168.1.130/26

/26 networks increase by **64**.

Possible ranges:

192.168.1.0  
192.168.1.64  
192.168.1.128  
192.168.1.192

Since 130 falls in the **128–191 range**:

Network address:

192.168.1.128

Broadcast address:

192.168.1.191

Usable hosts:

192.168.1.129 – 192.168.1.190

---

# 3. Subnet Mask and CIDR

A **Subnet Mask** is simply another way to represent CIDR.

Common mappings:

/24 = 255.255.255.0  
/16 = 255.255.0.0  
/8 = 255.0.0.0  
/26 = 255.255.255.192

Example:

255.255.255.192 in binary:

11111111.11111111.11111111.11000000

The first 26 bits represent the network.

---

# 4. Network Address, Broadcast Address, and Host Range

Example:

192.168.1.10/24

Network address:

192.168.1.0

Broadcast address:

192.168.1.255

Usable host range:

192.168.1.1 – 192.168.1.254

The network and broadcast addresses cannot be assigned to devices.

Therefore:

256 total addresses  
254 usable hosts

---

# 5. Public IP vs Private IP

## Public IP

A Public IP address is globally unique and assigned by an Internet Service Provider (ISP).

These addresses are reachable from the internet.

---

## Private IP

Private IP addresses are used inside local networks and are not directly accessible from the internet.

Common private ranges:

10.0.0.0/8

172.16.0.0 – 172.31.255.255 (/12)

192.168.0.0/16

When devices access the internet, routers typically use **NAT (Network Address Translation)** to convert private IP addresses into a public IP.

---

# 6. DHCP vs Static IP

## DHCP (Dynamic Host Configuration Protocol)

DHCP automatically assigns IP addresses to devices.

Advantages:

- Easy to manage
- No manual configuration required

Most home networks use DHCP.

---

## Static IP

A Static IP address is manually configured and does not change.

Static IPs are commonly used for:

- Servers
- Printers
- Network infrastructure devices

---

# 7. Default Gateway

The **Default Gateway** is the device that allows communication with other networks.

It acts as the **exit point** from a local network.

Example:

In many home networks:

Gateway = 192.168.1.1

If the gateway is incorrect:

Devices may communicate locally but **cannot access the internet**.

---

# 8. DNS (Domain Name System)

DNS converts **domain names into IP addresses**.

Example:

www.google.com → IP address

Without DNS, users would have to remember IP addresses instead of domain names.

If DNS fails:

- Ping to an IP may work (ping 8.8.8.8)
- Domain names may fail (ping google.com)

---

# 9. Common Special IPv4 Addresses

127.0.0.1

Loopback address (the local machine itself)

0.0.0.0

Represents an unspecified or default address

169.254.x.x

APIPA (Automatic Private IP Addressing)

This occurs when DHCP fails.

8.8.8.8 / 1.1.1.1

Well-known public DNS servers (Google and Cloudflare)

---

# 10. Determining if Devices Are on the Same Network

Devices are on the same network if the **network portion of their IP address is the same**.

Example:

192.168.1.10/24  
192.168.1.200/24

These are in the same network.

However:

192.168.1.10/24  
192.168.2.10/24

These are in different networks and require routing through a gateway.

---

# 11. IPv6 Basics

IPv6 was introduced to solve IPv4 address exhaustion.

IPv6 addresses are **128 bits long**.

Example:

2001:db8:abcd:0012::1

Key points:

- Written in hexadecimal
- Uses colons (:)
- :: represents compressed zeros

Common IPv6 subnet size:

/64

Example local address range:

fe80::/10 (link-local addresses)

---

# 12. Basic Network Troubleshooting Checklist

When a network problem occurs, check the following:

1. Verify the device has a valid IP address
2. Check the Subnet Mask or CIDR
3. Confirm the Default Gateway
4. Verify DNS configuration

Basic connectivity tests:

ping 127.0.0.1  
ping your own IP  
ping the gateway  
ping 8.8.8.8  
ping google.com

---

# 13. Summary

- An IP address identifies a device on a network
- CIDR defines how many bits represent the network portion
- Subnet masks represent CIDR in dotted decimal form
- A gateway connects networks together
- DNS converts domain names to IP addresses
- DHCP automatically assigns IP addresses
