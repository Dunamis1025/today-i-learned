# Mobile & Desktop OS Study Notes

Summary of 22 exam-style Q&A covering mobile operating systems (iOS/Android), macOS, and Linux fundamentals.

## Device Access & Restrictions

- **Jailbreaking / Rooting** — The two common methods for removing default OS restrictions. Jailbreaking bypasses Apple's iOS software limits (sideloading apps, custom system tweaks); rooting grants admin-level ("root") access on Android, allowing system file access and deep customization.
- **Factory Reset** — Restores a mobile device to its original out-of-box state, permanently erasing all user data, settings, and installed apps.
- **Passcode Lock** — Two purposes: (1) prevents unauthorized use of the device, and (2) protects private information (contacts, photos, messages) from theft if the device is lost or stolen.

## macOS (OS X) Basics

- **Force Quit** — The standard way to close an unresponsive Mac app, via `Cmd + Option + Esc` or the Apple menu.
- **Finder** — macOS's built-in file manager, equivalent to Windows File Explorer, used to browse and organize files/folders/apps.
- **APFS (Apple File System)** — The current default file system on Mac devices, optimized for speed, encryption, and reliability.

## Linux Fundamentals

- **vim** — A widely used command-line text editor for creating/editing files in Linux.
- **cp + mkdir** — To back up files into a new directory on another disk: `mkdir` creates the destination directory, `cp` copies the files into it.
- **ext3** — The Linux file system that introduced journaling, which logs changes so the system can recover and avoid corruption after a sudden power loss.
- **File permissions (rwxrwxrwx format)** — Permissions are read in 3 groups: **User / Group / Others**. Example `rw-r-x--x`:
  - `rw-` (User): read + write → can modify the file
  - `r-x` (Group): read + execute
  - `--x` (Others): execute only
- **Kernel panic** — A critical OS failure causing a freeze/stop screen at boot; a common cause is a **corrupted driver** interfering with hardware communication.
- **Boot manager** — A startup program that lets the user choose which OS to load and manages the boot process.

## Android Specifics

- **Sandbox** — Android apps run inside isolated "sandboxes," so even apps with elevated permissions can't freely affect other apps or core system areas — this balances default user-granted privileges with occasional extra system-level access needs.
- **Google Play** — The official, security-screened app store; the safest source for downloading Android apps (vs. unknown third-party sites).
- **Navigation icons — "Back"** — The system-bar icon used to return to the previously viewed screen.
- **Android's flexibility** — Because it's open-source, Android can be adapted by developers to run not just phones but laptops, smart TVs, and e-book readers.
- **Identifying an Android screen** — Recognizable by its bottom navigation icon layout (back / home / recent apps), which are its standard navigation tools.

## Wireless & Connectivity

- **Wi-Fi Calling** — Lets users make/receive phone calls over a Wi-Fi connection instead of cellular signal — useful where cell coverage is weak.
- **Auto-brightness** — Automatically adjusts LCD screen brightness based on ambient light, mainly to **conserve battery power** by avoiding unnecessarily bright screens.
- **Location data sources** — Locator apps determine device position using **Wi-Fi hotspots** (nearby wireless signals) and **cellular towers** (proximity to network base stations).

## Security

- **Signature files** — Contain sample code/patterns from known viruses and malware; security software compares scanned files against these signatures to detect threats (like a "most wanted" list for malicious code).

## Backup / Cloud

- **OneDrive** — Microsoft's cloud storage service, used for storing and backing up files remotely.

---
*Compiled from a study Q&A set on mobile device management, macOS, Linux administration, and Android fundamentals.*
