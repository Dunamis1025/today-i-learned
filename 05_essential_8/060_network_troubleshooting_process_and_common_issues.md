# Network Troubleshooting – Study Notes (Chapter 6)

---

## 1. The 6-Step Troubleshooting Process

A structured, repeatable method for diagnosing and resolving network issues.

| Step | Name | What You Do |
|------|------|-------------|
| 1 | **Identify the Problem** | Gather symptoms from the user; check for recent changes or error messages |
| 2 | **Establish a Theory of Probable Cause** | List likely causes ranked by probability, using experience and knowledge |
| 3 | **Test the Theory** | Verify the theory with hands-on checks; if wrong, return to Step 2 |
| 4 | **Plan & Implement the Solution** | Design a fix and carry it out |
| 5 | **Verify Full System Functionality** | Confirm everything works; add preventive measures if needed |
| 6 | **Document Findings** | Record the problem, steps taken, parts used, and time spent |

---

## 2. Identifying the Problem – Asking the Right Questions

Determine the **scope** first: Is only one device affected, or multiple? Single device → start there. Multiple devices → check the central network equipment (switch, router).

### Open-Ended Questions (gather detail)
- What problems are you experiencing with your device?
- What software has been installed recently?
- What were you doing when the problem appeared?
- What error message did you receive?
- What type of connection is the device using (wired/wireless)?

### Closed-Ended Questions (confirm facts)
- Has anyone else used this device recently?
- Can you see shared files or printers?
- Have you changed your password recently?
- Can you access the internet?
- Are you logged into the network?
- Is anyone else experiencing the same issue?
- Have there been any recent changes to the network environment?

---

## 3. Common Theories of Probable Cause

After gathering information, consider these frequent root causes:

| Probable Cause | Description |
|---|---|
| Loose/damaged cable | Cable not fully plugged in or physically broken |
| Faulty/misconfigured NIC | Network Interface Card not seated correctly or driver issue |
| ISP outage | Service provider experiencing an infrastructure failure |
| Weak Wi-Fi signal | Too far from router or obstacles causing interference |
| Invalid IP address | Incorrectly configured or conflicting address |
| DNS server issue | Cannot translate domain names to IP addresses |
| DHCP server issue | Server not assigning IP addresses to devices |

---

## 4. Testing the Theory – Quick Checks

Try these simple procedures first; they often both identify and fix the issue.

- **Check cable connections** – ensure all cables are in the correct ports
- **Reseat cables** – unplug and firmly re-plug connectors
- **Reboot the device or network equipment** – clears temporary glitches
- **Log in as a different user** – isolates whether the issue is account-specific
- **Repair/re-enable the network connection** – reset the network interface via OS tools
- **Contact the network administrator** – escalate if specialized access is needed
- **Ping the default gateway** – confirms local router reachability
- **Access a remote website** – tests general internet connectivity

---

## 5. Research Resources (when the fix isn't obvious)

If no quick fix works, consult:

- Helpdesk repair logs (internal records of past incidents)
- Colleagues or senior technicians
- Manufacturer FAQ / support pages
- Technical websites and IT documentation portals
- Online forums and community boards
- Device/computer manuals
- Internet search engines

---

## 6. Verifying Full System Functionality

After applying the fix, confirm the system is fully restored:

```bash
ipconfig /all        # Check that valid IP address information is assigned
ping <address>       # Verify connectivity to a specific host
```

Also manually confirm access to required resources (email server, internet, shared drives).

---

## 7. Documentation Checklist

Always record the full incident before closing:

- [ ] Discussed solution with the user
- [ ] User confirmed the problem is resolved
- [ ] Provided any relevant paperwork
- [ ] Recorded all troubleshooting steps in the work order / journal
- [ ] Listed any hardware components replaced
- [ ] Logged total time spent

---

## 8. Common Network Problems & Solutions

### Basic Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| NIC LED is off | Unplugged/damaged cable or faulty NIC | Check cable; reseat NIC; update driver |
| Cannot SSH to remote device | SSH disabled or firewall blocking port | Enable SSH service; open firewall port |
| Cannot detect wireless router | Router off, out of range, or SSID hidden | Power cycle router; check range; unhide SSID |
| IP address is `169.254.x.x` | DHCP server not reachable (APIPA address) | Restart router; check DHCP service |
| No response to ping | Device offline, disconnected, or ICMP blocked | Check device power; check firewall rules |
| Local network works, no internet | Bad gateway config, DNS issue, or ISP outage | Verify gateway/DNS settings; contact ISP |
| Wireless device won't connect | Wrong password, MAC filtering, weak signal | Re-enter password; disable MAC filter; reposition router |
| Shared files/printers not visible | Sharing disabled or firewall blocking | Enable file sharing; check network profile; adjust firewall |

### Intermediate Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| Connects by IP, not by hostname | DNS misconfiguration | Verify DNS server address settings |
| Cannot obtain/renew IP address | DHCP server failure | Check/restart DHCP service on router |
| IP address conflict message | Duplicate address on network | Switch to DHCP auto-assign or assign a unique static IP |
| Network access but no internet | Misconfigured gateway or ISP outage | Check default gateway; contact ISP |
| Slow/dropping Wi-Fi | Distance, obstacles, or channel interference | Reposition router; change wireless channel; update firmware |

### Advanced Issues

| Symptom | Likely Cause | Fix |
|---|---|---|
| Cannot access FTP server | Misconfigured server or firewall blocking FTP port | Check server config; open FTP port |
| FTP client can't find server | Wrong address or broken network path | Verify server address; test connectivity |
| Cannot access specific HTTPS site | Expired certificate or incorrect system clock | Sync system time; check certificate validity |
| Cannot ping across networks | Router not routing between subnets or firewall blocking ICMP | Check routing config; review firewall rules |
| Cannot Telnet to remote host | Telnet service disabled or firewall blocking port | Enable Telnet; open port in firewall |
| `nslookup` timeout | DNS server unresponsive or no internet | Check DNS server; verify internet connectivity |
| `ipconfig /release` or `/renew` fails – "media disconnected" | Cable unplugged or NIC disabled | Reconnect cable; enable network adapter |
| `ipconfig /release` or `/renew` fails – "operation failed" | NIC driver missing or adapter in invalid state | Reinstall NIC driver; reset network adapter |

---

## 9. Lab Exercise – Troubleshoot Network Problems

**Goal:** Diagnose and fix all connectivity issues between two computers and a wireless router.

**Equipment needed:**
- 2 Windows computers
- 1 wireless router
- 2 Ethernet cables
- Internet connection

**Procedure:**
1. Log in to both computers (Computer01, Computer02) with admin privileges.
2. Use `ipconfig`, the Windows Network Control Panel, and the router's web interface to investigate.
3. Fix problems **one at a time**, documenting each one as you go.
4. Final verification – all of the following pings must succeed:

```
Computer01 → Computer02
Computer02 → Computer01
Computer01 → Default Gateway (router)
Computer02 → Default Gateway (router)
```

**For each problem found, document:**
- What the problem was
- What the probable cause was
- Steps taken to identify it
- Root cause confirmed
- Steps taken to fix it

---

## 10. Chapter Summary

| Topic | Key Concept |
|---|---|
| NIC & Router Setup | Configure hardware and software settings for wired/wireless connectivity |
| MAC vs. IP Address | MAC = hardware identifier; IP = logical address for communication |
| Static vs. DHCP | Static = manually assigned; DHCP = automatically assigned by router |
| Diagnostic Commands | `ipconfig`, `ping`, `nslookup`, `tracert` for testing and inspection |
| Security | Firewall rules, access controls, QoS, encryption |
| IoT | Smart devices (appliances, vehicles) connected and managed over a network |
| Troubleshooting | Always follow the 6-step process: Identify → Theorize → Test → Plan → Verify → Document |
