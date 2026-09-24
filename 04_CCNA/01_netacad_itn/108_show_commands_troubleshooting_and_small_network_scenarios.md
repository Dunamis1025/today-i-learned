# 108. Show Commands, Troubleshooting Methodology, and Small Network Scenarios

Source: CCNA Module 17 (Build a Small Network) — sections 17.5–17.8

## 1. Common `show` Commands Revisited

| Command | Useful for... |
|---|---|
| `show running-config` | Verify current configuration and settings |
| `show interfaces` | Verify interface status and check for error messages |
| `show ip interface` | Verify Layer 3 information of an interface |
| `show arp` | Verify the list of known hosts on local Ethernet LANs |
| `show ip route` | Verify Layer 3 routing information |
| `show protocols` | Verify which protocols are operational |
| `show version` | Verify memory, interfaces, and licenses of the device |
| `show ip interface brief` | Quick summary of all interfaces: IP address, status, protocol (no prefix info) |
| `show cdp neighbors` | Show directly connected Cisco devices only (not multi-hop) |
| `show cdp neighbors detail` | Same as above but with more detail (including IP address) — works even without Layer 3 connectivity |
| `show users` | Show who is logged into the device and from where |
| `show flash:` | Show contents/size of flash memory (used before IOS upgrades) |

### Notes on `show version`
- Shows IOS version, image filename, uptime, last reload reason
- Shows licensing info (technology-package vs suite licensing)
- Shows memory breakdown: DRAM (main+shared, volatile), NVRAM (stores startup-config, non-volatile), Flash (stores IOS image, non-volatile)
- Shows the **configuration register** (e.g., `0x2102`) — controls boot behavior; can be changed for password recovery (skip loading startup-config on boot)

### Notes on `show ip interface brief` vs `show interfaces`
- `show ip interface brief` → gives IP address + up/down status, but **no subnet prefix**
- `show interfaces` (and `show ip interface`) → gives full Layer 1/Layer 2 detail including duplex, speed, and **Internet address with prefix** (e.g., `209.165.200.226/27`)
- Use `show interfaces` when troubleshooting **duplex mismatch** (only command that shows duplex/speed)

## 2. CDP (Cisco Discovery Protocol)

- Cisco proprietary, Layer 2, enabled by default on Cisco devices
- Works even without Layer 3 (IP) connectivity
- Only discovers **directly connected** neighbors (one hop only)
- Info revealed: Device ID, Address List, Port ID, Capabilities (router/switch/host), Platform
- Security risk: reveals network topology info to anyone with access — often disabled in production
  - `no cdp run` → disable globally
  - `no cdp enable` (interface config mode) → disable on a specific interface
  - Can be disabled globally OR per-interface (both are valid)

## 3. Troubleshooting Methodology (6 steps)

1. **Identify the problem**
2. **Establish a theory of probable causes**
3. **Test the theory to determine cause**
4. **Establish a plan of action and implement the solution**
5. **Verify full system functionality and implement preventive measures**
6. **Document findings, actions, and outcomes**

### Resolve or Escalate?
- Some fixes require approval outside the technician's authority (e.g., purchasing a replacement switch)
- In that case → **escalate the trouble ticket to a manager**, don't act unilaterally

## 4. `debug` Command

- Displays real-time protocol/process messages for troubleshooting (e.g., `debug ip icmp`)
- **High CPU overhead** — must be turned off when done
  - `no debug ip icmp` → turn off specific debug
  - `undebug all` → turn off all debugging at once
- **Sent to the console line by default**
- Remote (VTY/Telnet/SSH) users will NOT see debug output unless they run:
  - `terminal monitor` — redirects console log messages to their VTY session

## 5. Small Network Troubleshooting Scenarios

| Issue | Symptom | Cause | Verify with |
|---|---|---|---|
| **Duplex mismatch** | Slow performance, errors, collisions | One side manually set to full/half duplex, other side set to auto | `show interfaces` |
| **IP addressing (IOS devices)** | Interface unreachable, wrong IP | Manual IP misconfiguration (typo) since IOS devices are usually manually configured | `show ip interface brief` |
| **IP addressing (end devices / APIPA)** | Device can't reach anything outside local segment | DHCP process failed → Windows auto-assigns a `169.254.x.x` address (APIPA) | `ipconfig` |
| **Default gateway issues** | Local network works, but can't reach outside networks | Missing/incorrect gateway address | `ipconfig`, `show ip route` (check "Gateway of last resort") |
| **DNS issues** | Can reach a site by IP but not by domain name | Incorrect DNS server address (often a manual misconfiguration overriding DHCP) | `ipconfig /all`, `nslookup` |

## 6. Quiz/Exam Concepts Reinforced

- **Redundancy** matters more to large corporations (failure = bigger impact); **cost** and **modularity** (expandability) matter more to small businesses with growth forecasts.
- **QoS (Quality of Service)** — mechanism used to prioritize delay-sensitive traffic (Voice, Video) over less time-sensitive traffic (Email, FTP, Web).
- **Network baseline** should be established **at regular intervals over time**, not during traffic spikes/drops — a baseline needs to represent "normal" behavior.
- **Network documentation** = physical + logical topology records.
- True redundancy against a full router failure requires a **second physical router** (activating another interface on the same router does not help if the router itself fails).
- Windows uses `tracert`, not `traceroute` (Linux/macOS) — command names differ by OS.

## Key Takeaway

`show` commands map to specific troubleshooting questions:
- **"Is it up?"** → `show ip interface brief`, `show interfaces`, `show protocols`
- **"What's the IOS/hardware info?"** → `show version`
- **"What's connected to me physically?"** → `show cdp neighbors`
- **"What's my routing table?"** → `show ip route`
- **"Who's logged in?"** → `show users`
- **"What's happening right now?"** → `debug` (turn off when done!)
