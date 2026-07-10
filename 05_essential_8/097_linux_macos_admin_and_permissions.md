# OS Fundamentals — Study Notes (Linux & macOS)

## 1. Customization & Recovery

- Linux and macOS both let users freely install and remove system components to fit their needs.
- macOS specifically ships with a built-in **Disk Utility** for backups and image-based recovery.

## 2. Scheduled Tasks

- Systems need regular maintenance (backups, disk checks, etc.), and doing this manually is impractical.
- **cron** is the service responsible for running maintenance jobs automatically at set times.
- **crontab** is the configuration file that defines *what* job runs and *when*.

## 3. OS Updates & Security Management

| Area | Summary |
|---|---|
| **OS Updates** | Keep the system current to patch vulnerabilities and improve performance. Usually automatic, but can be checked manually. |
| **Firmware Updates** | Firmware is the lowest-level software running hardware; update it per manufacturer guidance. |
| **Antivirus / Malware Defense** | Antivirus software keeps a database of malware **signatures** (unique fingerprints). Files are scanned and flagged if they match a known signature. Since new malware appears constantly, the signature database must be updated frequently. |
| **Security Credential Management** | Securely stores usernames, passwords, and encryption keys. Ubuntu Linux provides the **Passwords and Keys** manager (GNOME Keyring) for this purpose. |

## 4. Term Matching (Core Vocabulary)

| Term | Meaning |
|---|---|
| **Patch** | Periodic update from an OS vendor that fixes known security vulnerabilities. |
| **Keychain** | macOS's built-in security credential manager. |
| **Signature** | A unique code fragment identifying a specific virus/malware, used by antivirus tools for detection. |
| **Cron** | Service on Linux/macOS that automates and schedules recurring maintenance tasks. |
| **Gnome-keyring** | Security credential manager used on Ubuntu/Linux (GNOME environment). |
| **Firmware** | The most fundamental software layer required for hardware to function. |

## 5. Basic Linux Commands (Directory & File Operations)

| Command | Function |
|---|---|
| `mkdir` | Creates a new directory (folder). |
| `cp` | Copies a file to a specified location. |
| `cd` | Changes the current working directory. |
| `ls` | Lists files and folders in the current directory. |

## 6. Reading `ls -l` Output

Running `ls -l` shows a detailed listing of files/directories. Each column means:

1. **Permissions** — who can access the item (read/write/execute). A leading `d` marks a directory.
2. **Link count** — number of hard links to the item, or number of sub-items inside a directory.
3. **User (owner)** — the account that owns the file/directory.
4. **Group** — the group that holds permissions over the file/directory.
5. **File size** — size in bytes.
6. **Date & time** — timestamp of the last modification.
7. **File name** — the name of the file or directory.

## 7. File Permissions (Unix-based Systems)

Unix-based systems (Linux, macOS) control access to files/directories via **permissions**, assigned separately to three categories of users:

- **User (owner)** — the creator/owner of the file
- **Group** — other users sharing the same group
- **Other** — everyone else

### Permission types
- **r (Read)** — permission to view/read the file
- **w (Write)** — permission to modify/write to the file
- **x (Execute)** — permission to run the file

### Octal (numeric) notation
Permissions can be compressed into a single digit (0–7), the sum of read (4) + write (2) + execute (1):

| Octal | Meaning |
|---|---|
| **7** (`rwx`) | Read, write, and execute |
| **6** (`rw-`) | Read and write |
| **5** (`r-x`) | Read and execute |
| **4** (`r--`) | Read only |
| **0** (`---`) | No access |

### Root user
The **root** account is the system administrator with unrestricted access — it can bypass normal permission settings entirely, which is necessary for system administration and maintenance.
