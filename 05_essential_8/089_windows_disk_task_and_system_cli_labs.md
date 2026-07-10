# Windows CLI Commands — Study Notes

Summary of two Cisco NetAcad labs: **Disk CLI Commands** and **Task and System CLI Commands**.

---

## 1. Disk CLI Commands

### `chkdsk` — Check Disk
Checks a volume's file system for errors and can repair some of them.

```
chkdsk <volume> [/f] [/r] [/x]
```

| Option | Meaning |
|---|---|
| `/f` | Fix errors found on the disk |
| `/r` | Same as `/f`, plus locates bad sectors and recovers readable data |
| `/x` | Forces the volume to dismount first if needed |

- Requires admin privileges.
- If the target volume is currently in use (e.g. `C:`), Windows can't lock it immediately and instead **schedules the check for the next restart**.

### `diskpart` — Partition Management
Opens its own sub-shell (`DISKPART>`) for managing disks/partitions/volumes — same functions as the GUI Disk Management tool.

Common commands:

| Command | Purpose |
|---|---|
| `list disk` | Show all physical disks |
| `select disk <n>` | Choose a disk to work on |
| `list partition` | Show partitions on selected disk |
| `list volume` | Show all volumes on the system |
| `select volume <n>` | Choose a volume to work on |
| `shrink desired=<MB>` | Shrink a volume to free up unallocated space |
| `shrink querymax` | Show the max size (MB) a volume can be shrunk by |
| `create partition primary` | Create a new primary partition from free space |
| `create partition extended` / `create partition logical` | Used when 4 primary partitions already exist |
| `format fs=ntfs label=<name>` | Format a new volume |
| `assign letter=<X>` | Assign a drive letter |
| `delete volume` | Delete the selected volume |
| `extend` | Grow the selected volume into adjacent free space |
| `exit` | Leave the diskpart shell |

**Typical workflow practiced:** shrink an existing NTFS volume → create a new partition in the freed space → format it (NTFS, then re-formatted to FAT32 with the standalone `format` command) → assign a drive letter → use it → delete it → extend the original volume back to full size.

⚠️ Formatting/deleting a volume **erases all data on it** — always back up first.

### `format` (standalone, outside diskpart)
```
format <volume> [/fs:<filesystem>] [/v:<label>] [/q]
```
- `/fs:` — specify file system (e.g. `fat32`, `ntfs`)
- `/v:` — set volume label
- `/q` — quick format (skips bad-sector scan)

---

## 2. Task and System CLI Commands

### `tasklist` — List Running Processes
```
tasklist
tasklist /?
tasklist | more                          # page results one screen at a time
tasklist /M <module.dll>                 # list processes using a given module/DLL
tasklist /FI "imagename eq notepad.exe"  # filter by process name
tasklist /FI "username eq <user>"        # filter by owning user
tasklist /FI "cputime gt 01:40:00"       # filter by cumulative CPU time
```
- Every running process has a unique **PID** (Process ID) — needed to target a specific instance precisely (useful when multiple processes share the same name, e.g. `chrome.exe`).
- Filter operators: `eq` (equal), `ne` (not equal), `gt`/`lt`/`ge`/`le` (greater/less than, etc.)
- **System Idle Process** is not a real program — it's a placeholder Windows uses to represent CPU time spent doing nothing (idle = "not in use").

### `taskkill` — Terminate a Process
```
taskkill /PID <pid>
taskkill /IM <imagename.exe>
taskkill /IM <imagename.exe> /T     # also kill child processes
taskkill /IM <imagename.exe> /T /F  # force-terminate if a graceful kill fails
taskkill /FI "username eq <user>"   # kill all processes owned by a user
```
- `/PID` targets one exact process instance; `/IM` targets by name (can match multiple PIDs at once, e.g. all `msedge.exe` instances).
- A graceful `taskkill` sometimes fails on processes that only accept forceful termination — add `/F`.
- **Key insight:** closing a program's visible window (GUI) does not always fully terminate its underlying process(es) — background processes can persist (e.g. Edge's Startup Boost keeps some processes alive after the window closes). `tasklist` reveals what's actually still running.
- Killing ordinary user apps (browsers, Notepad) is safe — only unsaved work is lost. Killing core system processes (e.g. `explorer.exe`) is riskier and can cause temporary display issues.

### `sfc` — System File Checker
```
sfc /scannow      # scan AND repair protected system files
sfc /verifyonly   # scan only, no repair
```
- Requires admin privileges.
- Verifies protected OS files against known-good cached copies and repairs corruption/missing files automatically.
- Result seen: *"Windows Resource Protection did not find any integrity violations"* → no problems found.

### `dism` — Deployment Image Servicing and Management
Used to inspect/service Windows images (drivers, features, editions).
```
dism /online /get-drivers                          # list 3rd-party drivers
dism /online /get-drivers /all                      # more detail
dism /online /get-drivers /all /format:table         # tabular output
dism /online /get-drivers /all /format:table | more  # page results
dism /online /get-drivers /all /format:table > results.txt   # save to file (overwrite)
dism /online /get-drivers /all /format:table >> results.txt  # append to file
```
- Requires admin privileges.
- `more <file>` or `type <file>` can be used afterward to view the saved output.

### `shutdown` — Power Control
```
shutdown /?
shutdown /l              # log off
shutdown /s /t 120       # shut down after 120 seconds (with on-screen warning)
shutdown /r              # restart
shutdown /h              # hibernate
shutdown /a              # abort a pending scheduled shutdown
shutdown /m \\<computer> # target a remote computer
```
- Useful when GUI shutdown fails, or for scripting/remote administration.
- A scheduled shutdown shows a countdown/warning notification; `/a` cancels it before it executes.

---

## Big Picture: Why This Matters
Both labs build core **IT support / sysadmin** skills:
- CLI tools work identically on machines with no GUI (servers) and can target **remote computers**, unlike mouse-driven tools.
- These commands are the basis for scripting and automating repetitive administration tasks across many machines (e.g. corporate IT managing hundreds of PCs).
- `tasklist`/`taskkill`, `sfc`, and `shutdown` are standard first-line troubleshooting tools for unresponsive systems or corrupted installations.

## Commands Practiced Today (Quick Reference)
```
tasklist
tasklist | more
tasklist /?
tasklist /M oleaut32.dll
tasklist /FI "imagename eq notepad.exe"
tasklist /FI "username eq yunho"
tasklist /FI "cputime gt 01:40:00"
taskkill /PID <pid>
taskkill /IM msedge.exe
taskkill /IM msedge.exe /T /F
sfc /scannow
dism /online /get-drivers
dism /online /get-drivers /all
dism /online /get-drivers /all /format:table
dism /online /get-drivers /all /format:table | more
shutdown /s /t 120
shutdown /a
```
