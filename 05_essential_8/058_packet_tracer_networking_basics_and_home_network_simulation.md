# Today's Networking Study Notes

## 1. Network Topology & Physical Setup
- Green triangles on both ends of a cable = correct cable type used
- Straight-through cables connect PCs to switches
- Devices in this lab: PC0, PC1, Switch, Server0, Router (BranchOffice), Cloud (Corporate)

---

## 2. IP Addressing Methods

### DHCP (Dynamic)
- Device automatically receives IP, subnet mask, gateway, and DNS from a DHCP server
- Used for end-user devices (PCs, laptops, phones, tablets)
- Command to verify: `ipconfig /all`

### Static (Manual)
- IP information entered manually — never changes
- Used for servers and network infrastructure that must always be reachable at the same address
- Example config used in lab:

| Field | Value |
|---|---|
| IP Address | 172.16.1.100 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 172.16.1.254 |
| DNS Server | 209.165.200.226 |

---

## 3. Subnetting Basics

For the network `172.16.1.0/24`:

| Address | Role |
|---|---|
| 172.16.1.**0** | Network address — represents the network itself, not assignable |
| 172.16.1.**1–254** | Usable host range |
| 172.16.1.**255** | Broadcast address — sends data to all devices simultaneously, not assignable |

- Default Gateway is conventionally set to `.254` or `.1` to avoid the reserved addresses at both ends
- `172.16.x.x` is a **private IP range**, used inside local networks only

---

## 4. Key Commands

```bash
ipconfig /all       # View full network info: IP, subnet mask, gateway, MAC, DNS
ping [IP/hostname]  # Test connectivity between two devices
ping /?             # Show all available ping options
ping -t [IP]        # Ping continuously until manually stopped (Ctrl+C)
```

---

## 5. Network Interface Cards (NIC)

- **Ethernet NIC** — wired connection via LAN cable
- **Wireless NIC** — connects via Wi-Fi (802.11)
- Most modern devices have both built into the motherboard
- Can be added via **expansion cards** (internal slot) or **USB adapters**

### Driver Management (Windows Device Manager)
- **Update** — install newer driver for performance/compatibility improvements
- **Roll Back** — revert to a previous driver version if a new update causes issues
- Best practices when updating drivers:
  - Temporarily disable antivirus
  - Close all running applications
  - Update one driver at a time

---

## 6. Network Scale & Equipment

| Scale | Equipment |
|---|---|
| Home / Small Office (<10 users) | Single wireless router (handles routing, switching, Wi-Fi, DHCP, firewall) |
| Large Enterprise | Dedicated switches, access points, firewall appliances, high-capacity routers — designed by a network architect |

---

## 7. ICMP & Ping

- **ICMP** is the protocol behind the `ping` command
- Sends a small signal to a target and waits for a reply
- Confirms: reachability, response time (latency), and packet loss
- Windows firewall **blocks incoming ping by default** — must enable "File and Printer Sharing" to allow responses

---

## 8. Real-World Observations (Home Lab)

- Running `ipconfig` on a Windows laptop shows multiple adapters:
  - **Media disconnected** — adapter exists but nothing is connected
  - **VMware Network Adapters (VMnet1, VMnet2, VMnet8)** — virtual adapters created by VMware for internal VM networking
  - **Wi-Fi adapter** — the actual active internet connection
- Successfully pinged an iPad (`192.168.4.60`) from the laptop — confirmed both devices are on the same local network

### Why does an iPad show multiple IPv6 addresses?
- **Privacy / Temporary addresses** — OS rotates addresses periodically to prevent tracking
- **Different scopes** — link-local vs. global vs. ULA addresses serve different routing purposes
- Normal and expected behavior on modern devices

### Is sharing your local IP a security risk?
- **No.** `192.168.x.x` addresses are private IPs — only valid inside your local network
- External attackers cannot directly reach a private IP from the internet
- Your router's public IP is what faces the outside world

---

## 9. Packet Tracer — Simulating a Home Network

- Can replicate a real home network layout in Packet Tracer
- To simulate a wireless laptop:
  1. Replace default wired NIC with **WPC300N** (wireless module) in the Physical tab
  2. Power off → swap module → power on
  3. Set SSID and WPA2 password under Config > Interface > Wireless
  4. Enable DHCP under Desktop > IP Configuration
  5. Verify with `ping` in the Command Prompt

---

## Key Vocabulary

| Term | Meaning |
|---|---|
| DHCP | Protocol that automatically assigns IP addresses |
| Static IP | Manually configured, fixed IP address |
| Subnet Mask | Defines which part of an IP is the network vs. host |
| Default Gateway | Router interface used to reach outside the local network |
| DNS | Translates domain names (e.g. google.com) to IP addresses |
| Broadcast Address | Sends data to all devices on the network simultaneously |
| NIC | Hardware that connects a device to a network |
| Roll Back | Reverting software/drivers to a previous stable version |
| Ping | Tool to test whether two devices can communicate |
| ICMP | Protocol used by ping to send and receive test signals |
| Private IP | IP address only valid within a local network (e.g. 192.168.x.x) |
| MAC Address | Unique physical hardware identifier for a network interface |
