# 🔎 Recon Tools

Reconnaissance (Recon) is the **information gathering phase** in penetration testing and ethical hacking.

The goal of recon is to collect as much useful information as possible about a target before any attack.

---

# 📌 Why Recon Tools Matter

- Identify open ports and services
- Discover domains, subdomains, directories
- Understand system architecture
- Plan attacks efficiently

---

# 🧠 Types of Recon

## Passive Recon
- No direct interaction with target
- Example: Google, Whois, DNS lookup

## Active Recon
- Direct interaction with target
- Example: Nmap, Gobuster

---

# 🛠️ Common Recon Tools

- Nmap
- Whois
- nslookup
- dig
- ping
- traceroute / tracert
- Gobuster
- theHarvester
- Netcat

---

# 🔥 ALL RECON COMMANDS (COPY ONCE)

# Nmap

# Basic scan
nmap 192.168.1.10

# Scan all ports
nmap -p- 192.168.1.10

# Service version detection
nmap -sV 192.168.1.10

# OS detection
nmap -O 192.168.1.10

# Skip host discovery
nmap -Pn 192.168.1.10


# Whois

whois example.com


# nslookup

# IP lookup
nslookup example.com

# MX record
nslookup -type=mx example.com


# dig

# Basic
dig example.com

# MX
dig example.com MX

# NS
dig example.com NS


# ping

ping 8.8.8.8


# traceroute / tracert

# Linux
traceroute example.com

# Windows
tracert example.com


# Gobuster

gobuster dir -u http://example.com -w /usr/share/wordlists/dirb/common.txt


# theHarvester

theHarvester -d example.com -b google


# Netcat

# Check port
nc -nv 192.168.1.10 80

# Banner grabbing
nc -nv 192.168.1.10 21

---

# 📂 What Recon Can Reveal

- IP addresses
- Open ports
- Running services
- DNS records
- Hidden directories
- Emails and subdomains

---

# ⚠️ Legal Notice

Always perform recon only on authorised systems.

---

# 🧩 Pentesting Flow

1. Planning  
2. Recon  
3. Scanning  
4. Exploitation  
5. Reporting  

---

# ✅ Summary

Recon tools help gather information before attacking a system.

Key tools:
- Nmap → ports & services
- Whois → domain info
- nslookup/dig → DNS
- Gobuster → directories
- Netcat → manual connection
