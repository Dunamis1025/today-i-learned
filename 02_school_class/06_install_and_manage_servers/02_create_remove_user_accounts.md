# Lab 02: Create and Remove User Accounts

**Course:** Windows 10 Administration  
**Platform:** NETLAB+ (Holmesglen)  
**Date Completed:** 2026-05-15  
**Lab Series:** Windows 10 Administration Lab Series

---

## 📌 Objective

Learn how to manage local user accounts on a Windows 10 client machine, including:
- Creating a new local user account
- Changing an account type from Standard User to Administrator
- Deleting a user account and removing associated data

---

## 🖥️ Lab Environment

### Network Topology

```
        [Server]
           |
   192.168.1.0/24
    .200 (Server)
   /              \
.203 (PC1)     .202 (PC2)
```

### Virtual Machine Credentials

| Virtual Machine       | IP Address     | Account       | Password   |
|-----------------------|----------------|---------------|------------|
| Windows 10 PC1        | 192.168.1.203  | student       | Train1ng$  |
| Windows 10 PC2        | 192.168.1.202  | student       | Train1ng$  |
| Windows Server 2012 R2| 192.168.1.200  | Administrator | Train1ng$  |

---

## 🔑 Key Concepts

| Term | Description |
|------|-------------|
| **User Account** | A profile that allows a person to log in and use a computer with personalized settings and permissions |
| **Local Account** | An account that only exists on one specific machine, not tied to any online/Microsoft account |
| **Standard User** | Default account type with limited permissions; cannot change system settings or install software |
| **Administrator** | Highest privilege account type; can install software, change system settings, and manage other accounts |
| **Control Panel** | A Windows utility hub for managing system settings, including user accounts |
| **Family & other users** | A section in Windows 10 Settings where non-family/guest accounts are managed |

---

## 🧪 Lab Steps

### Section 1 — Access the User Account Utility on PC1

1. Click on the **PC1** icon from the NETLAB topology page
2. Log in with:
   - Username: `student`
   - Password: `Train1ng$`
   > ⚠️ Note: The `1` in `Train1ng$` is the number one, not the letter i
3. Open the **Start Menu** → click **Control Panel**
4. In the All Control Panel Items window, click **User Accounts**
5. Click **"Make changes to my account in PC settings"**

---

### Section 2 — Create a New User Account

1. In the Settings window, click **"Family & other users"** in the left panel
2. Under **"Other users"**, click **"Add someone else to this PC"**
3. In the *Create an account for this PC* window, enter:
   - **Username:** `TEST`
   - **Password:** `password123`
   - **Re-enter password:** `password123`
   - **Password hint:** (any hint, e.g. `my password`)
4. Click **Next**
5. ✅ Verify: `TEST` now appears under **Other users** as a **Local account**

---

### Section 3 — Change Account Type to Administrator

1. Click on the **TEST Local account** entry to expand it
2. Click **"Change account type"**
3. In the *Change account type* window:
   - Note the current type: **Standard User** ← *(Answer to Question Bank 1)*
   - Click the **Account type** dropdown
   - Select **Administrator**
   - Click **OK**
4. ✅ Verify: TEST now shows as **"Administrator - Local account"**

---

### Section 4 — Delete a User Account and Remove Their Files

1. Click on the **TEST Administrator - Local account** entry
2. Click **"Remove"**
3. The *Delete account and data?* window opens — read the warning message ← *(Answer to Question Bank 2)*
4. Click **"Delete account and data"**
5. ✅ Verify: TEST account no longer appears under Other users
6. Close all open windows
7. End the NETLAB reservation to complete the lab

---

## ❓ Question Bank Answers

### Question Bank 1

**Q: What Account type was originally created for the TEST user account?**

> **A: Standard User**  
> When creating a new local account in Windows 10, the default account type is **Standard User**. This is a security best practice — new users are given the minimum permissions needed, and elevated access is only granted when necessary.

**Q: Why would someone want to change a user account from the default Account type to an Administrator account? What benefits does the Administrator account provide?**

> **A:**  
> An Administrator account is needed when the user requires elevated privileges such as:
> - Installing or uninstalling software
> - Changing system-wide settings
> - Managing other user accounts
> - Accessing protected system files and directories
> - Configuring network settings
>
> Standard Users are restricted from these actions as a security measure. In enterprise environments, the **Principle of Least Privilege** is applied — users only receive the minimum level of access required to perform their job.

---

### Question Bank 2

**Q: How is the delete account message in Windows 10 different from what you may have seen in a Windows 7 or Windows 8 client?**

> **A:**  
> In **Windows 7 / Windows 8**, when deleting an account, the system asked whether to **keep or delete** the user's files. The administrator had the choice to preserve files in a folder on the desktop before deletion.
>
> In **Windows 10**, there is **no such option**. The message directly states:
> *"Deleting this person's account will remove all their data from this PC, including items on their desktop, downloads, documents, photos, music, and other files. If this data hasn't been backed up or saved to another location, such as another PC, it will be lost."*
>
> This means Windows 10 **immediately and permanently deletes all user data** without giving the option to retain files — making data backup critical before account deletion.

---

## 💡 Key Takeaways

- **Always follow the Principle of Least Privilege** — create accounts as Standard Users by default; only promote to Administrator when necessary
- **Administrator ≠ Standard User** — Administrator accounts have full system control, which can be a security risk if misused
- **Deleting an account in Windows 10 is irreversible** — all user data is permanently removed; always back up data first
- **Local accounts** only exist on one machine — they are separate from Microsoft online accounts
- Windows 10 streamlined account management into the Settings app, moving away from the classic Control Panel interface used in Windows 7/8

---

## 🔗 References

- [Microsoft Docs — Manage user accounts in Windows](https://support.microsoft.com/en-us/windows/manage-user-accounts-in-windows-104dc19f-6430-4b49-6a2b-e4dbd1dcdf32)
- NDG NETLAB+ Windows 10 Administration Lab Series — Lab 02 (Document Version: 2016-11-14)
