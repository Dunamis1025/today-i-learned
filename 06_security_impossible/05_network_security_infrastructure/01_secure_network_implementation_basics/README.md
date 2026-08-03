# Secure Network Implementation Basics — Study Notes

**Course:** Certificate IV – Network Security Infrastructure
**Module:** 1. Secure Network Implementation Basics
**Platform:** Security Impossible Cyber Range (GNS3-based lab)
**Tools:** OPNsense (firewall), Open vSwitch, Ubuntu Docker containers, GNS3, GNS3 VM (Hyper-V)

---

## 1. Core Concepts

### 1.1 Network Segmentation and Zones

Network segmentation = dividing a network into smaller, independently secured sub-networks ("zones") to limit blast radius if one zone is compromised.

| Zone | Purpose |
|---|---|
| **WAN** | Untrusted network (the Internet) |
| **LAN / Internal Network** | Trusted internal network where end-users operate |
| **DMZ (Demilitarized Zone)** | Buffer zone between LAN and WAN; hosts public-facing services (web/DNS servers) |
| **IT-Department / Management** | Highest-privilege zone; used to access firewall GUI |

### 1.2 The DMZ — Buffer Zone Concept

If a server in the DMZ (e.g., Web Server) is compromised, the attacker is still **one firewall away** from the internal LAN — they must bypass a *second* layer of firewall rules to reach sensitive internal assets.

### 1.3 Principle of Least Privilege (PoLP)

> "DENY ALL, then PERMIT specific traffic. Instead of blocking bad traffic, you only allow the necessary traffic and implicitly block everything else."

- Default posture in firewall rule design = **Deny All**
- Only explicitly **Pass** rules for required (protocol, port, destination) combinations
- A *correctly* designed least-privilege ruleset should rarely need explicit "Block" rules — the implicit default-deny already covers it. Adding explicit Block rules can be a symptom that something *else* in the ruleset is too permissive.

### 1.4 Foundational Terminology

- **Bootstrap**: the minimal initial configuration done via text console before a system (e.g., OPNsense) is reachable enough to use its GUI.
- **OPNsense**: open-source, FreeBSD-based firewall/router OS; provides a web GUI for configuring zones, interfaces, and firewall rules. Stateful Packet Inspection (SPI) — remembers connection state so return traffic is automatically allowed without an explicit rule.
- **FreeBSD**: "Free" + "BSD" (Berkeley Software Distribution) — a Unix-like OS descended from the original Unix (Bell Labs, 1969) via UC Berkeley's BSD lineage.
- **Unix-like OS**: OSes that share Unix's design philosophy (CLI-first, "everything is a file", multi-user/multi-tasking) — includes FreeBSD, Linux, macOS. Windows is *not* Unix-like.
- **DHCP (Dynamic Host Configuration Protocol)**: automates IP assignment via the **DORA** process (Discover, Offer, Request, Acknowledge).
- **Static vs Dynamic IP**: Servers (Web/DNS) get **static IPs** so firewall rules always know where to find them; end-user clients get **DHCP** for ease of management.

---

## 2. Network Topology Built

```
                 [Internet]
                     |
                   nat0
                     |
              External Switch
                     |
                 [Firewall] (OPNsense)
        em2 ─────────┼───────── em3
   Internal Network            DMZ
   (Switch-2)                (Switch-3)
   ├─ Client-1                ├─ Web-Server
   ├─ Client-2                └─ DNS-Server
   └─ Client-3
                     |
                    em0
                     |
              IT-Department
               (Switch-1)
               └─ MGT machine
```

| Zone / Link | Network | Gateway (OPNsense) | Device IPs | Interface |
|---|---|---|---|---|
| IT Department | 10.10.0.0/24 | 10.10.0.1 | MGT: 10.10.0.10 (DHCP) | em0 (vtnet0) |
| WAN Link | DHCP assigned | N/A (NAT1) | — | em1 (vtnet1) |
| Internal Network (LAN) | 10.20.0.0/24 | 10.20.0.1 | Client-1/2/3: 10.20.0.10–.12 (DHCP) | em2 (vtnet2) |
| DMZ | 172.16.20.0/24 | 172.16.20.1 | Web-Server: .10, DNS-Server: .20 (static) | em3 (vtnet3) |

---

## 3. Lab Walkthrough — Step by Step

### Step 1 — Start the GNS3 Project
- Opened project **"Secure Network Implementation Unconfigured"** in GNS3.
- **Troubleshooting encountered:** GNS3 VM was pre-configured with 4 vCPUs, but the underlying host only had 2 vCPUs available. Fixed via **Edit → Preferences → GNS3 VM → vCPUs: 2** → Apply.
- Started all nodes (green play button). OPNsense (FreeBSD-based) takes longer (~1 min) to boot than the Docker-based clients/servers.

### Step 2 — OPNsense Console Bootstrap
Via console (`root` / `opnsense`):
- Menu option `2` → Set interface IP address → interface `1` (LAN/vtnet0)
- Configure IPv4 via DHCP? → **n**
- New LAN IPv4 address → **10.10.0.1**
- Subnet bit count → **24**
- Upstream gateway → blank (Enter)
- IPv6 prompts → **n**
- Enable DHCP server on LAN? → **y**, range **10.10.0.10 – 10.10.0.200**
- Change web GUI protocol to HTTP? → **n** (keep HTTPS)
- Generate new self-signed cert? → **y**
- Restore web GUI defaults? → **n**

Result: `LAN (vtnet0) → v4: 10.10.0.1/24`, web GUI reachable at `https://10.10.0.1`.

### Step 3 — Web GUI & Interface Assignment
- Logged into **MGT machine** (`osboxes.org` / `osboxes.org`).
- **Troubleshooting encountered:** MGT initially held a stale DHCP lease (192.168.1.101) from before the OPNsense LAN IP was changed. Fixed via:
  ```bash
  nmcli con show                     # found connection name has spaces: "Wired connection 1"
  sudo nmcli con down "Wired connection 1" ; sudo nmcli con up "Wired connection 1"
  ```
  → obtained correct lease `10.10.0.10`.
- Accessed `https://10.10.0.1` → bypassed self-signed cert warning → logged in (`root`/`opnsense`) → bypassed setup wizard via logo click.
- **Interfaces → Assignments**:
  - Added `vtnet2` → Description: **Internal Network**
  - Added `vtnet3` → Description: **DMZ**
  - Renamed [LAN] → intended "IT-Department" (OPNsense auto-stripped the hyphen → saved as **ITDepartment**; functionally identical, just a naming quirk).
- Configured static IPs per interface:
  - **[InternalNetwork]** → Static IPv4 → `10.20.0.1/24`
  - **[DMZ]** → Static IPv4 → `172.16.20.1/24`
  - Saved + Applied changes for each.

### Step 4 — DHCP for Internal Network
**Services → ISC DHCPv4 → [InternalNetwork]**:
- Enabled DHCP server
- Range: **10.20.0.10 – 10.20.0.200**
- Gateway: **10.20.0.1**
- Saved.

### Step 5 — IP Configuration for Clients & Servers

**DMZ servers (static, via console):**
```bash
# Web-Server
ip addr add 172.16.20.10/24 dev eth0
ip route add default via 172.16.20.1

# DNS-Server
ip addr add 172.16.20.20/24 dev eth0
ip route add default via 172.16.20.1
```

**Internal clients (DHCP, via config file edit):**
```bash
nano /etc/network/interfaces
```
- Commented out the **static** block (`#auto eth0`, `#iface eth0 inet static`)
- Uncommented the **DHCP** block (`auto eth0`, `iface eth0 inet dhcp`)
- Save: `Ctrl+O` → `Enter` → `Ctrl+X`
- Applied by **Stop → Start** the node in GNS3 (not "Reload" — Reload doesn't reinitialize networking the same way).

Results confirmed via console boot logs:
| Client | Leased IP |
|---|---|
| Client-1 | 10.20.0.10 |
| Client-2 | 10.20.0.11 |
| Client-3 | 10.20.0.12 |

### Step 6 — Least-Privilege Firewall Rules

**Firewall → Rules → DMZ** (inbound, from WAN → DMZ servers):

| # | Action | Proto | Source | Destination | Port | Description |
|---|---|---|---|---|---|---|
| 1 | Pass | TCP | Any | 172.16.20.10/32 | HTTP (80) | Allow Public HTTP Access to Web Server |
| 2 | Pass | UDP | Any | 172.16.20.20/32 | DNS (53) | Allow Public DNS Queries to DNS Server |

**Firewall → Rules → InternalNetwork** (outbound, from LAN clients → elsewhere):

| # | Action | Direction | Proto | Source | Destination | Port | Description |
|---|---|---|---|---|---|---|---|
| 1 | Pass | out | TCP | InternalNetwork net | Any | HTTPS (443) | Allow InternalNetwork to Internet |
| 2 | Pass | out | TCP | InternalNetwork net | 172.16.20.10/32 | HTTP (80) | Allow InternalNetwork to DMZ Web Server |
| 3 | Pass | out | UDP | InternalNetwork net | 172.16.20.20/32 | DNS (53) | Allow InternalNetwork to DMZ DNS |

**Everything else is implicitly blocked** by OPNsense's default-deny posture — including:
- DMZ → any internal zone (LAN or IT-Department) — blocked by default (no explicit Pass rule created)
- LAN → IT-Department — blocked by default

> ⚠️ Key gotcha: always remember to click **Save**, then **Apply changes** — rules are staged until applied.

---

## 4. Troubleshooting Log (Real Issues Hit During This Session)

1. **Wrong environment loaded** — Create Lab initially opened a stray Windows OOBE / Microsoft-account screen instead of the GNS3 desktop. Resolved by retrying — turned out to be a one-off platform glitch, not something to fix manually (never entered real Microsoft credentials).
2. **GNS3 VM vCPU over-allocation** — `"You have allocated too many vCPUs for the GNS3 VM! (max available is 2 vCPUs)"` → fixed by lowering vCPUs from 4 to 2 in GNS3 VM preferences.
3. **Stale DHCP lease on MGT** — MGT machine kept its pre-reconfiguration IP (192.168.1.101) instead of picking up the new OPNsense LAN subnet. `dhclient` wasn't available (this Ubuntu uses NetworkManager); fixed with `nmcli con down/up "Wired connection 1"` (quotes required due to the space in the connection name).
4. **OPNsense interface Description auto-sanitization** — Entering "IT-Department" as a description silently saved as "ITDepartment" (OPNsense strips hyphens/spaces from certain fields). Purely cosmetic — functionality unaffected.
5. **`/etc/network/interfaces` editing mistake** — First attempt to switch a client from static to DHCP left the file unchanged (static block still active). Second attempt, done more carefully with correct cursor placement, worked and was confirmed via `cat`.

---

## 5. Quiz Concepts Worth Remembering

**Q: A LAN interface is misconfigured with the wrong subnet mask (/16 instead of /24). What happens when Client-1 and Client-2 (same physical subnet) try to communicate?**
→ **Communication still succeeds.** Two hosts on the *same* L2 switch segment communicate directly via ARP/switching — this traffic never has to pass through the firewall/gateway at all, so a misconfigured gateway interface subnet mask doesn't affect it. This is a classic reminder that **not all traffic traverses the firewall** — only traffic destined for a different subnet does.

**Q: Which scenario violates the Principle of Least Privilege?**
→ Best-fit answer here (per PDF definition): an explicit **"Block All" rule** manually added to block DMZ → IT-Department traffic. Per PoLP's own definition — *"instead of blocking bad traffic, you only allow necessary traffic and implicitly block everything else"* — a properly least-privilege-designed ruleset shouldn't need an explicit Block rule for this at all, since default-deny already covers it. Needing one implies the ruleset elsewhere may be more permissive than it should be. *(Note: quiz answer keys on this platform were inconsistent/unreliable during this session — treat this as the best conceptual reasoning rather than a guaranteed "official" answer.)*

---

## 6. Final Outcome

- Fully segmented, "hardened" network built from an "Unconfigured" starting state.
- All 5 Milestone Checkpoints from the lab achieved: Infrastructure Ready → Gateway Authority → Logical Segmentation → Service Automation → Policy Enforcement.
- Module 1 (Secure Network Implementation Basics) — Lab + Quiz completed.
- **Time spent:** ~3 hours (including environment troubleshooting).

---

## 7. Real-World Application (from course conclusion)

These are foundational **Network Security Engineering** skills: segmenting networks and writing granular firewall rules is how organizations protect customer data and contain the spread of ransomware — from a small office to a global data center.

**Next steps to explore:** Inter-VLAN Routing, VPN configuration, Intrusion Detection Systems (IDS) on OPNsense.
