# Networking Fundamentals — Study Notes

> Topics: IP Addressing, DNS, DHCP, Network Troubleshooting, Wireless Security, IPv6

---

## 1. Key Commands for Network Troubleshooting

| Command | Purpose |
|---|---|
| `nslookup` | Troubleshoot DNS resolution (domain name → IP address) |
| `tracert` | Trace the route (hops) packets take to a destination |
| `arp -a` | Display ARP cache (IP ↔ MAC address mappings) |
| `ping` | Test connectivity between hosts using **ICMP** |
| `ipconfig /all` | View full IP configuration including gateway, subnet mask, DHCP status |
| `ipconfig /release` | Release the current IP address |
| `ipconfig /renew` | Request a new IP address from the DHCP server |

---

## 2. IP Address Concepts

### APIPA (Automatic Private IP Addressing)
- Address range: **169.254.0.0/16**
- Assigned automatically by the OS when a DHCP server is **unreachable**
- Indicates a network configuration problem
- Cannot communicate outside the local network
- Fix: `ipconfig /release` → `ipconfig /renew`

### Default Gateway
- Required to route traffic **outside** the local network (to the Internet)
- If a device can reach local devices (e.g., a printer) but **not** the Internet → gateway is likely misconfigured or missing

### Static vs. Dynamic IP
- Using a static IP is not inherently a problem — as long as the gateway and subnet mask are correctly configured

---

## 3. Core Protocols

| Protocol | Role |
|---|---|
| **DHCP** | Dynamically assigns IP addresses to devices on a network |
| **DNS** | Translates domain names (e.g., google.com) into IP addresses |
| **ICMP** | Used by `ping` — sends Echo Request / Echo Reply to test connectivity |
| **TCP** | Reliable, ordered data transmission protocol |
| **ARP** | Maps IP addresses to MAC (hardware) addresses on a local network |
| **RARP** | Obsolete; reverse of ARP — used a MAC address to request an IP |

---

## 4. DNS Troubleshooting

**Symptom:** Can access a server by IP address, but **not** by domain name.

**Conclusion:** The server and network are fine. The problem is in DNS.

**Two possible causes:**
1. DNS server address is misconfigured on the workstation
2. The web server record is incorrectly registered on the DNS server

**Not the cause:** misconfigured gateway, downed network connection — these would block IP access too.

---

## 5. DHCP Troubleshooting

- If the DHCP server is down → devices self-assign **APIPA** addresses (169.254.x.x)
- If a device receives an APIPA address, check: physical connection, DHCP server status
- When using `ipconfig /all` to verify DHCP is working, confirm:
  - **Default Gateway** is present and correct
  - **Subnet Mask** is present and correct

---

## 6. Port Forwarding vs. Port Triggering

| Feature | Port Forwarding | Port Triggering |
|---|---|---|
| Direction | Always-on, inbound | Temporary; opens only after outbound traffic |
| Use case | Hosting a server accessible from the Internet | Online gaming, certain apps |
| For web servers | ✅ Yes | ❌ No |

**Port forwarding** is the correct method to allow external users to access a server inside a private network without expensive DMZ hardware.

---

## 7. Network Security Concepts

### MAC Address Filtering
- Allows or blocks devices based on their unique **hardware (MAC) address**
- Set on the router; not IP-based

### Whitelisting vs. Blacklisting
| Method | Logic |
|---|---|
| **Whitelisting** | Only listed IP addresses are **allowed** |
| **Blacklisting** | Only listed IP addresses are **blocked** |

### Default Router Settings That Are Security Risks
1. **Well-known default admin password** (e.g., admin/admin) — easily guessed
2. **WEP encryption enabled** — outdated and highly vulnerable; should use WPA2 or WPA3

### WEP vs. WPA2
- **WEP**: obsolete, easily cracked
- **WPA2**: current standard for wireless encryption

---

## 8. Wireless Channel Selection

- Use channels **1, 6, or 11** on the 2.4GHz band
- These three channels are **non-overlapping**, minimizing interference from neighboring routers
- Other channels overlap and cause signal degradation

---

## 9. IPv6 Basics

### Address Structure
- 128-bit address, written in 8 groups of 16 bits, separated by colons
- Example: `2001:0db8:cafe:4500:1000:00d8:0058:00ab/64`

### Prefix Length
- `/64` means the first 64 bits (first 4 groups) = **Network Identifier**
- The remaining 64 bits = **Host Identifier**

### IPv6 Address Compression Rules
| Rule | Description | Example |
|---|---|---|
| **Leading zero omission** | Remove leading zeros in each segment | `0db8` → `db8` |
| **Double colon (::)** | Replace one contiguous block of all-zero segments | `0000:0000` → `::` |
| **:: can only be used once** | Using it twice is invalid | `2001:db8::835::aa0` ❌ |

**Example compression:**
```
Full:       2001:0db8:cafe:0000:0835:0000:0000:0aa0/80
Compressed: 2001:db8:cafe:0:835::aa0/80
```

---

## 10. Driver Updates

- Best source for NIC drivers: **manufacturer's official website**
- Provides the most current, device-specific, stable drivers
- Avoid: Windows Update (may be outdated/generic), installation media (likely old)

---

## 11. Default Router IP Address

- `192.168.0.1` is a common **factory default** admin IP for routers
- If a router shows this, it likely hasn't had its settings changed from out-of-the-box defaults

---

## 12. NetBIOS

- A **legacy** Windows network protocol from the 1980s
- Obsolete and insecure by modern standards
- Recommended to **disable** on modern networks
- NetBT (NetBIOS over TCP/IP) is an extension that adapted it for TCP/IP — not a replacement for TCP/IP itself

---

## 13. Troubleshooting Methodology

Standard steps (CompTIA A+ framework):

1. Identify the problem (talk to the user)
2. **Establish a theory of probable cause** ← *"I think the IP address is invalid"*
3. Test the theory
4. Establish a plan of action
5. Implement the solution
6. Verify full functionality
7. Document findings

---

## Quick Reference: Common Symptoms → Likely Causes

| Symptom | Likely Cause |
|---|---|
| IP address is 169.254.x.x | DHCP server unreachable (APIPA assigned) |
| Can ping by IP, not by name | DNS misconfiguration |
| Can reach LAN, not Internet | Default gateway missing or wrong |
| Can reach LAN, not Internet | TCP/IP stack issue (if even LAN fails) |
| Router shows 192.168.0.1 | Factory default settings still in use |
| Wireless slow/dropping | Channel interference; switch to 1, 6, or 11 |
