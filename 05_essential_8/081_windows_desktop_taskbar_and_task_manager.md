# Windows OS Configuration — Study Notes

> Chapter 11.1: Windows Versions, Desktop/Start Menu/Taskbar, and Task Manager

## 1. Windows Versions & Editions

- Windows has evolved since 1985 through many versions and editions, each suited to different use cases.
- **Corporate editions** (Pro, Enterprise, Ultimate, Education) support joining an **Active Directory domain** for centralized management and security.
- Key corporate security features:
  - **BitLocker** — full-disk/removable-media encryption.
  - **EFS (Encrypted File System)** — file/folder-level encryption.
  - **BranchCache** — reduces network traffic by letting branch-office computers share cached data.
- **Windows Media Center** (DVD playback, etc.) was available in older versions but discontinued starting with Windows 10.
- **Windows 10** (released 2015): desktop-focused UI, universal apps across devices, Microsoft Edge browser, stronger security, Action Center for quick settings. Feature updates twice a year, security patches monthly.
- **Windows 11** requires 64-bit hardware.

## 2. Desktop, Start Menu & Taskbar

### Desktop
- The desktop is the main workspace holding files and app shortcuts.
- Deleting a shortcut icon does **not** delete the underlying app/file.
- Icons vary depending on installed apps and OS version.

### Start Menu / Start Screen
- Opened via the **Start button** or the **Windows key**.
- **Live tiles** (e.g., Weather app) pull real-time info via internet connection; they can be turned off via right-click → More.
- Apps/folders/files can be pinned, dragged, or grouped for quick access.
- **Windows 10 Start Menu layout** (3 sections):
  1. Left: settings, power button, common folder shortcuts.
  2. Middle: alphabetical list of all installed apps.
  3. Right: category-based tiles (games, productivity, etc.).

### Taskbar
- Located by default at the bottom, but can be moved to any screen edge.
- Contains: app shortcuts, search box (Cortana/Bing), **Task View** (multiple virtual desktops/running apps), and the **notification area** (news, email, updates, network/VPN settings, Focus Assist).
- **Taskbar Settings** (right-click taskbar):
  - Lock/unlock the taskbar.
  - Auto-hide the taskbar.
  - Combine taskbar buttons: *Always hide labels* / *When taskbar is full* / *Never combine*.
- Common taskbar items: Edge browser, File Explorer (manage files/folders/drives), Microsoft Store, Mail app.
- **Jump Lists**: right-click an app icon to see frequently used tasks for that app.
- **Pinning apps**: right-click → Pin to taskbar.
- **Thumbnail previews**: hover over a running app's icon to preview its window.
- Taskbar behavior can vary slightly across Windows versions.

## 3. Task Manager

### Purpose
A tool to monitor system performance and force-close unresponsive or malfunctioning programs.

### How to Open
- `Ctrl + Shift + Esc`
- `Ctrl + Alt + Delete`
- `Windows + X`
- Right-click the taskbar → Task Manager

### Windows 10 Tabs (7 total)
| Tab | Function |
|---|---|
| **Processes** | Shows running apps and background processes; view resource usage (CPU, memory, disk, network); right-click to End Task or Search Online. |
| **Performance** | Real-time view of CPU, RAM, disk, and network (Ethernet/Wi-Fi) utilization. Includes an "Open Resource Monitor" shortcut. |
| **App History** | Tracks resource usage of Microsoft Store apps over time. |
| **Startup** | Manage which apps launch automatically at boot; disabling unnecessary ones speeds up startup. |
| **Users** | Shows logged-in users and the resources each is consuming; allows disconnecting a user. |
| **Details** | Full list of running executables (PID, status, memory); allows ending tasks, setting priority, opening file location. |
| **Services** | Lists background services (running/stopped); can start, stop, or restart a service. |

### ⚠️ Caution
Force-closing a process via Task Manager can cause **unsaved data loss** — use carefully.

## 4. Windows 7 vs. Windows 10 Task Manager

Windows 7 had **6 tabs**: Applications, Processes, Services, Performance, Networking, Users.

Key changes in Windows 10:
- **Applications + Processes** tabs merged into one **Processes** tab.
- **Networking** tab folded into the **Performance** tab.
- **Users** tab enhanced to show per-user resource consumption (not just who's connected).

## 5. Quick Quiz Review (True/False)

| Statement | Answer |
|---|---|
| Performance tab shows CPU, memory, network, and disk info | **True** |
| You can force-close a problematic process/app | **True** |
| Users tab only shows who is connected | **False** — it also shows each user's resource usage |
| Applications tab and Processes tab were merged | **True** |
| Running services are identified by PID | **True** |
| You can assign priority to a process in the Details tab | **True** |
| A separate "Networking" tab shows network interface usage in Win 10 | **False** — network info is now inside the Performance tab |
| Startup tab lets you disable auto-launching boot programs | **True** |
| Task Manager can be opened by right-clicking the taskbar | **True** |

## 6. Key Takeaway
Understanding Task Manager helps administrators quickly diagnose abnormal system behavior, identify resource-hungry processes, and maintain overall system stability and performance.
