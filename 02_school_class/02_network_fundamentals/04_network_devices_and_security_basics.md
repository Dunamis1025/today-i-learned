# Network Devices and Security Basics

Summary of core networking concepts: switches, routers, network security devices, and access protocols.

## 1. Switches vs. Routers (OSI Layers)

- **Switch** — Operates at **Layer 2 (Data Link layer)**. Connects multiple devices *within* the same local network (e.g., all computers in one office or building). Forwards data using **MAC addresses** (the unique hardware address of each device).
- **Router** — Operates at **Layer 3 (Network layer)**. Connects *different* networks together (e.g., your home network and the internet). Forwards data using **IP addresses** and determines the best path for data to travel.

**Key distinction:** switches handle traffic *inside* one network; routers handle traffic *between* networks.

## 2. Switch — Primary Function

A switch inspects the **MAC address** of incoming data frames and forwards them directly to the correct destination device on the local network, rather than broadcasting to every device.

## 3. Router — Primary Function

A router uses **IP addresses** to direct data packets across different networks, choosing the most efficient path for the data to reach its destination (e.g., routing traffic from a home network out to the internet).

## 4. Securing Network Devices

Access to switches and routers is typically secured using:
- Strong passwords / authentication
- Encrypted remote management protocols such as **SSH** (instead of unencrypted protocols like Telnet)

This prevents unauthorized users from configuring or controlling network hardware.

## 5. RADIUS

**RADIUS** = **Remote Authentication Dial-In User Service**

A centralized system that manages **AAA**:
- **A**uthentication — verifying who the user is
- **A**uthorization — determining what they're allowed to access
- **A**ccounting — logging/tracking usage

Commonly used by organizations to control and audit network access from a single system.

## 6. IEEE 802.11

The standard that defines **Wi-Fi** — the rules and protocols for wireless local area networks (WLANs). Governs how devices communicate wirelessly.

## 7. Network Security Infrastructure — Goal

The primary goal is to **prevent unauthorized access** and **protect sensitive/critical data** from both external and internal threats.

## 8. Firewall

A security device that inspects **incoming and outgoing traffic** and applies preset security rules to **allow or block** specific data. Acts as a gatekeeper between trusted and untrusted networks.

## 9. Intrusion Prevention System (IPS)

Actively monitors network traffic in real time, detects malicious or suspicious activity, and **automatically blocks** threats before they cause damage — more proactive than simple detection/logging systems (IDS).

## 10. SSH (Secure Shell)

The standard protocol for **secure remote access** to network devices. Encrypts the connection so commands, credentials, and configuration data can't be intercepted — the secure replacement for older protocols like Telnet.

---

## Quick Reference Table

| Concept | Layer / Category | Core Role |
|---|---|---|
| Switch | Layer 2 (Data Link) | Connects devices within one network via MAC address |
| Router | Layer 3 (Network) | Connects different networks via IP address |
| RADIUS | AAA protocol | Centralized authentication, authorization, accounting |
| IEEE 802.11 | Wireless standard | Defines Wi-Fi communication |
| Firewall | Security device | Filters traffic per security rules |
| IPS | Security system | Detects & blocks malicious traffic in real time |
| SSH | Remote access protocol | Encrypted secure device management |
