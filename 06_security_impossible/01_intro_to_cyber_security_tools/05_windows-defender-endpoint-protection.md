# Windows Security (Windows Defender) — Lab Study Notes

> **Module**: Endpoint Protection with Windows Defender  
> **Duration**: ~30 minutes  
> **Date**: June 3, 2026  
> **Type**: Walkthrough + Hands-on Virtual Machine Lab

---

## 1. Overview

Windows Security is **not just an antivirus** — it is a comprehensive, built-in endpoint security solution that protects your system across multiple layers: accounts, network, hardware, and file threats.

Think of it as a **24/7 security operations center** running natively on every Windows machine.

---

## 2. Windows Security Sections

| Section | Role |
|---|---|
| **Virus & Threat Protection** | Scans for malware; manages detected threats |
| **Account Protection** | Secures login credentials; manages Windows Hello (PIN, biometrics) |
| **Firewall & Network Protection** | Controls inbound/outbound traffic; blocks unauthorized connections |
| **Device Security** | Hardware-level protection; **Memory Integrity** prevents kernel-level attacks |
| **Device Performance & Health** | Monitors storage, battery, and Windows Update status |
| **Family Options** | Parental controls; screen time and content filtering |

### Key Concepts

- **Memory Integrity**: Uses virtualization to prevent malicious code from accessing protected kernel memory — one of the strongest defenses against kernel-level attacks.
- **Biometrics (Windows Hello)**: Replaces passwords with fingerprint or facial recognition for more secure and convenient authentication.
- **Firewall**: Acts as a checkpoint — allows legitimate traffic and blocks unauthorized external access.

---

## 3. Core Concepts

### Endpoint Protection
Windows Defender protects the **endpoint** (your local machine) as the first and last line of defense. It works even before threats reach the network layer.

### Layered Security
Security is not a single tool — it is a **suite** of protections working together:
- Identity layer → Account Protection
- Network layer → Firewall
- Hardware layer → Device Security (Memory Integrity)
- File/Malware layer → Virus & Threat Protection

---

## 4. Hands-On Lab: Detecting and Removing a Test Threat

### What is EICAR?
The **EICAR test file** (`important.txt`) is a globally recognized, **safe fake virus** used by security professionals to verify that antivirus software is functioning correctly. It contains no real malicious code.

---

### Step 1 — Open Windows Security
1. Press the **Windows key** and search for `Windows Security`
2. Open the app and familiarize yourself with the dashboard sections

---

### Step 2 — Run a Custom Scan via PowerShell

**Why a custom scan?**  
In real SOC (Security Operations Center) work, analysts isolate and scan **specific suspicious files** rather than running full system scans — it's faster and more targeted.

**Open PowerShell as Administrator:**
1. Press Windows key → search `PowerShell`
2. Right-click → **Run as administrator** → Yes

**Execute the scan command:**
```powershell
Start-MpScan -ScanType CustomScan -ScanPath "C:\Users\user010\Desktop\Lab-Files\important.txt"
```

**Command breakdown:**

| Parameter | Meaning |
|---|---|
| `Start-MpScan` | Initiates Microsoft Defender Antivirus scan |
| `-ScanType CustomScan` | Scan only a specified target (not the full system) |
| `-ScanPath "..."` | Path to the specific file or directory to scan |

> **Note**: In a browser-based VM (e.g., Guacamole), clipboard paste may not work directly into PowerShell. Use **right-click** inside the PowerShell window to paste, or type the command manually.

---

### Step 3 — Verify Detection

After pressing Enter:
- A **"Threats found"** notification appears in the bottom-right corner
- Windows Defender **automatically quarantines** the file — no manual action needed at this stage
- Navigate back to **Windows Security → Virus & Threat Protection** to see the warning indicator (⚠️)

---

### Step 4 — Review Protection History

Go to: `Windows Security → Virus & Threat Protection → Protection History`

You will see a log entry similar to:

| Field | Value |
|---|---|
| **Event** | Threat quarantined |
| **Severity** | Severe |
| **Status** | Quarantined |
| **Affected Item** | `C:\Users\user010\Desktop\Lab-Files\important.txt` |
| **Threat Name** | `Virus:DOS/EICAR_Test_File` |

**Expand the entry** to see available actions:

| Action | When to use |
|---|---|
| **Remove** | Confirmed threat → permanently delete from system |
| **Restore** | False positive → move file back to original location |

---

### Step 5 — Remove the Threat

Click **Remove** → the status updates to **"Threat removed"**

Lab complete. ✅

---

## 5. Incident Response Workflow (Standard Procedure)

This lab mirrors the real-world **Detect → Block → Verify** cycle used by security analysts:

```
1. DETECTION     → Antivirus identifies a suspicious file
2. QUARANTINE    → System isolates the file; prevents execution
3. ANALYSIS      → Analyst reviews Protection History logs
4. DECISION      → Remove (confirmed threat) or Restore (false positive)
5. REPORTING     → Log is preserved for future investigation/audit
```

> **Key principle**: Security analysts do not blindly delete files. They **review evidence**, understand the threat type, and make informed decisions before taking action.

---

## 6. Vocabulary Reference

| Term | Definition |
|---|---|
| **Endpoint** | A user device (laptop, desktop, VM) that connects to a network |
| **Quarantine** | Isolating a threat in a restricted area where it cannot execute |
| **False Positive** | A safe file incorrectly flagged as malicious |
| **Kernel-level attack** | Malware that targets the OS core, bypassing most standard defenses |
| **Biometrics** | Authentication using physical traits (fingerprint, face, iris) |
| **Comprehensive suite** | An all-in-one package of security tools working together |
| **Mitigate** | To reduce the severity or impact of a threat |
| **Vital** | Critical or essential (e.g., vital role, vital organs) |
| **Fraudulent** | Deceptive or dishonest (e.g., fraudulent transaction) |
| **Instrument cluster** | The dashboard panel displaying system metrics (speed, fuel, etc.) |
| **Relevance** | The degree to which something is related or applicable |
| **EICAR** | A safe, standardized test file used to verify antivirus functionality |
| **SOC** | Security Operations Center — a team that monitors and responds to threats |

---

## 7. Key Takeaways

- Windows Defender is a **multi-layered, built-in endpoint security solution**, not just a virus scanner.
- **Custom scans** are a core skill for security analysts handling incident investigations.
- The **Protection History** log is the primary tool for reviewing and acting on detected threats.
- The standard incident response flow is: **Detect → Quarantine → Analyze → Remove/Restore**.
- Knowing the difference between **Remove** and **Restore** is fundamental to avoiding accidental data loss.
