# IT Essentials Study Notes — Windows Troubleshooting & Mobile OS

## Part 1: Windows Troubleshooting Q&A (12 Questions)

### Q1 — Disabling a Monitor
**Scenario:** Technician needs to disable one of two connected monitors to isolate a symptom.
**Answer:** Device Manager
- Right-click the device → "Disable device" to turn it on/off.
- *BIOS* = pre-OS hardware setup, not for toggling devices within Windows.
- *Resource Monitor* = shows real-time resource usage (CPU, memory, disk).
- *Task Manager* = manages running programs/processes, not individual hardware devices.

### Q2 — Slow Boot Diagnosis
**Scenario:** Identify which user application is delaying Windows 10 startup.
**Answer:** Task Manager
- The **Startup** tab lists auto-launching programs and their "Startup impact" rating.
- *Resource Monitor* = real-time resource usage detail.
- *Performance Monitor* = long-term performance data logging/analysis.
- *System Configuration* = boot mode & services management, not startup impact ranking.

### Q3 — Centralized Wireless Authentication
**Scenario:** 15 wireless access points need centralized, secure, scalable authentication for 100 employees.
**Answer:** RADIUS
- Open-source protocol where multiple APs forward login checks to one central server.
- *TKIP* = outdated, weak encryption.
- *TACACS+* = mainly for admin/network device access control, not general user auth.
- *WPA2-PSK* = shared password, unmanageable at scale.

### Q4 — Password Complexity Requirement
**Scenario:** Password "dave" for account "dave" fails complexity rules.
**Answer:** D@ve4
- Windows complexity rules require: uppercase, lowercase, number, special character, and the password must NOT contain the username.
- D@ve4 = uppercase (D) + lowercase (ve) + special char (@) + number (4).

### Q5 — Viewing Per-User Processes
**Scenario:** See all processes run by the currently logged-in user.
**Answer:** "Users" tab in Task Manager
- Shows processes grouped by which logged-in account is running them.
- *Startup tab* = auto-launch apps.
- *Services tab* = background system services.
- *Performance tab* = overall real-time hardware graphs (CPU/RAM/Disk).

### Q6 — Cloned Image Network Issue
**Scenario:** DISM-created image, when deployed to another workstation, causes network connectivity problems.
**Answer:** The SID of the original PC was not cleared when creating the image.
- Every Windows PC has a unique Security Identifier (SID).
- Duplicate SIDs on the same network cause conflicts.
- Fix: run **Sysprep** before capturing the image to generalize/clear unique identifiers.

### Q7 — Disaster Recovery Media for Mixed Hardware
**Scenario:** Network has various vendors' desktops/laptops running mixed 32-bit and 64-bit Windows 10 Pro.
**Answer:** Prepare individual recovery discs for all computers.
- No universal disc works across different hardware drivers and OS architectures (32-bit vs 64-bit).

### Q8 — Removing a Broken App Installation
**Scenario:** New app fails to install fully, and uninstall also fails; must remove without affecting existing data.
**Answer:** Restore using a System Restore point.
- Rolls system files/settings back to before the problematic install while keeping personal files intact.
- *Restore from Windows image* = full backup overwrite, risks data loss.
- *Reset this PC* = factory reset, wipes apps/settings.
- *Roll back last driver* = only for hardware driver issues, not app installs.

### Q9 — Printer Sharing Permission
**Scenario:** User cannot share a printer attached to a Windows 10 PC.
**Answer:** Administrator account
- System-level changes like printer sharing require admin privileges.
- *Local Service / Network Service / System* = special OS-internal accounts, not for human login.

### Q10 — Slow PC After Windows Update
**Scenario:** Part-time-employee PC slows down after a Windows Update.
**Answer:** Run Disk Cleanup **and** Use the System File Checker (SFC) tool.
- Disk Cleanup removes leftover update files clogging storage.
- `sfc /scannow` repairs system files that may have been corrupted during the update.
- *mstsc* = Remote Desktop command, unrelated.
- *Repartitioning* = no performance benefit, risks data loss.
- *Disabling processes* = minor help at best; not the primary fix.

### Q11 — RAID Drive Not Found
**Scenario:** Help desk call — system can't find the RAID drive to save a file.
**Answer:** Use Device Manager to check for driver issues.
- Drive not appearing usually = OS doesn't recognize the device (driver problem), checkable via yellow-warning icons in Device Manager.
- *Replace RAID controller* = only after ruling out driver/software issues.
- *Task Manager* = for unresponsive apps, unrelated.
- *Check IP/gateway* = network troubleshooting, unrelated to drive recognition.

### Q12 — Managing Disks/Partitions/Volumes
**Scenario:** Need to manage drives, disks, partitions, volumes, virtual drives via command line.
**Answer:** `diskpart`
- Powerful CLI tool for creating/deleting/formatting disks and partitions.
- *net user* = manages user accounts.
- *del* = deletes files.
- *rd* = removes directories.
- *md* = creates directories.

---

## Part 2: Mobile Operating Systems

### Overview
- Two dominant **mobile OSes**: Android and iOS.
- Two non-Windows **desktop OSes** mentioned: Linux and macOS.
- Chapter topics: OS differences, common mobile features (screen rotation/calibration, Wi-Fi calling, virtual assistants, GPS), mobile security (screen lock, biometrics, remote lock/wipe, lockout after failed attempts), and the standard 6-step troubleshooting process.

### Android
- **Open source**, Linux-based, led by Google (Open Handset Alliance).
- First released 2008 on the HTC Dream.
- Highly customizable — used in phones, tablets, laptops, smart TVs, cameras, navigation systems, media players.
- **Apps:** available via Google Play or third-party stores (e.g., Amazon Appstore). Developed with Android Studio (Java-based SDK), works on Windows/Linux/macOS.
- Apps run in a **sandbox**, only get permissions the user grants.
- Supports **sideloading**: installing apps directly via an `.apk` file, bypassing the official store.

### iOS
- **Closed source**, Unix-based, made by Apple exclusively for iPhone/iPad.
- First released 2007 on the original iPhone.
- Source code is private; copying/modifying/redistributing requires Apple's permission.
- **Apps:** only via the App Store, under Apple's strict **"walled garden"** review model.
- Developers must use Apple's tools (Xcode + Swift), which only run on macOS.

**Key exam answer:** *Three features of iOS* = (1) closed source OS, (2) source code not publicly released, (3) uses the walled garden app model. (Linux-based, Open Handset Alliance, and .apk installs are Android traits, not iOS.)

### Windows 10 Mobile
- Microsoft's mobile OS lineage: Windows CE → Windows Phone 7/8 → Windows 10 Mobile.
- Aimed to unify UI/code across Microsoft's phone and Surface tablet devices.

### Android UI Basics
- **System bar** (always at screen bottom) buttons:
  - **Back** – previous screen / closes keyboard; repeated presses go back to home.
  - **Home** – jumps to home screen.
  - **Recent Apps** – shows thumbnails of recently used apps; swipe to remove.
  - **Menu** – extra options for current screen (if available).
- **Notification/status bar** (top): clock, battery, signal/Wi-Fi icons; app status icons (email, messages, etc.).
  - Swipe down to open notifications: tap to respond, swipe to dismiss, clear all, toggle quick settings, adjust brightness, open Settings.

### iOS UI Basics
- **Notification Center**: swipe down from top-center; view/manage/clear alerts.
- **Control Center**: swipe down from top-right corner; quick toggles (flashlight, timer, calculator, camera, etc.), customizable via Settings > Control Center.
- **Spotlight Search**: swipe down from mid-screen; searches apps, settings, web, iTunes, App Store, showtimes, nearby places — updates live as you type.
- **Home button** (older iPhones): wake device, return to home screen, long-press for Siri. (Newer iPhones replace this with gestures/side-button.)

---

## Part 3: Hands-On Labs

### Lab — Working with Android
1. **Apps & Widgets:** Add app shortcuts from "All Apps" by long-press + drag to home screen. Widgets (dynamic info displays) are added similarly via long-press on blank space → Widgets icon. Both must be installed from Google Play first.
2. **Move/Remove:** Drag icon to screen edge to move between screens; drag to "Remove" link to delete shortcut only (app itself stays installed).
3. **Folders:** Drag one app onto another to create a folder; tap "Unnamed folder" text to rename. Drag an app out of a folder to remove it.
   - **Lab question & answer:** If you remove apps from a folder until only one remains, the folder auto-dissolves, leaving just that single app icon on the home screen.
4. **Install/Uninstall apps:** Install via Google Play Store (e.g., LastPass) → Install → Accept permissions. Uninstall via long-press → drag to Uninstall link → confirm.

### Lab — Working with iOS
1. **Rearranging apps:** Long-press icon until it "jiggles," then drag to new position or screen edge (creates new home page if needed). Press Home to finish.
2. **Folders:** Drag one app onto another to auto-create a folder; iOS names it based on app category.
   - **Lab question & answer:** The folder's default name is auto-assigned by iOS based on the types of apps placed inside.
3. **Renaming folders:** Open folder → long-press its name → retype (e.g., "ITE Folder").
4. **Removing apps from folder:** Long-press app inside folder → drag out to home screen.
   - **Lab question & answer:** If all apps are removed from a folder, the (now-empty) folder is automatically deleted.
5. **Install apps:** Via App Store → search → Get → Install → enter Apple ID password if prompted. An Apple account is required even for free apps.
6. **Uninstall apps:** Long-press icon until it jiggles → tap the "X" / delete indicator → confirm Delete. Default system apps cannot be removed this way.
