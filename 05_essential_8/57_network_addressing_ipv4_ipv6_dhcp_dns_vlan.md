# Network Addressing Concepts — Study Notes

---

## 1. MAC Address vs. IP Address

| Feature | MAC Address | IP Address |
|---|---|---|
| Also known as | Physical Address | Logical Address |
| Analogy | Fingerprint / Social Security Number | Mailing Address |
| Changes when moving networks? | ❌ No — permanently fixed | ✅ Yes — changes per network |
| Example | `0050.56BE.D787` | `192.168.200.8` |

- **MAC Address**: Burned into the Network Interface Card (NIC). Globally unique. Used for local delivery on the same network segment.
- **IP Address**: Assigned logically. Used for routing data across networks.

---

## 2. IPv4

- **Format**: 32-bit address, written as 4 octets separated by dots (e.g., `192.168.200.8`)
- **Address Space**: ~4.3 billion addresses
- **Problem**: Address exhaustion — not enough addresses for all modern devices

### IPv4 Address Structure
Every IPv4 address has two parts:
- **Network Portion** — identifies which network the device belongs to
- **Host Portion** — identifies the specific device within that network

---

## 3. Subnet Mask

- Helps a device determine whether a destination is on the **same local network** or an **external network**
- When sending data:
  - **Same network** → deliver directly (no router needed)
  - **Different network** → send to the **Default Gateway** (router) for forwarding
- Acts as a "sorting tool" for efficient communication

---

## 4. IPv6

- **Format**: 128-bit address, written in hexadecimal, separated by colons (e.g., `2001:db8:1111::d787`)
- **Address Space**: Virtually unlimited
- **Purpose**: Solves IPv4 address exhaustion

### Shortening Rules

| Rule | Description | Example |
|---|---|---|
| Rule 1: Omit leading zeros | Drop leading zeros in any 16-bit segment | `0db8` → `db8`, `0001` → `1` |
| Rule 2: Replace consecutive all-zero segments with `::` | Can only be used **once** per address | `0000:0000:0000` → `::` |

---

## 5. IP Address Assignment

### Static Addressing
- Administrator **manually** assigns a fixed IP to each device
- Required settings:
  - IP Address
  - Subnet Mask
  - Default Gateway
  - DNS Server
- ✅ Predictable and consistent
- ❌ Tedious to manage at scale

### Dynamic Addressing (DHCP)
- A **DHCP server** automatically assigns IP settings when a device connects
- Default for most home computers and smartphones
- ✅ No manual input needed; prevents duplicate IP errors

---

## 6. DHCP — The 4-Step Process (DORA)

| Step | Who Acts | Message |
|---|---|---|
| **D**iscover | Client → Network | "Is there a DHCP server?" |
| **O**ffer | Server → Client | "I can offer you this IP." |
| **R**equest | Client → Server | "I'll take that IP, please." |
| **A**cknowledgement | Server → Client | "Confirmed. It's yours." |

- **Lease**: IP addresses are temporarily "leased," not permanently assigned
- **Renewal**: Clients periodically re-contact the server to keep the lease
- **Reservation**: Administrators can pre-assign a fixed IP to a specific device (e.g., servers, printers) based on its MAC address

---

## 7. DNS — Domain Name System

Acts as the **"phonebook of the internet"** — translates domain names (e.g., `google.com`) into IP addresses.

### Key DNS Record Types

| Record | Purpose |
|---|---|
| **A** | Maps domain → IPv4 address |
| **AAAA** | Maps domain → IPv6 address |
| **MX** | Specifies the mail server for a domain |
| **TXT** | Stores additional text-based info about a host |

### Email Security (Anti-Spam)

| Protocol | Role |
|---|---|
| **SPF** | Lists servers authorized to send email for a domain; blocks spoofing |
| **DKIM** | Adds a digital signature to verify email authenticity |
| **DMARC** | Policy that defines how to handle emails failing SPF/DKIM checks |

---

## 8. VLAN — Virtual LAN

- Logically segments a physical network into **separate virtual networks**
- Devices in the same VLAN communicate as if on the same switch, even if physically separate
- ✅ Reduces unnecessary broadcast traffic
- ✅ Enables per-group security and access policies
- ❌ Devices in **different VLANs cannot communicate directly** — a **router** is required

**Example**: One switch, three logical networks:
- VLAN 10 → Faculty
- VLAN 30 → Students
- VLAN 50 → Guests

---

## 9. Link-Local Addresses

Addresses used only for communication between devices on the **same direct network segment** — no routing to external networks.

| | IPv4 Link-Local (APIPA) | IPv6 Link-Local |
|---|---|---|
| Range | `169.254.0.0 – 169.254.255.255` | `fe80::/10` |
| When assigned | Automatically, when DHCP fails | **Always** — mandatory on every IPv6 device |
| Use case | Fallback / temporary | Essential for network discovery & routing protocols |

---

## 10. Quick Reference — Concept Matching

| Concept | Category |
|---|---|
| Analogous to a fingerprint | MAC Address |
| Does not change between networks | MAC Address |
| `0050.56BE.D787` | MAC Address |
| Analogous to a mailing address | IP Address |
| Changes between networks | IP Address |
| `192.168.200.8` | IPv4 Address |
| 32-bit, dotted-decimal format | IPv4 Address |
| Auto-assigned when DHCP fails | IPv4 Link-Local (APIPA) |
| `2001:db8:1111::d787` | IPv6 Address |
| 128-bit, hexadecimal format | IPv6 Address |
| Required on all IPv6 devices | IPv6 Link-Local |
| Automatically assigns IP settings | DHCP |
| Identifies the network a device belongs to | Subnet Mask |
| Exit point to reach the internet | Default Gateway |
| Manually assigned by an admin | Static Addressing |
