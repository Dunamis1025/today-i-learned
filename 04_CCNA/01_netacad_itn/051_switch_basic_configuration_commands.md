# Cisco Switch Basic Configuration — Study Notes

> **Topic:** Fundamental switch setup commands (Cisco IOS)
> **Level:** Beginner / Non-major friendly

---

## 1. Setting the Hostname

**Purpose:** Assign a unique name to a switch so administrators can identify which device they are logged into.

**Command:**
```
hostname Sw-Floor-2
```

**Key Points:**
- Must be typed as one word — `host name` (with a space) is invalid.
- This is typically the **very first command** run when configuring a new switch.
- Think of it as giving the machine a **name tag**.

---

## 2. Securing Privileged EXEC Mode (Administrator Mode)

**Purpose:** Protect the administrator-level access (Privileged EXEC mode) with an encrypted password.

**Command:**
```
enable secret class
```

| Part | Meaning |
|------|---------|
| `enable` | Command to enter Privileged EXEC mode |
| `secret` | Stores the password in **encrypted** form |
| `class` | The password value (example used in labs) |

**Key Points:**
- Using `enable secret` is more secure than `enable password` because it **automatically encrypts** the password in the config file.
- Privileged EXEC mode allows full configuration of the device — always protect it.

---

## 3. Enabling Password Authentication on User EXEC Mode

**Purpose:** Force users to enter a password when first connecting to the switch via console.

**Commands (run under `line console 0`):**
```
password cisco
login
```

| Command | Role |
|---------|------|
| `password cisco` | Sets the password value |
| `login` | **Activates** the password check |

**Key Points:**
- Setting a password alone is **not enough** — you must also type `login` to enforce it.
- Analogy: `password` creates the key; `login` turns on the lock.
- Without `login`, the switch lets anyone in even if a password is configured.

---

## 4. Encrypting All Plaintext Passwords

**Purpose:** Prevent passwords from being visible as plain text in the configuration file.

**Command:**
```
service password-encryption
```

**Key Points:**
- By default, simple passwords (console, VTY) are stored in **plain text** — anyone who views the config can read them.
- This command acts as a **master switch** that scrambles all existing and future plaintext passwords.
- Note: `enable secret` passwords are already encrypted by default; this command covers the rest.

---

## 5. Configuring a Login Banner (MOTD)

**Purpose:** Display a legal warning or notice to anyone attempting to connect to the switch.

**Command:**
```
banner motd $ Keep out $
```

| Part | Meaning |
|------|---------|
| `banner` | Tells the switch to create a display message |
| `motd` | "Message of the Day" — shown at login |
| `$ ... $` | **Delimiters** — mark the start and end of the message |

**Key Points:**
- Any character can be used as the delimiter, as long as it does **not appear inside the message**.
- Serves as a **legal deterrent** — proves unauthorized users were warned, which is important if legal action is ever needed.
- This banner appears **before** the login prompt.

---

## Quick Reference Summary

| Goal | Command |
|------|---------|
| Name the device | `hostname <name>` |
| Secure admin mode | `enable secret <password>` |
| Require password at console | `password <pw>` → `login` |
| Encrypt all plaintext passwords | `service password-encryption` |
| Show warning at login | `banner motd <delimiter> message <delimiter>` |

---

## Vocabulary

| Term | Meaning |
|------|---------|
| **VTY** (Virtual TeletYpe) | Virtual terminal lines used for remote access (Telnet/SSH) |
| **Privileged EXEC mode** | Administrator-level CLI mode; allows full device configuration |
| **User EXEC mode** | Basic read-only CLI mode; entered first upon connection |
| **Delimiter** | A character that marks the beginning and end of a string (e.g., `$`) |
| **Deterrent** | Something that discourages unauthorized access or behavior |
| **Prying eyes** | Unauthorized individuals who might read sensitive data |
| **Obscure** | To hide or make something unclear; used in "security through obscurity" |
| **MOTD** | Message of the Day — login banner message |
| **Plain text** | Unencrypted, human-readable text |
