# Lab 06: Customizing the Task Scheduler (Windows 10 Administration)

> **Course**: Windows 10 Administration Lab Series  
> **Institution**: Holmesglen (NETLAB+)  
> **Date Completed**: 2026-05-20  
> **Lab Reference**: CSSIA Win10ADM Lab 06

---

## Table of Contents

- [Overview](#overview)
- [Lab Environment](#lab-environment)
- [Key Concepts](#key-concepts)
- [Lab Walkthrough](#lab-walkthrough)
  - [Step 1: Access Task Scheduler](#step-1-access-task-scheduler)
  - [Step 2: View Active Tasks (QB1)](#step-2-view-active-tasks-qb1)
  - [Step 3: Create a Basic Task](#step-3-create-a-basic-task)
  - [Step 4: Explore cleanmgr (QB2)](#step-4-explore-cleanmgr-qb2)
  - [Step 5: Select ShutdownScript](#step-5-select-shutdownscript)
  - [Step 6: Review Settings Tab (QB3)](#step-6-review-settings-tab-qb3)
  - [Step 7: Modify Properties (QB4)](#step-7-modify-properties-qb4)
  - [Step 8: Delete the Task (QB5)](#step-8-delete-the-task-qb5)
- [Question Bank Answers](#question-bank-answers)
- [Key Takeaways](#key-takeaways)
- [Real-World Applications](#real-world-applications)

---

## Overview

The **Windows Task Scheduler** is a built-in Windows tool that allows administrators to automate tasks — running programs, scripts, or system tools at specified times or triggered by specific events — without requiring manual intervention.

Think of it like a **smartphone alarm**, but for computer tasks:
- Instead of waking you up, it runs a program or script automatically.
- It works even when no user is actively logged in (with the right settings).

---

## Lab Environment

| Virtual Machine       | IP Address      | Account       | Password   |
|-----------------------|-----------------|---------------|------------|
| Windows 10 PC1        | 192.168.1.203   | student       | Train1ng$  |
| Windows 10 PC2        | 192.168.1.202   | student       | Train1ng$  |
| Windows Server 2012 R2| 192.168.1.200   | Administrator | Train1ng$  |

**Network**: 192.168.1.0/24

---

## Key Concepts

### What is Task Scheduler?
Task Scheduler is a Windows administrative tool that:
- **Creates** automated tasks (programs, scripts, batch files)
- **Triggers** them based on time, events, or system states
- **Manages** permissions and conditions for each task

### Core Components

| Component | Description |
|-----------|-------------|
| **Trigger** | *When* the task runs (e.g., Daily, Weekly, At startup, On login) |
| **Action** | *What* the task does (e.g., run a program, send email) |
| **Condition** | *Under what conditions* it runs (e.g., only on AC power) |
| **Settings** | Additional behavior rules (e.g., stop if runs too long) |

### Trigger Types Available
- **Daily** — Runs every X days at a set time
- **Weekly** — Runs on specific days of the week
- **Monthly** — Runs on specific dates each month
- **One time** — Runs only once at a set time
- **When the computer starts** — Runs at boot
- **When I log on** — Runs at user login
- **When a specific event is logged** — Runs based on Event Viewer logs

---

## Lab Walkthrough

### Step 1: Access Task Scheduler

**Path**: `Start Menu → All Apps → Windows Administrative Tools → Task Scheduler`

The Task Scheduler window has three main panes:
- **Left pane**: Navigation tree (Task Scheduler Library)
- **Middle pane**: Task list and details tabs
- **Right pane**: Actions panel

---

### Step 2: View Active Tasks (QB1)

After opening Task Scheduler, scroll down to the **Active Tasks** section.

> **Active tasks** = tasks that are currently enabled and have not expired.

**Result observed**: `Summary: 49 total`

✅ **QB1 Answer: 49 active tasks**

---

### Step 3: Create a Basic Task

**Path**: Actions pane → `Create Basic Task...`

#### Wizard Steps:

**a) Name the Task**
- Name: `Shutdown Schedule`
- Click **Next**

**b) Set the Trigger**
- Selected: **Daily**
- Click **Next**

**c) Configure Daily Settings**
- Start date: Today's date (`5/20/2026`)
- Start time: `11:59:59 PM`
- Recur every: `1` days
- Click **Next**

> **Why 11:59:59 PM?**  
> This simulates a real-world scenario where a system administrator wants the computer to automatically shut down at the end of each business day — even if no one is around to do it manually.

> **What does "Recur every 1 days" mean?**  
> The task repeats every 1 day. Changing this to 7 would run it weekly, 2 would run it every other day, etc.

**d) Set the Action**
- Selected: **Start a program**
- Click **Next**

---

### Step 4: Explore cleanmgr (QB2)

In the file browser (System32 directory), searched for `cleanmgr`.

**Right-clicked → Open** to launch the application directly.

A small dialog appeared: **"Disk Cleanup : Drive Selection"**

✅ **QB2 Answers:**
- **Common name**: Disk Cleanup
- **Purpose**: A Windows utility that scans a selected drive (e.g., C:) and removes unnecessary/temporary files to free up disk space (temp files, recycle bin contents, system cache, etc.)

> Clicked **Exit** to close without running it.

---

### Step 5: Select ShutdownScript

Back in the file browser, searched for `ShutdownScript`.

- Selected `ShutdownScript.bat` located at `C:\Windows\System32\`
- Clicked **Open**

The wizard now showed:
```
Program/script: C:\Windows\System32\ShutdownScript.bat
```

Clicked **Next → Finish** to create the task.

The `Shutdown Schedule` task now appeared in the **Task Scheduler Library**.

---

### Step 6: Review Settings Tab (QB3)

Selected the `Shutdown Schedule` task → clicked the **Settings** tab in the bottom-middle pane.

**Default checked settings observed:**

| # | Setting | Purpose |
|---|---------|---------|
| ✅ 1 | **Allow task to be run on demand** | Lets administrators manually trigger the task immediately without waiting for the scheduled time. Useful for testing. |
| ✅ 2 | **Stop the task if it runs longer than: 3 days** | Safety limit — prevents a task from running indefinitely if something goes wrong. |
| ✅ 3 | **If the running task does not end when requested, force it to stop** | Forces the task to terminate even if it doesn't respond to a normal stop request. Ensures cleanup. |

✅ **QB3 Answer**: Allow task to be run on demand / Stop the task if it runs longer than 3 days / If the running task does not end when requested, force it to stop

---

### Step 7: Modify Properties (QB4)

**Right-clicked** `Shutdown Schedule` → **Properties**

In the Properties window (General tab), the Security options showed:
- 🔘 **Run only when user is logged on** ← default
- ⚪ **Run whether user is logged on or not**

Also checked: ✅ **Run with highest privileges**

> **Why does this matter?**  
> If a computer is powered on but the user has logged out, tasks set to "Run only when user is logged on" will **NOT execute**. To guarantee the task runs regardless of login state, you must switch to **"Run whether user is logged on or not"**.

✅ **QB4 Answer**: Change the setting in Properties from "Run only when user is logged on" to **"Run whether user is logged on or not"**

Clicked **OK** to save.

---

### Step 8: Delete the Task (QB5)

**Right-clicked** `Shutdown Schedule` → **Delete**

> **Why delete instead of just disabling?**  
> The lab asks what you *should* have done if you only wanted to **temporarily** stop the task.

**Comparison:**

| Action | Effect | Reversible? | Use Case |
|--------|--------|-------------|----------|
| **Delete** | Permanently removes the task | ❌ No | Task no longer needed |
| **Disable** | Pauses the task without deleting it | ✅ Yes (re-enable anytime) | Temporary suspension |

✅ **QB5 Answer**: **Disable** — visible in the right-click context menu and the Actions panel on the right side.

---

## Question Bank Answers

| # | Question | Answer |
|---|----------|--------|
| **QB1** | How many active tasks are displayed? | **49** |
| **QB2** | What is the common name of cleanmgr? | **Disk Cleanup** |
| **QB2** | What is the application used for? | **Removing unnecessary/temporary files to free up disk space** |
| **QB3** | Which three settings are checked by default? | **Allow task to be run on demand / Stop the task if it runs longer than 3 days / If the running task does not end when requested, force it to stop** |
| **QB4** | If a computer was logged out but still on, what ensures the task still runs? | **Change to "Run whether user is logged on or not" in Properties** |
| **QB5** | What action would temporarily prevent the task from running instead of deleting it? | **Disable** |

---

## Key Takeaways

1. **Automation**: Task Scheduler eliminates the need for manual execution of repetitive tasks. Admins can schedule maintenance, backups, shutdowns, and more.

2. **Triggers are flexible**: Tasks can be triggered by time (daily/weekly), system events (startup/login), or specific Windows Event Log entries.

3. **Permissions matter**: A task won't run if the required user isn't logged in — unless explicitly configured to run regardless of login state.

4. **Disable ≠ Delete**: Always prefer **Disable** over **Delete** when you might need to reactivate the task later. Deletion is permanent.

5. **Default safety settings**: Windows enables three protective settings by default to prevent tasks from running indefinitely or becoming unresponsive.

---

## Real-World Applications

| Scenario | Task Scheduler Use |
|----------|--------------------|
| Nightly server backup | Run a backup script daily at 2:00 AM |
| Weekly disk cleanup | Run `cleanmgr` every Sunday night |
| Automatic shutdown | Run shutdown script at 11:59 PM daily |
| Security scans | Trigger antivirus scan on system startup |
| Log rotation | Delete old log files on the 1st of each month |
| Software updates | Run update scripts when no user is logged in |

---

*Notes compiled from NETLAB+ Lab 06 hands-on session — Windows 10 Administration Lab Series*
