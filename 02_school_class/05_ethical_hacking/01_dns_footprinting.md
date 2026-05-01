# Lab 01: DNS Footprinting

## Overview
Hands-on practice with `nslookup` and `dig` — two commonly used DNS footprinting tools used in ethical hacking and reconnaissance.

## Key Concepts

### What is DNS?
DNS (Domain Name System) acts like a phone book for the internet — it translates human-readable domain names (e.g. `google.com`) into IP addresses. From an attacker's perspective, querying DNS records can reveal the structure of a target network.

### DNS Record Types
| Type | Description |
|------|-------------|
| A | Maps domain → IPv4 address |
| AAAA | Maps domain → IPv6 address |
| MX | Mail server information |
| NS | Nameserver information |
| CNAME | Alias for another domain |
| TXT | Text records (used for various purposes) |
| SOA | Start of Authority — zone metadata |
| AXFR | Full zone transfer (usually blocked) |

## Lab Environment
| Machine | IP | Role |
|---------|-----|------|
| Kali Linux | 192.168.9.2 | Attacker |
| pfSense | 192.168.0.254 | Firewall / DNS server |
| OpenSUSE | 192.168.0.30 | Target network machine |

## Task 1: Footprinting with nslookup

```bash
# Launch nslookup in interactive mode
nslookup

# Check current DNS server
> server

# Switch to lab DNS server
> server 192.168.0.254

# Basic domain lookup (A record by default)
> mylab.com

# Query nameserver records
> set type=ns
> mylab.com

# Query A record for a specific host
> set type=a
> opensuse.mylab.com        # Returns 192.168.0.30

# Query MX records
> set type=mx
> mylab.com                 # No answer — server blocks this type

# Query all record types
> set type=any
> mylab.com                 # Returns partial results only

# Attempt full zone transfer
> set type=axfr
> mylab.com                 # REFUSED — Kali is not authorised
```

**Key finding:** Zone transfer (AXFR) was refused from Kali but allowed from OpenSUSE — demonstrating that DNS servers can restrict which clients can perform zone transfers.

When zone transfer is allowed (from OpenSUSE), the output reveals **every host on the domain**: A, SOA, CNAME, TXT, MX, and NS records — essentially a full map of the internal network.

## Task 2: nslookup vs dig

```bash
# dig equivalent of an NS lookup (run from OpenSUSE)
dig @192.168.0.254 mylab.com ns

# Equivalent nslookup one-liner
nslookup -type=ns -debug mylab.com 192.168.0.254
```

### Comparison
| | nslookup | dig |
|--|----------|-----|
| Platform | Windows & Linux | Linux (manual install on Windows) |
| Output | Simple | Verbose and detailed by default |
| Common use | Quick lookups | Professional / scripting use |

## Takeaways
- DNS records expose significant information about a network's infrastructure
- A misconfigured DNS server allowing AXFR to any client leaks the entire zone — all hostnames and IPs
- Blocking zone transfers from unauthorised IPs is a basic but critical security measure
- `dig` provides richer output than `nslookup` without needing debug mode
