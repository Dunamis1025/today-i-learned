# Windows Control Panel Study Notes

Summary of Cisco NetAcad IT Essentials material covering Windows 10 Control Panel items, system tools, and related labs.

## 1. Power Options

Controls how the computer manages power consumption.

**Configurable settings:**
- Require a password on wake
- Define power button behavior
- Define laptop lid-close behavior
- Create custom power plans
- Set display timeout / sleep timeout

**Power actions:**

| Action | Effect |
|---|---|
| Do nothing | Computer stays at full power |
| Sleep | Open files/programs kept in RAM; resumes quickly; low power use |
| Hibernate | Session saved to hard drive; power fully cut; slower resume (reboot required) |
| Turn off display | Computer stays on; only the monitor powers down |
| Shut down | All programs closed; computer fully powered off |

## 2. System Properties

Found under **System > Advanced system settings**.

| Tab | Purpose |
|---|---|
| Computer Name | Sets computer name and workgroup for network identification |
| Hardware | Manages Device Manager and driver settings |
| Advanced | Performance settings, including virtual memory |
| System Protection | Manages restore points to roll back the system |
| Remote | Enables/configures remote access to the PC |

**Performance boosters:**
- **Virtual memory (paging file):** Uses hard drive space as extra RAM when physical RAM runs low (slower than real RAM).
- **Windows ReadyBoost:** Uses an external flash drive as supplemental memory.

**Scenario matching:**
- Restore system after a bad update → **System Protection**
- "Out of memory" warnings → **Advanced (virtual memory)**
- Mouse/driver acting up → **Hardware**
- Remote troubleshooting from another location → **Remote**
- PC moved to a new building/network → **Computer Name**

## 3. Lab – Manage Virtual Memory

**Goal:** Practice viewing and changing the paging file location/size.

**Steps:**
1. Control Panel → System → Advanced system settings → Advanced tab → Settings (Performance) → Advanced tab. View current paging file size.
2. In Virtual Memory window, uncheck "Automatically manage paging file size for all drives." Check which drive holds the paging file (default: C:). Note the *recommended* size shown. Set a custom size on a second drive, then set C: to "No paging file." Restart.
3. Return to the same window to confirm the paging file moved to the new drive.
4. Reset: set C: back to "System managed size," set the other drive to "No paging file," re-check automatic management, restart.

**Why change default virtual memory settings?** To optimize performance — e.g., free up space on a full C: drive, or manually tune memory allocation for memory-intensive tasks and avoid system bottlenecks.

## 4. Device Manager

Lists all hardware installed on the computer.

**Functions:**
- Update a driver
- Roll back a driver to the previous version
- Uninstall a driver
- Disable a device

**Status icons:**
- Yellow warning triangle = device error
- Down arrow = device disabled

## 5. Devices and Printers

Shows external devices connected via USB, Bluetooth, or network (mice, keyboards, printers, phones, external drives). A green checkmark marks the current **default device**.

## 6. Sound

Configure playback/recording devices (speakers, microphones) and customize notification/system sounds.

## 7. Date and Time ("Clock")

Set system time, date, and time zone. Can auto-sync with an internet time server, be adjusted manually, and auto-apply Daylight Saving Time.

## 8. Lab – Use Device Manager

**Goal:** Explore Device Manager and monitor driver details.

- **What does Device Manager show / why use it?** Full list of installed hardware; used to diagnose issues, manage/update drivers.
- **Installing drivers for old, unrecognized hardware:** Action menu → "Add legacy hardware," then manually browse to the driver files.
- **Driver Details info:** File paths, version numbers, digital signature info for the driver files.
- **Two ways to update a driver:** (1) Search automatically for updated driver software, (2) Browse the computer manually for driver software.
- **Roll Back Driver:** Reverts to the previously installed driver; grayed out if no driver update has occurred yet or no prior version exists.
- **Other options:** Update driver, Disable device, Uninstall device.

## 9. Programs / Windows Features / Default Programs

| Control Panel Item | Purpose |
|---|---|
| **Programs** (Programs and Features) | Install/uninstall/repair applications; also used to uninstall problematic Windows updates |
| **Windows Features** | Turn built-in OS components on/off (e.g., Telnet Client) |
| **Default Programs** | Set which app opens a given file type (e.g., audio files) and configure AutoPlay behavior for removable media (e.g., CDs) |

**Scenario matching:**
- Reinstall a broken program → Programs
- Remove an unneeded app → Programs
- Remove a problematic Windows update → Programs
- Enable Telnet Client → Windows Features
- Set default audio editor for all audio files → Default Programs
- Make CDs always open in File Explorer instead of prompting → Default Programs

## 10. Other Control Panel Items

- **Troubleshooting:** Built-in scripts that automatically detect and fix common Windows problems; keeps a history of past fixes.
- **BitLocker Drive Encryption:** Encrypts an entire drive/volume so data stays protected even if the device or drive is stolen.
- **File Explorer / Folder Options:** Controls how files/folders display and behave — e.g., open folders in new windows, single- vs. double-click, show hidden files, search behavior for system folders and compressed files.

## 11. Quick Check Answers

- **What can BitLocker do in Windows 10?** → Encrypts an entire data volume to protect it.
- **Purpose of the Troubleshooting tool?** → Finds solutions to common Windows problems.
- **Purpose of the File Explorer Options applet?** → Customize the appearance and behavior of files/folders in File Explorer.

## 12. Lab – Privacy and Gaming

**Objective:** Research gaming-related privacy/security risks and configure Windows privacy & gaming settings.

**Part 1 – Privacy and Gaming:** Research and document 3 real gaming data/privacy breaches (company, date, games affected, data lost, method used).

**Part 2 – Mitigation:** Research and record protection strategies for:
- Oversharing personal info in-game
- Avoiding malware/ransomware from game downloads
- Login safety (account security)
- Other general protective measures

**Part 3 – Windows PC Privacy Settings** (Settings > Privacy, or Privacy & security on Windows 11):
- Turn off unnecessary general privacy toggles
- Decide on Location access and clear location history
- Review Camera/Microphone app permissions
- Identify 2+ additional privacy settings worth changing from default, with reasoning
- Research how to temporarily disable Cortana (privacy risk as an always-listening voice assistant)

**Part 4 – Windows Gaming Settings** (Settings > Gaming):
- Review available gaming settings
- Identify which options to adjust to improve privacy while gaming

*(This is an open-ended research lab — answers depend on the student's own findings and current OS version, so no fixed "correct" answers apply.)*
