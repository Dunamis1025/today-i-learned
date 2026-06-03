# Cisco Switch Configuration Management — Study Notes

> **Topic:** How to save, erase, and revert configurations on a Cisco switch using Packet Tracer  
> **Skill Level:** Beginner  
> **Source:** Video walkthrough of Cisco switch CLI management

---

## 🧠 The Core Concept: Two Types of Memory

Everything in this topic comes down to understanding **two storage areas** inside a switch:

| Memory Type | Name in CLI | Volatile? | What it holds |
|---|---|---|---|
| **RAM** | `running-config` | ✅ Yes (wiped on power loss) | Current, active configuration |
| **NVRAM** | `startup-config` | ❌ No (survives reboots) | Permanently saved configuration |

**Rule of Thumb:**  
> If you change a setting but don't save it, it's gone after a reboot.  
> Always copy `running-config` → `startup-config` to make changes permanent.

---

## 🎬 The Inception Analogy (Mode Hierarchy)

Think of CLI modes like **layers of a dream** in the movie *Inception*:

```
Reality (User Mode)
  └── 1st Dream: Privileged Exec Mode  [enable]
          └── 2nd Dream: Global Config Mode  [configure terminal]
                  └── Deep Unconscious: NVRAM  [startup-config]
```

| Dream Level | CLI Mode | How to Enter | What You Can Do |
|---|---|---|---|
| Reality | User EXEC Mode | (default on login) | Very limited — view only |
| 1st Dream | Privileged EXEC Mode | `enable` | Manage files, save, reload, erase |
| 2nd Dream | Global Config Mode | `configure terminal` | Modify device settings (hostname, passwords, etc.) |
| Deep Unconscious | NVRAM (`startup-config`) | via `copy` commands | Permanent memory — survives reboots |

**`exit`** = waking up one level (going back up one dream layer)  
**`reload`** = fully waking up (rebooting the switch) — then falling back into a new dream based on what's stored in NVRAM

---

## 📋 Step-by-Step: What the Instructor Did (In Order)

### Part 1 — Saving a Configuration

| Step | Command | Purpose |
|---|---|---|
| 1 | `enable` → password: `cisco` | Enter Privileged EXEC Mode (1st dream) |
| 2 | `configure terminal` | Enter Global Config Mode (2nd dream) |
| 3 | `hostname S1` | Rename the switch to "S1" as a visible test change |
| 4 | `exit` | Return to Privileged EXEC Mode |
| 5 | `copy running-config startup-config` | **[SAVE]** Copy active settings (RAM) → permanent storage (NVRAM) |
| 6 | *(press Enter to confirm filename)* | Accept default filename `startup-config` |
| 7 | `dir nvram:` | Verify the saved file exists in NVRAM |
| 8 | `reload` | Reboot the switch to confirm settings survive a power cycle |

✅ **Result:** After reload, hostname "S1" and banner message are still there → save was successful.

---

### Part 2 — Erasing a Configuration (Factory Reset)

| Step | Command | Purpose |
|---|---|---|
| 1 | `erase startup-config` | **[DELETE]** Wipe the saved config file from NVRAM |
| 2 | *(press Enter to confirm)* | Confirm the erase operation |
| 3 | `reload` | Reboot to confirm the device starts fresh |

✅ **Result:** After reload, no hostname, no banner, no password prompt → device is factory fresh.

---

### Part 3 — Reverting to Last Saved State (Rollback)

| Step | Command | Purpose |
|---|---|---|
| 1 | `enable` | Re-enter Privileged EXEC Mode |
| 2 | `configure terminal` | Enter Global Config Mode |
| 3 | `hostname MySwitch` | Set hostname to "MySwitch" |
| 4 | `exit` | Return to Privileged EXEC Mode |
| 5 | `copy startup-config running-config` | **[SAVE]** Save "MySwitch" state to NVRAM |
| 6 | *(back in config mode)* | Make more changes: add console password, rename to "S1" |
| 7 | `copy startup-config running-config` | **[ROLLBACK]** Load NVRAM's saved state back into RAM |

✅ **Result:** The switch reverts to "MySwitch" — the unsaved changes ("S1") are discarded.

> ⚠️ **Important:** `copy startup-config running-config` does NOT fully erase running-config.  
> It **merges** the startup-config into the running-config. The last saved state takes precedence.

---

## 🔑 The 3 Core Commands (Cheat Sheet)

```bash
# SAVE — Make current settings permanent
copy running-config startup-config
# Shortcut:
copy run start

# ERASE — Wipe saved config (factory reset prep)
erase startup-config

# ROLLBACK — Revert to last saved state
copy startup-config running-config
# Shortcut:
copy start run
```

---

## 💡 Pro Tips from the Video

- **Command Shortening:** You don't have to type full command names.
  - `copy running-config startup-config` → `copy run start`
  - `erase startup-config` → type `erase sta` then press **Tab** to autocomplete

- **The `dir` command:** Use `dir nvram:` to list files stored in NVRAM and confirm your save worked.

- **Interactive prompts:** The CLI will ask for confirmation on destructive actions (like `erase`). Pressing **Enter** accepts the default answer shown in brackets `[ ]`.

- **`reload` as a test:** After saving, reloading the switch is the best way to verify your configuration truly persisted.

---

## 🗂️ Storage Locations Summary

| Storage | Command Reference | Volatile | Contains |
|---|---|---|---|
| Flash Memory | — | ❌ No | IOS Operating System |
| NVRAM | `startup-config` | ❌ No | Saved configuration file |
| RAM | `running-config` | ✅ Yes | Active/current configuration |

---

## 🎯 Key Takeaway

> The entire video teaches one thing:  
> **How to move your configuration between RAM (temporary) and NVRAM (permanent).**

- **RAM** = your working draft. Fast, flexible, but gone after reboot.  
- **NVRAM** = your saved document. Safe, permanent, survives everything.  
- Every command (`copy`, `erase`, `reload`) is just managing data between these two places.
