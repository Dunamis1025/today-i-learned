# Cisco Networking Basics — Study Notes

> Topics covered: CLI modes, memory types, SVI, SSH vs Telnet, IOS command syntax

---

## 1. Cisco IOS CLI — Mode Hierarchy

Cisco IOS uses a layered command-line interface. Think of it like **levels of a dream in Inception** — each level gives you more power, but you need the right credentials to go deeper.

```
SW1>            # User EXEC Mode       — Level 1 (read-only, basic commands)
SW1#            # Privileged EXEC Mode — Level 2 (full visibility, reboot, etc.)
SW1(config)#    # Global Config Mode   — Level 3 (change device-wide settings)
SW1(config-line)#  # Line Config Mode  — Level 3 sub-mode (console/VTY settings)
SW1(config-if)#    # Interface Config Mode — Level 3 sub-mode (per-port settings)
```

### How to navigate

| From | Command | To |
|---|---|---|
| `SW1>` | `enable` | `SW1#` |
| `SW1#` | `configure terminal` | `SW1(config)#` |
| `SW1(config)#` | `line console 0` | `SW1(config-line)#` |
| `SW1(config)#` | `interface fa0/1` | `SW1(config-if)#` |

### How to go back

| Command | Effect |
|---|---|
| `exit` | Go back **one level** |
| `end` / `Ctrl-Z` | Jump directly back to `SW1#` (Privileged EXEC) from anywhere in Level 3 |
| `disable` | `SW1#` → `SW1>` |
| `exit` (at `SW1>`) | Closes the terminal session entirely |

> **Note:** `end` always lands at `SW1#`, not `SW1>`. To reach `SW1>` from `SW1#`, use `disable`.  
> `end` and `exit` at `SW1#` both drop you to `SW1>`.

---

## 2. Password Configuration

Passwords can be set at different access points:

```cisco
SW1(config)# enable password letmein       ! Unencrypted password for Privileged EXEC mode
SW1(config)# enable secret secretin        ! Encrypted password — takes priority over 'enable password'

SW1(config)# line console 0               ! Enter console line config
SW1(config-line)# password lineconin      ! Password for physical console access
SW1(config-line)# login                   ! Enforce password prompt on console

SW1(config)# line vty 0 15               ! Enter VTY lines 0–15 (up to 16 simultaneous remote sessions)
SW1(config-line)# password linevtyin     ! Password for remote access (Telnet/SSH)
SW1(config-line)# login                  ! Enforce password prompt on VTY
```

### Which password is used when?

| Access Method | Password Used |
|---|---|
| Console cable (physical) | `line console 0` password → enters `SW1>` |
| Remote (Telnet / SSH) | `line vty` password → enters `SW1>` |
| `SW1>` → `SW1#` (enable) | `enable secret` (or `enable password` if no secret set) |

> `enable secret` always overrides `enable password` when both are configured.

---

## 3. Global Configuration Mode — What Does "Global" Mean?

`SW1(config)#` is called **Global Configuration Mode** because changes made here affect the **entire switch** — not just one port or one connection.

This is in contrast to sub-modes like:
- `SW1(config-if)#` — applies only to a specific interface/port
- `SW1(config-line)#` — applies only to a specific line (console or VTY)

> "Global" does **not** mean the settings propagate to other connected devices — it means device-wide scope on *this* switch.

---

## 4. SVI — Switch Virtual Interface

An **SVI (Switch Virtual Interface)** is a logical, software-based interface on a switch that provides Layer 3 (IP-level) functionality without being tied to any physical port.

### Key Characteristics

| Characteristic | Explanation |
|---|---|
| Associated with VLAN1 by default | The default management SVI is VLAN 1 |
| Not tied to any physical interface | It exists in software only — no cable, no port |
| Provides remote management capability | Assign an IP to the SVI → manage the switch via SSH/Telnet |

### Why it matters
Without an SVI, a switch has no IP address and cannot be accessed remotely. Assigning an IP to `interface vlan 1` is the standard way to enable remote management.

```cisco
SW1(config)# interface vlan 1
SW1(config-if)# ip address 192.168.1.1 255.255.255.0
SW1(config-if)# no shutdown
```

---

## 5. Memory Types on a Cisco Device

| Memory Type | Volatile? | Stores |
|---|---|---|
| **RAM** | ✅ Yes (lost on reboot) | Running configuration (`running-config`), active routing tables |
| **NVRAM** | ❌ No (persists) | Startup configuration (`startup-config`) |
| **Flash** | ❌ No (persists) | Cisco IOS operating system image |
| **ROM** | ❌ No (read-only) | Bootstrap program, POST |

### Key points about RAM
- The **running-config** lives in RAM — it's what the device is currently using.
- If you make changes but don't save (`copy running-config startup-config`), they are **lost on reboot**.
- RAM is fast but volatile.

---

## 6. SSH vs Telnet

Both are remote access protocols, but they differ critically in security:

| | Telnet | SSH (Secure Shell) |
|---|---|---|
| Encryption | ❌ None — plaintext | ✅ Fully encrypted |
| Authentication | Basic | Username + key/password |
| Default Port | 23 | 22 |
| Current usage | Largely deprecated | Industry standard |

> **Rule of thumb:** Always use SSH. Telnet transmits passwords and commands in plaintext — anyone sniffing the network can read them.

---

## 7. IOS Command Syntax — Keywords vs Arguments

Cisco IOS commands follow a structured syntax:

```
show running-config
^     ^
|     └── keyword   (fixed, predefined option)
└── command         (the base action)
```

- **Command** — the verb/action (e.g., `show`, `copy`, `configure`)
- **Keyword** — a fixed, predefined word that specifies what the command acts on (e.g., `running-config`, `terminal`)
- **Argument** — a variable value supplied by the user (e.g., an IP address, interface name)

> `running-config` is a **keyword**, not an argument, because it is a fixed option defined by the IOS system — not a value the user provides.

---

## Quick Reference — Common Commands

```cisco
enable                          ! Enter Privileged EXEC mode
configure terminal              ! Enter Global Config mode
exit                            ! Go back one level
end                             ! Jump back to Privileged EXEC from anywhere
disable                         ! Drop from Privileged EXEC to User EXEC
show running-config             ! Display current active configuration (stored in RAM)
show startup-config             ! Display saved configuration (stored in NVRAM)
copy running-config startup-config  ! Save current config so it survives reboot
```
