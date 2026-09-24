# Cisco IOS Basics — Study Notes

## 1. Accessing a Network Device (Connection Methods)

| Method | Type | Use Case |
|--------|------|----------|
| **Console** | Out-of-band | First-time setup of a **brand-new device**. Requires a physical rollover/console cable directly plugged into the device's console port. Works even with zero network configuration. |
| **Telnet / SSH** | In-band | Remote access **over an existing network**. Requires the device to already have IP/network settings configured. SSH is the secure version of Telnet. |
| **Aux (Auxiliary)** | Out-of-band | Legacy emergency remote access via a **telephone line (modem)**. Used when the network is down and you need to manage a remote device. Rarely used in modern environments. |

### Key Decision Rules
- **New device with no config?** → Use **Console**
- **Manager hands you a special cable?** → **Console** (rollover cable)
- **Managing remotely over the network?** → **Telnet / SSH**
- **Network is down, device is in another city?** → **Aux** (telephone line)
- **"In-band" access question?** → **Telnet / SSH**
- **"Out-of-band" access question?** → **Console** or **Aux**

---

## 2. Cisco IOS Command Modes

Think of these as **floors in a building** — each floor gives you different abilities. You must use specific commands to move between them.

```
User EXEC Mode      →  enable         →  Privileged EXEC Mode
                    ←  disable        ←

Privileged EXEC     →  configure terminal  →  Global Config Mode
                    ←  exit               ←

Global Config       →  interface [name]   →  Interface Config Mode
                    →  line console 0     →  Line Config Mode
                    ←  exit               ← (one level back)

Any sub-mode        →  end  /  Ctrl+Z     →  Privileged EXEC Mode (jump to top)
```

### Mode Summary Table

| Mode | Prompt | Access Level | What You Can Do |
|------|--------|-------------|-----------------|
| **User EXEC** | `Switch>` | Lowest | Basic status checks only. Read-only. No config changes. |
| **Privileged EXEC** | `Switch#` | Full admin | All commands — save config, reboot, debug, view everything. |
| **Global Config** | `Switch(config)#` | Config | Change device-wide settings (hostname, passwords, etc.) |
| **Interface Config** | `Switch(config-if)#` | Sub-config | Configure a specific port/interface |
| **Line Config** | `Switch(config-line)#` | Sub-config | Configure console or VTY (remote) access lines |

---

## 3. Navigation Commands (Cheat Sheet)

| Command | From → To | Notes |
|---------|-----------|-------|
| `enable` | User EXEC `>` → Privileged EXEC `#` | Gain admin access |
| `disable` | Privileged EXEC `#` → User EXEC `>` | Drop back to limited access |
| `configure terminal` (or `config t`) | Privileged EXEC `#` → Global Config `(config)#` | Enter config mode |
| `exit` | Current mode → one level up | Goes back **one step only** |
| `end` | Any sub-config → Privileged EXEC `#` | Jump straight to the top |
| `Ctrl + Z` | Any sub-config → Privileged EXEC `#` | Same as `end` — the "panic button" |
| `interface [name]` | Global/sub-config → Interface Config `(config-if)#` | Jump directly to a port |
| `line console 0` | Global Config → Line Config (console) | Configure the console port |
| `line vty 0 15` | Global Config → Line Config (VTY) | Configure remote access (Telnet/SSH) lines |

### Pro Tips
- **Direct jump between sub-modes**: You don't need to `exit` first. Typing `interface vlan 1` from Line Config mode takes you directly to Interface Config mode.
- **The golden rule**: If a command isn't working, **check your prompt**. You're probably in the wrong mode. Beginners commonly try to run Global Config commands while in Interface Config mode.
- **`Ctrl+Z` = Home button**: Lost deep in sub-menus? `Ctrl+Z` always brings you back to `Switch#`.

---

## 4. Prompt Quick-Reference

```
Switch>            →  User EXEC Mode
Switch#            →  Privileged EXEC Mode
Switch(config)#    →  Global Configuration Mode
Switch(config-if)# →  Interface Configuration Mode
Switch(config-line)# → Line Configuration Mode
```

> **Rule of thumb**: See `>` → read-only. See `#` → admin power. See `(config...)` → you're changing settings.

---

## 5. Why These Modes Exist

The mode hierarchy is a **safety mechanism**:
- Prevents accidental changes to critical settings
- Forces you to "unlock" higher levels of access before making changes
- Limits the blast radius of mistakes — you can only change what the current mode allows

---

## 6. Key Vocabulary

| Term | Meaning |
|------|---------|
| **IOS** | Internetwork Operating System — Cisco's device OS |
| **EXEC** | Short for *Execute* — a mode where you can run commands |
| **Privileged** | Having special rights/permissions (= admin) |
| **Global** | Applies to the **entire device** (not just one port) |
| **In-band** | Management traffic travels over the **same network** as regular data |
| **Out-of-band** | Management uses a **separate, dedicated physical path** (console cable, modem) |
| **Console** | Direct physical connection to a device for local management |
| **Blank slate** | A device with no configuration — fresh out of the box |
| **Rollover cable** | The special flat cable used for console connections |
| **VTY** | Virtual Terminal — logical lines used for remote (Telnet/SSH) access |
