# System Utilities Lab Notes

## Lab 1: Managing Consoles (MMC)

- Built a custom Microsoft Management Console (`mmc`) and added the following snap-ins: Computer Management, Device Manager, Disk Management.
- Saved the console to the desktop as a `.msc` file for one-click access to all admin tools.
- **Path to Event Viewer**: Computer Management snap-in → System Tools → Event Viewer.
- **Key takeaway**: MMC snap-ins can also target remote computers, which is the real value of building a custom console — an admin can manage multiple machines on a network from a single console instead of visiting each machine physically.

## Lab 2: Registry Editor (regedit)

Goal: observe how a GUI setting (desktop background color) is stored in the registry, and how export/import (`.reg` files) work.

Steps performed:
1. Set desktop background to a solid blue color via **Settings → Personalization → Background**.
2. Opened `regedit`, navigated to `HKEY_CURRENT_USER\Control Panel\Colors`, and found the `Background` value stored as an RGB string (e.g. `0 99 177`).
3. Exported the `Colors` key to `BlueBKG.reg` on the desktop.
4. Opened the `.reg` file in Notepad — confirmed it's a plain text file containing `"Background"="0 99 177"` along with all other color values.
5. Changed the desktop background to red — registry `Background` value updated to a new RGB string (e.g. `232 17 35`), while the exported file still contained the old blue value.
6. Re-imported `BlueBKG.reg` — the registry value changed back to blue **immediately**, but the actual desktop color stayed red until a **reboot**.
7. After reboot, the desktop displayed blue again.

**Key takeaway**: Importing a `.reg` file updates the registry database instantly, but running processes (like `explorer.exe`) don't necessarily re-read that data in real time. A reboot (or logoff/logon) forces Explorer to reload settings from the registry, which is why the visual change was delayed. This demonstrates the difference between *where a setting is stored* and *when it gets applied*.

## Lab 3: Managing System Files

### msinfo32 (System Information) — read-only tool

- **System Summary**:
  - Processor: Intel(R) Core(TM) i7-1065G7 CPU @ 1.30GHz, 4 cores / 8 logical processors (Hyper-Threading)
  - BIOS Version/Date: Insyde F.23, 23/08/2024 (Insyde = third-party BIOS/UEFI firmware vendor licensed by HP)
  - Installed Physical Memory (RAM): 16.0 GB
- **Components → Network**: Listed all network adapters. Learned to distinguish **real physical adapters** (Intel Wireless-AC 9560 Wi-Fi, Realtek PCIe GbE Ethernet, Bluetooth PAN) from **virtual/software adapters** created by installed software (WAN Miniports for VPN protocols, VMware VMnet1/2/8 virtual switches, SoftEther VPN client adapter, DisplayLink docking station adapter, Wi-Fi Direct virtual adapters).
- **Software Environment → Startup Programs**: Found the list of programs registered to auto-launch at boot (via registry Run keys), including KakaoTalk, OneDrive, Teams, Steam, SoftEther VPN, AhnLab Safe Transaction, Webex, etc. Confirmed this list reflects registry *registration*, not necessarily active runtime status.

### Task Manager → Startup Apps tab (where enable/disable actually happens)

- Reviewed startup app list with Status and Startup Impact columns.
- Confirmed Steam and Microsoft Teams were already disabled.
- Disabled several low-value/non-essential startup items: WSHelper.exe, Logi Download Assistant / LogiLDA.DLL, Intel Graphics Command Center, Mobile devices, UBIKeyService.exe (fingerprint service — not used), StSess.exe (AhnLab Safe Transaction — Korean online banking security tool, not used).
- Left HP-specific hardware helpers and driver-related services untouched to preserve hotkey/device functionality.
- **Key takeaway**: msinfo32 shows what's *registered* to start; Task Manager's Startup Apps tab is the actual control switch for enabling/disabling those items. Realistic impact on boot speed is modest since most disabled items were flagged "Not measured" (low impact) rather than "High."

### msconfig (System Configuration)

- **General tab**: Startup selection options — Normal startup (all drivers/services), Diagnostic startup (minimal, for troubleshooting), Selective startup (manually choose services/startup items/boot config). Left on Normal startup.
- **Boot tab**: Lists installed OS entries (only Windows 11 present — no dual boot). Boot options reviewed but left unchecked: Safe boot (boots into Safe Mode — has sub-options Minimal/Alternate shell/AD repair/Network), No GUI boot, Boot log, Base video (low-res VGA driver, useful for display driver troubleshooting), OS boot information (verbose driver load info during boot). Timeout value controls OS selection menu wait time (irrelevant with only one OS installed).
- **Services tab**: Lists all Windows services with checkbox (registered to start) and Status (Running/Stopped right now). Used "Hide all Microsoft services" to isolate third-party services only, revealing installed software footprint: gaming (Battle.net, BattlEye, Steam, PUBG anti-cheat), cloud/collab (Dropbox x3, Discord, Bonjour/Apple), audio/graphics drivers (Realtek, NVIDIA, Intel, ELAN touchpad, Sound Research), AhnLab Safe Transaction service, Logitech Options+, and VMware core services (Authorization, DHCP, USB Arbitration — required for VM networking). No changes made in this tab (avoided using "Disable all").
- **Startup tab**: Confirmed it redirects to Task Manager for managing startup items (msconfig no longer manages this directly in modern Windows).
- **Tools tab**: Not yet reviewed in detail — pending.

### dxdiag (DirectX Diagnostic Tool)

- Not yet performed in this session — pending for a future study block.

## Reflection Questions

1. **Why is it useful to disable a service in System Configuration?**
   Disabling unused services frees up CPU/memory and can shorten boot time, though the real-world impact depends heavily on which services are involved — most non-critical third-party services have negligible impact, while a few (flagged "High" impact) matter more.

2. **When would you use the Startup tab of System Configuration?**
   When boot time is unacceptably slow or unwanted programs keep auto-launching on startup — though in modern Windows this management actually happens through Task Manager's Startup Apps tab rather than msconfig itself.

## Outstanding items for next session
- [ ] msconfig → Tools tab review
- [ ] dxdiag (System / Display / Sound / Input / extra tabs)
