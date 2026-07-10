# Windows Control Panel & System Administration — Study Notes

## 1. Control Panel Categories Overview

| Category | Used For |
|---|---|
| Clock and Region | Changing date/time format and regional/locale settings |
| Network and Internet | Checking connection status, network adapters |
| User Accounts | Creating/managing user accounts and permissions |
| Hardware and Sound | Configuring printers, speakers, and other external devices |
| System and Security | Checking firewall status, general system security |
| Appearance and Personalization | Managing themes, fonts, visual settings |
| Programs | Managing installed programs, default apps for file types |
| Ease of Access | Accessibility settings (text size, screen reader, etc.) |

## 2. User Accounts

- A single **Administrator account** is created automatically during Windows installation. Additional accounts are created via the **User Accounts** Control Panel item.
- **Administrator account**: full control — can change any system setting and access any file/folder. Must be managed carefully due to its power.
- **Standard account**: limited to the user's own files/folders; cannot make system-wide changes.

**Why use Standard accounts for most users?**
Standard accounts prevent accidental or malicious changes to critical system files/settings — reducing security risk and keeping the system stable.

### User Account Control (UAC)
- A security feature that monitors programs attempting to change the system and prompts the user for approval.
- Sensitivity level is adjustable via a slider.
- Default: notify only when a program tries to make changes to the computer.
- **Admin account running elevated task** → only needs to click "Yes" (no password, since already an admin).
- **Standard account running elevated task** → must enter an *administrator's* password to proceed.

### Deleting Accounts
- Two options when removing a user account:
  - **Delete Files** — removes the user's data along with the account.
  - **Keep Files** — preserves the user's files (useful when data belongs to the organization or must be handed off to someone else).

### Reflection Takeaways
- Strong passwords protect against unauthorized access to personal data and the system.
- Standard privileges limit a user's ability to alter core settings or install harmful software.
- IT admins keep files (rather than deleting) when the data is a company asset or needed by another team member.

## 3. Permissions

### Permission Inheritance
- Files/folders created inside a folder automatically **inherit** that folder's permissions.
- A new file's permissions match its parent folder's permissions — it doesn't set its own.
- The **Permissions tab** (Advanced Security Settings) lets you manually allow/deny specific rights (Read, Write, Modify, Full Control) per user/group.
- Effective permissions can be checked per user via **Advanced → Effective Access**.

### Encrypting File System (EFS)
- Encrypts individual files/folders so only the encrypting user's account can access the content.
- **Not available in Windows Home edition.**
- If another user tries to open/edit an EFS-encrypted file, access is denied — protecting data privacy between accounts.

## 4. Other User/Account Tools

- **Credential Manager**: securely stores usernames/passwords for websites and Windows apps; lets you view, edit, or delete saved credentials (useful when you forget a network app's password).
- **Sync Center**: keeps network files synchronized across devices — edits made offline are automatically merged with the network copy once reconnected.

### Quick Reference — Which Tool for Which Task?
| Scenario | Tool |
|---|---|
| Promote an employee to admin | Change account type |
| Forgot password for a network app | Credential Manager |
| Need access to another user's files | Administrator account |
| Create account for new employee on shared PC | Manage another account |
| Need to edit network files while offline | Sync Center |
| Want fewer/more UAC prompts | UAC settings |
| Account limited to own profile only | Standard user |

## 5. Networking

- Windows 10+ provides a **unified Settings app** for network configuration (replacing scattered Control Panel items), including Airplane Mode, Mobile Hotspot, and Data Usage — useful for both Wi-Fi and cellular connections.
- **Network and Sharing Center**: central hub to view network status and configure sharing; automatically adjusts settings based on whether the network is Public or Private.
- **Internet Options**: configures Internet Explorer (and related) settings — General, Security, Privacy, Content, Connections, Programs, Advanced tabs.
- **HomeGroup**: legacy feature for simple file/printer sharing between PCs on the same network via a shared password. **Removed starting with Windows 10 version 1803.**

### Quick Reference
| Task | Tool |
|---|---|
| Settings change automatically by network type | Network and Sharing Center |
| Change adapter protocols/services | Network and Sharing Center |
| Reset browser to default settings | Internet Options |
| Clear browsing history | Internet Options |
| Removed in new Windows 10 versions | HomeGroup |
| Easily share files/devices on LAN | HomeGroup |

## 6. Browser Settings (Microsoft Edge)

- **Set as default browser**: via Edge Settings → Default browser, or Windows Settings → Default apps.
- **Check version**: Edge Settings → About Microsoft Edge.
- **Clear browsing history**: Edge → History (Ctrl+H) to view, then Settings → Privacy, search, and services → Clear browsing data.
- **Clear diagnostic data**: Windows Settings → Privacy → Diagnostics & feedback → Delete.
- **Security settings**: Edge Settings → Privacy, search, and services → Security section (includes "Enhanced security" toggle).
- **Tracking prevention**: three levels available in Privacy, search, and services.
- **Cookies**: managed under Cookies and site permissions → See all cookies and site data.
- **Microsoft Defender SmartScreen**: found in Windows Security → App & browser control → Reputation-based protection settings. Protects against phishing/malware by scanning downloaded files and visited sites.

**Why clear browsing data/history?**
Protects privacy, improves browser performance, and frees up storage space.

## 7. Display Settings

- Windows 10: accessed via **Settings → System → Display**, or right-click desktop → Display settings.
- Use the monitor's **native (recommended) resolution** for the sharpest image, especially on LCD screens.

### Key Display Properties
| Setting | Meaning |
|---|---|
| Display | Select/configure a specific monitor (multi-monitor setups) |
| Screen resolution | Number of horizontal × vertical pixels; higher = sharper |
| Orientation | Landscape or Portrait |
| Refresh rate | Times the screen redraws per second (Hz) |
| Display colors | Color depth (bit depth) — higher = richer color range |
| Multiple displays | Extend desktop across monitors, or mirror the same image |

---
*Summarized from Windows OS / networking coursework notes (Cisco NetAcad-style material).*
