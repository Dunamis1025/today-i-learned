# Lab 12: Configure Local User File Sharing (Windows 10)

## Overview

This lab covers the configuration of **local file sharing** on a Windows 10 client machine.  
The goal is to create a new user account, share a folder with restricted permissions, verify the access control, and clean up afterward.

---

## Lab Environment

| Virtual Machine        | IP Address     | Account       | Password   |
|------------------------|----------------|---------------|------------|
| Windows 10 PC1         | 192.168.1.203  | student       | Train1ng$  |
| Windows 10 PC2         | 192.168.1.202  | student       | Train1ng$  |
| Windows Server 2012 R2 | 192.168.1.200  | Administrator | Train1ng$  |

---

## Key Concepts

### 1. User Account Types in Windows 10

| Account Type   | Description |
|----------------|-------------|
| **Standard User** | Default type. Can use most software but cannot make system-level changes. |
| **Administrator** | Full control over the system — can install software, change settings, manage other accounts. |

> When a new local account is created without Microsoft sign-in, it defaults to **Standard User**.

---

### 2. Creating a Local User Account

**Path:** `Start Menu → Control Panel → User Accounts → Make changes to my account in PC settings → Family & other users → Add someone else to this PC`

- Enter **Username**, **Password**, and a **Password Hint**
- The new account is created as a **Local Account** with **Standard User** privileges by default

---

### 3. File Sharing with Specific Users

**Path:** `Right-click folder → Share with → Specific people`

- You can share a folder with individual user accounts on the same PC
- When sharing, you assign a **Permission Level** to each user:

| Permission Level | What the user can do |
|------------------|----------------------|
| **Read**         | View and open files only. Cannot modify or save changes. |
| **Read/Write**   | View, open, modify, and save files. |

> In this lab, the `TestShare` folder was shared with the `TEST` account using **Read** permission only.

---

### 4. Testing Access Control

- Logged in as `TEST` user and navigated to the shared folder via:  
  `File Explorer → Network → PC1 → Users → student → Desktop → TestShare`
- Successfully **opened** the `SharedDATA.txt` file (Read access confirmed)
- Attempted to **save changes** → received **"Access is denied"** error

**Why?**  
The `TEST` account was granted **Read-only** permission, which prevents any write operations (editing/saving) to the shared file.

---

### 5. Stopping File Sharing & Cleanup

**Stop Sharing:**  
`Right-click folder → Share with → Stop sharing`

**Delete Folder:**  
`Right-click folder → Delete → Empty Recycle Bin`

**Delete User Account:**  
`Control Panel → User Accounts → PC Settings → Family & other users → Select TEST → Remove → Delete account and data`

> Deleting an account also removes all associated data (desktop files, downloads, documents, etc.)

---

## Step-by-Step Summary

1. **Login** to PC1 as `student`
2. **Create** a new local account named `TEST` (Standard User)
3. **Create** a folder `TestShare` on the Desktop with a text file `SharedDATA.txt` inside
4. **Share** `TestShare` with the `TEST` account using **Read** permission
5. **Sign out** and log in as `TEST`
6. **Navigate** to the shared folder via Network path and attempt to edit the file
7. **Observe** "Access is denied" error — confirming Read-only restriction works
8. **Sign out** of `TEST`, log back in as `student`
9. **Stop sharing** the folder, delete it, and remove the `TEST` account

---

## Key Takeaways

- Windows 10 supports **per-user file sharing** with granular permission control
- **Read-only** sharing allows viewing but blocks any modification — useful for protecting sensitive files
- New local accounts are created as **Standard Users** by default, limiting system access
- Proper **cleanup** (removing shares and accounts) is important for security hygiene
- File sharing permissions are separate from file ownership — even if a file is visible, write access can be denied

---

## Vocabulary

| Term | Meaning |
|------|---------|
| **Local Account** | A user account that exists only on this specific PC (not linked to Microsoft) |
| **Standard User** | Limited account type — cannot make system-wide changes |
| **Administrator** | Full-privilege account type |
| **Read Permission** | Can only view/open files, not edit or save |
| **Read/Write Permission** | Can view, edit, and save files |
| **Access is denied** | Error shown when a user tries to perform an action they don't have permission for |
| **Share with** | Windows feature to grant other users access to a specific folder |
| **Stop sharing** | Revokes all shared access to a folder |
