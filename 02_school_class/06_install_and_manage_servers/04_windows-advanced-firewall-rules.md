# Lab 04: Configuring Advanced Firewall Rules on Windows 10

> **Course:** Windows 10 Administration Lab Series  
> **Topic:** Windows Defender Firewall with Advanced Security  
> **Environment:** NETLAB+ Virtual Lab (NDG / CSSIA)  
> **Date Completed:** May 2026

---

## 🎯 Objective

Learn how to configure inbound firewall rules using the **Windows Firewall with Advanced Security** snap-in on a Windows 10 client, and verify the effect of those rules using ICMP (ping) traffic between two machines.

---

## 🖧 Lab Topology

```
          [Server - 192.168.1.200]
                    |
        +-----------+-----------+
        |                       |
[PC1 - 192.168.1.203]   [PC2 - 192.168.1.202]
  (target / firewall)      (tester / attacker)
```

| VM | IP Address | Account | Password |
|----|-----------|---------|----------|
| Windows 10 PC1 | 192.168.1.203 | student | Train1ng$ |
| Windows 10 PC2 | 192.168.1.202 | student | Train1ng$ |
| Windows Server 2012 R2 | 192.168.1.200 | Administrator | Train1ng$ |

---

## 📚 Key Concepts Learned

### 1. Windows Firewall with Advanced Security
- Accessed via: `Control Panel → Windows Firewall → Advanced Settings`
- Provides granular control over inbound and outbound traffic
- Supports rule types: **Program**, **Port**, **Predefined**, and **Custom**
- Rules can be scoped by: protocol, IP range, port, profile, and program

### 2. Firewall Profiles
Windows applies firewall rules based on the detected network type:

| Profile | Description |
|---------|-------------|
| **Domain** | Connected to a corporate domain |
| **Private** | Home or work trusted network |
| **Public** | Untrusted public network (most restrictive) |

> ⚠️ **Lesson learned:** If a machine is classified as a **Public** network, rules scoped to **Private** only will NOT apply. This caused ping to fail in this lab until the network was changed to Private.

### 3. ICMPv4 and Ping
- `ping` uses **ICMP Echo Request / Echo Reply** messages
- ICMP is controlled at the protocol level, not by port numbers
- In Windows Firewall, ICMP traffic is managed via:
  - Protocol type: **ICMPv4**
  - Or via the predefined rule: `File and Printer Sharing (Echo Request - ICMPv4-In)`

### 4. Inbound vs Outbound Rules
| Direction | Meaning |
|-----------|---------|
| **Inbound** | Traffic coming INTO the machine |
| **Outbound** | Traffic leaving the machine |

> A rule blocking **inbound** ICMP on PC1 prevents PC2 from pinging PC1,  
> but PC1 can still ping PC2 (outbound is unaffected).

---

## 🔧 Step-by-Step: What Was Done

### Step 1 — Verify Baseline Connectivity
From PC2, confirmed PC1 was reachable **before** any firewall changes:
```
ping 192.168.1.203
# Result: Reply from 192.168.1.203 — Success (0% loss)
```

### Step 2 — Create a Custom Inbound Rule on PC1

1. Open **Windows Firewall with Advanced Security**
2. Click **Inbound Rules** → **New Rule**
3. Rule Type: `Custom`
4. Program: `All programs`
5. Protocol type: `ICMPv4`
6. ICMP Settings: `All ICMP types` (default)
7. Scope: `Any IP address` (default)
8. Action: **Block the connection**
9. Profile: `Domain`, `Private`, `Public` (all checked)
10. Name: `ICMP DENY`

### Step 3 — Verify the Rule Works
From PC2, re-ran ping after the rule was applied:
```
ping 192.168.1.203
# Result: Request timed out — Blocked successfully ✅
```

From PC1, tested outbound ping to PC2:
```
ping 192.168.1.202
# Result: Reply from 192.168.1.202 — Still works ✅
```

---

## 🐛 Troubleshooting Encountered (Real Lab Issues)

### Issue 1: `PING: transmit failed. General failure`
- **Cause:** Command Prompt was opened as a regular user, not Administrator
- **Fix:** Right-click CMD → **Run as administrator**

### Issue 2: `Destination host unreachable`
- **Cause:** PC1's IP was on the wrong subnet (`192.168.0.x` instead of `192.168.1.x`)
- **Fix:** Manually set PC1's IPv4 address to `192.168.1.203` via Network Adapter Properties

### Issue 3: `Request timed out` before the DENY rule was created
- **Cause:** PC1 was classified as a **Public network**, so the `File and Printer Sharing (Echo Request - ICMPv4-In)` rule (scoped to Private only) was not active
- **Fix:** 
  1. Changed network to Private (clicked "Yes" on discoverability prompt)
  2. Enabled all Echo Request rules via CMD:
  ```
  netsh advfirewall firewall set rule name="File and Printer Sharing (Echo Request - ICMPv4-In)" new enable=yes
  ```

---

## 📝 Lab Questions & Answers

| Question | Answer |
|----------|--------|
| Is PC1 responding to ping from PC2 before the rule? | **Yes** — 4 packets sent, 4 received, 0% loss |
| How many ICMP message types can be individually controlled? | **11** (Packet Too Big, Destination Unreachable, Source Quench, Redirect, Echo Request, Router Advertisement, Router Solicitation, Time Exceeded, Parameter Problem, Timestamp Request, Address Mask Request) |
| Does PC1 respond to ping after ICMP DENY rule is applied? | **No** — Request timed out (100% loss) |
| Can PC1 still ping PC2 after the rule? | **Yes** — The rule is **inbound only**, so outbound traffic from PC1 is unaffected |

---

## 💡 Key Takeaways

- **Inbound rules only block incoming traffic** — outbound traffic requires a separate outbound rule
- **Network profile matters** — always verify whether the machine is on Domain / Private / Public before troubleshooting firewall rules
- **ICMPv4 is not port-based** — you must select it as a protocol type, not a port number
- **`netsh advfirewall`** is a powerful CLI alternative to the GUI for managing firewall rules
- Always run Command Prompt as **Administrator** when working with network diagnostics

---

## 🔗 Related Commands

```powershell
# Check IP configuration
ipconfig /all

# Test connectivity
ping <ip_address>

# Enable all Echo Request rules via CLI
netsh advfirewall firewall set rule name="File and Printer Sharing (Echo Request - ICMPv4-In)" new enable=yes

# Show all firewall rules containing ICMP
netsh advfirewall firewall show rule name=all | findstr /i "icmp echo"
```

---

*Study notes from Windows 10 Administration Lab Series — CSSIA / NDG NETLAB+*
