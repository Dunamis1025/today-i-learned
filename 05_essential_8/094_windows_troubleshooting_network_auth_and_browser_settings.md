# IT Troubleshooting Study Notes

A collection of exam-style questions and answers covering Windows OS troubleshooting, networking, and browser configuration.

---

## 1. Failing Hard Drive — Data Protection First

**Scenario:** A PC is losing files, some files won't open, and performance is slow — classic signs of a failing hard drive.

**Correct answer:** Back up all important files, then run `chkdsk`.

**Key points:**
- **Data protection is priority #1.** Before doing any diagnostics or repairs, back up everything important — you cannot risk losing data on a drive that's already failing.
- **`chkdsk` (Check Disk):** A built-in Windows utility that scans and repairs logical file system errors.
- **Never format** a suspect drive — formatting erases all data and should only ever come *after* a successful backup.
- If the drive shows physical symptoms (e.g., clicking noises), even `chkdsk` can add stress. In that case, back up immediately and replace the drive rather than relying on software tools.

---

## 2. Corrupted System Files After Malware Removal

**Scenario:** Malware was removed successfully, but after reboot the system shows missing/corrupted system file errors.

**Correct answer:** `SFC` (System File Checker)

**Key points:**
- `SFC` is a built-in Windows recovery tool that scans for and replaces damaged or missing system files with correct versions.
- Run via **Command Prompt (Administrator)** using: `sfc /scannow`
- **Why not the alternatives:**
  - `Fixboot` / `Fixmbr` — used for boot sector issues (computer won't start), not file corruption.
  - `ASR` (Automated System Recovery) — legacy Windows XP-era recovery method, rarely used today.
  - `Regedit` — edits the registry directly; unrelated to automatic system file repair and risky if misused.

---

## 3. Registry Entry Exists but Program Files Are Missing

**Scenario:** A program is listed in the Windows registry, but its actual files no longer exist on disk (a "ghost" entry).

**Correct answer:** Reinstall the application, then run the uninstall program.

**Key points:**
- Reinstalling recreates the correct registry keys and links them to real, present files — repairing the broken registry-to-file connection.
- Running the official uninstaller afterward lets the software cleanly remove all its own files and registry entries, avoiding leftover clutter.
- **Why not the alternatives:**
  - `fdisk /mbr` — repairs the Master Boot Record, unrelated to individual application registry entries.
  - Restoring `ntdetect.com` / `boot.ini` — critical **boot** files, unrelated to application management.
- **Tip:** Tools like CCleaner or Revo Uninstaller can also safely remove leftover "ghost" registry references without needing a reinstall.

---

## 4. Wireless File Transfer Between macOS and iOS

**Scenario:** Which feature enables Wi-Fi Direct file transfer between macOS and iOS devices?

**Correct answer:** AirDrop

**Key points:**
- AirDrop is Apple's proprietary technology combining **Bluetooth + peer-to-peer Wi-Fi** for direct file transfer — no internet connection required.
- **Why not the alternatives:**
  - Homegroup / Workgroup — Windows-only network sharing features for LAN file/printer sharing.
  - Nearby Sharing — Windows' equivalent of AirDrop, but only works between Windows devices, not with Apple's ecosystem.
- **Advantages:** Fast local transfer of large files (photos/videos) without using mobile data; adjustable privacy (Everyone / Contacts Only / Off) to prevent unwanted transfers.

---

## 5. Forcing Group Policy Updates on a Workstation

**Scenario:** A company using Active Directory fixes a network issue by modifying Group Policy. Which command makes the workstation sync with the new settings immediately?

**Correct answer:** `gpupdate`

**Key points:**
- Group Policy centrally manages security settings and permissions across networked computers.
- Workstations normally refresh policy on a scheduled interval — `gpupdate` forces an **immediate** refresh instead of waiting.
- **Why not the alternatives:**
  - `runas` — runs a program under a different user's credentials.
  - `rstrui` — launches System Restore.
  - `tasklist` — lists currently running processes/services.
  - `gpresult` — shows *which* policies are currently applied (a reporting tool), it does not force an update.
- **Pro tip:** `gpupdate /force` re-applies *all* policies (not just changed ones), useful for guaranteeing a fix takes effect.

---

## 6. Speed and Duplex Misconfiguration

**Scenario:** A technician is changing "Speed and Duplex" settings on a network adapter. What happens if configured incorrectly?

**Correct answer:** The network connection may experience issues.

**Key points:**
- Speed and Duplex settings determine the communication speed and direction (Half vs. Full Duplex) between a NIC and network device (switch/router).
- **Duplex mismatch** (e.g., one side Full, the other Half) causes data collisions, packet loss, and severe performance degradation or dropped connections.
- Severely incompatible settings can prevent the connection from establishing at all.
- **Why not the alternatives:**
  - NIC power management / Wake-on-LAN — controlled separately, under the Power Management tab.
  - VLAN support — configured via VLAN ID / protocol settings, unrelated to Speed and Duplex.
- **Best practice:** Leave this on **Auto Negotiation** unless troubleshooting compatibility with old legacy hardware, in which case both ends must be manually matched exactly.

---

## 7. Windows 10 Libraries Feature

**Scenario:** Which statement about Windows 10 Libraries is true?

**Correct answer:** Libraries allow Windows 10 to link multiple different directories.

**Key points:**
- A Library is a **virtual container** — it doesn't move or store files itself. Instead, it **aggregates** (gathers/combines) content from various physical locations (different hard drive folders, external drives, network locations) into a single unified view.
- Lets users manage scattered files as if they were all in one place, without knowing/remembering exact file paths.
- **Why not the alternatives:**
  - Indexing speed — handled by the separate Windows Search Indexer service.
  - EFS (Encrypted File System) — a security/encryption feature, unrelated to library organization.
  - File name length limits — determined by the underlying file system (e.g., NTFS), not by Libraries.

---

## 8. Enterprise Wireless Authentication Methods

**Scenario:** Which two server-based authentication methods suit a corporate wireless network? (Choose two.)

**Correct answers:** RADIUS and TACACS

**Key points:**
- **Server-based authentication** uses a centralized server to verify user credentials, rather than configuring each device individually — essential at enterprise scale.
- **RADIUS** (Remote Authentication Dial-In User Service): Industry standard for network access control; authenticates users via username/password against a central database (e.g., Active Directory).
- **TACACS** (Terminal Access Controller Access-Control System): Primarily used for authenticating administrators managing network infrastructure devices (routers, switches).
- **Why not the alternatives:**
  - TKIP / AES — encryption algorithms for securing data in transit, not authentication methods.
  - WPA2-PSK — "Personal" mode using one shared password for everyone; not scalable or secure enough for enterprise use, since there's no per-user tracking.
- **Best practice:** Use WPA2/WPA3-Enterprise with a RADIUS server — each employee gets unique credentials, and access is instantly revoked by disabling their account (no need to change a shared password when someone leaves).

---

## 9. Internet Explorer Settings Tabs

**Scenario:** Match each Internet Options tab to its function.

| Tab | Function |
|---|---|
| **Connections** | Configure Dial-up, VPN, and Proxy Server settings |
| **Programs** | Set default browser, manage add-ons, choose HTML editor, set programs for internet services |
| **Advanced** | Reset all IE settings back to default (factory reset) |
| **Content** | Adjust AutoComplete settings; manage feeds and web slices |
| **General** | Set homepage, view/delete browsing history, adjust search settings, customize appearance |

**Key points:**
- **Connections** — manages *how* the browser connects to the network (important for corporate proxies/VPNs).
- **Programs** — manages the "ecosystem" around the browser (default apps, add-ons).
- **Advanced** — the deep/troubleshooting settings; includes the full Reset button.
- **Content** — manages personal browsing data and dynamic content features.
- **General** — the everyday user-facing dashboard (homepage, history, appearance).

---

## 10. Chrome Not Auto-Saving Passwords (vs. Edge)

**Scenario:** Edge auto-fills login credentials on a secure site, but Chrome does not save them for the same site.

**Correct answer:** Google Chrome does not automatically save web credentials (for this site/setting).

**Key points:**
- **Browsers are independent applications** — they don't share saved passwords or settings with each other by default.
- Most likely cause: Chrome's "Offer to save passwords" feature is disabled, or the user previously chose "Never" for that specific site.
- **Why not the alternatives:**
  - Site compatibility issues — Chrome fully supports secure (HTTPS) sites.
  - Certificate problems — would trigger an explicit "connection not private" warning, not just a silent failure to save a password.
  - Browser corruption — not saving one password is a setting issue, not a sign the whole browser is corrupted.
- **Fix:** Chrome menu (⋮) → Settings → **Autofill and passwords** → ensure "Offer to save passwords" is **On**; also check the "Never saved" list for blocked sites.

---

## 11. 32-bit Program Files Location on 64-bit Windows

**Scenario:** Where are 32-bit program files stored on 64-bit Windows 10 Pro?

**Correct answer:** `C:\Program Files (x86)`

**Key points:**
- Windows separates folders so 32-bit and 64-bit applications don't conflict:
  - `C:\Program Files` — native 64-bit applications
  - `C:\Program Files (x86)` — 32-bit applications ("x86" = 32-bit architecture designation)
- Keeping them separate ensures 32-bit software runs stably alongside 64-bit system components.
- For reference: `C:\Users` stores personal user data; `C:\Windows\System32` holds core OS system files.

---

*Compiled from CompTIA A+ / IT support style practice questions.*
