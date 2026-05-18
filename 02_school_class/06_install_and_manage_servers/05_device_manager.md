# Lab 05: Managing the Device Manager

## Overview

This lab focuses on using the **Device Manager** in Windows 10 to view, manage, and update hardware device drivers installed on a client machine.

---

## What is Device Manager?

Device Manager is a built-in Windows tool that acts as a **control tower** for all hardware components connected to a computer (monitors, mice, keyboards, etc.).

Every hardware device needs a **driver** — a translator that allows Windows to communicate with the hardware. Device Manager lets you:

- View all installed devices and their status
- Update or roll back drivers
- Disable or uninstall devices

---

## Lab Environment

| Virtual Machine      | IP Address     | Account       | Password   |
|----------------------|----------------|---------------|------------|
| Windows 10 PC1       | 192.168.1.203  | student       | Train1ng$  |
| Windows 10 PC2       | 192.168.1.202  | student       | Train1ng$  |
| Windows Server 2012  | 192.168.1.200  | Administrator | Train1ng$  |

---

## How to Open Device Manager

1. Right-click the **Start Menu**
2. Select **System**
3. Click **Device Manager** in the left pane

---

## Task 1: Generic PnP Monitor

### Steps
1. Expand **Monitors** in Device Manager
2. Right-click **Generic PnP Monitor** → Select **Properties**
3. Check the **General** tab for Device Status
4. Click the **Driver** tab → Click **Update Driver**
5. Click **Cancel** → Review the **Roll Back Driver** button

### Q&A

**Q1. What is the Device Status of the Generic PnP Monitor?**  
> "This device is working properly."

**Q2. What are the two methods to update the driver?**  
> 1. **Search automatically for updated driver software** — Windows searches the internet and local computer automatically  
> 2. **Browse my computer for driver software** — Manually locate and install a driver file

**Q3. What is the purpose of the Roll Back Driver button?**  
> If a device stops working correctly after a driver update, Roll Back Driver reverts to the previously installed driver version.

**Q3b. Why is Roll Back Driver grayed out?**  
> Because the driver has never been updated before — there is no previous version to roll back to.

---

## Task 2: VMware Pointing Device

### Steps
1. Expand **Mice and other pointing devices**
2. Right-click **VMware Pointing Device** → Select **Properties**
3. Navigate to the **Driver** tab

### Driver Info Observed

| Field           | Value                                      |
|-----------------|--------------------------------------------|
| Driver Provider | VMware, Inc.                               |
| Driver Date     | 3/26/2012                                  |
| Driver Version  | 12.5.2.0                                   |
| Digital Signer  | Microsoft Windows Hardware Compatibility Publisher |

### Q&A

**Q4. Who is the provider of the VMware Pointing Device driver?**  
> **VMware, Inc.**

**Q4b. Can this driver use the Roll Back Driver feature?**  
> **No** — the Roll Back Driver button is grayed out, meaning the driver has not been previously updated.

---

## Key Takeaways

- Device Manager is the go-to tool for diagnosing and managing hardware issues in Windows.
- **Device Status** tells you whether a device is functioning correctly.
- **Update Driver** has two options: automatic (internet) or manual (local file).
- **Roll Back Driver** is only available if the driver has been updated at least once before.
- A grayed-out button means the feature is unavailable in the current state.
