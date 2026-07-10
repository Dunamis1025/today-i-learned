# Networking Study Notes: Wireless Security & Remote Access

## 1. Wireless Network Security Types (Windows Configuration)

Configured via **Settings > Network & Internet > Wi-Fi > Manage known networks**.

| Security Type | Description |
|---|---|
| **Open (No Authentication)** | No password; data is transmitted unencrypted. Insecure. |
| **WEP** | Legacy standard with very weak security; deprecated. |
| **WPA2-Personal** | Most common for home/small office. Uses **AES cipher** + **Pre-shared Key (PSK)** to encrypt traffic. |
| **WPA2-Enterprise** | Used in corporate environments. Authentication is offloaded from the access point to a centralized **RADIUS server**. |

### Key Terms
- **Cipher**: The encryption algorithm itself (e.g., AES) — the method used to scramble data.
- **PSK (Pre-shared Key)**: The actual key/password used with the cipher.
- **Passphrase**: Functionally similar to a password, but implies a longer, multi-word string (Wi-Fi keys accept 8–63 characters). In practice, used interchangeably with "password."

### Enterprise Remote Authentication
- **RADIUS** and **TACACS+** provide **scalable** authentication architectures — meaning they can handle growing numbers of users/devices without requiring per-device manual configuration.
- Both rely on a centralized **AAA server** (Authentication, Authorization, Accounting).
- Network devices forward credential checks to the AAA server instead of storing/validating credentials locally — this centralizes management and improves security at scale.

---

## 2. Lab: Connect and Test Wireless Connection (Packet Tracer / Physical Router)

**Note:** This lab requires a physical wireless router, 2 Windows computers, and a partner — not easily done solo on a personal laptop.

Key steps:
1. Configure router (IP, subnet, DHCP range, admin credentials, SSID, security passphrase) per instructor settings.
2. Connect wirelessly using assigned SSID + passphrase; record IP address and default gateway.
3. Test connectivity: `ping 127.0.0.1` (loopback test), ping gateway, ping partner's computer.
4. Disable SSID broadcast (hides network name from scan list — obscurity, not real security) and rename SSID.
5. Manually connect to the hidden network via **Control Panel > Network and Sharing Center > Set up a new connection or network > Manually connect to a wireless network**, checking "Connect even if network is not broadcasting."
6. Test internet access:
   - `tracert www.netacad.com` — traces the path (hops) to a destination.
   - `nslookup <IP>` — resolves an IP address back to a domain name.
   - Check Wireless Network Connection **Status** for media state and signal quality.

**Reflection concepts:**
- A successful ping to the default gateway confirms local network connectivity is working.
- If the gateway responds but the internet doesn't work, the problem lies **beyond the local network** (ISP, DNS, or external routing issue).

---

## 3. Lab: Use Telnet and SSH (Packet Tracer)

**Goal:** Practice remote CLI access to routers using both insecure (Telnet) and secure (SSH) protocols.

### Telnet (to router "East")
```
telnet 209.165.200.225
Username: ITEUser
Password: ITEPassword
```
- Transmits data in **plain text** — insecure, vulnerable to interception.

### SSH (to router "West")
```
ssh -l ITEUser 209.165.200.226
Password: ITEPassword
```
- `-l` = lowercase L (specifies the username), not the number 1.
- SSH **encrypts** the session — the secure replacement for Telnet.
- **Default SSH port: 22** (Telnet uses port 23).

### Part 2 (Optional, skipped)
Using PuTTY or similar terminal emulators to connect to a real instructor-provided SSH server — requires physical lab equipment.

---

## 4. Remote Access Protocols Overview

### VPN (Virtual Private Network)
- Creates a secure, encrypted tunnel over an insecure public network (like the Internet).
- Makes a remote user appear as if physically connected to a private (e.g., corporate) network.
- Configured in Windows via **Network and Sharing Center**.

### Telnet vs SSH (protocol-level)
- **Telnet**: Plain-text remote CLI access — insecure.
- **SSH**: Encrypted alternative. Supports multiple authentication methods:
  - Username/Password
  - **Kerberos** — enables Single Sign-On (SSO) across multiple systems (used in Windows Active Directory).
  - **Host-based authentication** — devices authenticate each other using public keys.
  - **Public key authentication** — most secure; uses a private key (protected by a passphrase) instead of a password.

---

## 5. Windows Remote Desktop vs Remote Assistance

| Feature | Remote Desktop | Remote Assistance |
|---|---|---|
| **Purpose** | Full remote control, work as if physically at the machine | Get/give help; screen-sharing with an invited trusted person |
| **Who starts it** | Remote user can **initiate independently** at any time (with valid credentials) | Requires the host to send an **invitation file + password** first |
| **Session behavior** | The local user is **logged off** when a remote session connects (single-user access) | **Both users stay logged in simultaneously** and can both view the desktop |
| **Control** | Full control automatically | View-only by default; helper must click **"Request Control"** and be approved |
| **Port** | Fixed: **TCP 3389** | Dynamic port range: **49152–65536** (harder to configure through firewalls; best for local network use) |
| **Best suited for** | Remote work (e.g., accessing office PC from home) | Tech support / troubleshooting scenarios |
| **Requirement** | Available on Windows Pro/Enterprise (host side); Home edition can only initiate, not host | Available on all Windows editions |

### Lab: Windows Remote Desktop and Assistance
**Note:** Requires 2 Windows computers on the same local network + a partner. Not fully practicable solo, especially if using Windows Home edition (can't host Remote Desktop connections).

Key steps covered:
1. Enable Remote Desktop; record PC name/IP and RDP port.
2. Create a local user account authorized for remote access.
3. Connect from partner's machine using Remote Desktop Connection tool.
4. Enable Remote Assistance; set invitation expiration (default: **6 hours**, configurable 1 minute–99 days).
5. Send invitation file + password (via email, USB, file sharing, etc.) — **single-use only**.
6. Partner connects, host approves, control can be requested/granted.

---

## Summary: Core Takeaways
- **AES + PSK** secures WPA2-Personal; **RADIUS/TACACS+ + AAA servers** provide scalable enterprise authentication.
- **SSH > Telnet** for security — always prefer encrypted remote access.
- **Remote Desktop** = one user takes over completely, replacing the local session.
- **Remote Assistance** = collaborative, invitation-based, view/control-limited support session.
- Both remote access labs assume a **multi-device, partnered, instructor-configured lab environment** (e.g., school network lab) rather than a single personal laptop.
