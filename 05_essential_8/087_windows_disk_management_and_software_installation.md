# Windows System Utilities & Disk Maintenance — Study Notes

## System Utilities Overview

| Tool | Best Used For |
|---|---|
| **System Information** | Getting a full overview of hardware specs, running services, and installed drivers — useful for admins checking a computer remotely. |
| **Regedit (Registry Editor)** | Directly editing the Windows registry. Used when a program won't run due to an installation error and support has provided specific registry keys to change. |
| **MMC (Microsoft Management Console)** | A container/framework for adding administrative snap-ins (Device Manager, Event Viewer, Local Users and Groups, etc.). Lets a technician build a custom console with only the tools they need — e.g., a security-focused toolkit. |
| **DxDiag (DirectX Diagnostic Tool)** | Diagnosing graphics card, sound card, and DirectX issues — the go-to tool when a 3D application crashes or has rendering errors. |
| **System Configuration (msconfig)** | Managing startup programs/services. Used to boot into a minimal configuration (similar to Safe Mode) to isolate which program is causing a computer to freeze after new software is installed. |

---

## Disk Management Concepts

| Task | Scenario |
|---|---|
| **Mount disk** | Browsing an ISO file's contents as if it were a real disc, without burning it. |
| **Initialize disk** | Preparing a brand-new physical disk so the OS can recognize and use it. |
| **Extend partition** | Growing a partition that's running out of space by pulling in adjacent free space. |
| **Split partition** | Dividing one large partition into two (e.g., separating OS files from data files). |
| **Shrink partition** | Reducing the size of an existing partition to free up unallocated space for a new partition. |

### Drive Status Meanings
- **Healthy** — functioning normally.
- **Foreign** — a disk brought over from another computer.
- **Initializing** — a basic disk being converted to dynamic.
- **Missing / Offline** — disconnected, corrupted, or inaccessible.
- **Not Initialized** — disk lacks a valid signature; needs setup before first use.
- **Unavailable** — hardware failure or I/O errors.

### Key Point: "Shrink" vs "Split"
Shrinking a volume doesn't carve out a new partition directly — it **redraws the boundary of the existing partition smaller**, converting part of its previously-used free space into **unallocated** space. That unallocated space can then be turned into a new partition separately. The amount you can shrink is limited not by total free space, but by where **unmovable files** sit on the disk — Windows can only pull the boundary back to the point before the first immovable file.

### Mounting
Mounting makes an image file (ISO) or an entire drive accessible without needing it to be a physical disc:
- Mount a **file** (ISO) → browse contents directly in File Explorer.
- Create a **mount point** → an entire drive appears as a folder inside another drive, for convenient access.

### Adding Arrays
- Windows Disk Management supports **mirrored**, **striped**, and **RAID-5** arrays across multiple dynamic disks.
- **Storage Spaces** (Windows 8/10+) pools multiple physical disks into virtual drives — recommended for redundancy (mirroring) or performance.

---

## Disk Optimization

### Defragmentation
- Consolidates **scattered file fragments** into **contiguous** (physically adjacent) blocks, which speeds up read/write access — especially for large files.
- **Not recommended for SSDs** — SSDs have no read-time penalty for scattered data, and unnecessary optimization writes shorten SSD lifespan.
- Windows 8/10 calls this tool **"Optimize Drives"**; Windows 7 calls it **"Disk Defragmenter."**
- SSDs are instead maintained via **TRIM/Retrim**, handled automatically by the drive's own controller/firmware and scheduled weekly by Windows.

### Disk Cleanup
- Removes unnecessary temporary files, cached data, and other junk to free up space.
- Safe on both SSDs and HDDs.
- Frees space rather than directly boosting speed, though a very full drive may feel slightly faster once cleaned.

---

## Disk Error-Checking (chkdsk)

- Checks **file system integrity** and scans for **physical bad sectors** (areas that can no longer reliably store data), attempting to recover readable data from damaged areas.
- Access: right-click drive → **Properties** → **Tools** tab → **Check** (or **Scan Drive**, depending on Windows version).
- Results can be viewed via **Show Details**, which opens the **Event Viewer** with a detailed log (Source: **Chkdsk**, under *Windows Logs → Application*).
- Especially recommended after a **sudden power loss or improper shutdown**, since these frequently cause file system corruption.

### Chkdsk process — 3 stages
1. **Examining basic file system structure** — verifies file records.
2. **Examining file name linkage** — verifies index entries, checks for orphaned files.
3. **Examining security descriptors** — verifies security/data attributes.

At the end, the log states whether problems were found and, if not: *"Windows has scanned the file system and found no problems. No further action is required."*

---

## Practical Lab Walkthrough (Hands-On)

1. **Check partition layout** in Disk Management — confirm free space is available.
2. **Shrink the C: volume** to free up ~2GB+ of unallocated space.
   - Note: "Size of available shrink space" can be much smaller than total free space, due to immovable file placement.
3. **Create a new simple volume** from the unallocated space → becomes a new drive (e.g., D:).
4. **Run Error-Checking (chkdsk)** on the new drive → confirms 3 stages, no errors found (since it's a fresh, empty volume).
5. **Skip Disk Defragmenter** if the drive is an SSD (as confirmed via Media Type = "Solid state drive" in Optimize Drives).
6. **Clean up afterward:** delete the temporary volume, then **Extend Volume** on C: to reabsorb the unallocated space back — restoring the original partition layout.

---

## Vocabulary Notes

- **necessitate** — a formal way of saying "make necessary / require." *"X necessitates Y"* = X makes Y unavoidable.
- **contiguous** — adjacent, touching, forming an unbroken sequence (opposite: scattered/fragmented).

---

## Software Installation & Environment Setup

### System Requirements
Before installing software, check:
- **Processor (CPU)** — architecture/speed needed.
- **RAM** — memory needed to run smoothly.
- **Operating System** — compatible OS/version.
- **Hard Disk Space** — storage needed for install + data.
- **Software Dependencies** — required frameworks/runtimes.
- **Graphics/Display** — resolution and hardware capability requirements.

### Graphics Considerations
- **Integrated Graphics** — built into motherboard/CPU, shares system RAM; fine for basic tasks (browsing, documents).
- **Dedicated Graphics** — separate GPU with its own VRAM; needed for gaming, video editing, 3D rendering — better performance and cooling.

### Installation Methods
- **Attended** — user manually clicks through the installer.
- **Unattended** — installer runs automatically with no user input.
- **Scheduled/Automated** — installation triggered by pre-set time/conditions.
- **Clean** — removes all previous versions before installing fresh; good for fixing corruption issues.
- **Network** — install files pulled from a central server across a network; common in corporate IT environments.

### ISO Mountable Files
- Windows 10+ lets you right-click an ISO → **Mount** → the OS treats it like a real optical drive, no burning or third-party tools needed.

### External Hardware Tokens (Multi-Factor Authentication)
- **USB Fingerprint Scanner Token** — verifies identity via fingerprint scan.
- **PIN-Generating Hardware Token** — generates a time-sensitive one-time password (OTP).
- Purpose: even if a password is stolen, the attacker still needs the physical token.

### Installing an Application
- Setup wizards guide configuration during install.
- Once installed, apps launch from the Start menu; malfunctioning apps can be repaired or uninstalled via built-in tools.
- **Microsoft Store** (Windows 10/11) offers a centralized, secure way to find/install/update apps.

### Compatibility Mode
- Lets an older program run as if on an earlier Windows version.
- Setup: right-click program → **Properties** → **Compatibility** tab → check "Run this program in compatibility mode for" → select the older OS version.
- **Compatibility Troubleshooter** can auto-detect the right settings if unsure.

### Uninstalling or Changing a Program
- Don't just delete files — leftover registry entries and junk files can degrade performance.
- Use **Programs and Features** (Control Panel) to fully and cleanly uninstall.
- Same tool supports **Change/Repair** to fix corrupted installs without a full reinstall.
- Some programs include their own uninstaller (check the Start menu program folder).
