# DNS

## What is DNS?

DNS stands for **Domain Name System**.

DNS is the system that translates a **human-friendly domain name** into an **IP address** that computers can understand.

For example:

- Humans type: `google.com`
- Computers use: `142.250.66.14` (example)

Without DNS, users would need to remember IP addresses for every website.

So, DNS works like the **phonebook of the internet**.

---

## Why DNS Is Important

DNS is important because people remember names more easily than numbers.

It helps users:

- Access websites by name
- Connect to servers and services quickly
- Use the internet in a more convenient way

Without DNS, browsing the internet would be much harder and less practical.

---

## Simple Example

When you type `www.youtube.com` into a web browser, your computer does not automatically know where that website is.

It first asks a DNS server:

> "What is the IP address of www.youtube.com?"

The DNS server replies with the correct IP address.

Then your browser uses that IP address to connect to the website.

---

## How DNS Works

DNS resolution usually happens in several steps.

### 1. User Enters a Domain Name

A user types a domain name such as `www.example.com` into a browser.

### 2. The Computer Checks Local Cache

The device first checks whether it already knows the IP address.

It may look in:

- Browser cache
- Operating system cache
- Local hosts file

If the answer is already stored, the process is faster.

### 3. Query Is Sent to a Recursive DNS Resolver

If the device does not know the answer, it sends a query to a **recursive resolver**.

This resolver is usually provided by:

- Internet Service Provider (ISP)
- Public DNS provider such as Google DNS or Cloudflare DNS

### 4. Resolver Contacts Other DNS Servers

If the recursive resolver does not already know the answer, it may contact:

- Root DNS server
- TLD DNS server
- Authoritative DNS server

### 5. Authoritative Server Returns the Correct IP Address

The authoritative DNS server holds the final answer for the domain.

It returns the correct IP address.

### 6. Resolver Sends the Answer Back to the User

The recursive resolver sends the IP address back to the user's device.

### 7. Browser Connects to the Website

The browser uses that IP address to communicate with the web server and load the page.

---

## Main DNS Components

### 1. Domain Name

A domain name is the human-readable address of a website.

Examples:

- `google.com`
- `youtube.com`
- `holmesglen.edu.au`

### 2. IP Address

An IP address is the numeric address used by computers on a network.

Examples:

- IPv4: `192.168.1.1`
- IPv6: `2001:db8::1`

### 3. DNS Resolver

A DNS resolver receives the DNS query and finds the correct answer.

It acts like a helper between the user and the DNS system.

### 4. Root DNS Server

The root server is the starting point of the DNS hierarchy.

It helps direct the query to the correct Top-Level Domain server.

### 5. TLD Server

TLD stands for **Top-Level Domain**.

Examples of TLDs:

- `.com`
- `.org`
- `.net`
- `.edu`
- `.au`

The TLD server directs the query to the authoritative DNS server for the domain.

### 6. Authoritative DNS Server

This server holds the official DNS records for a domain.

It gives the final answer, such as the IP address linked to that domain.

---

## DNS Hierarchy

DNS is organized in a hierarchy.

### Root Level

This is the top of the DNS system.

### TLD Level

This includes domain endings such as:

- `.com`
- `.gov`
- `.edu`
- `.org`
- `.au`

### Second-Level Domain

This is the main name registered by an organization or person.

Example:

- In `google.com`, `google` is the second-level domain

### Subdomain

A subdomain comes before the main domain.

Example:

- In `mail.google.com`, `mail` is the subdomain

---

## Common DNS Record Types

DNS records are pieces of information stored on DNS servers.

They tell the internet how to handle a domain.

### 1. A Record

Maps a domain name to an **IPv4 address**.

Example:

- `example.com -> 93.184.216.34`

### 2. AAAA Record

Maps a domain name to an **IPv6 address**.

### 3. CNAME Record

CNAME stands for **Canonical Name**.

It points one domain name to another domain name.

Example:

- `www.example.com -> example.com`

### 4. MX Record

MX stands for **Mail Exchange**.

It tells email systems where to deliver email for a domain.

### 5. NS Record

NS stands for **Name Server**.

It identifies which DNS servers are authoritative for the domain.

### 6. TXT Record

Stores text information in DNS.

It is often used for:

- Domain verification
- Email security
- SPF, DKIM, DMARC configuration

### 7. PTR Record

Used for **reverse DNS lookup**.

It maps an IP address back to a domain name.

---

## Forward Lookup and Reverse Lookup

### Forward Lookup

A forward lookup means:

- Domain name -> IP address

Example:

- `example.com -> 93.184.216.34`

This is the most common DNS operation.

### Reverse Lookup

A reverse lookup means:

- IP address -> Domain name

This is often used in:

- Logging
- Email server checks
- Troubleshooting

---

## DNS Cache

DNS caching means temporarily storing previous DNS answers.

This improves speed and reduces repeated queries.

DNS cache can exist in:

- Web browser
- Operating system
- Recursive resolver

### Benefits of DNS Caching

- Faster browsing
- Less traffic to DNS servers
- Better performance

### Possible Problem

If a cached record is outdated, a user may be directed to the wrong or old IP address until the cache is refreshed.

---

## TTL in DNS

TTL stands for **Time To Live**.

TTL tells devices and DNS servers how long a DNS record can stay in cache before it must be checked again.

For example:

- A TTL of 3600 means the record can be cached for 1 hour

### Why TTL Matters

A shorter TTL:

- Updates more quickly
- Causes more DNS queries

A longer TTL:

- Reduces DNS traffic
- May keep old information longer

---

## Public DNS Examples

Some popular public DNS services include:

- Google DNS: `8.8.8.8`, `8.8.4.4`
- Cloudflare DNS: `1.1.1.1`, `1.0.0.1`

People may use public DNS for:

- Speed
- Reliability
- Privacy features
- Troubleshooting

---

## DNS Uses in Real Life

DNS is used in many everyday internet activities.

Examples include:

- Opening websites
- Sending email
- Accessing cloud services
- Connecting apps to servers
- Finding online systems by name instead of IP address

---

## DNS and Cybersecurity

DNS is very important in cybersecurity because attackers often abuse DNS.

If DNS is attacked or manipulated, users may be redirected to the wrong systems.

### Common DNS-Related Threats

#### 1. DNS Spoofing

DNS spoofing happens when false DNS information is given to a user.

This can redirect the victim to a fake website.

#### 2. DNS Cache Poisoning

Cache poisoning means corrupting cached DNS data so users receive a false IP address.

#### 3. DNS Tunneling

DNS tunneling is the abuse of DNS queries to secretly transfer data.

Attackers may use it for:

- Data exfiltration
- Command and control communication

#### 4. DDoS Against DNS Servers

Attackers may flood DNS servers with traffic to make them unavailable.

If DNS is down, users may not be able to reach websites even if the web servers are still working.

#### 5. Malicious Redirects

Attackers may change DNS settings on a router or device and redirect users to phishing pages.

---

## Signs of DNS Problems

Some common signs of DNS issues include:

- Website name does not work, but IP address works
- Slow website loading
- Wrong website opens
- "Server not found" errors
- Intermittent connection problems

---

## Basic DNS Troubleshooting

Here are common ways to troubleshoot DNS problems.

### 1. Check Internet Connection

Make sure the device is connected to the network.

### 2. Try Another Website

Check whether the issue affects one site or all sites.

### 3. Use IP Address Instead of Domain Name

If the IP works but the domain name does not, DNS may be the problem.

### 4. Flush DNS Cache

Clearing the local DNS cache may remove outdated or incorrect records.

### 5. Change DNS Server

Try switching to another DNS service such as Google DNS or Cloudflare DNS.

### 6. Restart Router or Device

This may refresh network settings.

### 7. Use Diagnostic Commands

Examples:

- `nslookup`
- `ping`
- `ipconfig /flushdns` on Windows

---

## Common DNS Commands

### nslookup

Used to query DNS and find domain-related information.

Example:

```bash
nslookup google.com

ping

Can test whether a device can reach a destination.

Example:

ping google.com
ipconfig /flushdns

Used on Windows to clear the DNS cache.

Example:

ipconfig /flushdns
dig

A more advanced DNS lookup tool commonly used on Linux and macOS.

Example:

dig google.com
DNS vs DHCP

DNS and DHCP are different, but they often work together.

DNS

Translates domain names into IP addresses

DHCP

Automatically gives IP addresses to devices on a network

Relationship

DHCP helps devices join the network.

DNS helps devices find other systems by name.

DNS vs URL

DNS and URL are not the same thing.

DNS

DNS is the naming system that converts domain names to IP addresses.

URL

A URL is the full address of a resource on the web.

Example:

https://www.example.com/login

In this URL:

https is the protocol

www.example.com is the domain name

/login is the path

DNS mainly helps resolve the domain name part.

Easy Summary

DNS is the system that helps users access websites by name instead of remembering IP addresses.

It translates domain names into IP addresses so devices can communicate over the internet.

DNS works through a hierarchy of servers and uses records such as A, AAAA, CNAME, and MX.

It is essential for normal internet use, but it is also a target for cyber attacks such as spoofing, cache poisoning, and DNS tunneling.

Understanding DNS is important for both networking and cybersecurity.

Key Points to Remember

DNS stands for Domain Name System

DNS translates domain names into IP addresses

It works like the phonebook of the internet

Common record types include A, AAAA, CNAME, MX, NS, TXT, and PTR

DNS caching improves speed

TTL controls how long records stay in cache

DNS can be abused in cyber attacks

DNS is essential for browsing, email, and many online services

One-Line Definition

DNS is a system that converts human-readable domain names into machine-readable IP addresses so devices can find each other on a network or the internet.
