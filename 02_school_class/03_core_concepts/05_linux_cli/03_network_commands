# 🌐 Linux / CLI - Network Commands

Network commands in Linux are used to **check connectivity, troubleshoot issues, and inspect network configurations**.

This is essential for:
- Cybersecurity
- Network troubleshooting
- System administration
- Penetration testing

---

# 📌 Why Network Commands Matter

Without understanding network commands:

- You cannot diagnose connectivity issues
- You cannot verify if a system is reachable
- You cannot analyze network behavior

With proper usage:

- You can quickly identify problems
- You can test network security
- You can understand how systems communicate

---

# 🌍 Basic Network Concepts (Quick Reminder)

- IP Address → Identifies a device on a network
- DNS → Converts domain names to IP addresses
- Gateway → Route to external networks (Internet)
- Port → Specific service endpoint (e.g. 80, 443)

---

# 🧪 1. ping (Check Connectivity)

Tests if a host is reachable.

    ping google.com

### What it does:
- Sends ICMP Echo Request
- Waits for Echo Reply

### Key Output:
- time=XX ms → latency
- packet loss → network issue indicator

### Useful Options:
    ping -c 4 google.com   # send only 4 packets

### When to use:
- Check if server is alive
- Quick connectivity test

---

# 🧭 2. traceroute (Trace Network Path)

Shows the path packets take to reach a destination.

    traceroute google.com

### What it shows:
- Each hop (router) along the path
- Delay at each hop

### When to use:
- Diagnose slow network
- Identify where connection fails

---

# 🔍 3. ip (Modern Network Tool)

Replaces older tools like ifconfig.

## Check IP address:

    ip a

## Check routing table:

    ip route

### Key Info:
- inet → IPv4 address
- inet6 → IPv6 address
- UP → interface is active

### When to use:
- Check your IP
- Verify network interface status

---

# 🌐 4. nslookup (DNS Query Tool)

Finds IP address of a domain.

    nslookup google.com

### Output:
- DNS server used
- Resolved IP address

### When to use:
- Check DNS issues
- Verify domain resolution

---

# 📡 5. netstat (Network Connections)

Shows active connections and ports.

    netstat -tuln

### Options:
- t → TCP
- u → UDP
- l → Listening ports
- n → Show numbers (no DNS)

### Output:
- Local Address
- Port
- Status

### When to use:
- Check open ports
- Detect suspicious connections

---

# ⚡ 6. ss (Modern Alternative to netstat)

Faster and more detailed than netstat.

    ss -tuln

### Why use ss:
- Faster
- More accurate
- Recommended in modern Linux

---

# 📥 7. curl (Transfer Data / Test HTTP)

Used to send requests to servers.

    curl http://example.com

### Example:
    curl -I http://example.com   # get headers only

### When to use:
- Test web server
- Check API response
- Debug HTTP issues

---

# 📦 8. wget (Download Files)

Downloads files from the internet.

    wget http://example.com/file.zip

### When to use:
- Download files
- Test file accessibility

---

# 🔐 9. ssh (Secure Remote Access)

Connect to remote system securely.

    ssh user@192.168.1.10

### What it does:
- Encrypted connection
- Remote command execution

### When to use:
- Remote server access
- System administration

---

# 🚪 10. nmap (Port Scanning - Basic)

Scans open ports on a target.

    nmap 192.168.1.1

### What it shows:
- Open ports
- Running services

### When to use:
- Security testing
- Network scanning

⚠️ Note: Use only on authorized systems

---

# 🔄 11. hostname (Check System Name)

Displays system hostname.

    hostname

### When to use:
- Identify machine in network

---

# 🧠 Quick Summary

| Command     | Purpose                    |
|------------|--------------------------|
| ping       | Check connectivity        |
| traceroute | Trace network path        |
| ip         | Show IP / interfaces      |
| nslookup   | DNS lookup               |
| netstat    | Show connections          |
| ss         | Modern netstat            |
| curl       | Test HTTP/API             |
| wget       | Download files            |
| ssh        | Remote login              |
| nmap       | Port scanning             |
| hostname   | Show system name          |

---

# 🎯 Final Tip

In real-world troubleshooting:

1. Start with `ping`
2. Check IP using `ip a`
3. Verify DNS with `nslookup`
4. Inspect ports with `ss`
5. Test services with `curl`

👉 This flow solves most network problems quickly.

---

# 🧩 One-line Summary

Network commands help you **see, test, and control how systems communicate over a network.**
