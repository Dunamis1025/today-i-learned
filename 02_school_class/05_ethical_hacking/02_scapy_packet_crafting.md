# Lab 02: Packet Crafting with Scapy

## Overview
Hands-on practice building and sending custom network packets layer-by-layer using Scapy — a powerful Python-based packet manipulation tool.

## Key Concepts

### What is a Packet?
A packet is a unit of data transmitted over a network. It is built in layers, each serving a different purpose:

```
Ethernet  →  physical delivery (which device on the local network)
  └── IP  →  addressing (where to send it)
        └── TCP/ICMP  →  delivery method (which port / what type)
                  └── Data  →  the actual content
```

### What is Scapy?
Scapy is a Python-based tool that allows you to craft, send, receive, and analyse network packets manually — field by field, layer by layer. This is useful for understanding how protocols work under the hood and for testing network security.

### TTL (Time To Live)
- A field in the IP header that limits how many routers a packet can pass through
- Each router decrements it by 1; when it reaches 0, the packet is discarded
- Prevents packets from looping endlessly on a network
- **Can be used to fingerprint the target OS:**
  - TTL ≈ 64 → Linux / macOS
  - TTL ≈ 128 → Windows
  - TTL ≈ 255 → Network devices
- Note: TTL can be spoofed, so it is a clue, not a guarantee

### What is RFC?
RFC (Request for Comments) documents are the official standards that define how internet protocols work. For example, RFC 791 defines the IP protocol, including that the default TTL is 64.

## Lab Environment
| Machine | IP | Role |
|---------|-----|------|
| Kali Linux | 192.168.9.2 | Attacker |
| pfSense | 192.168.9.1 | Firewall / Gateway |
| OWASP BWA | 192.168.68.12 | Vulnerable web server (target) |

## Task 1: Creating Packets with Scapy

```python
# Launch Scapy
scapy

# List all supported protocols
ls()

# List all available commands
lsc()

# Create an IP packet with TTL set to 10
ip = IP(ttl=10)

# Inspect the packet
ip

# Check default destination
ip.dst       # '127.0.0.1' (loopback by default)

# Set destination IP
ip.dst = "192.168.9.1"

# Set source IP
ip.src = "192.168.9.2"

# Remove TTL (resets to RFC default of 64)
del(ip.ttl)
ip.ttl       # → 64

# Stack TCP on top of IP
ip/TCP()

# Configure TCP ports
tcp = TCP(sport=1025, dport=80)

# Display the full packet stack
(tcp/ip).show()

# Add Ethernet layer
Ether()/ip
```

## Task 2: Sending Crafted Packets

```python
# Send an ICMP packet (ping) to the target and capture the response
packet = sr1(IP(dst="192.168.68.12")/ICMP()/"XXXXXXXXXXX")
# Output: Received 2 packets, got 1 answers — target responded

# Perform a SYN scan on port 80
packet = sr1(IP(dst="192.168.68.12")/TCP(dport=80, flags="S"))
# Output: SYN-ACK received — port 80 is open
```

### What is sr1?
`sr1` = Send and Receive 1 packet. It sends a packet and returns only the first response.

### What is a SYN Scan?
- Sends a TCP SYN packet (connection request) to a target port
- If the port is **open**: target replies with SYN-ACK
- If the port is **closed**: target replies with RST
- This is the same technique used internally by port scanners like `nmap`

### Wireshark
Used alongside Scapy to visually confirm packets were sent and received. The green-highlighted SYN-ACK packet confirmed that port 80 on the OWASP target was open.

## Takeaways
- Network packets are structured in layers — each layer has a specific role
- Scapy allows full manual control over every field in a packet
- TTL, source IP, and flags can all be manipulated — useful for evasion or testing
- A SYN scan is a lightweight way to check if a port is open without completing the full TCP handshake
- Tools like `nmap` perform these same operations automatically under the hood
