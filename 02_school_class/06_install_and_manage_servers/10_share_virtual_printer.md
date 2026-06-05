# Lab 10: Share a Virtual Printer — Study Notes

## Overview
This lab teaches how to share a printer between two Windows 10 machines (PC2 as host, PC1 as client) over a local network, covering installation, sharing configuration, and remote connection.

---

## Key Concepts

### What You're Learning
- How computers share resources (printers) over a network without physical cable connections
- How to configure sharing permissions and security settings
- How a client PC discovers and connects to a shared network printer

### Real-World Analogy
Like using a printer in your living room from your bedroom computer — through your home router (network) as the virtual pathway.

---

## Lab Environment
| Machine | IP Address | Account | Password |
|---|---|---|---|
| Windows 10 PC1 (Client) | 192.168.1.203 | student | Train1ng$ |
| Windows 10 PC2 (Host) | 192.168.1.202 | student | Train1ng$ |
| Windows Server 2012 R2 | 192.168.1.200 | Administrator | Train1ng$ |

---

## Step-by-Step Summary

### Section 1 — On PC2 (Host): Install a Virtual Printer
1. Open **Control Panel** → **Devices and Printers** → **Add a printer**
2. Click **"The printer that I want isn't listed"**
3. Select **"Add a local printer or network printer with manual settings"**
4. Port: **FILE: (Print to File)**
5. Driver: Manufacturer = **Generic**, Printer = **Generic / Text Only**
6. Printer name: `Network Virtual Printer`
7. Select **"Do not share this printer"** (sharing is configured separately)
8. Click **Finish**

### Section 2 — On PC2: Configure Sharing & Network Settings
1. Right-click **Network Virtual Printer** → **Printer Properties** → **Sharing tab**
2. Go to **Network and Sharing Center** → **Change advanced sharing settings**
3. Under **Private profile**: Turn on **Network discovery** + **File and printer sharing**
4. Under **All Networks**: Turn off **Password protected sharing** → **Save changes**
5. Back in Printer Properties → Sharing tab:
   - Check **"Share this printer"**
   - Share name: `PC2 Network Virtual Printer`
   - Click **Apply** → **OK**

### Section 3 — On PC1 (Client): Connect to Shared Printer
1. Open **Network and Sharing Center** → **Change advanced sharing settings**
2. Turn on **File and printer sharing** (Private profile)
3. Turn off **Password protected sharing** (All Networks) → **Save changes**
4. Open **Devices and Printers** → **Add a printer**
5. Click **"The printer that I want isn't listed"**
6. Select **"Select a shared printer by name"**
7. Enter: `\\PC2\PC2 Network Virtual Printer` → **Next** → **Finish**

### Section 4 — Verify the Connection
1. Right-click the newly added **Network Virtual Printer on PC2** → **Printer Properties**
2. On the **General** tab → click **Print Test Page**
3. Save the file as `NetworkPrint` to the Desktop
4. A dialog confirms: *"A test page has been sent to your printer"* → Click **Close**

---

## Troubleshooting: PC2 Not Visible in Network Browser

This was encountered during the lab. Here's what was tried and what worked:

| Attempt | Result |
|---|---|
| Refresh file explorer | ❌ PC2 still not visible |
| `\\192.168.1.202\PC2 Network Virtual Printer` (IP path) | ❌ "Windows couldn't connect to the printer" |
| Checked Network Discovery on PC2 | ✅ Already enabled — not the issue |
| Turned off Windows Firewall on PC2 (Private + Public) | ❌ Still failed with IP path |
| Ran `net share` on PC2 to verify share name | ✅ Confirmed `PC2 Network Virtual Printer` is shared |
| Ran `net use \\PC1\IPC$ /user:student Train1ng$` on PC2 | ✅ Authenticated session opened |
| `\\PC2\PC2 Network Virtual Printer` (hostname path) | ✅ **SUCCESS** |

### Root Cause
Using the **IP address** in the UNC path failed due to authentication/session issues in the virtual lab environment. Using the **computer hostname** (`PC2`) instead of the IP address resolved the issue.

### Key Takeaway
> When connecting to a shared printer in a Windows workgroup environment, always try the **hostname-based UNC path** (`\\computername\sharename`) before falling back to an IP address.

---

## Core Concepts to Remember

### UNC Path Format
```
\\ComputerName\ShareName
```
Example: `\\PC2\PC2 Network Virtual Printer`

### Important Settings Locations
- **Sharing permissions**: Control Panel → Devices and Printers → Printer Properties → Sharing
- **Network discovery**: Control Panel → Network and Sharing Center → Advanced sharing settings
- **Verify active shares**: Command Prompt → `net share`
- **Open authenticated session**: Command Prompt → `net use \\TargetPC\IPC$ /user:username password`

### Why This Matters (Real World)
- Offices share one printer across many computers → saves cost
- Admins must manage **who can access** shared resources (access control)
- Understanding UNC paths and network authentication is fundamental to Windows administration
