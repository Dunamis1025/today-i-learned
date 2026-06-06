# Lab 11: Using the Startup Folder — Study Notes

> **Course:** Windows 10 Administration Lab Series  
> **Topic:** Managing Startup Programs on Windows 10  
> **Environment:** NETLAB+ Virtual Lab (PC1: 192.168.1.203 / Server: 192.168.1.200)

---

## 📌 Objective

Learn how to **view, add, enable, disable, and manually remove** programs that automatically launch when a Windows 10 user logs in.

---

## 🧠 Key Concepts

### 1. What is the Startup Folder?
The Startup Folder is a special Windows directory that contains **shortcuts to programs** that should automatically run when a user logs in.

- **Per-user path:**  
  `C:\Users\<username>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
- **Quick access via Run dialog:**  
  Press `Win + R` → type `shell:Startup` → press OK

> Any shortcut placed in this folder will be executed at login for that specific user.

---

### 2. Task Manager — Startup Tab
Task Manager provides a GUI to **monitor and control** startup programs.

**How to open:**
- Right-click the Start Menu → Select **Task Manager**
- If minimized view appears, click **"More details"**
- Navigate to the **Startup** tab

**Columns explained:**

| Column | Description |
|--------|-------------|
| Name | Application name |
| Publisher | Developer/company |
| Status | Enabled = will run at login / Disabled = will NOT run |
| Startup impact | Performance impact on boot time |

---

## 🔬 Lab Walkthrough

### Step 1 — View Current Startup Programs

1. Right-click Start Menu → **Task Manager** → **Startup tab**
2. Observed the following entries:

| Name | Publisher | Status |
|------|-----------|--------|
| Microsoft OneDrive | Microsoft Corporation | Disabled |
| Vmtoolsd (VMware Tools Core Service) | VMware, Inc. | Enabled |

**Q1: Which applications are set to start at login?**  
→ `Vmtoolsd` is the only **Enabled** startup application.

**Q2: How do you prevent an app from starting at login?**  
→ Right-click the application in the Startup tab → click **Disable**

**Q2: Where is the Vmtoolsd executable located?**  
→ `C:\Program Files\VMware\VMware Tools\vmtoolsd.exe`

---

### Step 2 — Add a New Program to Startup

1. Open Run dialog: Start Menu → type `Run` → open it
2. Type `shell:Startup` → click OK  
   → Opens: `C:\Users\student\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`
3. Right-click empty space → **New → Shortcut**
4. Enter location: `http://192.168.1.200` → click **Next**
5. Name the shortcut: `WebServer` → click **Finish**

**Q3: What folder opened?**  
→ `C:\Users\student\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

**Q4: When will the WebServer shortcut run?**  
→ Every time the user **logs in**, as long as it is **Enabled** in Task Manager.

---

### Step 3 — Verify in Task Manager

1. Re-open Task Manager → Startup tab
2. WebServer now appears in the list

| Name | Status |
|------|--------|
| Microsoft OneDrive | Disabled |
| Vmtoolsd | Enabled |
| WebServer | Disabled *(default when added via folder)* |

**Q5: How many applications are now listed?**  
→ **3 applications**

> ⚠️ Important: When a shortcut is added to the Startup folder, it may appear as **Disabled** in Task Manager by default. You must manually **Enable** it via Task Manager for it to run at next login.

---

### Step 4 — Enable WebServer & Verify at Login

1. In Task Manager → Startup tab → Right-click **WebServer** → **Enable**
2. Restart PC1: Start Menu → Power → **Restart**
3. Log back in as `student` / `Train1ng$`

**Q6: Did anything open automatically after login?**  
→ **Yes** — Internet Explorer launched automatically and attempted to connect to `http://192.168.1.200`  
(Connection failed because the web server service was not running, but the browser launch itself confirmed the startup shortcut worked correctly.)

---

### Step 5 — Disable the WebServer Startup Entry

1. Right-click Start Menu → Task Manager → Startup tab
2. Right-click **WebServer** → click **Disable**

**Q7: Will the browser open again at next restart?**  
→ **No** — because WebServer is now Disabled in Task Manager.

**Q7: If there is no Delete button, how do you fully remove the startup entry?**  
→ Open `shell:Startup` via Run dialog → **manually delete the WebServer shortcut file** from the folder.

---

## 🔐 Security Relevance

Understanding startup programs is critical in IT security because:

- **Malware** commonly registers itself in the Startup folder or registry to survive reboots
- IT administrators should **regularly audit** startup entries using Task Manager or tools like Autoruns (Sysinternals)
- Unauthorized startup entries may indicate a **compromised system**

---

## 📋 Two Ways to Manage Startup Programs

| Method | How | Scope |
|--------|-----|-------|
| **Startup Folder** | Place/delete shortcut in `shell:Startup` | Per-user |
| **Task Manager** | Enable/Disable in Startup tab | Per-user (toggle only, no delete) |

> To **permanently remove** a startup entry added via the Startup folder, you must delete the shortcut file directly from the folder — Task Manager only toggles Enable/Disable.

---

## 🗂️ Lab Environment Reference

| Virtual Machine | IP Address | Account | Password |
|----------------|------------|---------|----------|
| Windows 10 PC1 | 192.168.1.203 | student | Train1ng$ |
| Windows 10 PC2 | 192.168.1.202 | student | Train1ng$ |
| Windows Server 2012 R2 | 192.168.1.200 | Administrator | Train1ng$ |

---

*Document created based on hands-on lab completion — Windows 10 Administration Lab Series, Lab 11*
