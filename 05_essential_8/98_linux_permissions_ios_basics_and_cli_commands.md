# Study Notes: Linux Permissions, iOS, and CLI Commands

## 1. Linux File Permissions (chmod)

**Scenario:** A team creates a `webteam` group and a `webpages` directory for a company website. Team members report they cannot create or edit files inside `webpages`. Running `ls -l` shows the permissions as `drwxr-xr--`.

**Answer:** `chmod 775 -R webpages`

**Explanation:**
- Linux permissions are split into three categories: **Owner**, **Group**, and **Others**.
- In `drwxr-xr--`, the group portion is `r-x` — read and execute allowed, but **no write permission**. That's why group members can't create or modify files.
- `chmod 775` sets the group permission to `rwx` (read, write, execute), fixing the issue.
- The `-R` flag means **recursive** — it applies the new permissions to the directory itself *and* all files/subdirectories inside it, all at once.

| Permission Set | Meaning |
|---|---|
| Owner (`rwx`) | Full control |
| Group (`rwx` after fix) | Read, write, execute |
| Others (`r--`) | Read only |

---

## 2. iOS Home Button Functions

**Question:** What two tasks can be performed using the Home button on an iOS device?

**Answer:** Wake the device, and return to the home screen.

**Explanation:**
- **Wake the device:** Pressing the Home button when the screen is off/locked turns the screen on.
- **Return to the home screen:** Pressing it while inside an app closes/minimizes that app and returns to the main home screen.
- Other actions (organizing apps into folders, responding to alerts, showing navigation icons) are done via touch gestures, **not** the Home button.

---

## 3. Linux CLI Commands and Their Functions

| Command | Function |
|---|---|
| `man` | Displays documentation/help for a specific command |
| `mkdir` | Creates a new directory under the current directory |
| `ls` | Lists the files inside a directory |
| `cd` | Changes the current directory (navigation) |
| `rm` | Removes (deletes) files |
