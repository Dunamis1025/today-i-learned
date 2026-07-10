# Windows CLI & Software Installation — Study Notes

## 1. Installing Third-Party Software (Lab: Packet Tracer)

**Install steps:**
1. Log in as Administrator, locate the installer (`PacketTracer_<version>_Windows_<32/64>bit.exe`).
2. Run installer → accept license → keep default install location → keep default Start Menu folder → keep default additional tasks → click Install → Finish.
3. On first launch, log in with netacad.com / Skills for All credentials.

**Uninstall steps:**
1. Control Panel → Programs and Features.
2. Select Cisco Packet Tracer → right-click → Uninstall → confirm.
3. Verify it no longer appears in the list.

**Reflection:** Microsoft recommends using *Uninstall or change a program* (rather than manually deleting folders) because the proper uninstaller removes related registry entries, shared files, and system references cleanly — deleting folders manually can leave orphaned data or break the system.

---

## 2. Security & Business Considerations for Installing Software

**Security considerations:**
- Letting regular users freely install software is risky — they may be tricked into installing **malware** (malicious software), causing data theft or destruction, and potentially spreading across the whole network.
- IT policy should restrict software installation and keep antimalware tools (e.g., Windows Defender) active and updated.

**Impact to operation:**
- Manually installing software on hundreds of machines is inefficient.
- **Automated deployment tools** (e.g., Windows Group Policy / GPO) let admins push installer packages from a shared network location; software installs automatically when users log on — no admin rights needed by end users.
- Users typically only need read/execute permission on the install directory; personal settings are stored in the user's home folder to prevent accidental changes to program files.

**Impact to business:**
- **Software licensing** — must match the number of licensed devices/users; unlicensed use creates legal/financial risk.
- **Technical support** — decide whether issues are handled internally or outsourced to the vendor.
- **User training** — needed whenever software updates or new employees join; internal IT staff also need **in-depth (thorough) technical training** to securely support and maintain programs.

---

## 3. Key Term Check — Application Installation Concepts

| Concept | Meaning |
|---|---|
| Repair | Fixes a broken installed app without a full reinstall |
| Malware | Malicious software (e.g., encrypts your drive, steals/destroys data) |
| System requirements | Minimum hardware/software needed to run a program |
| Automated Install | Deploying software to many machines at once (e.g., via GPO) |
| Compatibility mode | Runs old software by emulating an older OS environment |
| Microsoft Store | Official, verified/safe source for downloading apps |

---

## 4. Windows Command Line Tools Overview

### PowerShell
- Modern, powerful CLI — supports **scripting** for automating repetitive tasks.
- Uses **cmdlets** (its native commands).
- Supports **aliases** (alternate names) so legacy commands (like `dir`, `ls`) still work, mapped internally to real cmdlets (e.g., `Get-ChildItem`).
- Comes with **Windows ISE**, an integrated scripting/development environment.

### Command Prompt (cmd)
- Legacy tool dating back to MS-DOS; largely replaced by PowerShell but still available for compatibility/simple tasks.
- Open via Start menu search (`cmd`), Win+X menu, or Run dialog (Win+R → `cmd`).
- `whoami` shows the current logged-in user and computer name.

---

## 5. Basic CLI Commands

| Command | Function |
|---|---|
| `help` | Lists all available commands |
| `command /?` | Shows detailed help for a specific command |
| `help \| more` | Pages long output one screen at a time (Space = next page, Enter = next line) |
| `cls` | Clears a **cluttered** (messy) screen |
| `↑` (Up Arrow) | Recalls the previous command, one at a time |
| `F7` | Pops up a window listing command history; navigate with arrows, Enter to run, Esc to close |
| `Ctrl+C` | Immediately aborts a running command |
| `exit` | Closes the command line window |

Alternative to F7: `doskey /history` prints the full command history directly to the screen.

---

## 6. Lab: Work in the Windows Command Shell (Practical Exercise)

**Goal:** Practice navigating files/folders via CMD.

1. Open Command Prompt as Administrator.
2. Use `help` and `help | more` to browse available commands.
3. Look up commands: `CD`, `CHKDSK`, `COPY`, `DEL`, `DIR`, `DISKPART`, `EXIT`, `FORMAT`, `GPRESULT`, `MD`, `TASKLIST`, `RD`, `ROBOCOPY`, `SHUTDOWN`, `XCOPY`.
4. Use `md /?` to learn nested directory creation.
   - **Create nested folders in one command:**
     ```
     md a\b\c
     ```
     (creates `C:\Users\ITEUser\a\b\c` in one step)
   - **Verify folder structure:**
     ```
     dir /s
     ```
     (or `tree` for a visual structure)
5. Clear the screen: `cls`
6. Press `F7` to view command history (Esc to close).
7. Press `↑` to recall the last command.
8. Type `exit` to close the terminal.

---

## 7. Command Syntax Conventions

| Symbol | Meaning |
|---|---|
| `< >` | Required value |
| `[ ]` | Optional value |
| `{ }` | Must choose one item from a list |
| `\|` (vertical bar) | **Mutually exclusive** choices — pick one, not both |
| `...` | The preceding item can repeat |
| `*` | Wildcard for any group of characters |
| `?` | Wildcard for a single character |

---

## 8. File System Navigation Commands

- **Switch drives:** type drive letter + colon, e.g. `D:`
- **`dir`** — lists files/folders in the current directory
  - `/a` — show all files, including hidden ones
  - `/o` — sort listing (e.g., by size)
  - `/w` — wide-format listing
- **`cd`** — change directory, e.g. `cd foldername`

---

## Key Vocabulary Learned
- **Malware** — malicious software designed to steal or destroy data
- **In-depth** — thorough, detailed, comprehensive
- **Aliases** — alternate names mapped to real commands
- **Cluttered** — messy, filled with too much output
- **Mutually (exclusive)** — cannot happen/be chosen together; only one option applies
