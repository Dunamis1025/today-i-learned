# Security Threats, Troubleshooting Commands, and SSH Configuration — Quiz Review

## 1. Information Security Threat Types

Four representative types of information security threats:

| Threat Type | Definition | Example |
|---|---|---|
| **Identity theft** | Stealing someone's personal information (ID number, credit card number, Medicare number, etc.) and pretending to be that person | Using stolen personal information to open a credit card under someone else's name |
| **Information theft** | Sneaking into a company's or individual's system and taking sensitive information/documents out | Illegally obtaining a company's trade secret documents (e.g., battery manufacturing process, chip design) |
| **Disruption of service** | Preventing users from accessing a service by overwhelming it with traffic | Sending a large number of requests in a short time to paralyze a website (DoS/DDoS) |
| **Data loss** | Destroying or deleting data so it can no longer be accessed | Installing a virus that deletes CCTV recordings or corrupts important files |

**One-line summary:**
- Identity theft → pretending to be someone else
- Information theft → sneaking in and stealing information
- Disruption of service → overwhelming a system to shut it down
- Data loss → deleting or destroying data

---

## 2. AAA — Authentication, Authorization, Accounting

Three core security concepts, often confused with each other:

- **Authentication** — proving that you really are who you say you are ("Who are you? Prove it.") This is why Multi-Factor Authentication is called MFA, not MFA (Authorization).
- **Authorization** — determining what a user is allowed to do once authenticated (access boundaries/permissions).
- **Accounting** — recording/logging what a user has done.

**Example:**
- Logging in with a username and password → Authentication
- "Only administrators can view this file" → Authorization
- A log showing who accessed what and when → Accounting

**Quiz answer:** The purpose of the network security authentication function is **"to require users to prove who they are."**
- "Determine which resources a user can access" = Authorization (not authentication)
- "Keep track of the actions of a user" = Accounting (not authentication)

---

## 3. Types of Network Attacks

| Attack | Description |
|---|---|
| **Reconnaissance** | An attacker gathers information about a network before attacking — open ports, vulnerabilities, system types — similar to a thief scouting a house (checking cameras, doors, weak points) before breaking in. Any "pre-attack information gathering / vulnerability assessment" scenario = reconnaissance. |
| **Man-in-the-middle (MITM)** | An attacker inserts themselves between two communicating parties (A and B). Both A and B believe they are talking directly to each other, but they are actually both communicating through the attacker, who can eavesdrop on or alter the data. |
| **Dictionary attack** | An attacker uses a list ("dictionary") of commonly used usernames/passwords and tries them one by one to crack a system. |
| **DoS/DDoS (Disruption of Service)** | DoS: one computer overwhelms a target with traffic. DDoS: many "zombie" computers attack a target simultaneously. Both paralyze a website/service by flooding it with requests in a short time. |

---

## 4. Small Business Network Upgrade: Analyzer & Traffic Requirements

**Scenario:** A small company uses a protocol analyzer to capture traffic *while considering* a network upgrade (before the upgrade happens).

**Correct purpose:** To document and analyze network traffic requirements on each network segment — this is pre-upgrade planning, not post-upgrade baseline security analysis.

---

## 5. Cisco IOS Ping Indicators

When running `ping` on a Cisco device, the output uses symbols:

| Symbol | Meaning |
|---|---|
| **!** | Success — reply received |
| **.** | Timeout — no reply received in time |
| **U** | Destination Unreachable — a router along the path has no route to the destination |

**ICMP** = Internet Control Message Protocol. It is the protocol used to send control/status messages between network devices (not for transferring actual data). `ping` works by sending ICMP Echo Requests and receiving ICMP Echo Replies.

**Example interpretation:**
```
Sending 5, 100-byte ICMP Echos to 10.1.1.1, timeout is 2 seconds:
UUUUU
Success rate is 0 percent (0/5)
```
This means all 5 pings returned "U" (Destination Unreachable) — a router along the path did not have a route to the destination.

---

## 6. Troubleshooting Commands: nslookup / tracert / netstat / ipconfig

| Command | Purpose |
|---|---|
| **nslookup** | Checks which IP address a domain name resolves to — used to diagnose DNS problems |
| **tracert (traceroute)** | Shows the route (each hop/router) to a destination — used to identify where a packet is lost or delayed |
| **netstat** | Shows the active network connections on the local computer |
| **ipconfig** | Shows the local computer's IP address, gateway, and DNS server configuration |

**Classic diagnostic scenario:** If `ping` succeeds using an IP address but fails using a domain name, this indicates a **DNS problem** — use **nslookup** to check whether the domain name resolves correctly.

**Ping vs. Tracert:**
- Tracert shows every hop along the path to the destination.
- Ping only shows whether a reply came back from the final destination (and how long it took) — it does not show the intermediate path.

---

## 7. Extended Ping

- Typing `ping <destination address>` runs immediately with no chance to configure extra options.
- Typing `ping` alone (with no destination) triggers **Extended ping mode**, which prompts for additional settings step by step (protocol, target IP, repeat count, timeout, and — after answering "yes" to extended commands — **source address**).
- This is the method used to specify a **source address** for a ping.

---

## 8. Interpreting Ping Round-Trip Time (Baseline Comparison)

**Scenario:** Baseline ping statistics between two hosts were 36/97/132 (min/avg/max, in ms). Today's ping shows 1458/2390/6066 — 20–50x larger.

- The three numbers = **minimum / average / maximum** round-trip time in milliseconds.
- A reply was still received (connectivity is not broken), but it took much longer than usual.
- This does NOT mean the connection is down — it means something is causing a **delay**.
- **Correct interpretation:** "Something is causing a time delay between the networks."

---

## 9. Displaying Log/Debug Messages on Remote Sessions

- Connecting via a **console cable** → log/debug messages appear automatically on screen.
- Connecting via **Telnet or SSH (VTY line — a virtual/logical terminal line, not a physical port)** → log/debug messages do NOT appear by default.
- **`terminal monitor`** — enables log and debug messages to be displayed on the current remote (VTY) session. Correct answer for both "log messages" and "debug messages" questions involving VTY lines.
- **`logging synchronous`** — prevents log messages from getting jumbled together with the command line being typed; keeps the display clean and readable.
- **`logging console`** — sends log messages to the console session (enabled by default; unrelated to VTY).
- **`logging buffered`** — stores log messages in the router's memory (buffer) for later review via `show logging`; does not display them live on screen.

**Log message vs. Debug message:**
- A **log message** is an automatically generated record of an event (interface up/down, errors, security events, configuration changes).
- A **debug message** is a more detailed, real-time version of a log message, focused on a specific process (e.g., `debug ospf`), used for active troubleshooting.

---

## 10. Interfaces and Routing Protocols

**Interface** — a physical port on a router/switch where a cable is plugged in (e.g., `GigabitEthernet0/0` for Ethernet cables, `Serial0/0` for WAN connections). Each interface can be assigned its own IP address.

**Routing** — finding the best/shortest path for data to travel from source to destination.

**Routing protocol** — the set of rules routers use to automatically exchange path information with each other and calculate the best route (similar to how Google Maps calculates routes). This avoids the need to manually configure every router in large networks.

Representative routing protocols:
- **RIP** — the oldest and simplest (mnemonic: "Rest In Peace" — very old)
- **OSPF** — popular, link-state protocol; reacts quickly to network changes and is more effective than RIP in large networks
- **EIGRP** — developed by Cisco (mnemonic: both "EIGRP" and "Cisco" have 5 letters)
- **BGP** — connects the entire internet (mnemonic: "Big Gateway Protocol")

---

## 11. QoS — Prioritizing Real-Time Traffic

**Scenario:** A network administrator wants to give high priority to real-time application traffic.

**Correct answers: Voice and Video**
- Real-time traffic (VoIP calls, video conferencing) is highly sensitive to delay — any lag is immediately noticeable.
- Non-real-time traffic (FTP, instant messaging, SNMP) can tolerate small delays without a noticeable impact, so it does not need high priority.

---

## 12. Redundancy

**Definition:** Designing a network to use **multiple paths** between switches to ensure there is **no single point of failure**.

If only one cable connects two switches, a single cable failure breaks connectivity. Adding multiple physical paths means traffic can reroute if one path fails — similar to having more than one road to the same destination.

---

## 13. Latency

**Definition:** The delay time it takes for data to travel from source to destination.

**Question: Which situation would best depict (show/describe) a possible latency issue?**

**Correct answer: An increase in host-to-host ping response times** — this is a **direct measurement** of how long a reply takes, making it the clearest evidence of latency.

**Why other options are indirect, not direct, evidence:**
- **Bandwidth change** (`show interfaces`) — bandwidth is the capacity of a link (how much data can pass at once). A narrower "road" (lower bandwidth) *can* lead to congestion and increased latency, but the bandwidth value itself doesn't directly prove that latency occurred.
- **RAM change** (`show version`) — RAM amount is hardware specification information. A change in RAM doesn't directly confirm that network latency is currently happening.
- **Next-hop timeout from a traceroute** — this indicates a complete lack of response (connection failure) at a specific hop, not a "slowdown." It's a different kind of problem than latency.

---

## 14. show version Command

`show version` displays a Cisco device's own hardware/software information, including:
- IOS version
- Uptime
- RAM and Flash memory amounts
- **Configuration register value**
- Hardware model information

**Correct answer for "what can be verified using show version":** the value of the configuration register (controls how the router boots).

Other options are checked with different commands:
- Operational status of serial interfaces → `show interfaces`
- Routing protocol version enabled → `show ip protocols`
- Administrative distance → `show ip route`

---

## 15. show ip route Command

**Question:** Which command determines what interface a router will use to reach remote networks?

**Correct answer: `show ip route`** — displays the routing table, which shows:
- Which interface to use to reach a given destination network
- The next-hop router

**Command breakdown:** show (display) + ip (IP-related information) + route (path) = "show me the IP routing information."

**Other commands (for comparison):**
- `show arp` — shows the mapping between IP addresses and MAC addresses (Address Resolution Protocol table)
- `show protocols` — shows which routing protocol is enabled and interface up/down status; does NOT show which interface to use for a destination
- `show interfaces` — shows the status (speed, errors, traffic statistics) of interfaces themselves; does NOT show routing path information

---

## 16. CDP — Cisco Discovery Protocol

**Question:** How to find the IP address, hostname, and IOS version of a *neighboring* (directly cable-connected) Cisco device?

**Correct answer: `show cdp neighbors detail`**

CDP is a Cisco proprietary protocol that allows directly connected Cisco devices to automatically exchange information about themselves — device name, IP address, model, IOS version, and connected port. CDP only works between Cisco devices (not other vendors).

**Why other commands don't work here:**
- `show ip route`, `show version`, `show interfaces` all show information about the **local (own) device**, not about neighboring devices.

---

## 17. Worm Attack Mitigation

**Worm:** Self-propagating malware that spreads through a network without requiring any user action, by exploiting **system vulnerabilities**.

**Most effective mitigation: Download security updates from the OS vendor and patch all vulnerable systems.**
- This directly closes the vulnerability ("hole") that worms exploit, similar to patching a flat tire.
- OS vendors regularly identify vulnerabilities and release patches to fix them.

**Why other options don't directly address worms:**
- **AAA configuration** — relates to user authentication/authorization, not vulnerability exploitation.
- **Updated virus definitions** — detects known virus patterns; this is a defense against viruses, not against the vulnerability a worm exploits.
- **Changing passwords every 30 days** — helps prevent account takeover/brute-force attacks, unrelated to how worms spread.

---

## 18. Secure Remote Access: Telnet vs. SSH

**Scenario:** An administrator needs to securely access network devices in off-site buildings for documentation purposes.

**Correct answer: SSH**

| Protocol | Purpose | Encrypted? |
|---|---|---|
| Telnet | Remote CLI access | No (plaintext) |
| **SSH** | Remote CLI access | **Yes** |
| HTTP | Web page transfer | No |
| FTP | File transfer | No |

Telnet transmits data (including passwords) in plaintext, making it vulnerable to interception. SSH encrypts the session, protecting it from eavesdropping — hence it is the best choice for secure remote management.

---

## 19. exec-timeout — Where to Configure It

**Question:** On which two interfaces/ports can security be improved by configuring executive timeouts?

**Correct answers: vty ports and console ports**

`exec-timeout` automatically logs a user out after a period of inactivity, preventing unauthorized access if an administrator leaves a session open. This setting applies to **login access lines** — the paths through which a person logs in:
- **Console ports** — direct cable connection
- **VTY ports** — Telnet/SSH remote connection

It does NOT apply to physical data interfaces (Fast Ethernet, Serial) or virtual interfaces (loopback), since those are not login pathways.

---

## 20. Completing an SSH Configuration

**Given:** `login local` and `transport input ssh` have already been configured on the VTY lines.

**Three additional actions required to complete SSH configuration:**
1. **Create a valid local username and password database** — `login local` requires actual local user accounts to exist.
2. **Configure the correct IP domain name** — required because the RSA key is generated using the hostname + domain name.
3. **Generate the asymmetric RSA keys** (`crypto key generate rsa`) — SSH requires RSA keys to encrypt communication.

**Trap answer to avoid:** "Manually enable SSH after the RSA keys are generated" — this is incorrect because SSH is **automatically enabled** the moment the RSA keys are generated; no separate manual step is needed.

### Practical Lab Walkthrough (Packet Tracer PT Activity)
1. Connect to Router0 via PC0's **Terminal** application (not Command Prompt — Terminal connects to network devices via console; Command Prompt runs local OS commands like `ipconfig`/`ping`).
2. Enter `enable` and run `show running-config` to check the current configuration.
3. Review output for: hostname, `ip domain-name`, `username`/`password`, and the `line vty 0 4` block.
4. In one observed lab: hostname, domain name, and username/password were already configured, but `line vty 0 4` showed `transport input telnet` — meaning only Telnet was permitted, not SSH.
5. **Correct fix:** Enter `line vty 0 4`, then type `transport input ssh` to permit SSH access (in addition to or instead of Telnet).

*(Note: `crypto key generate rsa` output does not appear in `show running-config`; it must be verified separately, e.g., with `show crypto key mypubkey rsa`.)*

---

## 21. Password Strength Evaluation

**Example password:** `5$7*4#033!`

Character breakdown:
- Length: 10 characters
- Numbers: 5, 7, 4, 0, 3, 3 → present
- Special characters: $, *, #, ! → present
- **Letters (alphabet): none**

**Correct answer:** "It is strong because it contains 10 numbers and special characters."

**Why the "letters" option is wrong:** A similar-looking option claims the password contains "numbers, letters, and special characters" — but this password contains **no alphabetic letters at all**, making that statement factually incorrect despite sounding plausible.

---

## 22. Determining a Website's IP Address

**Question:** Best command to determine the IP address of a website?

**Correct answer: `nslookup`** — resolves a domain name to its corresponding IP address via DNS lookup. (Same principle as the DNS troubleshooting scenario in Section 6.)

Other options are unrelated:
- `copy startup-config running-config` — copies saved configuration to running configuration
- `show ipv6 route` — displays the IPv6 routing table
- `show ipv6 interface` — displays IPv6 interface status on the local device
