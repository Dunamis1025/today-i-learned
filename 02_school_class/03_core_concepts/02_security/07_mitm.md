# Man-in-the-Middle (MITM) Attack

## What is a Man-in-the-Middle Attack?

A Man-in-the-Middle (MITM) attack is a type of cyber attack where an attacker secretly intercepts and possibly alters communication between two parties who believe they are directly communicating with each other.

In this attack, the attacker places themselves between the victim and the intended destination, allowing them to monitor, capture, or manipulate the transmitted data without the victims realizing it.

MITM attacks are particularly dangerous because they can occur silently while normal communication continues.

---

## How Man-in-the-Middle Attacks Work

A typical MITM attack involves three main stages.

### 1. Interception

The attacker intercepts the communication between two systems.

This can happen through several techniques such as:

- Rogue Wi-Fi hotspots
- ARP spoofing
- DNS spoofing
- Packet sniffing
- Session hijacking

Once interception is successful, the attacker can observe the traffic being exchanged.

---

### 2. Decryption (if encryption exists)

If communication is encrypted, the attacker may attempt to decrypt the data using techniques such as:

- SSL stripping
- Certificate spoofing
- Downgrade attacks

These techniques force the victim to use an insecure connection instead of a secure one.

---

### 3. Data Manipulation

After gaining access to the communication channel, the attacker may:

- Steal login credentials
- Capture sensitive data
- Modify transmitted information
- Inject malicious code
- Redirect victims to fake websites

---

## Common Types of MITM Attacks

### ARP Spoofing

ARP spoofing occurs when an attacker sends fake ARP messages on a local network.

This causes devices to associate the attacker's MAC address with the IP address of another device (such as the router).

As a result, network traffic is redirected through the attacker.

---

### DNS Spoofing

DNS spoofing involves corrupting the DNS cache so that a domain name resolves to a malicious IP address.

For example, a user trying to visit a bank website could be redirected to a fake login page controlled by the attacker.

---

### SSL Stripping

SSL stripping downgrades a secure HTTPS connection to an unencrypted HTTP connection.

The victim believes they are communicating securely, but the attacker can read all transmitted data.

---

### Session Hijacking

Session hijacking occurs when an attacker steals a user's session token.

With this token, the attacker can impersonate the victim and gain unauthorized access to accounts.

---

## Real-World Example

A common real-world MITM scenario occurs on public Wi-Fi networks.

An attacker creates a fake Wi-Fi hotspot with a name similar to a legitimate network, such as:

Free Airport WiFi
Airport_Free_WiFi
CoffeeShop_WiFi


When victims connect to the fake network, the attacker can monitor all network traffic, including:

- Login credentials
- Emails
- Credit card information
- Browsing activity

---

## Risks and Impact

MITM attacks can lead to serious consequences including:

- Identity theft
- Financial loss
- Data breaches
- Unauthorized system access
- Malware distribution

Organizations may also suffer reputational damage and legal consequences if customer data is compromised.

---

## How to Prevent MITM Attacks

Several security measures can reduce the risk of MITM attacks.

### Use HTTPS

Always ensure websites use HTTPS encryption.

HTTPS protects communication using TLS encryption.

---

### Avoid Public Wi-Fi for Sensitive Activities

Public Wi-Fi networks are commonly used for MITM attacks.

Sensitive activities such as online banking should be avoided on public networks.

---

### Use VPN

A Virtual Private Network (VPN) encrypts all traffic between the device and the VPN server.

This prevents attackers from reading intercepted data.

---

### Enable Multi-Factor Authentication (MFA)

Even if login credentials are intercepted, MFA adds an extra layer of security.

---

### Verify Website Certificates

Users should check that websites have valid security certificates before entering sensitive information.

---

## Summary

A Man-in-the-Middle attack occurs when an attacker secretly intercepts communication between two parties.

The attacker can monitor, steal, or manipulate sensitive data during the communication process.

MITM attacks commonly occur through techniques such as ARP spoofing, DNS spoofing, SSL stripping, and session hijacking.

Using secure protocols, avoiding untrusted networks, and enabling security features such as VPN 
