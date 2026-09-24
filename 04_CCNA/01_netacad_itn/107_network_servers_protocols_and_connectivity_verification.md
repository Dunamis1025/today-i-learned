# 107. Network Servers, Protocols, Network Scaling, and Connectivity Verification

> Module 17: Build a Small Network — Sections 17.2 (Small Network Applications and Protocols), 17.3 (Scale to Larger Networks), 17.4 (Verify Connectivity)

---

## 17.2.2 Common Protocols

Network administrators commonly need remote access to devices and servers. The two most common remote access solutions are:

- **Telnet** — sends data in plain text (unencrypted), insecure
- **SSH (Secure Shell)** — the secure, encrypted replacement for Telnet; recommended for production use

For SSH to work:
- **Network device** (router, switch, AP, etc.) must support SSH server
- **Server** (web/email server, etc.) must support SSH server for remote administration

### Common Network Servers and Their Protocols

| Server | Protocol(s) | Purpose |
|---|---|---|
| **Web Server** | HTTP / HTTPS | Serves web content. HTTPS is the secure version. |
| **Email Server** | SMTP (send), POP3/IMAP (retrieve) | Addresses use `user@xyz.xxx` format |
| **FTP Server** | FTP / FTPS / SFTP | File upload/download; FTPS and SFTP are secure alternatives |
| **DHCP Server** | DHCP | Automatically assigns IP config (IP address, subnet mask, default gateway) to clients |
| **DNS Server** | DNS | Resolves domain names (e.g., cisco.com) to IP addresses (e.g., 72.163.4.185) |

**Note:** A single server can host multiple services simultaneously (e.g., one server can be an email, FTP, and SSH server at once).

Network protocols define:
- Processes on either end of a communication session
- Types and syntax of messages
- Meaning of informational fields
- How messages are sent and the expected response
- Interaction with the next lower layer

Best practice: use secure protocol versions (SSH, SFTP, HTTPS) whenever possible.

---

## 17.2.3 Voice and Video Applications

Businesses increasingly rely on IP telephony and streaming media, especially with remote work. Network admins must ensure proper equipment and configuration for **priority delivery** of real-time traffic.

### Key Factors

1. **Infrastructure**
   - Network must support real-time applications
   - Existing cabling/devices must be tested and validated
   - Newer equipment may be required

2. **VoIP (Voice over IP)**
   - Converts analog telephone signals into digital IP packets
   - Generally cheaper than IP telephony, but lower quality
   - Small networks can use Skype or non-enterprise Cisco WebEx

3. **IP Telephony**
   - Uses dedicated IP phones that perform voice-to-IP conversion themselves
   - Requires a dedicated server for call control and signaling
   - Example: Cisco Business Edition 4000 Series

4. **Real-Time Applications**
   - Require **QoS (Quality of Service)** to minimize latency
   - **RTP (Real-Time Transport Protocol)** — delivers audio/video data
   - **RTCP (Real-Time Transport Control Protocol)** — monitors and reports delivery quality

---

## 17.3.1 Small Network Growth

As a business grows, the network must scale accordingly. Proper planning requires documenting the current network state:

1. **Network documentation** — physical and logical topology
2. **Device inventory** — list of devices and their capabilities
3. **Traffic analysis** — protocols, applications, services in use and their requirements

These elements form the baseline for planning growth (along with **budget** considerations).

---

## 17.3.2 Protocol Analysis

To manage growing traffic, admins must understand current traffic flow using a **protocol analyzer** (e.g., **Wireshark**).

- Capture traffic during **peak usage** to determine how much bandwidth each application uses
- Compare traffic patterns across different departments/functions
- Use findings to anticipate performance issues and tune the network as traffic patterns evolve

---

## 17.3.3 Employee Network Utilization

Modern employee traffic patterns are increasingly diverse. Admins should monitor:

- CPU and disk utilization
- Wired/wireless network utilization
- Network application usage

**Example:** Windows 10's built-in **Data Usage** tool (Settings → Network & Internet → Data usage) shows how much data each app has consumed over the last 30 days — useful for identifying bandwidth-heavy applications.

---

## 17.4.1 Verify Connectivity with Ping

**Ping** uses ICMP Echo Request/Reply messages to verify Layer 3 connectivity between two devices.

- Available on nearly all OSes: Windows, Linux, macOS, Cisco IOS
- Syntax: `ping [destination IP]`

### Ping Result Interpretation

| Result | Meaning |
|---|---|
| Successful reply | Layer 3 connectivity confirmed |
| Partial replies (dots) | Possible firewall blocking ICMP or routing issue |
| Request timed out | Delay or failure somewhere along the path |
| Destination unreachable | Routing problem — no path exists |

---

## 17.4.2 Extended Ping

A standard ping automatically uses the **interface closest to the destination** as the source IP. This can be a problem when you want to verify connectivity **from a specific source network** (e.g., a LAN behind the router).

**Extended Ping** (Cisco IOS) lets you manually configure the source address:

```
R1# ping
Protocol [ip]:
Target IP address: 10.1.1.10
Repeat count [5]:
Datagram size [100]:
Timeout in seconds [2]:
Extended commands [n]: y
Source address or interface: 192.168.10.1
...
Success rate is 100 percent (5/5)
```

Enter extended mode by typing `ping` with **no destination IP** in privileged EXEC mode.
Note: `ping ipv6` is used for IPv6 extended pings.

---

## 17.4.3 Verify Connectivity with Traceroute

**Ping** only tells you if a connection works — not **where** a problem is. **Traceroute** shows every hop along the path to a destination, helping pinpoint failure locations.

| OS | Command |
|---|---|
| Windows | `tracert` |
| Cisco IOS | `traceroute` |

### Example: Windows tracert (failure case)
```
C:\> tracert 10.1.1.10
1  2ms  2ms  2ms  192.168.10.1
2  *    *    *    Request timed out.
3  *    *    *    Request timed out.
```
→ Hop 1 (R1) responds fine; failure occurs beyond R1.

### Example: Cisco IOS traceroute (success case)
```
R1# traceroute 10.1.1.10
1  209.165.200.226  1msec  0msec  1msec
2  209.165.200.230  1msec  0msec  1msec
3  10.1.1.10  1msec  0msec
```
→ All hops respond — destination reached successfully.

**Technical note:**
- Windows/Linux tracert uses **ICMP Echo Requests**
- Cisco IOS traceroute uses **UDP** with an invalid port number, triggering a "port unreachable" ICMP message from the destination

Interrupt commands: `Ctrl+C` (Windows), `Ctrl+Shift+6` (Cisco IOS)

---

## 17.4.4 Extended Traceroute

Like Extended Ping, Cisco IOS's **Extended Traceroute** allows specifying a custom **source address**, enabling testing from a specific network's perspective (e.g., a LAN behind the router) rather than the router's default outgoing interface.

```
R1# traceroute
Protocol [ip]:
Target IP address: 10.1.1.10
Source address: 192.168.10.1
...
1  209.165.200.226  1msec  1msec  1msec
2  209.165.200.230  1msec  0msec  1msec
3  10.1.1.10  1msec  1msec
```

---

## 17.4.5 Network Baseline

A **baseline** establishes what "normal" network performance looks like, enabling later comparison to detect anomalies.

### How to Build One
- Run **ping** repeatedly over an extended time period (multiple days/times of day)
- Record round-trip times and packet loss for the same destination

### Example
```
Aug 19: Sent=4, Received=4, Loss=0%, RTT Min/Max/Avg = 1/1/1 ms
Sep 18: Sent=4, Received=4, Loss=0%, RTT Min/Max/Avg = 1/1/1 ms
```
Consistent results across dates confirm network stability. Sudden deviations (higher latency, packet loss) from baseline indicate a developing problem. Companies typically automate baseline data collection with dedicated monitoring software.

---

## Lab: Test Network Latency with Ping and Traceroute

**Objective:** Measure and document real-world network latency/geographic relationship using `ping` and `tracert` against Regional Internet Registry (RIR) websites.

### Part 1 — Ping
```
ping -n 25 www.lacnic.net > lacnic.txt
ping -n 25 www.afrinic.net > afrinic.txt
ping -n 25 www.apnic.net > apnic.txt
```
- `-n 25` sends 25 echo requests
- `>` redirects output to a file (overwrites); `>>` appends
- View saved results with `more filename.txt`

### Part 2 — Traceroute
```
tracert www.lacnic.net > traceroute_lacnic.txt
tracert www.afrinic.net > traceroute_afrinic.txt
tracert www.apnic.net > traceroute_apnic.txt
```

### Part 3 — Extended Traceroute (`-d` option)
```
tracert -d www.lacnic.net > traceroute_d_lacnic.txt
```
`-d` skips reverse DNS lookup (no hostname resolution), producing faster results showing raw IP addresses only instead of domain names.

### Lab Results Summary (example run)

| Destination | Region | Hops | Avg RTT |
|---|---|---|---|
| www.apnic.net | Asia-Pacific | 6 | ~6 ms |
| www.lacnic.net | South America | 23 | ~352 ms |
| www.afrinic.net | Africa | 17 | ~450 ms |

**Conclusion:** Geographic distance strongly correlates with both hop count and round-trip latency — closer destinations (Asia-Pacific) show dramatically lower latency than distant ones (South America, Africa), which require crossing intercontinental submarine cable routes. `Request timed out.` entries mid-trace typically indicate routers configured not to respond to ICMP, not necessarily a network fault.

**Reflection:**
1. An accurate baseline requires repeated measurements across multiple days and times of day, not a single test.
2. Baseline data is used later to quickly distinguish "normal" fluctuation from a genuine emerging problem by comparison.
