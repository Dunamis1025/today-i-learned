# Lab 03: Customize the Virtual Memory

## Overview

This lab covers how to customize virtual memory (paging file) settings on a Windows 10 client machine. By manually configuring the paging file size and location, administrators can optimize system performance based on specific workload requirements.

---

## Environment

| Virtual Machine      | IP Address     | Account       | Password   |
|----------------------|----------------|---------------|------------|
| Windows 10 PC1       | 192.168.1.203  | student       | Train1ng$  |
| Windows 10 PC2       | 192.168.1.202  | student       | Train1ng$  |
| Windows Server 2012 R2 | 192.168.1.200 | Administrator | Train1ng$  |

---

## Key Concepts

### What is Virtual Memory?
- Virtual memory is a section of the hard disk that Windows uses **as if it were RAM**.
- It is managed through a **paging file** (`pagefile.sys`), which temporarily holds data that cannot fit in physical RAM.
- When RAM is full, Windows moves inactive pages of memory to the paging file on disk, freeing up RAM for active processes.

### Why Customize Virtual Memory?
- The default "System managed" setting may allocate more or less space than needed.
- Manual configuration allows you to:
  - **Control the minimum and maximum size** of the paging file to avoid unexpected disk usage.
  - **Improve performance** by placing the paging file on a dedicated, faster drive separate from the OS drive.
  - **Reduce disk I/O contention** by offloading paging activity away from the C: drive (which handles OS read/write operations).

---

## Steps Performed

### Step 1 — Access System Properties

1. Right-click the **Start Menu** and select **System**.
2. In the System window, click **Advanced system settings** from the left pane.
3. In the **System Properties** dialog, go to the **Advanced** tab.
4. Under the **Performance** section, click **Settings**.
5. In the **Performance Options** window, click the **Advanced** tab.
6. Note the current **Total paging file size for all drives** shown under the *Virtual memory* section.
7. Click **Change** to open the **Virtual Memory** window.

---

### Step 2 — Configure a Custom Paging File on Drive X:

1. **Uncheck** the option: `Automatically manage paging file size for all drives`.
2. Select the **X: [New Volume]** drive from the drive list.
   - Space available: **2023 MB**
3. Select the **Custom size** radio button.
4. Enter the following values:
   - **Initial size (MB):** `500`
   - **Maximum size (MB):** `1100`
     > Maximum must be larger than the minimum allowed (16 MB) but smaller than the recommended size (1151 MB).
5. Click **Set** to apply the custom paging file to X:.

---

### Step 3 — Remove Paging File from Drive C:

1. Select the **C:** drive from the drive list.
2. Select the **No paging file** radio button.
3. Click **Set**.
4. A **System Properties warning** will appear:
   > *"If you disable the paging file or set the initial size to less than 200 megabytes and a system error occurs, Windows might not record details that could help identify the problem. Do you want to continue?"*
5. Click **Yes** to confirm.

> ✅ After this step, the drive list should show:
> - **C:** → `None`
> - **X: [New Volume]** → `500 - 1100`

---

### Step 4 — Apply and Close

1. Click **OK** on the Virtual Memory window.
2. Click **OK** on the Performance Options window.
3. Click **OK** on the System Properties window.
4. Close all remaining open windows.

---

## Observations

| Setting                        | Value       |
|-------------------------------|-------------|
| Selected Drive                | X: [New Volume] |
| Space Available               | 2023 MB     |
| Initial Size (MB)             | 500         |
| Maximum Size (MB)             | 1100        |
| Minimum Allowed               | 16 MB       |
| Recommended                   | 1151 MB     |
| Currently Allocated (before)  | 640 MB      |
| C: Drive Paging File (after)  | None        |

---

## Lab Questions & Answers

**Q1. What is the total paging file size listed for the Virtual memory?**  
The total paging file size was **640 MB** (currently allocated before changes).

**Q2. What Drive [Volume Label] contains the paging file?**  
The **C:** drive originally contained the paging file (System managed).

**Q3. What is the Recommended value for Total paging file size for all drives?**  
The recommended value was **1151 MB**.

**Q4. What is a benefit of customizing the size of the Virtual memory?**  
Customizing virtual memory allows the administrator to prevent Windows from over-allocating disk space for the paging file, and ensures the system has a predictable, controlled amount of virtual memory available — improving stability and performance tuning.

**Q5. Why would it be beneficial to move the Virtual memory to a different physical disk than the C: drive?**  
The C: drive is heavily used by the operating system for read/write operations. Moving the paging file to a separate physical disk (e.g., X:) distributes disk I/O load across multiple drives, reducing bottlenecks and improving overall system performance.

---

## Summary

In this lab, virtual memory was manually configured on a Windows 10 machine by:
- Disabling automatic paging file management
- Creating a custom paging file on the X: drive (500 MB initial, 1100 MB maximum)
- Removing the paging file from the C: drive to reduce I/O contention on the OS drive

This kind of configuration is useful in environments where performance tuning and disk management are critical administrative tasks.
