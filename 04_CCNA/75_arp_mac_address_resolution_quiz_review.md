# ARP & MAC Address Resolution — Study Notes

## Core Concept

Sending data across a network requires two addresses:

- **IP address** — used for end-to-end routing across networks
- **MAC address** — used to identify hardware on the same local link

Every time data moves across a network segment, these two addresses must be mapped to one another so the frame reaches the correct physical device.

### ARP (IPv4)

- **ARP (Address Resolution Protocol)** resolves a known IPv4 address to an unknown MAC address.
- Works by **broadcasting** a request to every device on the local network, asking "who has this IP address?"
- Downsides: broadcast traffic can degrade network performance, and it is vulnerable to **ARP spoofing/poisoning** attacks (used in man-in-the-middle attacks).

### Neighbor Discovery (IPv6)

- IPv6 replaces ARP with **ND (Neighbor Discovery)**, built on **ICMPv6**.
- More efficient than ARP — avoids blind broadcasting; used to resolve addresses, discover routers, and manage traffic.
- Two key ICMPv6 messages:
  - **Neighbor Solicitation (NS)** — "What is your MAC address?"
  - **Neighbor Advertisement (NA)** — response containing the MAC address

---

## Key Terms

| Term | Meaning |
|---|---|
| **Resolving** | The process of looking up one identifier to find its paired identifier (e.g., IP → MAC, domain name → IP). Same concept as DNS resolution. |
| **ARP table / ARP cache** | A local "phonebook" mapping IPv4 addresses to MAC addresses, stored in a device's memory. |
| **Broadcast address** | `255.255.255.255`-style local broadcast (e.g. `192.168.1.255` on a /24 network) — reaches every device on the segment. |
| **Broadcast MAC address** | `FF-FF-FF-FF-FF-FF` (or `FFFF.FFFF.FFFF`) — the hardware-level "everyone" address. |
| **Network interface** | The physical or logical "doorway" through which a device connects to a network (e.g., `en0`, `eth0`, `wlan0`, `lo`). A device can have multiple interfaces (Wi-Fi, Ethernet, loopback), each potentially showing different ARP mappings. |
| **BSD-style output** | Sentence-style command output format used by Unix-family OSes (macOS, Linux, BSD) — e.g. `host (IP) at MAC on interface`. Uses colons in MAC addresses. Contrasts with Windows' table-style output, which uses hyphens. |

### `arp -a` command

- `-a` = "all" — displays **all** entries currently in the local ARP cache.
- Used to check what MAC address a host currently associates with a given IP (e.g., the default gateway), which is critical for **detecting ARP spoofing / MITM attacks**.
- **Windows format** (table): `192.168.1.1   aa-bb-cc-dd-ee-ff   dynamic`
- **BSD/macOS/Linux format** (sentence): `gateway.local (192.168.1.1) at aa:bb:cc:dd:ee:ff on en0 [ethernet]`

---

## Quiz Q&A Summary

| # | Question (short) | Answer |
|---|---|---|
| 1 | Router component storing routing table, ARP cache, running-config | **RAM** (volatile, cleared on reboot) |
| 2 | What info is in an ARP table? | **IPv4-to-MAC address mappings** |
| 3 | `arp -a` shows `192.168.1.255 ff-ff-ff-ff-ff-ff` — what is this entry? | **Static mapping** (broadcast IP + broadcast MAC, fixed permanently) |
| 4 | Command to check MAC address used to reach default gateway (suspected MITM/spoofing) | **`arp -a`** |
| 5 | Layer 2 switch receives a frame whose destination MAC isn't in the MAC table — what does it do? | **Floods the frame out all ports except the one it arrived on** |
| 6 | Two ICMPv6 messages used in Ethernet MAC address resolution | **Neighbor Solicitation** and **Neighbor Advertisement** |
| 7 | How does ARP use an IPv4 address? | To **determine the MAC address of a device on the same network** |
| 8 | One function of ARP | **Resolving an IPv4 address to a MAC address** |
| 9 | Switch receives a Layer 2 broadcast frame — action taken? | **Sends frame out all ports except the one it was received on** |
| 10 | What addresses does ARP map? | **IPv4 address → destination MAC address** |
| 11 | ARP info provided when packet goes to a remote-network host | **MAC address of the router interface closest to the sending host** (default gateway) |
| 12 | Two address types mapped in a switch's ARP table | **Layer 3 address (IP) ↔ Layer 2 address (MAC)** |
| 13 | Purpose of ARP in an IPv4 network | **To obtain a MAC address when the IP address is already known** |
| 14 | Destination address used in an ARP request frame | **FFFF.FFFF.FFFF** (broadcast) |

---

## Big Picture Takeaway

ARP is fundamentally a **lookup/translation mechanism**: it bridges Layer 3 (IP) and Layer 2 (MAC) so frames can be delivered correctly on a local network. Because it trusts broadcast replies without built-in authentication, it's a common attack surface (ARP spoofing/poisoning) — which is exactly why security analysts check the ARP cache (`arp -a`) to verify that the MAC address bound to the default gateway's IP hasn't been tampered with.
