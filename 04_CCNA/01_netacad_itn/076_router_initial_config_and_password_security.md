# Packet Tracer Lab: Configure Initial Router Settings

## Overview

This lab covers basic router configuration on a Cisco router (R1) using Packet Tracer: establishing a console connection, verifying default settings, configuring hostname/banner/passwords, and saving the configuration.

---

## Part 1: Verify the Default Router Configuration

**Connection setup**
- Console cable connects PC (RS232) to Router (Console port).
- Console cables don't show green/red link lights like Ethernet — connection status shows as a plain dot since there's no "link up/down" concept for a direct management connection.
- Terminal access via PC > Desktop > Terminal, then Enter to reach `Router>` (User EXEC mode).

**Findings from `show running-config` (before any changes)**

| Item | Value |
|---|---|
| Hostname | `Router` (default) |
| GigabitEthernet interfaces | 2 (Gi0/0, Gi0/1) |
| Serial interfaces | 2 (S0/0/0, S0/0/1) |
| FastEthernet interfaces | 4 (Fa0/1/0–0/1/3, via an HWIC switch module) |
| VTY line range | 0–4 (5 concurrent remote sessions) |

**`show startup-config` → "startup-config is not present"**
- No configuration has ever been saved to NVRAM. The router only has a `running-config` in RAM (volatile); nothing has been written to `startup-config` yet.

---

## Part 2: Configure and Verify the Initial Configuration

**Commands used**

```
Router> enable
Router# configure terminal
Router(config)# hostname R1
R1(config)# banner motd #Unauthorized access is strictly prohibited.#
R1(config)# enable password cisco
R1(config)# enable secret itsasecret
R1(config)# line console 0
R1(config-line)# password letmein
R1(config-line)# login
R1(config-line)# exit
R1(config)# service password-encryption
```

**Verification**
- `show running-config` confirmed all passwords stored in encrypted form (`enable secret 5 ...`, `enable password 7 ...`, console `password 7 ...`).
- Logged out and reconnected: banner displayed → prompted for console password (`letmein`) → reached `R1>` → `enable` → prompted for enable password (`itsasecret`) → reached `R1#`. All worked as expected.

**Key concepts**
- **MOTD banner**: Warns unauthorized users before login and provides a legal basis for prosecution if they proceed anyway.
- **Missing `login` command**: If a console/line password is set but users aren't prompted for it, the `login` command under that line was forgotten — it's what activates the password check.
- **`enable secret` vs `enable password`**: When both are configured, `enable secret` (MD5-hashed, stronger) always takes priority; `enable password` is effectively ignored.
- **Password display**: By default, most passwords display in plain text in the config file. `service password-encryption` encrypts all currently-configured and future passwords in the saved configuration (note: this is weak Type 7 encryption, not cryptographically strong).

---

## Part 3: Save the Configuration

**Save running-config to NVRAM**

```
R1# copy running-config startup-config
```
Shortest unambiguous form: `copy run start`

Confirms with `[OK]`. This creates the `startup-config` in NVRAM so settings survive a reboot/power loss.

**Check flash memory**

```
R1# show flash
```

Result:

| File # | Size (bytes) | Name |
|---|---|---|
| 3 | 33,591,768 | `c1900-universalk9-mz.SPA.151-4.M4.bin` |
| 2 | 28,282 | `sigdef-category.xml` |
| 1 | 227,537 | `sigdef-default.xml` |

- **3 files** total in flash.
- The **IOS image** is `c1900-universalk9-mz.SPA.151-4.M4.bin` — identified by:
  - `.bin` extension (typical for compiled OS images)
  - Vastly larger file size than the other two files
  - Filename encodes platform (`c1900`), feature set (`universalk9`), image type (`mz` = compressed, runs from RAM), and IOS version (`15.1(4)M4`)

---

## Supporting Concepts Learned

- **Interface**: A physical port on the router where cables connect (like a computer's LAN/USB port).
- **HWIC (High-speed WAN Interface Card)**: A modular expansion card slot on the router (like a PCIe slot on a motherboard) used to add interfaces such as serial ports or switch ports not built in by default.
- **VTY line**: Virtual TeletYpe line — used for remote access (Telnet/SSH), as opposed to the physical console line.
- **NVRAM**: Non-Volatile RAM — retains data (the `startup-config`) even without power.
- **MOTD**: Message Of The Day — a login banner.
- **RAM vs NVRAM vs Flash**:
  - RAM: holds `running-config`; wiped on power loss.
  - NVRAM: holds `startup-config`; persists through power loss.
  - Flash: persistent storage (like a USB drive) that holds the IOS image itself (the router's operating system).
- **`copy running-config startup-config` vs `write memory`**: Functionally identical (both save running-config to NVRAM); `write memory` (`wr`) is the older/legacy syntax, while `copy run start` is the modern standard command syntax.
