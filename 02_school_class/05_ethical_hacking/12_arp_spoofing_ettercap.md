# Lab 12: ARP Spoofing and Man-in-the-Middle (MiTM) Attacks

> **Course:** NDG Ethical Hacking v2  
> **Date Completed:** 2026-06-04  
> **Tools Used:** Ettercap, Apache2, Kali Linux

---

## 1. Overview

This lab demonstrates how an attacker can position themselves between two communicating parties on a network to intercept, monitor, and manipulate traffic in real time — a technique known as a **Man-in-the-Middle (MiTM) attack**.

The lab covers four core attack phases:
1. ARP Spoofing with Ettercap
2. Capturing HTTP credentials
3. Manipulating HTTP images
4. Injecting JavaScript into live web traffic

---

## 2. Network Topology

| Machine       | IP Address(es)                          | Role             |
|---------------|-----------------------------------------|------------------|
| Kali Linux    | 192.168.9.2 / 192.168.0.2              | Attacker         |
| OpenSUSE      | 192.168.0.30                            | Victim           |
| pfSense       | 192.168.0.254 / 192.168.68.254 / 192.168.9.1 | Gateway/Firewall |
| OWASP BWA     | 192.168.68.12                           | Target Web Server|

---

## 3. Phase 1 — ARP Spoofing

### What is ARP Spoofing?
ARP (Address Resolution Protocol) maps IP addresses to MAC addresses on a local network. ARP spoofing **poisons** the ARP table of target devices by sending forged ARP replies, tricking them into sending traffic through the attacker's machine instead of the legitimate gateway.

### Steps Performed
1. Switched Kali from `eth0` (WAN) to `eth1` (LAN) to join the target network (192.168.0.0/24)
2. Verified IP with `ip addr` → confirmed `192.168.0.2/24` on eth1
3. Launched Ettercap in GUI mode: `ettercap -G`
4. Set Primary Interface to `eth1`
5. Scanned for hosts (magnifying glass icon) → discovered live hosts
6. Assigned targets:
   - **Target 1:** `192.168.0.30` (OpenSUSE — victim)
   - **Target 2:** `192.168.0.254` (pfSense — gateway)
7. Started ARP Poisoning via **MITM → ARP Poisoning → Sniff remote connections**

### Why Two Targets?
Selecting both the victim AND the gateway confines the attack to only that traffic path, avoiding unnecessary disruption to other hosts on the network.

### Result
All traffic between OpenSUSE and the gateway was now flowing through Kali — the attacker is now in the middle.

---

## 4. Phase 2 — Capturing HTTP Credentials

### How It Works
Ettercap automatically parses intercepted packets for HTTP login data. Since HTTP traffic is **unencrypted**, credentials are transmitted in **plaintext** and are directly readable.

### Steps Performed
1. From OpenSUSE, browsed to `http://192.168.0.254` (pfSense web interface)
2. Logged in with `admin` / `pfsense`
3. Checked Ettercap's status window on Kali → credentials appeared in plaintext

### Key Takeaway
> HTTP = No encryption = Credentials fully exposed to anyone positioned in the middle.  
> HTTPS encrypts the payload, making this attack ineffective against it without additional techniques (e.g., SSL stripping).

---

## 5. Phase 3 — Manipulating HTTP Images

### Concept
Ettercap can apply **filters** — scripts that intercept and modify live traffic as it passes through the attacker's machine. This phase replaces all images on a target webpage with an attacker-controlled image.

### How the Filter Works (`logo.filter`)
- **Rule 1 (Outbound — port 80 destination):** Strips the `Accept-Encoding` header from requests, preventing compressed responses that the filter cannot parse.
- **Rule 2 (Inbound — port 80 source):** Finds all `<img src>` tags in the HTML response and rewrites the URL to `http://192.168.0.2/logo.jpg` (attacker's server).

### Why Apache2 Was Needed
The filter redirects image requests to `192.168.0.2`. Without a running web server at that address, the victim's browser would receive a broken image. Apache2 serves the replacement image file from `/var/www/html/logo.jpg`.

```bash
service apache2 start
```

### Steps Performed
1. Started Apache2 on Kali
2. Loaded `logo.ef` (compiled filter) into Ettercap via **Menu (⋮) → Filters → Load a filter**
3. From OpenSUSE, browsed to `http://192.168.68.12`
4. All images on the OWASP page were replaced with the attacker's image ✅

### Analogy
> Think of Ettercap's filter like an Instagram filter — but instead of making your face look better, it intercepts network data mid-transit and rewrites the content before the victim sees it.

---

## 6. Phase 4 — Injecting JavaScript

### Concept
Instead of swapping images, this phase injects a JavaScript `alert()` popup into every HTML page the victim loads. In a real attack, this technique could be used with tools like **BeEF (Browser Exploitation Framework)** to hook the victim's browser and launch further attacks.

### How the Filter Works (`hacked-alert.filter`)
- **Rule 1:** Strips `Accept-Encoding` (same as before — allows HTML modification)
- **Rule 2:** Finds the `</head>` closing tag in HTML responses and inserts a `<script>alert('You got hacked!')</script>` block before it

### Steps Performed
1. Loaded `hacked-alert.ef` into Ettercap (replaces previous filter)
2. From OpenSUSE, performed a hard refresh: `Ctrl + Shift + R`
   - *Hard refresh bypasses cached pages, forcing the browser to fetch fresh content through the attacker*
3. "You got hacked!" alert appeared on the OWASP page ✅
4. Images from Phase 3 remained changed — **multiple filters can be chained simultaneously**

---

## 7. Key Concepts Summary

| Concept | Explanation |
|---|---|
| **ARP Spoofing** | Poisons ARP tables to redirect traffic through attacker |
| **MiTM** | Attacker silently relays and can modify communication between two parties |
| **Ettercap Filter (.ef)** | Compiled ruleset that defines how intercepted traffic should be modified |
| **Apache2** | Web server run on Kali to serve attacker-controlled content to victims |
| **HTTP vs HTTPS** | HTTP traffic is plaintext and fully vulnerable; HTTPS encrypts payload |
| **Browser Cache** | Stores previously loaded pages locally — hard refresh forces re-fetch through the attacker |
| **BeEF** | Browser Exploitation Framework — real-world tool that uses JS injection to hook and control victim browsers |

---

## 8. Defensive Takeaways

- **Always use HTTPS.** HTTP exposes all traffic including credentials to anyone on the same network.
- **Use HSTS (HTTP Strict Transport Security)** to prevent SSL stripping attacks.
- **Dynamic ARP Inspection (DAI)** on managed switches can detect and block ARP spoofing.
- **Network segmentation** limits the blast radius of MiTM attacks.
- **VPNs** encrypt traffic end-to-end, making MiTM interception useless even on compromised networks.
