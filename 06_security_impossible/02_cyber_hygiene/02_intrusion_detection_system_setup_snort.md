# Snort IDS Lab — Session Notes

**Lab:** Intrusion Detection System (IDS) Configuration with Snort
**Environment:** Ubuntu 22.04.5 LTS (Azure VM), Security Impossible Cyber Range
**Difficulty:** Easy
**Date:** June 11, 2026

---

## 1. Lab Overview

This lab walks through deploying **Snort**, the industry-standard open-source
Intrusion Detection System (IDS), on a Linux host acting as a network gateway.

### Network Topology
| Role | IP Address | Description |
|---|---|---|
| Target system | `10.10.10.10` | Victim machine receiving attack traffic |
| Attacker system | `10.10.10.20` | Sends automated attack signals every ~60 seconds |
| Gateway / Snort host | `10.10.10.1` (via `eth1`) | Where Snort is installed and traffic is monitored |

### Key Concept: NIDS vs HIDS
- **NIDS (Network-based IDS):** Installed at a network choke point; monitors all traffic passing through.
- **HIDS (Host-based IDS):** Installed on an individual machine; monitors only that host's internal activity.

This lab implements a **NIDS** — Snort sits at the gateway (`eth1` interface) and inspects all traffic flowing between the attacker and the target.

### IDS vs IPS
- **IDS (`-A console` mode, used in this lab):** Passively sniffs a copy of traffic and *alerts* on suspicious activity. Does **not** block traffic.
- **IPS (Intrusion Prevention System):** If Snort were placed *inline* (directly between attacker and target), it could use the `drop` action to actively block malicious packets in real time.

---

## 2. Step-by-Step Walkthrough

### Step 1: Observe Automated Traffic
**Goal:** Confirm that simulated attack traffic is actively flowing on the interface before configuring Snort.

```bash
sudo tcpdump -i eth1
```
- `-i eth1` — listen on the interface where the simulated attacker traffic resides.
- **Result:** Captured 501 packets, including repeated SYN/RST exchanges from `10.10.10.20:60339` toward `10.10.10.10` on multiple ports (e.g., `8009`, `49156`, `rsync`, `5190`, `7070`, `ipp`, `ldp`, `sip`, `2717`, `iprop`, `3986`, `5009`, `echo`, `svrloc`, `x11`), plus an ARP request/reply between `10.10.10.20` and `10.10.10.10`.
- This confirmed the attacker (`10.10.10.20`) was performing a **port scan** against the target (`10.10.10.10`) on a recurring schedule.

---

### Step 2: Configure Snort for Network Monitoring
**Goal:** Define the protected network range and verify rule directory paths in `snort.conf`.

```bash
sudo nano /etc/snort/snort.conf
```

**Change made:**
```diff
- ipvar HOME_NET 10.10.10.10
+ ipvar HOME_NET 10.10.10.0/24
  ipvar EXTERNAL_NET !$HOME_NET
```
- `HOME_NET` defines the "internal"/protected network. Originally set to a single host (`10.10.10.10`); changed to the full `/24` subnet (`10.10.10.0/24`) so the entire lab network (gateway, target, attacker) is treated as "home."
- `EXTERNAL_NET !$HOME_NET` — everything **not** in `HOME_NET` is considered external (the `!` is negation).

**Verified (no changes needed):**
```
var RULE_PATH /etc/snort/rules
var SO_RULE_PATH /etc/snort/so_rules
var PREPROC_RULE_PATH /etc/snort/preproc_rules

include $RULE_PATH/local.rules
```
- `RULE_PATH` — directory containing standard detection rules.
- `SO_RULE_PATH` — directory containing pre-compiled ("shared object") rules.
- `PREPROC_RULE_PATH` — directory containing preprocessor/normalization rules.
- `include $RULE_PATH/local.rules` — Snort will load custom rules from `local.rules` (used in Step 4).

Saved with `Ctrl+O` → `Enter` → `Ctrl+X`.

---

### Step 3: Test Configuration
**Goal:** Validate the edited config file in test mode (no live capture) before going live.

```bash
sudo snort -T -c /etc/snort/snort.conf -i eth1
```
- `-T` — Test Mode: checks for syntax/configuration errors without capturing live traffic.
- `-c /etc/snort/snort.conf` — path to the configuration file edited in Step 2.
- `-i eth1` — confirms the interface is ready for monitoring.

**Result:**
```
Snort successfully validated the configuration!
Snort exiting
```
This confirms the config syntax and rule paths are correct — **not** that an attack has been detected or blocked.

**Audit task — Rule Statistics:**
```bash
sudo snort -T -c /etc/snort/snort.conf -i eth1 2>&1 | grep -i "rules read"
```
**Result:**
```
4057 Snort rules read
```
Total number of detection signatures loaded from all included `*.rules` files (e.g., `attack-responses.rules`, `backdoor.rules`, `bad-traffic.rules`, `chat.rules`, `ddos.rules`, `dns.rules`, etc.).

---

### Step 4 & 5: Custom Rules Configuration

**Snort Rule Structure:**
```
<action> <protocol> <source IP> <source port> -> <destination IP> <destination port> (<options>)
```

| Component | Meaning |
|---|---|
| **Action** (`alert`) | What Snort does when traffic matches (alternatives: `log`, `pass`, `drop`, `reject`, `sdrop`) |
| **Protocol** (`icmp`, `tcp`, `udp`) | Type of traffic to match |
| **Source/Destination IP & Port** | `any` = match anything; `$HOME_NET` = our protected network |
| **Direction** (`->`) | Traffic flow direction (`<->` = bidirectional) |
| **Options** (`msg`, `sid`, `rev`, etc.) | Alert text, unique rule ID, revision number |

**File edited:**
```bash
sudo nano /etc/snort/rules/local.rules
```

**Three custom rules added:**

**Rule 1 — Detect ICMP Floods (sid:1000001)**
```
alert icmp any any -> $HOME_NET any (msg:"ICMP Flood Detected"; itype:8; detection_filter:track by_src, count 20, seconds 5; sid:1000001; rev:1;)
```
- Matches ICMP Echo Request (`itype:8`, i.e., ping) toward `HOME_NET`.
- `detection_filter:track by_src, count 20, seconds 5` — only fires if a **single source IP** sends **20+ pings within 5 seconds**. This avoids false positives from normal/occasional "health check" pings.

**Rule 2 — Detect Clear-text HTTP Login Attempts (sid:1000002)**
```
alert tcp any any -> $HOME_NET 80 (msg:"HTTP POST Login Attempt"; flow:to_server,established; content:"POST"; http_method; content:"username=admin"; nocase; content:"password=admin123"; nocase; sid:1000002; rev:1;)
```
- Inspects the **payload** of TCP traffic to port 80 (web).
- Looks for an HTTP `POST` request (`http_method`) containing the literal strings `username=admin` and `password=admin123` (case-insensitive via `nocase`).
- Note: a typo (`tec` → `tcp`) was caught and corrected during editing.

**Rule 3 — Detect Nmap TCP Scans (sid:1000003)**
```
alert tcp any any -> $HOME_NET any (msg:"Nmap TCP Scan Detected"; flags:S; threshold:type both, track by_src, count 20, seconds 10; sid:1000003; rev:1;)
```
- Monitors for the **SYN flag (`flags:S`)** — used to probe whether a port is open.
- `threshold:type both, track by_src, count 20, seconds 10` — alerts if a single source sends 20+ SYN packets within 10 seconds, indicating an automated port scan (e.g., Nmap).

**Validation after editing:**
```bash
sudo snort -T -c /etc/snort/snort.conf -i eth1
```
**Result:** `Snort successfully validated the configuration! / Snort exiting` — all 3 custom rules passed syntax validation.

---

### Step 6: Start Snort in IDS Mode (Live Monitoring)

```bash
sudo snort -A console -c /etc/snort/snort.conf -i eth1
```
- `-A console` — print alert summaries directly to the terminal in real time.
- `-c /etc/snort/snort.conf` — use the edited config (including custom rules).
- `-i eth1` — monitor live traffic on this interface.
- (No `-T` flag → this is **live monitoring**, not a syntax test.)

**Live alerts observed:**
```
[1:1000001:1] ICMP Flood Detected [**] {ICMP} 10.10.10.20 -> 10.10.10.10
[1:1000003:1] Nmap TCP Scan Detected [**] {TCP} 10.10.10.20:61933 -> 10.10.10.10:993
[1:1000001:1] ICMP Flood Detected [**] {ICMP} 10.10.10.20 -> 10.10.10.10
[1:1000003:1] Nmap TCP Scan Detected [**] {TCP} 10.10.10.20:33070 -> 10.10.10.10:3389
```

**Alert format breakdown — `[Generator ID : SID : Revision]`:**
- `1:1000001:1` → Generator 1, our custom **ICMP Flood** rule (sid 1000001), revision 1.
- `1:1000003:1` → Generator 1, our custom **Nmap Scan** rule (sid 1000003), revision 1.
- `SourceIP:SourcePort -> DestIP:DestPort` shows the attacker (`10.10.10.20`) probing the target (`10.10.10.10`) on various ports (e.g., 993, 3389).

This confirmed both custom signatures (1 and 3) successfully detected the live, automated attack traffic from `10.10.10.20` against `10.10.10.10`. (Rule 2, the HTTP credential rule, did not trigger — the simulated traffic in this run did not include a matching HTTP POST.)

---

### Step 7: Monitoring, Analysis & Log Locations

**Stopping Snort & reviewing statistics:**
```
Ctrl+C
```
Printed **Snort Event Statistics** and **Packet I/O Totals**, including a "filtered events" summary:
```
gen-id=1   sig-id=1000003   type=Both   tracking=src count=20   seconds=10   filtered=396
```
- `sig-id=1000003` (Nmap Scan rule) — 396 packets matched the rule's base condition during the session, with the threshold (`count 20 / seconds 10`) controlling how many actual alerts were generated.

**Locating persistent log files:**
```bash
sudo cat /var/log/snort/alert        # → "No such file or directory" (wrong filename)
sudo ls -la /var/log/snort/          # → lists actual files
```

**Findings in `/var/log/snort/`:**
| File | Description |
|---|---|
| `snort.alert.fast` (0 bytes) | Default text-based alert log. Empty because `-A console` sent alerts to the terminal instead of this file. |
| `snort.log.<unix-timestamp>` | Binary **PCAP** capture of all packets seen during a session — can be opened in **Wireshark** for deep packet analysis. The most recent file (`snort.log.1781146847`) corresponds to this lab session. |

**Key takeaway:** Alert *summaries* are normally written to `/var/log/snort/alert` (text, human-readable), while full packet *captures* are written to `/var/log/snort/snort.log.*` (binary, for forensic replay in Wireshark).

---

## 3. Post-Lab Optional Tasks (Not Completed)
- **Task 1 — Advanced Alerting:** Change the ICMP rule's action from `alert` to `log` and observe how console output changes (logs silently vs. actively alerting).
- **Task 2 — Signature Research:** Browse community rules on snort.org and find a rule tied to a specific CVE, then explain its detection logic.

---

## 4. Quiz — Questions & Answers (10/10)

| # | Question (summary) | Correct Answer | Why |
|---|---|---|---|
| 1 | Purpose of `HOME_NET` in `snort.conf`? | Tells Snort which network range is "internal" so it can distinguish local vs. external traffic | Defines the protected boundary used by all other rules |
| 2 | What does `-T` do in `sudo snort -T -c ... -i eth1`? | Activates "Test Mode" to validate the configuration | Checks syntax/config without live capture |
| 3 | What does "Snort successfully validated the configuration!" indicate? | The configuration file syntax and rule paths are correct and ready for execution | Does **not** mean attacks were detected/blocked |
| 4 | What does `alert tcp any any -> $HOME_NET 80` match? | TCP traffic from any source IP/port destined for a web server (port 80) inside the home network | Header defines source `any any` → destination `$HOME_NET:80` |
| 5 | Why use `detection_filter:track by_src, count 20, seconds 5` in Rule 1? | Ensures Snort only alerts if 20+ pings arrive from a single source within 5 seconds, preventing false alarms from normal "health check" pings | Reduces false positives via thresholding |
| 6 | In `alert tcp any any -> $HOME_NET any (msg:"Nmap TCP Scan Detected"; flags:S; sid:1000003;)`, which part is the "Action"? | `alert` | First field of every rule = the action |
| 7 | In `[1:1000001:1] ICMP Flood Detected ... {ICMP} 10.10.10.20 -> 10.10.10.10`, which IP is the suspected attacker? | `10.10.10.20` | Format is `source -> destination`; source = sender = attacker |
| 8 | In Rule 2 (`content:"POST"`, `http_method`), which OSI layer is Snort inspecting? | Layer 7 (Application) | Inspecting actual HTTP request content/method, not just headers |
| 9 | Where to find the persistent **text-based** summary of a brute-force login event? | `/var/log/snort/alert` | Designated location for human-readable alert summaries |
| 10 | During an Nmap SYN scan, which TCP flag does the rule look for? | `S` (SYN) | SYN packets are used to probe whether ports are open |

---

## 5. Overall Summary

In this session, Snort was configured from a default state into a working **Network Intrusion Detection System (NIDS)**:

1. Verified live traffic flow with `tcpdump`.
2. Configured `snort.conf` — set `HOME_NET` to the full lab subnet (`10.10.10.0/24`) and confirmed rule-path variables.
3. Validated the configuration in test mode (`-T`), confirming 4,057 base rules loaded successfully.
4. Wrote three custom detection rules (ICMP flood, HTTP credential capture, Nmap SYN scan) with appropriate thresholds to reduce false positives.
5. Ran Snort live (`-A console`) and observed real-time alerts confirming the attacker (`10.10.10.20`) was actively flooding ICMP and port-scanning the target (`10.10.10.10`).
6. Reviewed event statistics and identified where Snort stores persistent alert logs (`/var/log/snort/alert*`) vs. full packet captures (`/var/log/snort/snort.log.*`, viewable in Wireshark).

**Real-world relevance:** Tools like Snort form the backbone of **Security Operations Centers (SOCs)**. Analysts use these alerts to catch early-stage reconnaissance (port scans) and credential-harvesting attempts (HTTP POST monitoring) before they escalate into full breaches.
