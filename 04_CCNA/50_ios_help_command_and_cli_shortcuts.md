# Cisco IOS – Study Notes

## Topic 1: The Help Command (`?`)

The Cisco IOS CLI includes a **context-sensitive help system** accessible via the `?` key.
"Context-sensitive" means the output changes depending on which **mode** you are currently in.

---

### 1.1 Cisco IOS Modes (Quick Reference)

| Mode | Prompt Example | Access Command |
|---|---|---|
| User EXEC | `Switch>` | Default on login |
| Privileged EXEC | `Switch#` | `enable` |
| Global Configuration | `Switch(config)#` | `configure terminal` |

---

### 1.2 Uses of the `?` Command

#### List All Available Commands
Type `?` alone to display every command available in your current mode.
```
Switch> ?
Switch# ?
Switch(config)# ?
```

#### Complete a Partial Command (Command Lookup)
Type the beginning of a command followed immediately by `?` (no space) to find matching commands.
```
Switch(config)# in?
  interface
```

#### Show Required Parameters / Arguments
Type a command, add a **space**, then `?` to see what comes next.
```
Switch(config)# interface ?
  Ethernet         IEEE 802.3
  FastEthernet     FastEthernet IEEE 802.3
  GigabitEthernet  GigabitEthernet IEEE 802.3
  Vlan             Catalyst Vlans
  range            interface range command
```

---

### 1.3 The Command Syntax Checker

The IOS automatically validates every command entered. There are three types of errors:

| Error Type | Meaning | Example |
|---|---|---|
| **Invalid Input** | A value or keyword does not exist | Typing `33` instead of `vlan` or `range` |
| **Ambiguous Command** | Multiple commands match the letters typed | Typing `i` alone (matches both `interface` and `ip`) |
| **Incomplete Command** | Command entered without all required arguments | Typing `interface` and pressing Enter with no interface name |

> **Tip:** When an invalid input error occurs, the IOS places a caret (`^`) under the exact position where the mistake begins, making troubleshooting much faster.

---

## Topic 2: Hotkeys & Shortcuts

Cisco IOS supports a range of keyboard shortcuts that significantly speed up CLI configuration.

---

### 2.1 Command Completion

#### Tab Key – Auto-complete
Press `Tab` after typing the first few letters of a command to auto-complete it.
- Only works if the letters typed **uniquely identify** one command.
- If multiple commands match, Tab will not complete — add more letters first.

```
Switch# en[Tab]  →  enable
Switch# conf[Tab]  →  configure
Switch(config)# t[Tab]  →  terminal
```

#### Command Shortening – No Tab Required
You can omit the Tab key entirely. The IOS accepts abbreviated commands as long as they are **unambiguous**.

```
Switch(config)# int f 0/1
```
This is equivalent to `interface fastethernet 0/1`.

---

### 2.2 Command History

| Key | Action |
|---|---|
| `↑` (Up Arrow) | Recall the previous command |
| `↓` (Down Arrow) | Move forward in command history |

Useful for repeating commands without retyping them.

---

### 2.3 Control Key Shortcuts

| Shortcut | Function |
|---|---|
| `Ctrl + Z` | Exit to Privileged EXEC Mode immediately |
| `Ctrl + C` | Cancel current command / Exit to Privileged EXEC Mode |
| `Ctrl + A` | Move cursor to the **beginning** of the line |
| `Ctrl + E` | Move cursor to the **end** of the line |
| `Ctrl + Shift + 6` | **Interrupt / abort** a running command (e.g., stuck DNS lookup) |
| `Ctrl + R` | Redisplay the current line (useful when a system message interrupts your typing) |

---

### 2.4 When to Use `Ctrl + Shift + 6`

If you mistype a hostname or command, the IOS may attempt to resolve it as a DNS address and appear to freeze.  
Press `Ctrl + Shift + 6` to **force-stop** the process immediately.

---

### 2.5 When to Use `Ctrl + R`

While typing a command, the device may display a **system log message** that disrupts your input on screen.  
Press `Ctrl + R` to **refresh and redisplay** your incomplete command at a clean prompt.

> **Note:** `Ctrl + R` may not be supported in all versions of Packet Tracer. It works on physical Cisco devices.

---

## Summary

| Skill | Tool |
|---|---|
| Find available commands | `?` |
| Complete a command | `?` after partial input, or `Tab` |
| See required parameters | space + `?` after a command |
| Fix ambiguous / incomplete errors | Syntax Checker output |
| Repeat a recent command | Arrow keys |
| Exit or cancel | `Ctrl + Z` / `Ctrl + C` |
| Abort a stuck command | `Ctrl + Shift + 6` |
| Recover from screen disruption | `Ctrl + R` |
