# Windows 10 Administration - Lab 01: Create a Disk Partition
> 📅 Date: 2026-05-14
> 🏫 Course: Windows 10 Administration Lab Series (CSSIA / NDG NETLAB+)

---

## Objectives
- Create a new disk partition (K: drive) on Windows 10
- Format the partition using the FAT32 file system
- Convert the partition from FAT32 to NTFS
- Compare and analyze the differences before and after conversion

---

## Key Concepts

### Partition
- A logically divided section of a physical hard disk
- A single physical disk can be split into multiple drives (e.g., C:, D:, K:)
- In this lab, a new K: drive is created from the Unallocated space on Disk 0

### File System
- The set of rules an OS uses to store and manage files on a disk
- Common types: FAT32, NTFS

### FAT32 (File Allocation Table 32)
- Introduced with Windows 95 in 1996
- FAT = File Allocation Table, 32 = 32-bit addressing (successor to FAT16)
- **Pros**: Simple structure, high compatibility (USB drives, camera memory cards, etc.)
- **Cons**:
  - Maximum single file size limited to 4GB
  - No file-level security permissions
  - No Quota support

### NTFS (New Technology File System)
- Introduced alongside Windows NT in 1993
- NT = New Technology, FS = File System
- Default file system for modern Windows
- **Pros**:
  - File and folder-level security permissions (Security tab)
  - Quota support: limit disk usage per user
  - Large file support
  - Superior stability and recovery capability

### Non-destructive Conversion
- Converting FAT32 to NTFS preserves all existing files
- Confirmed in this lab: the NDG Test Graphic file survived the conversion intact

---

## Lab Environment

| Item | Details |
|------|---------|
| Platform | NETLAB+ (Holmesglen) |
| VM | Windows 10 PC1 |
| IP Address | 192.168.1.203 |
| Credentials | student / Train1ng$ |

---

## Lab Procedure

### Step 1: Open Disk Management
```
Start Menu → Control Panel → Administrative Tools → Computer Management → Disk Management
```
- Disk Management is located under the Storage section
- Confirm Unallocated space (2.69 GB) on Disk 0

### Step 2: Create a New Partition
- Right-click the **Unallocated** block on Disk 0 → select **New Simple Volume**
- Settings:
  - Volume size: **1024 MB**
  - Drive letter: **K**
  - File system: **FAT32**
  - Perform a quick format: **checked**

### Step 3: Rename the Partition
```
This PC → right-click NEW VOLUME (K:) → Properties → rename to NDG → OK
```

### Step 4: Create a Test File
```
Open NDG (K:) → right-click empty space → New → Bitmap image → rename to: NDG Test Graphic
```

### Step 5: Convert FAT32 to NTFS
Open Command Prompt as Administrator and run:
```cmd
convert K: /fs:NTFS
```
When prompted for the current volume label, type: `NDG`

### Step 6: Verify the Conversion
```
This PC → right-click NDG (K:) → Properties → check File system and tabs
```

---

## Question Bank Answers (FAT32 vs NTFS Comparison)

### Question Bank 1 — K: Drive Properties (FAT32)
| Item | Value |
|------|-------|
| File System | FAT32 |
| Free Space | 0.99 GB |
| Number of Tabs | 7 |
| Tab Names | General, Tools, Hardware, Sharing, ReadyBoost, Previous Versions, Customize |

### Question Bank 2 — NDG Test Graphic Properties (FAT32)
| Item | Value |
|------|-------|
| Number of Tabs | 3 |
| Tab Names | General, Details, Previous Versions |

### Question Bank 3 — K: Drive Properties (NTFS)
| Item | Value |
|------|-------|
| File System | NTFS |
| Free Space | 0.97 GB |
| Number of Tabs | 9 |
| Tab Names | General, Tools, Hardware, Sharing, **Security**, ReadyBoost, Previous Versions, **Quota**, Customize |
| Newly Added Tabs | **Security, Quota** |

### Question Bank 4 — NDG Test Graphic Properties (NTFS)
| Item | Value |
|------|-------|
| Number of Tabs | 4 |
| Tab Names | General, **Security**, Details, Previous Versions |
| Newly Added Tab | **Security** |

---

## Key Findings (FAT32 vs NTFS)

| Comparison | FAT32 | NTFS |
|------------|-------|------|
| Drive property tabs | 7 | 9 |
| File property tabs | 3 | 4 |
| Security tab | ❌ Not available | ✅ Available |
| Quota tab | ❌ Not available | ✅ Available |
| File preservation after conversion | - | ✅ Confirmed (non-destructive) |

> **Conclusion**: NTFS adds Security and Quota features not available in FAT32, making it the standard for enterprise environments.

---

## Key Command

```cmd
# Convert a FAT32 partition to NTFS
convert K: /fs:NTFS
```

---

## Glossary

| Term | Definition |
|------|------------|
| Partition | A logically divided section of a hard disk |
| File System | The method used to store and organize files on a disk |
| FAT32 | File Allocation Table 32 — an older file system |
| NTFS | New Technology File System — the modern Windows standard |
| Unallocated | Disk space not yet assigned to any partition |
| Quick Format | Formats the volume rapidly without scanning for bad sectors |
| Security | Feature allowing access permissions per file/folder (NTFS only) |
| Quota | Feature limiting disk usage per user (NTFS only) |
| Non-destructive Conversion | Conversion process that preserves existing data |
| Disk Management | Windows GUI tool for managing disks and partitions |
