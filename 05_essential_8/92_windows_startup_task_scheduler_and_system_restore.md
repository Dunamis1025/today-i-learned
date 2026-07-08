# Windows OS Maintenance — Study Notes

## 1. Preventive Maintenance Plan

A preventive maintenance plan keeps an OS reliable by reducing downtime, improving performance, and lowering repair costs. Key components:

- **Routine maintenance** — disk error checking, defragmentation, backups.
- **Updates** — keep OS, applications, and security software current.
- **Documentation** — maintain a repair log to track recurring hardware/software issues.
- **Scheduling** — run maintenance during low-usage hours (nights/weekends) to avoid disrupting users.
- **Security** — install antivirus/antimalware, run regular scans, use tools like the Windows Malicious Software Removal Tool.
- **Startup configuration** — ensure critical software (e.g., antivirus) launches automatically at boot.

---

## 2. Lab: Managing the Startup Folder

**Goal:** Control which applications launch automatically when Windows starts, using three different mechanisms.

### Part 1 — Startup Folder
- Create a shortcut to an executable (e.g., `msedge.exe`).
- Open the Startup Folder via Run → `shell:startup`.
- Any shortcut placed here launches automatically on boot.

### Part 2 — Task Manager
- Task Manager's **Startup tab** lists all apps configured to auto-launch.
- Only desktop applications can appear here — Windows Store (UWP) apps cannot.

### Part 3 — Windows Registry
- Path: `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run`
- Adding a new **String Value** here (name + path to the .exe) forces that program to launch at every login.
- This is a common location malware also (ab)uses to persist across reboots — a key spot IT/security staff check when diagnosing unwanted auto-run behavior.

### Part 4 — Disabling Startup Apps
- In Task Manager's Startup tab, right-click → **Disable**.
- The entry stays visible in the list but no longer launches at boot.
- The **Startup impact** column shows how much each program slows down boot time (None/Low/Medium/High).

**Reflection:** Users disable auto-launching programs to speed up boot time, reduce resource usage, and prevent unwanted/unknown software from running silently.

---

## 3. Windows Updates

- Windows Update (`update.microsoft.com`) delivers maintenance updates, critical updates, and security patches.
- Uses **BITS** (Background Intelligent Transfer Service) to download/install updates.
- Microsoft releases updates on the second Tuesday of each month — **"Patch Tuesday."**
- Windows 10 auto-downloads/installs updates; usually only a restart is required to finish.
- Manual check: **Settings → Update & Security**.
- Update history/log: `windowsupdate.log` in `%SystemRoot%`; failed updates can be diagnosed via error codes in the Microsoft Knowledge Base, and problematic updates can be uninstalled from **View Update History**.

### Driver Updates
- Drivers translate between OS and hardware.
- Update when hardware misbehaves or for security fixes.
- If a new driver causes problems, use **Roll Back Driver** to revert.

### Firmware Updates
- Less frequent than driver updates; embedded directly in hardware.
- Can improve speed, add features, or increase stability.
- Riskier — failed/incorrect updates can permanently damage hardware, and reverting is often impossible. Follow manufacturer instructions carefully.

---

## 4. Task Scheduler

**Purpose:** Automate running programs, scripts, or batch files at scheduled times — no manual intervention needed.

### Basic workflow
1. Open via Start → **Windows Administrative Tools → Task Scheduler**.
2. Click **Create Basic Task** → give it a name/description.
3. Choose a trigger: daily, weekly, monthly, one-time, at boot, at logon, or on a specific logged event.
4. Choose the action: **Start a program** (sending email/message options are deprecated).
5. Select the executable (or script/batch file) to run.

### Example: Automating Disk Cleanup
- Executable: `cleanmgr.exe` (found in `System32`).
- Since Disk Cleanup normally requires manual clicks, use command-line arguments to fully automate it:
  - `cleanmgr.exe /sageset:1` — opens Disk Cleanup once to let you pick options (temp files, Recycle Bin, Downloads, etc.); saves these choices to the registry under "instance 1."
  - `cleanmgr.exe /sagerun:1` — silently runs Disk Cleanup using the saved "instance 1" settings, with no user interaction needed.
- In Task Scheduler, set the program to `cleanmgr.exe` with argument `/sagerun:1` so it runs unattended on schedule (e.g., every Sunday at 11:55 PM).

### Managing scheduled tasks
- From the Task Scheduler Library, you can: run a task immediately, end it, disable it, export/import it to another PC, modify its properties, or delete it.

---

## 5. Lab: System Restore and Hard Drive Backup

### Part 1 — System Restore
**Concept:** A restore point is a snapshot of system settings (not personal files) that lets you undo problematic changes (e.g., a bad install) without losing documents.

Steps performed:
1. Create a restore point named "Application Installed" (Control Panel → System → System Protection → Create).
2. Install a Windows feature (**Internet Information Services / IIS**) as a test change — verified via `http://localhost` and IIS Manager.
3. Save a test file in Documents (`Restore Point Test file`).
4. Run System Restore back to "Application Installed" — this triggers a restart.
5. After restore completes, verify:
   - IIS Manager is no longer installed.
   - `http://localhost` no longer shows the IIS page.
   - The test file in Documents **still exists**, because System Restore only reverts system/program settings — it does not touch personal data files.

**Key concept:** System Restore ≠ file backup. It protects system configuration/programs, not documents.

### Part 2 — File History (Hard Drive Backup)
**Concept:** File History automatically backs up personal files (Desktop, Documents, etc.) to an external drive or network location, creating multiple timestamped versions you can browse and restore from.

Steps performed:
1. Turn on File History (Control Panel → File History), pointing to an external drive.
2. Create two test files on the Desktop; run a backup (**Run now**).
3. Modify/delete the files, run another backup.
4. Use **Restore personal files** to browse different backup versions (shown as "1 of 2," "2 of 2," etc.) and step through history using the navigation arrows.
5. Restore individual files/versions, including recovering an earlier version of a file whose content changed later.
6. Clean up: delete test files, turn File History off.

**Key concept:** Each backup run creates a new "version" you can step back through — useful for recovering deleted files or earlier edits, unlike System Restore which only affects system settings.

---

## Summary Comparison

| Feature | Protects | Reverts Whole System? | Typical Use |
|---|---|---|---|
| **Startup Folder / Registry Run key / Task Manager** | Boot-time program launches | No | Control what auto-starts |
| **Task Scheduler** | Automated recurring tasks | No | Run maintenance (e.g., disk cleanup) unattended |
| **System Restore** | System settings & installed programs | Yes (to a point in time) | Undo a bad install/update |
| **File History** | Personal files (Documents, Desktop, etc.) | No (file-level only) | Recover deleted/changed files |
