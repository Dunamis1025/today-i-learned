# IT Essentials — Boot Process, Storage & Windows 10 Study Notes

> Compiled from a Gemini study session (34 questions, 76% score). One answer was
> factually incorrect and has been corrected below — see the ⚠️ **CORRECTED** flag.

---

## 1. Boot Process

- **BIOS boot location:** The BIOS searches the **active partition** on the hard
  disk to find the OS boot instructions.
- **Boot sequence (32-bit Windows 10, before `bootmgr.exe` loads):**
  1. **POST** — hardware self-check
  2. **CMOS settings loaded** — boot device order read from CMOS
  3. **MBR** — Master Boot Record is read
  4. **VBR** — Volume Boot Record hands off to the boot manager
- **Safe Mode key:** Pressing **F8** during boot opens the advanced boot options
  menu, including Safe Mode.
- **Undo a bad driver install:** Use **"Boot to Last Known Good Configuration"**
  to revert to the last successful boot state.
- **PXE (Preboot eXecution Environment):** Used when **the computer needs a
  replacement operating system** — it lets a PC boot and install an OS over the
  network without local install media.
- **Windows Boot Manager:** The utility that manages OS selection/launch during
  a **direct, local installation** of Windows 10 (as opposed to Upgrade
  Assistant, USMT, or Windows Easy Transfer, which serve other purposes).

---

## 2. Partitions & Disk Structure

- **MBR (Master Boot Record):** A small section at the start of a hard drive
  that stores **how the drive's partitions are organized** and where to find
  the OS to boot.
- **Active partition:** The partition flagged as bootable; BIOS looks here first.
- **Volume:** A logical drive that has been **formatted** with a file system so
  the OS can store data on it (e.g., your `C:` or `D:` drive).
- **Formatting:** The process of **creating a file system in a partition or
  volume** so it can store files.
- **Dynamic disks:** Allow you to **create volumes that span more than one
  physical disk**, combining their space into a single logical volume.
- **Two OSes + three data locations on one drive:**
  → **2 primary partitions, 1 marked active, 1 extended partition containing 3
  logical drives.** (2 primaries support the two OSes; the extended partition's
  3 logical drives give the three separate data locations.)
- **MBR partition limit:** Under the traditional MBR boot standard (max
  partition size 2 TB), a disk supports a maximum of **4 primary partitions**.
- **GPT (GUID Partition Table):** The modern partitioning scheme, commonly used
  on computers with **UEFI firmware** (replaces the older MBR/BIOS combo).

---

## 3. File Systems

| File System | Key Fact |
|---|---|
| **NTFS** | Default file system for Windows 10 installs; supports files >5 GB and partitions up to 16 EB; adds strong security (file-level permissions) and extended attributes — its two big advantages over FAT32 are **more security features** and **support for larger partitions**. |
| **FAT32** | Older standard; max partition size ~2 TB / 2,048 GB; cannot hold files over 4 GB. |
| **exFAT** | Supports files larger than 4 GB; mainly used on flash/USB drives. |
| **NFS (Network File System)** | Lets a computer access files stored on another computer **over a network** as if they were local. |
| **CDFS** | Built specifically for optical media (CD/DVD). |

- **True/False — local vs. network file access:** **False.** Even though NFS
  makes remote files *look* local, accessing them still goes through the
  network, so there are real differences in speed and reliability versus a
  locally stored file.

---

## 4. User Accounts & Permissions

- **Account for system management only (not daily use):** **Administrator.**
  Using it for everyday tasks raises the risk that malware run under it could
  compromise the whole system — daily use should be a Standard account.
- **Account auto-created and enabled during Windows 10 setup:** **Administrator.**
- **Windows 10's two default account types:** **Administrator** and **Standard
  User.**
- **Action restricted to Administrator accounts:** **Changing system-wide
  settings** (standard users can run apps and manage their own files, but not
  system-level configuration).

---

## 5. Operating System Concepts

- **CPU component for immediate data access:** **Registers** — tiny, ultra-fast
  storage built directly into the CPU.
- **Support for 2+ CPUs:** **Multiprocessing.**
- **Two types of user interface:** **CLI** (Command Line Interface — typed
  commands) and **GUI** (Graphical User Interface — icons/windows/mouse).
- ⚠️ **CORRECTED — Breaking a program into smaller loadable parts:**
  The original notes said "multitasking," but that's incorrect.
  **The correct term is multithreading.** Multithreading splits a program into
  threads that the OS can load and run as needed, often concurrently.
  *(Multitasking = running multiple separate programs/processes at once;
  multiprocessing = using 2+ physical CPUs; multithreading = splitting one
  program into smaller parts/threads — which is exactly what this question
  describes.)*

---

## 6. Windows 10 Editions & Deployment

- **Edition-to-use-case matching:**
  - **Enterprise** → large/mid-size business, advanced security & management
  - **Pro** → small business, security + productivity/management features
  - **Education** → academic institutions, volume licensing
  - **Home** → personal/gaming use, family safety & parental controls
- **USMT (User State Migration Tool):** Microsoft's command-line tool for
  migrating **files and settings** to a new Windows installation — used both
  for individual upgrades and for **bulk migration across networked PCs**
  during an enterprise deployment.
- **32-bit Windows 10 Pro RAM limit:** Can address a maximum of **4 GB** of
  physical RAM, regardless of how much is physically installed.

---

## Quick-Reference Answer Key

| # | Question Topic | Answer |
|---|---|---|
| 1 | BIOS boot search location | Active partition |
| 2 | 2 OS + 3 data areas, 1 drive | 2 primary, 1 active, 1 extended, 3 logical |
| 3 | File system, files >5GB, internal drive | NTFS |
| 4 | Management-only account | Administrator |
| 5 | Holds partition layout info | MBR |
| 6 | Formattable logical drive | Volume |
| 7 | File system for network file access | NFS |
| 8 | Two NTFS advantages over FAT32 | More security features; supports larger partitions |
| 9 | Max primary partitions (2TB/MBR standard) | 4 |
| 10 | Two UI types | CLI, GUI |
| 11 | Max RAM, 32-bit Windows 10 Pro | 4 GB |
| 12 | Default file system, fresh Win10 install | NTFS |
| 13 | Account auto-created during install | Administrator |
| 14 | Tool to migrate files/settings to new Windows | User State Migration Tool (USMT) |
| 15 | Windows 10 edition matching | Enterprise/Pro/Education/Home as above |
| 16 | Boot steps before bootmgr.exe (32-bit) | POST → CMOS → MBR → VBR |
| 17 | Tool for bulk deployment + user state migration | USMT |
| 18 | Key for Safe Mode during boot | F8 |
| 19 | CPU component for immediate data access | Registers |
| 20 | Accurate statement about GPT | Used with UEFI firmware |
| 21 | Fix after bad driver breaks boot | Boot to Last Known Good Configuration |
| 22 | Admin-only Windows 10 task | Change system settings |
| 23 | ⚠️ Term for splitting a program into loadable parts | **Multithreading** (not multitasking) |
| 24 | Dynamic disk description | Volumes can span multiple disks |
| 25 | File system matching (NTFS/NFS/FAT32/exFAT/CDFS) | See table in §3 |
| 26 | Two default Windows 10 account types | Administrator, Standard User |
| 27 | Feature enabling 2+ CPU support | Multiprocessing |
| 28 | When to use PXE | OS needs to be replaced (network boot/install) |
| 29 | Statement describing formatting | Creates a file system in a partition/volume |
| 30 | Tool to install Windows 10 directly, guided setup | Windows Boot Manager |
| 31 | T/F: local vs. network file access is identical | False |
