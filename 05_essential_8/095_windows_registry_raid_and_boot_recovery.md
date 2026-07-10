# Windows 10 Troubleshooting & Administration — Study Notes

A study summary covering Windows 10 Registry, RAID, boot recovery, file sharing, ISO images, OS reinstallation, Event Viewer, driver rollback, and network diagnostics.

---

## 1. Windows 10 Registry Keys

The Windows Registry is a central hierarchical database that stores low-level settings for the OS and applications.

| Registry Key | Description |
|---|---|
| `HKEY_CLASSES_ROOT` (HKCR) | File type associations, shortcuts, and settings used when Windows opens a file or views a directory |
| `HKEY_CURRENT_USER` (HKCU) | Preferences of the currently logged-on user — personalization, default devices, programs |
| `HKEY_CURRENT_CONFIG` (HKCC) | Information about the current hardware profile actively in use |
| `HKEY_USERS` (HKU) | Configuration settings for **all** user accounts on the machine; `HKEY_CURRENT_USER` is effectively a pointer into this hive for the active user |

**Key takeaway:** HKCR = file associations, HKCU = "my" personal settings, HKCC = active hardware profile, HKU = every user's settings (superset of HKCU).

---

## 2. Open-Ended vs. Closed-Ended Troubleshooting Questions

**Best open-ended question example:** *"What programs have you installed recently?"*

- **Open-ended questions** cannot be answered with a simple yes/no — they prompt the customer to explain details, which helps narrow down root cause.
- **Closed-ended questions** (e.g., "Is the computer plugged in?") only elicit yes/no and are less useful for initial diagnosis, though useful for confirmation later.

---

## 3. RAID Levels Supported in Windows 10 Pro

**Answer: RAID 0, 1, and 5**

| RAID Level | Focus | Trade-off |
|---|---|---|
| RAID 0 (Striping) | Speed | No redundancy — one disk failure = total data loss |
| RAID 1 (Mirroring) | Redundancy | Data duplicated across disks; usable capacity is halved |
| RAID 5 | Balance | Distributes data + parity info across ≥3 disks; can survive one disk failure |

RAID 3 and RAID 4 are not typically supported/used in standard Windows environments.

---

## 4. Advanced Recovery Option for Boot Problems

**Scenario:** Common boot failure needs diagnosis and repair.
**Answer: Startup Repair**

- Automatically diagnoses and fixes common issues preventing Windows from starting.
- It's the **first-step, least invasive** tool.
- More drastic alternatives (used only if Startup Repair fails):
  - **System Restore** — rolls back to a previous restore point
  - **System Image Recovery** — restores a full backup image
  - **Reset this PC** — wipes/reinstalls the system

---

## 5. Nearby Sharing

**Question:** What Windows 10 feature enables simple file sharing via Wi-Fi and Bluetooth?
**Answer: Nearby Sharing**

- Built-in feature that lets nearby devices exchange files/links wirelessly.
- Conceptually similar to Apple's **AirDrop**.

---

## 6. Viewing an ISO Disk Image File

**Answer:** Use File Explorer to locate the ISO file and **mount** it using the Disk Image tools.

- An ISO file is a single archive representing the full contents of a physical disc.
- Windows 10 lets you right-click → **Mount** to treat the ISO as if it were a real inserted disc — no extraction needed.

---

## 7. Reinstalling a Corrupted OS — Next Step After Inserting Installation Media

**Answer: Change the boot sequence in the BIOS.**

- After inserting the installation media, the computer must be told to boot from that media rather than the (corrupted) hard drive.
- This is done by entering BIOS/UEFI settings and changing the **boot order/sequence** so the optical drive or USB is prioritized.

---

## 8. Windows 10 Event Viewer — Message Types

| Message Type | Description |
|---|---|
| **Error** | A software component isn't functioning correctly (potential problem) |
| **Critical** | A severe issue requiring immediate attention |
| **Information** | A successful event was logged (informational only) |
| **Warning** | A problem exists, but no immediate action is required |
| **Success Audit** | A security-related event completed successfully |

---

## 9. "Invalid Boot Disk" Error After POST

**Probable cause: The MBR (Master Boot Record) is corrupted.**

- The MBR acts as a "roadmap" telling the computer where to find the OS at boot time.
- If it's damaged, the system can't locate bootable files, resulting in this error.

---

## 10. Reverting a Problematic Driver Without Data Loss

**Scenario:** A driver installed 3 weeks ago causes intermittent freezes; the user wants to revert without losing data or apps.

**Answer:** Uninstall and reinstall the device using **Device Manager** (or use the **"Roll Back Driver"** feature in the driver's Properties).

- Both methods restore the previously working driver.
- Neither affects personal files or other installed applications.

---

## 11. Checking Active TCP Connections (Suspected Hacking)

**Answer: `netstat`**

- Stands for **"network statistics."**
- Displays all active network connections on the PC.
- Used to identify suspicious or unauthorized inbound/outbound connections.

---

## Quick Reference Summary Table

| Topic | Key Answer |
|---|---|
| Registry keys | HKCR = file types, HKCU = user prefs, HKCC = hardware profile, HKU = all users |
| Best troubleshooting question type | Open-ended (e.g., "What programs have you installed recently?") |
| RAID levels in Windows 10 Pro | 0, 1, 5 |
| First boot-repair tool | Startup Repair |
| Wireless file sharing feature | Nearby Sharing |
| Viewing ISO contents | Mount via File Explorer |
| Step after inserting install media | Change BIOS boot sequence |
| Event Viewer message types | Error / Critical / Information / Warning / Success Audit |
| Cause of "Invalid Boot Disk" | Corrupted MBR |
| Safe driver revert method | Device Manager uninstall/reinstall or Roll Back Driver |
| Command for active TCP connections | `netstat` |
