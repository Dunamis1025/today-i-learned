# IPS Operation and Configuration (Session 12, Module 12)

> VU23218 – Implement Network Security Infrastructure
> Topics: IPS concepts, signatures, alerts, Cisco IPS options, Snort IPS, Cisco IOS IPS lab (Packet Tracer 5.4.1.2)

---

## 1. IDS vs IPS

| | IDS (Intrusion **Detection** System) | IPS (Intrusion **Prevention** System) |
|---|---|---|
| Role | Detects and alerts only | Detects and blocks |
| Placement | Out of band (monitors a copy of traffic, e.g. SPAN port) | **Inline** (traffic must pass through it) |
| Analogy | Burglar alarm / CCTV | Security guard at the door |
| Drawback | Attack may already have passed | False positives can block legitimate traffic; adds latency |

---

## 2. IPS Signatures

A **signature** is a set of rules an IPS uses to detect known malicious activity (viruses, worms, protocol anomalies). When traffic matches, the sensor takes a predefined action.

### 2.1 Three signature attributes
1. **Type**: atomic or composite
2. **Trigger** (also called the *alarm*): the condition that fires the signature
3. **Action**: what the IPS does on a match

### 2.2 Signature types
- **Atomic**: a single packet / activity / event identifies the attack. Stateless, fast, efficient.
- **Composite (stateful)**: needs multiple packets and remembered state. The state window is the **event horizon**, whose length varies per signature.

### 2.3 Signature alarms (trigger types)
| Type | Also called | How it works |
|---|---|---|
| **Pattern-based** | Signature-based | Matches traffic against a database of known attack patterns |
| **Anomaly-based** | Profile-based | Builds a baseline of normal activity; alerts when activity exceeds a threshold |
| **Policy-based** | Behavior-based | Admin defines suspicious behavior (from historical analysis); one signature can cover a whole class of activity |
| **Honey pot-based** | | Decoy server lures attackers away from production and lets admins study attack behavior to tune signatures |

### 2.4 Signature actions
- **Generate an alert**: produce alert; produce verbose alert (more detail)
- **Log the activity**: log attacker packets; log victim packets; log pair packets
- **Deny the activity**: deny packet inline; deny connection inline; deny attacker inline (blocks for a period of time)
- **Reset the TCP connection**: send a TCP reset to kill the flow
- **Block future activity**: request block connection; request block host (asks another device such as a router/firewall to block); request SNMP trap (notify the management system)

Logs from IPS, firewalls, switches and routers are typically collected in a **SIEM** (Security Information and Event Management) for dashboards and incident-response reporting. Very serious events can also notify the incident response lead by SMS/email.

---

## 3. Evaluating Alerts

| Result | Traffic | IPS reaction | Verdict |
|---|---|---|---|
| **True positive** | Attack | Alert | Ideal |
| **True negative** | Normal | No alert | Ideal |
| **False positive** | Normal | Alert | Needs tuning; costs time to investigate (benign trigger) |
| **False negative** | Attack | No alert | Most dangerous; attack may go unnoticed and data leak |

Memory trick: *positive/negative* = did the IPS fire? *true/false* = was it right?

**Sensor sensitivity**: too low means more false negatives; too high means more false positives. The goal is to fine-tune the balance.

---

## 4. Cisco IPS Options

1. **Cisco Firepower NGIPS** (Next-Generation IPS): dedicated inline appliance, built on open-source Snort, uses vulnerability-focused rules and IP/URL/DNS intelligence from **Cisco Talos**. Features: sandboxing for zero-day detection, **AVC** (Application Visibility and Control), **AMP** (Advanced Malware Protection), **URL filtering**.
2. **Cisco Snort IPS**: IPS service enabled on ISR routers (e.g. ISR 4000). ISR 4000 no longer supports legacy Cisco IOS IPS.
3. **External Snort IPS server**: separate Snort server receiving a copy of traffic via a switch SPAN (promiscuous) port.

---

## 5. Snort

- Open-source network IDS/IPS (created 1998 by Martin Roesch; now owned by Cisco via the Sourcefire acquisition, 2013).
- Real-time traffic analysis, protocol analysis, content searching/matching; detects buffer overflows, stealth port scans, etc.
- Rule format (similar to an ACL line):

```
[action] [protocol] [src IP] [src port] -> [dst IP] [dst port] ([options])
alert tcp $EXTERNAL_NET $HTTP_PORTS -> $HOME_NET any
```

- **IDS mode**: alert, log, pass. **IPS mode**: adds drop, reject, block.
- ISR 4000 Snort features: IDS/IPS modes, three signature levels, allowed list, Snort health monitoring, fail open/close, signature updates, event logging.

### 5.1 Snort IPS architecture on an ISR
Needs two **VirtualPortGroup (VPG)** interfaces:
- **VPG0 (management)**: sends logs and fetches signature updates from Cisco.com; needs a routable (public) IP, e.g. `209.165.201.0/30`.
- **VPG1 (data)**: carries user traffic between the router and the Snort container, e.g. `192.168.0.0/30`. Snort inspects, then drops or forwards the traffic.

### 5.2 Snort IPS deployment steps
1. Download the Snort **OVA** (Open Virtualization Archive) from Cisco (requires a Cisco account)
2. Install the OVA: `virtual-service install name <name> package <path> media <fs>`; verify with `show virtual-service list`
3. Configure the VirtualPortGroup interfaces
4. Activate the virtual service: `virtual-service <name>` → `vnic gateway VirtualPortGroupX` → `guest ip address <ip>` → `activate`
5. Configure Snort: `utd engine standard` → `threat-inspection`; `threat protection` = IPS mode, `threat detection` = IDS mode; logging to syslog/external server; signature update method
6. Enable IPS globally or per interface
7. Verify with show commands

---

## 6. Subnetting Refresher (for /30 links)

- Bit values: 128 64 32 16 8 4 2 1
- Block sizes: /25=128, /26=64, /27=32, /28=16, /29=8, /30=4
- **/30 = 255.255.255.252**: 4 addresses, **2 usable hosts** (network and broadcast addresses are reserved). Ideal for router-to-router point-to-point links and saves scarce public IPs.
- Network count = number of separate segments between routers (LANs + each router-to-router link).
- Serial links: one end is **DCE** (supplies the clock, `clock rate`), the other is **DTE**.

---

## 7. Lab: Configure IOS IPS Using the CLI (Packet Tracer 5.4.1.2)

**Topology**: Syslog server + PC-A on 192.168.1.0/24 → R1 ←10.1.1.0/30→ R2 ←10.2.2.0/30→ R3 → PC-C on 192.168.3.0/24 (4 networks in total). Syslog server = 192.168.1.50.

**Objective**: enable IOS IPS on R1 for traffic entering 192.168.1.0, log to the syslog server with correct time, modify a signature, and verify that ICMP echo replies are alerted and dropped.

### Part 1: Enable IOS IPS
1. **Enable the security technology package**
   ```
   R1# show version
   R1(config)# license boot module c1900 technology-package securityk9
   (accept EULA: yes)
   R1# copy running-config startup-config
   R1# reload
   R1# show version      ! Current = securityk9
   ```
   Note: the license command alone is not enough. You must save and reload.
2. Verify connectivity: PC-A ↔ PC-C ping succeeds.
3. Create the config directory: `R1# mkdir ipsdir`
4. Set the signature storage location: `R1(config)# ip ips config location flash:ipsdir`
5. Create the IPS rule: `R1(config)# ip ips name iosips`
6. **Enable logging**
   ```
   R1(config)# ip ips notify log
   R1# clock set 01:37:00 22 October 2026     ! privileged EXEC, UTC time
   R1(config)# service timestamps log datetime msec
   R1(config)# logging host 192.168.1.50
   ```
   Accurate time matters because logs must be correlated across devices and over time. In production, use NTP.
7. **Signature categories**: retire the `all` category (`retired true`), un-retire `ios_ips basic` (`retired false`).
8. **Apply the rule to an interface**
   ```
   R1(config)# interface g0/1
   R1(config-if)# ip ips iosips out
   ```
   `in` inspects traffic entering the interface; `out` inspects traffic leaving it. IPS engine build messages appear in the console.

### Part 2: Modify the signature
```
R1(config)# ip ips signature-definition
R1(config-sigdef)# signature 2004 0          ! ICMP echo request
R1(config-sigdef-sig)# status
R1(config-sigdef-sig-status)# retired false
R1(config-sigdef-sig-status)# enabled true
R1(config-sigdef-sig)# engine
R1(config-sigdef-sig-engine)# event-action produce-alert
R1(config-sigdef-sig-engine)# event-action deny-packet-inline
```
Signature ID range is 1–65535; SubID range is 0–65535.

### Verify
- `show ip ips all` shows the IPS configuration summary and where `iosips` is applied (interface and direction).
- Ping from PC-C to PC-A **times out** because matching ICMP packets are alerted and dropped.
- The syslog server records the matching events; traffic that does not match the signature is not logged.

---

## 8. Key Takeaways

- IDS detects; IPS detects and prevents inline.
- Signature = Type + Trigger + Action.
- False negatives are the most dangerous; tune sensitivity to balance false positives against false negatives.
- Snort is the engine behind Cisco NGIPS and ISR Snort IPS; Cisco Talos supplies the intelligence feeds.
- IOS IPS needs the securityk9 license (save and reload), a config directory, an IPS rule, logging with correct time, and the rule applied to an interface with a direction.
- Use `?` and Tab completion in the CLI to avoid typos and discover options.
