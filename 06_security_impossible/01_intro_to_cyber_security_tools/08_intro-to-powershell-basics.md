# PowerShell Basics for Cybersecurity
> Security Impossible – Cyber Range Lab Notes  
> Duration: 30 min | Difficulty: Easy

---

## Overview

This lab introduces **Windows PowerShell** as a command-line and automation tool for cybersecurity operations. The goal is to build foundational skills for SOC analysts, incident responders, and security practitioners.

### Lab Scenario
You are a **junior SOC analyst** assigned to investigate and manage a Windows system using only PowerShell. You must prepare an investigation workspace, inspect files, monitor processes, review services, and perform basic triage tasks.

---

## Key Concepts

### PowerShell vs CMD
| Feature | CMD | PowerShell |
|--------|-----|------------|
| Released | 1987 | 2006 |
| Output type | Plain text | **Objects** |
| Scripting | Weak | Powerful |
| Security features | Minimal | Rich |

> PowerShell outputs **objects**, not plain text. This allows precise filtering, sorting, and automation — essential for large-scale security investigations.

### Why Run as Administrator?
- Required to access system files, services, and security settings
- Without it: `PermissionDenied` errors on protected paths
- SOC analysts need full system visibility during investigations

### Case Sensitivity
- PowerShell **commands** are case-insensitive (`get-process` = `Get-Process`)
- Windows file paths are also case-insensitive (`C:\users` = `C:\Users`)
- ⚠️ Linux **is** case-sensitive — important when analyzing cross-platform logs

---

## Commands Reference

### Task 1 – Understanding the PowerShell Interface

```powershell
Get-Location
```
- Displays the current working directory
- Equivalent to `pwd` in Linux
- **Why it matters:** Always confirm your location before running commands to avoid unintended actions

---

### Task 2 – File System Navigation

```powershell
Get-ChildItem          # List files and folders in current directory
Set-Location C:\Users\ # Change directory
Clear-Host             # Clear the screen
```

**Aliases (CMD-compatible shortcuts):**
| Alias | PowerShell Command |
|-------|--------------------|
| `ls` / `dir` | `Get-ChildItem` |
| `cd` | `Set-Location` |
| `cls` / `clear` | `Clear-Host` |

> **Cybersecurity Context:** Navigating directories is required when collecting logs, reviewing artifacts, or locating suspicious files during investigations.

---

### Task 3 – Investigation Workspace

```powershell
# Create investigation folder
New-Item -ItemType Directory -Name Investigation

# Move into it
Set-Location Investigation

# Create evidence files
New-Item suspect.txt
New-Item logs.txt
New-Item notes.txt

# Verify contents
Get-ChildItem

# Rename a file
Rename-Item suspect.txt suspect_user.txt
```

**Command breakdown:**
| Flag | Meaning |
|------|---------|
| `-ItemType Directory` | Specifies item type as a folder |
| `-Name Investigation` | Sets the folder name |

> **Cybersecurity Context:** SOC analysts organize evidence and logs systematically to maintain investigation integrity (chain of custody).

---

### Task 4 – Understanding PowerShell Objects

```powershell
Get-Process            # List all running processes
Get-Process | Get-Member  # Show all properties and methods of process objects
```

**Key properties exposed by `Get-Member`:**
| Property | Type | Security Relevance |
|----------|------|--------------------|
| `ProcessName` | string | Identify suspicious process names |
| `Id` | int | Unique process identifier (PID) |
| `CPU` | ScriptProperty | High CPU → possible cryptominer/malware |
| `Path` | ScriptProperty | Unexpected path → suspicious |
| `StartTime` | datetime | Unusual start time (e.g., 3AM) → suspicious |

> **Why this matters:** Objects allow powerful filtering, sorting, and automation — essential for large-scale security investigations.

---

### Task 5 – Monitoring Processes and Services

```powershell
Get-Process   # List all running processes
Get-Service   # List all services and their status
```

**Get-Service output columns:**
| Column | Meaning |
|--------|---------|
| `Running` | Service is active |
| `Stopped` | Service is inactive |
| Short name | Service identifier |
| Display name | Human-readable name |

**Security-critical services to watch:**
| Service | Expected State | If Changed → |
|---------|---------------|--------------|
| `WinDefend` | Running | Defender disabled = red flag |
| `wscsvc` | Running | Security Center off = red flag |
| `WinRM` | Stopped | If running unexpectedly = attacker may have enabled remote access |

> **Used to detect:** Suspicious processes, unauthorized services, malware persistence mechanisms.

---

### Task 6 – Suspicious Process Hunt

```powershell
# Get info on a specific process
Get-Process powershell

# Sort all processes by CPU usage (highest first)
Get-Process | Sort-Object CPU -Descending

# Show only top 5 CPU consumers
Get-Process | Sort-Object CPU -Descending | Select-Object -First 5
```

**Pipeline (`|`) explained:**
```
Get-Process                    → get all processes
  | Sort-Object CPU -Descending  → sort by CPU, highest first
  | Select-Object -First 5       → keep only top 5
```

> **SOC Use Case:** High CPU or memory usage may indicate **cryptominers**, malware, or abnormal behavior.

---

### Task 7 – PowerShell Pipeline and Filtering

```powershell
# Filter processes using CPU > 100 seconds
Get-Process | Where-Object { $_.CPU -gt 100 }
```

**Key operators:**
| Operator | Meaning |
|----------|---------|
| `-gt` | Greater than |
| `-lt` | Less than |
| `-eq` | Equal to |
| `-ne` | Not equal to |
| `$_` | Current object in the pipeline |

> **Cybersecurity Context:** Filtering helps analysts quickly isolate suspicious activity from large datasets.

---

### Task 8 – Finding Large Files

```powershell
Set-Location C:\Windows
Get-ChildItem -Recurse | Where-Object { $_.Length -gt 50MB }
```

**Flag breakdown:**
| Flag | Meaning |
|------|---------|
| `-Recurse` | Search all subdirectories recursively |
| `$_.Length` | File size in bytes |
| `-gt 50MB` | Filter files larger than 50MB |

> **Cybersecurity Context:** Attackers may hide large malicious payloads in unexpected directories. Unusually large or strangely-named files (e.g., hash-like filenames) are red flags.

---

### Task 9 – Accessing PowerShell Help

```powershell
Get-Help Get-Process             # Basic help
Get-Help Get-Process -Examples   # Practical usage examples
Get-Help Get-Process -Detailed   # Detailed parameter info
Get-Help Get-Process -Full       # Complete technical reference
```

> **Cybersecurity Context:** Analysts must quickly learn unfamiliar commands during live investigations — `Get-Help` enables self-sufficient learning without internet access.

---

### Task 10 – Execution Policy and Security

```powershell
Get-ExecutionPolicy
```

**Policy levels:**
| Policy | Meaning | Risk |
|--------|---------|------|
| `Restricted` | No scripts allowed | Safest |
| `AllSigned` | Only signed scripts | Secure |
| `RemoteSigned` | Downloaded scripts need signature | Moderate |
| `Unrestricted` | All scripts allowed | ⚠️ Most dangerous |

**Result in this lab:** `Unrestricted` — all scripts run without restriction.

> ⚠️ **Security Importance:**
> - Attackers abuse PowerShell for **living-off-the-land (LotL)** attacks — using built-in tools to avoid detection
> - Defenders monitor PowerShell **logs** and **execution policies** to detect abuse
> - `Unrestricted` means a malicious script could run without any warning

---

## Pipeline Cheat Sheet

```powershell
# Find processes using more than 100 CPU seconds
Get-Process | Where-Object { $_.CPU -gt 100 }

# Top 5 memory-hungry processes
Get-Process | Sort-Object WS -Descending | Select-Object -First 5

# Find all running services
Get-Service | Where-Object { $_.Status -eq "Running" }

# Find large files recursively
Get-ChildItem -Recurse | Where-Object { $_.Length -gt 50MB }
```

---

## Summary: What You Learned

| Skill | Command(s) |
|-------|------------|
| Check current location | `Get-Location` |
| List files/folders | `Get-ChildItem` |
| Navigate directories | `Set-Location` |
| Create files/folders | `New-Item` |
| Rename files | `Rename-Item` |
| View running processes | `Get-Process` |
| View services | `Get-Service` |
| Filter data | `Where-Object { $_.Property -gt value }` |
| Sort data | `Sort-Object PropertyName -Descending` |
| Select top N results | `Select-Object -First N` |
| Explore object properties | `Get-Member` |
| Read built-in help | `Get-Help CommandName -Examples` |
| Check execution policy | `Get-ExecutionPolicy` |

---

## Key Takeaways

1. **PowerShell works with objects**, not plain text — enabling precise, programmatic filtering
2. **Always run as Administrator** for full system visibility during investigations
3. **The pipeline (`|`)** is the most powerful feature — chain commands to build complex queries
4. **`Where-Object` + `Sort-Object`** = your primary tools for isolating suspicious activity
5. **High CPU, unusual paths, strange file names** = red flags in security investigations
6. **Execution policy `Unrestricted`** = serious security risk; monitor this in production environments
7. **`Get-Help`** = your best friend when learning new cmdlets on the fly

---

*Security Impossible – Cyber Range Documentation | Lab 10 | v1.0*
