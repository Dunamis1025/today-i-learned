# Packet Tracer Lab: Securing Network Devices (Router & Switch)

**Activity:** Cisco NetAcad Packet Tracer - Secure Network Devices
**Devices:** RTR-A (router), SW-1 (switch), PC, Laptop, Remote PC

## Topology & Addressing

| Device | Interface | Address | Mask | Gateway |
|---|---|---|---|---|
| RTR-A | G0/0/0 | 192.168.1.1 | 255.255.255.0 | N/A |
| RTR-A | G0/0/1 | 192.168.2.1 | 255.255.255.0 | N/A |
| SW-1 | SVI (Vlan1) | 192.168.1.254 | 255.255.255.0 | 192.168.1.1 |
| PC | NIC | 192.168.1.2 | 255.255.255.0 | 192.168.1.1 |
| Laptop | NIC | 192.168.1.10 | 255.255.255.0 | 192.168.1.1 |
| Remote PC | NIC | 192.168.2.10 | 255.255.255.0 | 192.168.2.1 |

PC and Laptop sit on the 192.168.1.0/24 LAN behind SW-1, which uplinks to RTR-A. Remote PC sits on the separate 192.168.2.0/24 LAN directly off RTR-A's second interface.

## Key Concepts Learned

- **IOS (Internetwork Operating System)**: Cisco's OS that runs on routers/switches; all CLI commands (`enable`, `configure terminal`, `hostname`, etc.) are IOS commands.
- **Host vs. Domain**: A *host* is a single device's name (e.g., `RTR-A`); a *domain* is the broader group/organization name it belongs to (e.g., `security.com`). Combined, they form a fully qualified name like `RTR-A.security.com`, used automatically when generating RSA keys.
- **Interface**: A physical (or logical) connection point on a device (e.g., `GigabitEthernet0/0/0`). Where cables plug in, or where an IP address is bound.
- **SVI (Switch Virtual Interface)**: A *logical* (not physical) interface on a Layer 2 switch (e.g., `interface vlan 1`), used to assign a management IP address so admins can remotely reach the switch over the network (ping, SSH) since switches otherwise don't route traffic.
- **RSA keys (asymmetric cryptography)**: A key *pair* — a **public key** (shareable) and a **private key** (must stay secret) — mathematically linked. Used to establish encrypted SSH sessions instead of plaintext Telnet.
  - `non-exportable`: the private key can never be copied out of the device, reducing risk of theft.
  - Modulus size = key strength (bits). Larger = more secure but slower to generate and more CPU-intensive per session. 1024 was chosen as a balance suitable for lab purposes (2048+ recommended in real-world use).
- **enable secret vs. enable password**: `secret` is automatically hashed (encrypted) in the config; the older `password` keyword stores it in plaintext.
- **username ... secret**: Creates a locally stored user account with an encrypted (hashed) password, used later for VTY/SSH login.
- **service password-encryption**: Applies weak (Type 7) encryption to any remaining plaintext passwords in the config (e.g., the console line password), which are not automatically hashed the way `secret` commands are. Complements — doesn't replace — `enable secret`/`username secret`.
- **`!` character**: read as "exclamation point" (or casually "bang").
- **`^` (caret) marker**: IOS's way of pointing to exactly where in a mistyped command it detected invalid input. Read as "caret" (sometimes casually "hat").
- **VTY (Virtual TeletYpe) lines**: Virtual (not physical) terminal lines used for *remote* access (Telnet/SSH) over the network, as opposed to the physical console port which requires a direct cable connection. `line vty 0 15` configures all 16 VTY lines at once with identical settings (splitting into `0 4` / `5 15` is only needed when different lines need different policies).
- **`ip default-gateway`** (switch-specific): Since a Layer 2 switch doesn't route, it needs this command (set in global config mode) to know where to forward its *own* management traffic destined for other networks — required for the switch's SVI to be reachable/pingable from a remote subnet.
- **Brute-force login protection**: `login block-for <seconds> attempts <n> within <seconds>` throttles repeated failed login attempts.

## Router (RTR-A) Configuration Steps

```
enable
configure terminal
no ip domain-lookup
hostname RTR-A
security passwords min-length 10
line console 0
 password @Cons1234!
 login
 exec-timeout 7 0
 exit
enable secret @Cons1234!
username NETadmin secret LogAdmin!9
service password-encryption
banner motd #Unauthorized access is strictly prohibited#
ip domain-name security.com
crypto key generate rsa      ! modulus: 1024
login block-for 45 attempts 3 within 100
line vty 0 15
 transport input ssh
 login local
 exec-timeout 7 0
 exit
exit
copy running-config startup-config
```

## Switch (SW-1) Configuration Steps

```
enable
configure terminal
no ip domain-lookup
hostname SW-1
enable secret @Cons1234!
interface vlan 1
 ip address 192.168.1.254 255.255.255.0
 no shutdown
 exit
interface range fa0/1, fa0/3-9, fa0/11-24, gi0/2
 shutdown           ! disable all unused ports
 exit
username NETadmin secret LogAdmin!9
ip domain-name security.com
crypto key generate rsa      ! modulus: 1024
line vty 0 15
 transport input ssh
 login local
 exit
ip default-gateway 192.168.1.1   ! required for switch mgmt reachability across subnets
exit
copy running-config startup-config
```

**Note:** `security passwords min-length` is a router-only command in Packet Tracer's switch IOS image — it is not part of the switch requirements and was correctly skipped.

## Verification / Testing

| Test | Result |
|---|---|
| PC (192.168.1.2) → ping SW-1 SVI (192.168.1.254) | Success (first packet timeout due to ARP resolution, then 3/3 replies) |
| Remote PC (192.168.2.10) → ping SW-1 SVI, before `ip default-gateway` | 100% failure |
| Remote PC → ping SW-1 SVI, after `ip default-gateway 192.168.1.1` | Success, 0% loss |
| PC → SSH to RTR-A (192.168.1.1) as NETadmin | Success — banner displayed, logged into `RTR-A>` |
| RTR-A → SSH to SW-1 (192.168.1.254) as NETadmin | Configured, session in progress |

## Outcome

Activity completed successfully in Packet Tracer ("Congratulations Guest! You completed the activity.")

## Takeaways

1. Console access secures *local* physical access; VTY + SSH secures *remote* network access — both need independent hardening.
2. `enable secret` / `username ... secret` auto-encrypt; `service password-encryption` is still needed to protect any remaining plaintext passwords (like console/line passwords).
3. RSA key generation is a prerequisite for enabling SSH — no keys, no SSH.
4. A Layer 2 switch needs a default gateway configured explicitly for its *own* management traffic to cross subnet boundaries, even though it doesn't route user traffic.
5. Disabling unused switch ports (`shutdown`) is a basic but important hardening step against unauthorized physical connections.
