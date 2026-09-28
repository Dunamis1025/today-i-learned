# Day 04: Basic Device Security Configuration Lab

> Notes for Day 04 of Jeremy's IT Lab CCNA 200-301 course — **Basic Device Security** lab, covering Cisco IOS CLI mode navigation, hostname configuration, and progressively securing Privileged EXEC access with `enable password`, `service password-encryption`, and `enable secret`.

---

## 1. Accessing a Cisco Device

| Context | Access Method |
|---------|----------------|
| **Real-world / physical device** | Connect a PC to the device's **Console Port** using a cable (see Day 03 notes: this requires a **Rollover cable**, not Crossover) |
| **Packet Tracer lab** | Click directly on the device → **CLI tab** — a shortcut that skips the physical cabling step for practice purposes |

---

## 2. Cisco IOS CLI Modes

Cisco IOS has a hierarchy of command modes, each with a distinct prompt and its own set of available commands.

| Mode | Prompt | How to Enter |
|------|--------|----------------|
| **User EXEC Mode** | `Router>` | Default mode on connecting to the device |
| **Privileged EXEC Mode** | `Router#` | Type `enable` (short form: `en`) from User EXEC |
| **Global Configuration Mode** | `Router(config)#` | Type `configure terminal` (short form: `conf t`) from Privileged EXEC |

### Mode Hierarchy (Least → Most Privileged/Deep)

```
User EXEC (Router>)
      ↓ enable
Privileged EXEC (Router#)
      ↓ configure terminal
Global Configuration (Router(config)#)
```

### A Note on Command Abbreviation Ambiguity

Cisco IOS allows abbreviating commands as long as the abbreviation is unambiguous. Typing just `e` produces an error, because IOS cannot tell whether you mean `enable` or `exit` — both start with "e". This is called an **ambiguous command** error. You must type enough characters to make the command unique (e.g., `en` unambiguously means `enable`).

---

## 3. Lab Steps

### Step 1: Set the Hostname

Renaming a device makes it identifiable on the network (e.g., a router named `r1`, a switch named `switch1`).

```
Router(config)# hostname r1
```

After this command, the prompt itself changes to reflect the new name:
```
r1(config)#
```

### Steps 2–3: Configure and Test an Unencrypted `enable password`

This protects access to Privileged EXEC mode by requiring a password.

```
r1(config)# enable password CCNA
```

**Testing it:**
1. Type `exit` to return to User EXEC mode.
2. Type `enable` again — IOS now prompts for the password (`CCNA`).
3. **Three consecutive incorrect attempts** locks you out with a `% Bad secrets` error.

### Steps 4–6: Viewing the Running Configuration & Encrypting Passwords

**Viewing the active configuration** (the configuration currently loaded in RAM):

```
r1# show running-config
```
(short form: `sh run`) — must be run from **Privileged EXEC mode**.

**Problem discovered:** inspecting the running-config shows `enable password CCNA` stored in **plain, readable text** — anyone who views the configuration file can read the password directly.

**Using `do` to run Privileged EXEC commands from Global Config mode:**

Normally, `show` commands aren't available in Global Configuration mode (they belong to Privileged EXEC). Prefixing a command with `do` lets you run a Privileged EXEC command *without* leaving Global Config mode:

```
r1(config)# do show running-config
```

**Enabling password encryption:**

```
r1(config)# service password-encryption
```

This encrypts all currently-visible plaintext passwords in the configuration so they can no longer be read directly. After running this and checking `do show running-config` again, the password now appears as:

```
enable password 7 <encrypted string>
```

The `7` indicates **Type 7 encryption**.

> **Important caveat:** Type 7 encryption is **not cryptographically strong**. It's more of a "shoulder-surfing deterrent" (stops someone from casually reading your password off the screen) than real security — Type 7 can be reversed/decrypted fairly easily with widely available tools. It should not be relied on as strong protection.

### Steps 7–9: Configuring the Stronger `enable secret`

`enable secret` uses **MD5 hashing (Type 5)**, which provides significantly stronger protection than the Type 7 encryption used by `service password-encryption`.

```
r1(config)# enable secret Cisco
```

**Key behavior when both are configured:**

> If **both** `enable password` and `enable secret` are set on the same device, **only `enable secret` takes effect** — the `enable password` is ignored entirely (though it may still be visible in the running-config).

**Verifying in the running-config:**

```
r1(config)# do show running-config
```

The `enable secret` line appears with **Type 5 (MD5)** encryption — a cryptographic hash, distinct from the reversible Type 7 encoding used for `enable password`.

### Step 10: Saving the Configuration

Changes made so far exist only in the **Running Configuration**, which lives in **RAM** — this is lost if the device loses power. To make changes persistent, they must be copied to the **Startup Configuration**, stored in **NVRAM** (non-volatile memory that survives a reboot/power loss).

**Three equivalent ways to save:**

```
write
```
```
write memory
```
```
copy running-config startup-config
```

**Verifying the save:**

```
r1# show startup-config
```

---

## 4. Password Type Comparison

| Command | Encryption Type | Strength | Behavior |
|---------|-------------------|----------|----------|
| `enable password` | None by default (plaintext); Type 7 if `service password-encryption` is enabled | Weak — Type 7 is easily reversible | Ignored entirely if `enable secret` is also configured |
| `enable secret` | Type 5 (MD5 hash), always, automatically | Strong — not designed to be reversible | Always takes priority over `enable password` |

This directly echoes the Day 03 note on `service password-encryption`: **`enable secret` is always encrypted regardless of the `service password-encryption` setting**, because it hashes on its own at configuration time.

---

## 5. Running Config (RAM) vs. Startup Config (NVRAM)

| Configuration | Storage | Persists Through Reboot? | Command to View |
|-----------------|---------|-----------------------------|-------------------|
| **Running-config** | RAM | ❌ No — lost on power loss/reboot | `show running-config` (`sh run`) |
| **Startup-config** | NVRAM | ✅ Yes | `show startup-config` |

**Rule of thumb:** any change you make to a Cisco device only affects the running-config until you explicitly save it (`write` / `copy running-config startup-config`) — if you forget to save and the device restarts, all unsaved changes are lost.

---

## 6. Command Cheat Sheet

| Command | Purpose |
|---------|---------|
| `enable` (`en`) | Enter Privileged EXEC mode |
| `configure terminal` (`conf t`) | Enter Global Configuration mode |
| `hostname [name]` | Set the device's hostname |
| `enable password [password]` | Set a (weak) Privileged EXEC password |
| `service password-encryption` | Encrypt plaintext passwords in the config (Type 7 — weak) |
| `enable secret [password]` | Set a strong Privileged EXEC password (Type 5 / MD5) |
| `do [command]` | Run a Privileged EXEC command while in Global Config mode |
| `show running-config` (`sh run`) | View the currently active (RAM) configuration |
| `show startup-config` | View the saved (NVRAM) configuration |
| `write` / `write memory` / `copy running-config startup-config` | Save the running-config to startup-config (persist changes) |

---

## 7. Quick Summary

- Cisco IOS has three core CLI modes: User EXEC (`>`) → Privileged EXEC (`#`) via `enable` → Global Configuration (`(config)#`) via `configure terminal`.
- `enable password` sets a weak, plaintext-by-default password for Privileged EXEC access; it's stored in cleartext unless `service password-encryption` is enabled (which only applies weak, reversible Type 7 encoding).
- `enable secret` sets a strong password, always hashed with MD5 (Type 5), and always overrides `enable password` if both are configured.
- `do [command]` lets you run Privileged EXEC-only commands (like `show running-config`) without leaving Global Config mode.
- Changes live only in the running-config (RAM) until saved to the startup-config (NVRAM) with `write` or `copy running-config startup-config` — otherwise they're lost on reboot.

---

## 8. Review Questions

| Question | Answer |
|----------|--------|
| What command enters Privileged EXEC mode? | `enable` (`en`) |
| What command enters Global Configuration mode? | `configure terminal` (`conf t`) |
| Why does typing just `e` cause an error? | Ambiguous command — could mean `enable` or `exit` |
| What happens after 3 incorrect password attempts at the `enable` prompt? | Locked out with a "Bad secrets" error |
| What command shows the currently active (RAM) configuration? | `show running-config` (`sh run`) |
| How do you run a Privileged EXEC command while still in Global Config mode? | Prefix it with `do` |
| What encryption type does `service password-encryption` apply? | Type 7 (weak, reversible) |
| What encryption type does `enable secret` use? | Type 5 (MD5 hash, strong) |
| If both `enable password` and `enable secret` are configured, which one is used? | `enable secret` — the `enable password` is ignored |
| Where is the running-config stored, and does it survive a reboot? | RAM; no, it does not survive a reboot |
| Where is the startup-config stored, and does it survive a reboot? | NVRAM; yes, it survives a reboot |
| Name three commands that save the running-config to startup-config. | `write`, `write memory`, `copy running-config startup-config` |

---

## My Study Log

- [x] Watched Basic Device Security Day 4 Lab video
- [x] Practiced CLI mode navigation (User EXEC → Privileged EXEC → Global Config) in Packet Tracer
- [x] Configured hostname, `enable password`, `service password-encryption`, and `enable secret`
- [x] Verified running-config vs. startup-config behavior with `show running-config` / `show startup-config`
- [ ] Reviewed Day 04 Anki flashcards

### Notes / Confusing Points

- (add your own notes here)
