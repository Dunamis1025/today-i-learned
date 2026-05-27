# Lab 7: Connecting Through Remote Desktop
> Windows 10 Administration Lab Series  
> Source: CSSIA / NDG NETLAB+  
> Date Studied: 2026-05-27

---

## 📌 Overview

| Item | Detail |
|------|--------|
| **Objective** | Configure and use Remote Desktop Connection (RDC) between two Windows 10 machines |
| **Platform** | Windows 10 Pro |
| **Lab Environment** | NDG NETLAB+ virtual lab |

---

## 🖧 Lab Topology

```
          [Server]
        192.168.1.200
              |
    192.168.1.0/24 Network
       /              \
  [PC1]             [PC2]
192.168.1.203    192.168.1.202
```

---

## ⚙️ Lab Settings

| Virtual Machine      | IP Address      | Account       | Password   |
|----------------------|-----------------|---------------|------------|
| Windows 10 PC1       | 192.168.1.203   | student       | Train1ng$  |
| Windows 10 PC2       | 192.168.1.202   | student       | Train1ng$  |
| Windows Server 2012 R2 | 192.168.1.200 | Administrator | Train1ng$  |

---

## 🔬 Lab Walkthrough

### Section 1 — Access PC1 and Check IP Address

**Goal:** Verify PC1's IP address using `ipconfig` before attempting any remote connection.

**Steps on PC1:**
1. Log in as `student` / `Train1ng$`
   - If a black screen with date/time appears → click anywhere to get the login prompt
2. Right-click the **Start Menu** → select **Command Prompt**
3. Run the following command:
   ```cmd
   ipconfig
   ```
4. Record the IPv4 address (expected: `192.168.1.203`)

---

### Section 1.3 — Attempt Remote Desktop from PC2 (Initial Failure)

**Steps on PC2:**
1. Log in as `student` / `Train1ng$`
2. Click **Start Menu** → type `Remote Desktop` → open **Remote Desktop Connection**
3. Enter PC1's IP address (`192.168.1.203`) → click **Connect**

**Result:** ❌ Connection fails with the following error message:

> *"Remote Desktop can't connect to the remote computer for one of these reasons:*
> 1. Remote access to the server is not enabled
> 2. The remote computer is turned off
> 3. The remote computer is not available on the network"*

#### 💬 Question Bank 1
**Q: Which of the three reasons is the most likely cause of the failure?**  
**A:** Reason **#1 — Remote access to the server is not enabled.**  
PC1 and PC2 are both powered on and reachable on the same network (`192.168.1.0/24`), so the machine being off or unreachable is unlikely. The root cause is that Remote Desktop was not enabled on PC1 beforehand.

---

### Section 2 — Enable Remote Desktop on PC1

**Steps on PC1:**
1. Right-click **Start Menu** → select **System**
2. In the System window (Control Panel), click **Remote settings** in the left pane
3. In the **System Properties** dialog → go to the **Remote** tab
4. Under **Remote Desktop**, select:
   - ✅ **Allow remote connections to this computer**
5. Click **OK** to save

> ⚠️ Note: The option *"Allow connections only from computers running Remote Desktop with Network Level Authentication (recommended)"* can optionally be checked for added security. In this lab it is left unchecked for simplicity.

---

### Section 3 — Connect from PC2 to PC1 (Success)

**Steps on PC2:**
1. Return to the **Remote Desktop Connection** window
2. Enter PC1's IP (`192.168.1.203`) → click **Connect**
3. A **Windows Security** dialog appears → enter password `Train1ng$` for the `student` account → click **OK**
4. A certificate warning appears:
   - *"The identity of the remote computer cannot be verified."*
   - Certificate error: *"The certificate is not from a trusted certifying authority."*
   - Click **Yes** to proceed anyway

**Result:** ✅ Remote Desktop session to PC1 is established successfully.

#### 💬 Question Bank 2

**Q: What is displayed at the top of the screen after connecting that identifies PC1 is being used?**  
**A:** The Remote Desktop toolbar at the top shows PC1's IP address — `192.168.1.203` — confirming the remote session is connected to PC1.

**Q: While remotely connected to PC1, what option(s) appear under the Start Menu Power icon?**  
**A:** Only **Disconnect** is shown (instead of the usual Shut down / Restart / Sleep options). This is because Windows restricts power management options during a remote session to prevent unintended shutdowns of the remote machine.

---

### Section 3 (continued) — Create a File Remotely

**Steps (while connected to PC1 via Remote Desktop from PC2):**
1. Right-click on the **Desktop** → **New** → **Text Document**
2. Name the file: `PC2 Was Here`
3. Click the **white X** on the Remote Desktop toolbar to disconnect
4. Click **OK** to confirm disconnection

> 📝 Note: When you disconnect from a Remote Desktop session, programs on the remote computer continue running. You can reconnect later by logging in again.

---

### Section 4 — Verify the File on PC1

**Steps on PC1:**
1. Return to the PC1 viewer
2. Log in again as `student` / `Train1ng$`

#### 💬 Question Bank 3
**Q: Why is it necessary to log in to PC1 again?**  
**A:** When PC2 connected via Remote Desktop and then disconnected, the session on PC1 was locked/logged off. A Remote Desktop session locks the local screen of the remote machine, so physical re-login is required to access it locally.

#### 💬 Question Bank 4

**Q: Is the file created by PC2 (`PC2 Was Here`) on PC1's desktop?**  
**A:** Yes. The file appears on PC1's desktop because the Remote Desktop session gave PC2 full control of PC1's environment, including the ability to create, edit, and delete files.

**Q: What are some benefits of using Remote Desktop Connection?**  
**A:**
- Access and control a remote computer from anywhere on the network
- Manage files and applications on the remote machine without physical presence
- Administrators can troubleshoot and configure systems remotely
- Reduces the need for on-site support
- Supports centralized administration of multiple machines

---

## 🧠 Key Concepts

### What is Remote Desktop Connection (RDC)?
Remote Desktop Connection is a Windows built-in feature (using the **RDP — Remote Desktop Protocol**, port **3389**) that allows a user to remotely control another computer over a network.

### Requirements for RDP to Work
| Requirement | Details |
|---|---|
| Remote Desktop enabled | Must be turned on in System Properties → Remote tab |
| Network connectivity | Both machines must be on the same network or routable |
| Firewall | Port 3389 (TCP) must be allowed |
| User account | Must have valid credentials on the remote machine |
| Windows edition | Remote Desktop *host* requires Windows Pro, Enterprise, or Server (not Home) |

### How the Connection Flow Works
```
PC2 (Client)                        PC1 (Host/Server)
    |                                       |
    |-- RDP connection request (port 3389) ->|
    |                                       |-- Check if RDP is enabled
    |<-- Certificate presented -------------|
    |-- Accept cert + send credentials ---->|
    |                                       |-- Authenticate user
    |<===== Remote Desktop Session =========|
    |    (PC1 screen locked locally)        |
```

### Remote vs. Local Session Behavior
| Feature | Local Session | Remote Desktop Session |
|---|---|---|
| Power options | Shut down, Restart, Sleep | Disconnect only |
| Screen lock | User-controlled | Locked when RDP connects |
| File access | Full | Full (same user permissions) |
| Running programs | Visible locally | Continues after disconnect |

---

## ⚠️ Common Errors & Troubleshooting

| Error | Likely Cause | Fix |
|---|---|---|
| "Remote access to server is not enabled" | RDP not turned on | Enable in System → Remote Settings |
| Certificate warning on connect | Self-signed cert (not from CA) | Click Yes to proceed (safe in trusted networks) |
| Connection refused | Firewall blocking port 3389 | Allow RDP through Windows Firewall |
| Login fails after disconnect | Session was locked | Log back in with valid credentials |

---

## 📝 Summary

This lab demonstrated the end-to-end process of setting up and using Windows Remote Desktop between two machines:

1. **Diagnosed** a connection failure caused by RDP being disabled on the host
2. **Enabled** Remote Desktop on PC1 via System Properties
3. **Connected** successfully from PC2 using Remote Desktop Connection
4. **Performed actions** (created a file) on PC1 remotely from PC2
5. **Verified** the changes persisted on PC1 after the session ended

> Remote Desktop is a foundational tool for Windows system administration, enabling remote access, management, and troubleshooting without physical access to the machine.
