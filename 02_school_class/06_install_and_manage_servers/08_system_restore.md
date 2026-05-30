# Lab 8: Utilizing System Restore — Study Notes
> **Course:** Windows 10 Administration Lab Series (CSSIA / NETLAB+)
> **Topic:** System Restore on Windows 10 Client
> **Date Studied:** 2026-05-30

---

## 📌 Overview

**System Restore** is a Windows built-in recovery feature that allows you to roll back system files, registry settings, and installed programs to a previously saved state called a **Restore Point** — without affecting personal documents or files.

> Think of it as a "time machine" for your OS configuration.

---

## 🎯 Learning Objectives

1. Enable and configure **System Protection** on the C: drive
2. Manually create a named **Restore Point**
3. Execute a **System Restore** to revert the system to a prior state
4. Verify the restore was successful through observable system changes

---

## 🖥️ Lab Environment

| Virtual Machine       | IP Address      | Account       | Password   |
|-----------------------|-----------------|---------------|------------|
| Windows 10 PC1        | 192.168.1.203   | student       | Train1ng$  |
| Windows 10 PC2        | 192.168.1.202   | student       | Train1ng$  |
| Windows Server 2012 R2| 192.168.1.200   | Administrator | Train1ng$  |

> All lab tasks are performed on **PC1**.

---

## 🔑 Key Concepts

### Restore Point
- A **snapshot** of the system's configuration at a specific moment in time
- Stores: system files, registry, installed program settings
- Does **NOT** store: personal documents, pictures, or user data
- Created: manually by a user, or automatically by Windows before major changes (driver installs, Windows Updates)

### System Protection
- The feature that must be **enabled** before restore points can be created
- Configured per drive (e.g., Local Disk C:)
- Allocates a percentage of disk space to store restore point data
- When storage fills up, **older restore points are automatically deleted** to make room for new ones

---

## 🛠️ Step-by-Step Procedure

### Phase 1 — Enable System Protection

1. Right-click **Start Menu** → select **System**
2. In the System window, click **System protection** (left pane)
3. In *System Properties* → **System Protection** tab → select **Local Disk (C:) (System)**
4. Click **Configure**
5. Select **Turn on system protection**
6. Set **Max Usage** to **10%** of disk space
7. Click **Apply** → **OK**

> ⚠️ If System Protection is **Off**, the **Create** button for restore points is grayed out.

---

### Phase 2 — Create a Restore Point

1. Back in *System Properties* → click **Create**
2. Enter the name: **`BACKUP`**
   - *(Windows automatically appends the current date and time)*
3. Click **Create**
4. Wait for the process to complete
5. Click **Close** when the success message appears
6. Click **OK** to close System Properties

---

### Phase 3 — Simulate a System Change

> This step intentionally alters the system so the restore can be verified visually.

1. Right-click the desktop → select **Personalize**
2. In Personalization Settings, select the **Orange** background color
3. Close the settings window
4. Confirm the desktop background is now **orange**

---

### Phase 4 — Perform System Restore

1. Right-click **Start Menu** → select **System**
2. Click **System protection** → **System Restore...**
3. In the System Restore wizard, click **Next**
4. Select the restore point named **`BACKUP`** from the list → click **Next**
5. Review the confirmation screen:
   - **Time:** date/time of the BACKUP point
   - **Description:** Manual: BACKUP
   - **Drives:** Local Disk (C:) (System)
6. Click **Finish**
7. Read the warning message (*"Once started, System Restore cannot be interrupted"*) → click **Yes**
8. The system will **reboot automatically** and restore to the BACKUP state

---

### Phase 5 — Verify the Restore

1. After reboot, log in as `student` / `Train1ng$`
2. A **System Restore** dialog appears confirming success → click **Close**
3. Observe the desktop background — it should have returned to its **original color (black/default)**

---

## ❓ Question Bank Answers

**Q: What color is the Desktop background after the restore?**
> **Black** (the default color that was set when the BACKUP restore point was created)

**Q: Why?**
> Because System Restore reverted the system's configuration — including the personalization/color settings — back to the state it was in at the time the BACKUP restore point was created, before the orange color change was applied.

---

## ⚠️ Important Limitations & Notes

| Aspect | Detail |
|---|---|
| Personal files | NOT affected by System Restore |
| Installed programs | May be **removed** if installed after the restore point |
| Drivers | May be **rolled back** if installed after the restore point |
| Interruption | System Restore **cannot be interrupted** once started |
| Safe Mode | If run from Safe Mode or System Recovery, it **cannot be undone** |
| Disk space | Older restore points are **auto-deleted** when space runs out |

---

## 🔄 Navigation Path Summary

```
Start Menu (right-click)
  └── System
        └── System Protection (left pane)
              ├── [Configure] → Turn on protection / set disk %
              ├── [Create]    → Name and create a restore point
              └── [System Restore...] → Launch the restore wizard
```

---

## 💡 Key Takeaways

- Always **enable System Protection** before expecting restore points to exist
- **Name your restore points** descriptively so you can identify them later
- System Restore is a **non-destructive** recovery tool for system settings — it won't touch your documents
- The **10% disk allocation** is a common best-practice starting point
- System Restore requires a **system reboot** to apply changes
- This is a fundamental **Windows administration skill** for IT support and troubleshooting

---

*Notes compiled from CSSIA Win10ADM Lab 08 — NDG NETLAB+ (Document Version: 2016-11-14)*
