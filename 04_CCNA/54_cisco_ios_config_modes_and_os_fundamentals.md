# Cisco IOS Study Notes

## 1. Running Configuration File (`running-config`)

**Key fact:** Changes take effect **immediately** when a command is entered and Enter is pressed.

| Property | Detail |
|----------|--------|
| Storage location | RAM (volatile) |
| When changes apply | Instantly upon command entry |
| Lost when? | On reboot/power loss if not saved |
| How to save permanently | `copy running-config startup-config` |

> ⚠️ **Apply ≠ Save.** Applying a change is automatic. Saving requires a manual command.

**Wrong options to watch out for:**
- ❌ Stored in NVRAM → that's `startup-config`
- ❌ `erase running-config` command → does not exist; use `erase startup-config`
- ❌ Auto-saved on reboot → must be saved manually

---

## 2. User EXEC Mode

**Prompt:** `Router>`  
**Access level:** Read-only, lowest privilege

**What you CAN do:**
- View limited router configuration (`show` commands)
- Use it as an entry point to access higher modes

**What you CANNOT do:**
- Change configurations
- Access all commands

**Wrong options to watch out for:**
- ❌ `enable` → goes to **Privileged EXEC** (`#`), not Global Config
- ❌ Can configure interfaces/routing protocols → requires higher privilege
- ❌ All commands available → only a very limited set

---

## 3. `enable secret` Command

**Protects:** Access to **Privileged EXEC mode** (`Router#`)

**How it works:**
- When a user types `enable` from User EXEC mode, they are prompted for this password
- Without it, anyone can escalate to full admin access

| Access Type | How to Secure |
|-------------|---------------|
| **Privileged EXEC** (`#`) | `enable secret` |
| Console port (physical cable) | `line console 0` → `password` |
| Remote access (SSH/Telnet) | `line vty 0 4` → `password` |
| AUX port | `line aux 0` → `password` |

> 💡 **Analogy:** User EXEC = guest room. Privileged EXEC = private office. `enable secret` = the deadbolt on the office door.

---

## 4. Default SVI (Switch Virtual Interface)

**Answer: VLAN 1**

- **VLAN:** A virtual "room" inside a switch
- **SVI:** A virtual interface (gateway) for managing that VLAN
- By default, all switch ports belong to **VLAN 1**, so Cisco automatically creates an SVI for VLAN 1

> All other VLANs (99, 100, 999, etc.) must be manually created and assigned an SVI.

---

## 5. Hostname Naming Conventions (Cisco CLI)

Three rules that **must** be followed:

| Rule | Detail |
|------|--------|
| ✅ Fewer than 64 characters | Avoids management issues |
| ✅ No spaces | Spaces break command parsing (use `-` or `_` instead) |
| ✅ Must begin with a letter | Prevents confusion with IP addresses or numeric data |

**Not required:**
- ❌ Must end with special characters → false
- ❌ Must be all lowercase → uppercase is allowed (e.g., `Router-Office-01`)

---

## 6. Shell in an OS

**Function:** Acts as the interface between the **user** and the **kernel**

| Component | Role |
|-----------|------|
| **Kernel** | Core engine; controls hardware directly |
| **Shell** | Translator/middleman; takes user commands and passes them to the kernel |
| **User** | Gives instructions via the shell |

> 💡 **Analogy:** You (user) → Waiter (shell) → Chef (kernel)

**Wrong options:**
- ❌ Provides firewall services → separate security software
- ❌ Interacts with hardware directly → that's the kernel's job
- ❌ Provides intrusion prevention → separate security solution

---

## 7. Router Boot: What Mode Appears?

**Scenario:** Valid OS + startup-config exists in NVRAM + `enable secret` set + **no console password**

**Result: User EXEC mode (`>`)**

**Why:**
- No console password = front door is unlocked → router lets you in without asking
- Even though `enable secret` exists, it only applies when escalating to Privileged EXEC
- The router drops you into the lowest mode by default

**Mode comparison:**

| Mode | Appears when... |
|------|----------------|
| **Setup mode** | No startup-config found in NVRAM |
| **User EXEC (`>`)** | startup-config exists, no console password |
| **Privileged EXEC (`#`)** | Console password set + authenticated |
| **Global Config** | Never on boot; must be entered manually |

---

## 8. Applying vs. Saving Configuration Changes

| Action | Command | Effect |
|--------|---------|--------|
| **Apply** | Just press Enter after typing the command | Immediate, no extra step needed |
| **Save** | `copy running-config startup-config` | Persists across reboots |

**Wrong options:**
- ❌ Reload the device → not needed to apply; risks losing unsaved changes
- ❌ Copy startup-config → running-config → overwrites your new settings with old ones
- ❌ Copy running-config → startup-config → this is "saving", not "applying"

---

## 9. Key Terms Glossary

| Term | Meaning |
|------|---------|
| **Console port** | Physical port on a router/switch for direct cable access; the "emergency door" |
| **Console password** | Password required when connecting via console cable |
| **enable secret** | Password required to escalate from User EXEC → Privileged EXEC |
| **VTY lines** | Virtual Teletype lines; remote access paths via SSH/Telnet |
| **running-config** | Active config in RAM; volatile |
| **startup-config** | Saved config in NVRAM; persists after reboot |
| **Shell** | Interface between user and OS kernel |
| **Kernel** | Core of the OS; manages hardware |
| **SVI** | Switch Virtual Interface; virtual gateway for a VLAN |
| **NVRAM** | Non-volatile RAM; retains data after power loss |
