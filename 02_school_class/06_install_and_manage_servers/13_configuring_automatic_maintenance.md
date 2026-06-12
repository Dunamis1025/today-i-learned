# Lab 13: Configuring Automatic Maintenance (Windows 10 Administration)

## Overview

This lab covers how Windows 10's **Automatic Maintenance** feature works, how to configure its schedule through the GUI, and how to fully disable it using the **Windows Registry** (since there is no built-in "off" toggle in the GUI).

**Environment:**
- Windows 10 PC1 (192.168.1.203) — `student` / `Train1ng$`
- Accessed via Control Panel → Security and Maintenance

---

## Part 1: Configuring the Automatic Maintenance Schedule

### What is Automatic Maintenance?
A built-in Windows 10 feature that automatically runs background tasks to keep the system healthy, including:
- Software updates
- Security scanning (Windows Defender)
- System diagnostics / reliability checks
- Disk and performance optimization

### Steps
1. Right-click **Start Menu** → **Control Panel**
2. Open **Security and Maintenance**
3. Expand the **Maintenance** section
4. Click **Change maintenance settings**
5. Set **"Run maintenance tasks daily"** to a custom time (e.g., **10:00 PM**)
6. Confirm the checkbox **"Allow scheduled maintenance to wake up my computer at the scheduled time"** is enabled
7. Click **OK**

### Manually Triggering Maintenance
- From the **Maintenance** section, click **Start maintenance**
- Status changes to **"Maintenance in progress"**, with an option to **Stop maintenance**
- The process can take **10–15 minutes**
- Once complete, the status returns to **"No action needed"**

---

## Key Q&A (Question Banks)

### Q1 — Why leave "Allow scheduled maintenance to wake up my computer" checked?
Even if the computer is asleep at the scheduled maintenance time (e.g., 10:00 PM), Windows will **wake the device**, complete updates/scans/diagnostics, and then allow it to return to sleep. This ensures maintenance happens **off-hours** rather than interrupting the user during active work hours — improving both performance during the day and keeping the system up to date.

### Q2 — What status is shown after Start Maintenance completes?
**"No action needed"** — indicating maintenance ran successfully and no further user action is required.

### Q3 — What would happen if the registry value `MaintenanceDisabled` were set to `0` instead of `1`?
A value of `0` means **"do not disable maintenance"** — Automatic Maintenance would continue to function **normally**, exactly as if the registry key had never been created. The key acts as a binary switch:
- `0` = Maintenance **enabled** (default behavior)
- `1` = Maintenance **disabled**

---

## Part 2: Disabling Automatic Maintenance via Registry Editor

> ⚠️ There is no native GUI "off" switch for Automatic Maintenance — it must be disabled via the Windows Registry.

### Steps
1. Right-click **Start Menu** → **Run**
2. Type `regedit` → click **OK**
3. Approve the **User Account Control (UAC)** prompt (**Yes**)
4. Navigate to:
   ```
   HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Maintenance
   ```
5. In the right pane, right-click empty space → **New** → **DWORD (32-bit) Value**
6. Name the new value: **`MaintenanceDisabled`**
7. Right-click the new value → **Modify**
8. Set **Value data** from `0` to `1` (Base: Hexadecimal) → click **OK**

### Result
The registry now contains:
| Name | Type | Data |
|------|------|------|
| MaintenanceDisabled | REG_DWORD | 0x00000001 (1) |

---

## Part 3: Verifying Automatic Maintenance is Disabled

1. Open **Control Panel** → **Security and Maintenance**
2. Expand the **Maintenance** section
3. Click **Start maintenance**

### Expected Result
**No action occurs** — clicking "Start maintenance" produces no response (no "Maintenance in progress" status, no progress indication).

This confirms that the `MaintenanceDisabled = 1` registry value successfully overrides the GUI control and **prevents the Automatic Maintenance service from running**, even when manually triggered.

---

## Key Takeaways

1. **GUI-level configuration**: Automatic Maintenance's *schedule* (time of day) can be customized via Control Panel → Security and Maintenance, but the feature **cannot be turned off** from the GUI.
2. **Registry-level control**: Creating a `DWORD` value named `MaintenanceDisabled` under
   `HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\Maintenance` and setting it to `1` **fully disables** the feature, including manual triggers ("Start maintenance").
3. **Binary switch logic**: `0` = feature behaves normally (enabled); `1` = feature is disabled. This is a common pattern across many Windows registry-based feature toggles.
4. **Wake-on-maintenance**: Keeping "Allow scheduled maintenance to wake up my computer" enabled ensures maintenance tasks run during off-hours without disrupting active use — a useful consideration for IT administrators managing fleets of PCs.
5. **Verification methodology**: After making a system-level change (like a registry edit), always verify the change took effect by testing the original functionality (here, attempting to manually start maintenance and observing no response).

---

*Lab Source: NDG Windows 10 Administration Lab Series — Lab 13: Configuring Automatic Maintenance (Document Version: 2016-11-14)*
