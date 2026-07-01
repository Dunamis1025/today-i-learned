# Windows File Explorer — Study Notes

## 1. This PC
Central view of all drives and devices connected to your computer. Appears by default when opening File Explorer (Windows 10/8.1). In Windows 7, the equivalent is accessed via "Computer" from the Start menu.

## 2. Run as Administrator
Some files/programs need elevated permissions to run for security reasons. Right-click → "Run as Administrator" → accept the UAC (User Account Control) prompt. Non-admin accounts may need to enter an administrator password.

## 3. Windows Libraries
Virtual folders that gather files from multiple physical locations (different folders, drives, or network locations) into one view — without actually moving the files. Windows ships with 6 default libraries, found in File Explorer's left pane.

## 4. Directory Structure
- Files are organized in a folder hierarchy, typically rooted at the C: drive.
- Folders inside folders are called **subfolders**.
- Each user account gets a separate folder; users cannot access each other's files without admin rights.

## 5. File & System Locations
- **User folder**: `C:\Users\<username>` — stores personal files (documents, photos, music).
- **System/Program folders**: contain OS and installed program files needed to run the computer.

## 6. File Extensions
- Max filename length: 255 characters; slashes (`/`, `\`) not allowed.
- A 3–4 letter extension (e.g., `.txt`, `.docx`) identifies file type; not case-sensitive.
- Hidden by default — enable via File Explorer → **View** tab → "File name extensions."

## 7. File Attributes
| Attribute | Meaning |
|---|---|
| **R** – Read-only | File can't be modified/overwritten; edits must be saved as a new file |
| **A** – Archive | Marks file as needing backup |
| **S** – System | Warns before deletion/modification |
| **H** – Hidden | File not shown in directory listing |

Set/viewed via file **Properties**.

## 8. File Properties Dialog (tabs)
- **General**: type, extension, location, size, dates, attributes.
- **Security**: controls which users/groups can read, modify, execute, or change permissions on the file.
- **Details**: same core info plus creator/owner.
- **Previous Versions**: restore older backups (if File History is enabled).

## 9. Folder Properties (additional tabs vs. files)
- **Sharing**: create access paths so other users/computers on a network can reach the folder.
- **Customize**: optimize folder appearance/icon for content type (music, videos, etc.) — purely aesthetic.
- Read-only/Hidden attributes on a folder apply to the files inside it.

## 10. Lab Answers — File Explorer
- Dragging Folder2 into Folder1 moves it inside; it disappears from the Desktop.
- Text document extension: `.txt`
- Copy a file: right-click → Copy → right-click destination → Paste.
- Common attributes shown: R, A, S, H.
- Full path example: `C:\Users\<username>\Desktop\Folder1\Folder2\Folder3`
- **Quick Access** default entries: Desktop, Downloads, Documents, Pictures — pinning folders here gives one-click access to frequently used locations.
- **Local Disk (C:)** typically contains: Windows, Program Files, Users, etc.
- **Users** folder contains one folder per account + a **Public** folder (shared by all local users, can also be networked).
- You can open your own user folder (you own the permissions); you generally cannot open another user's folder without admin rights (privacy/security separation).

## 11. Windows Libraries — Lab Answers
- Default library categories: Documents, Music, Pictures, Videos.
- To remove a folder from a library **without deleting it**: open the library's **Manage Library** (or Properties → Library locations) and remove the folder reference — the original files on disk are untouched.

## 12. Matching Recap
| Term | Definition |
|---|---|
| Users folder | Auto-created per account |
| A | Archive attribute |
| .docx | Word document extension |
| System folder | Core files Windows needs to run |
| This PC | Access point for all storage devices |
| Libraries | Virtual folders aggregating files from multiple locations |
| Run as Administrator | Opens files/apps needing elevated privileges |

---

## 13. Control Panel

**Settings app vs. Control Panel**: Windows 10 offers both. The modern **Settings** app handles simple/common changes; the classic **Control Panel** offers deeper, more technical configuration options — favored by IT professionals.

**Accessing it**: search "Control Panel" from Start; can be pinned to Start for convenience.

**View modes**: Category, Large icons, Small icons. Category view (default) groups related settings together, making things easier to find.

### Main Categories
- **System and Security** – system health checks, troubleshooting, firewall, security settings.
- **Network and Internet** – internet connections, Wi-Fi, network sharing.
- **Hardware and Sound** – printers, mice, keyboards, audio devices, AutoPlay.
- **Programs** – install/uninstall software, set default apps, enable/disable Windows features.
- **User Accounts** – manage account types, passwords, credentials.
- **Ease of Access** – accessibility tools (screen reader, voice recognition).
- **Clock and Region** – time zone, date/time format, region settings.
- **Appearance and Personalization** – desktop background, themes, fonts, taskbar, File Explorer options.

### Lab Answers — Control Panel Categories
| Question | Answer |
|---|---|
| View options | Category, Large icons, Small icons |
| Example categories | System and Security, Network and Internet, Hardware and Sound |
| Troubleshoot common problems | Security and Maintenance → Troubleshooting |
| Allow a program through firewall | Windows Defender Firewall |
| View network info / set up connections | Network and Sharing Center |
| Choose action for inserted media/device | AutoPlay |
| Add a printer | Devices and Printers |
| Set default program for a file type | Default Programs |
| Uninstall a program | Programs and Features |
| Install Windows Telnet client | Turn Windows features on or off |
| Change account type (admin → standard) | User Accounts → Change account type |
| Manage web/Windows credentials | Credential Manager |
| Customize the Taskbar | Taskbar and Navigation settings |
| Show hidden files/folders | File Explorer Options → View tab |
| Show known file type extensions | File Explorer Options → View tab |
| Change time zone | Date and Time → Change time zone |
| Change date format | Region → Additional settings |
| Sync time with internet server | Date and Time → Internet Time tab |
| Read screen text aloud | Ease of Access Center → Start Narrator |
| Improve voice/dictation accuracy | Speech Recognition settings |
