# IT Technician & Call Center Fundamentals — Study Notes

## 1. Call Centers

- A call center is a highly organized, professional environment where technicians provide computer-related support to customers.
- Technicians are **tiered**:
  - **Level 1**: First point of contact. Gathers customer information and attempts to resolve the issue.
  - **Level 2**: Subject matter expert. Handles issues escalated by Level 1, often using remote access tools for advanced fixes (driver updates, BIOS checks, configuration changes).
- All support must comply with the **Service Level Agreement (SLA)** — a contract defining expected response/resolution times.
- Many call centers operate 24/7.

### Support Software Functions
- Log and track incidents
- Record contact information
- Research product information
- Run diagnostic utilities
- Search a knowledge base
- Collect customer feedback

### Call Prioritization
| Priority | Level | Description |
|---|---|---|
| 1 | Down (most urgent) | Company cannot operate any computer equipment |
| 2 | Hardware/Software/Network (urgent) | A specific computer is malfunctioning or can't access the network |
| 3 | Enhancement (important) | Request for additional functionality |

### Level 1 Responsibilities
- Gather all pertinent information from the customer.
- Record it in a structured ticket/work order (contact info, computer make/model, OS, connection status, software, problem description, priority).
- Resolve simple issues directly; otherwise escalate with clear documentation so Level 2 doesn't need to re-ask the customer.

---

## 2. Remote Technician Labs (Practice Scenarios)

### Lab A — Hardware Problem
- **Scenario**: Customer opened the computer case out of curiosity, reassembled it, and now the PC won't boot — it just beeps continuously.
- **Likely cause**: Loose internal component (RAM, GPU) due to improper reassembly.
- **Tasks**: Document the problem, diagnose using beep codes, write a customer-friendly explanation, and cite any reference resources used.

### Lab B — Operating System Problem
- **Scenario**: Customer can't access email, internet, or files; a restart didn't help. The system detected "new hardware" at boot but failed to install it.
- **Likely cause**: Missing/corrupted network adapter driver.
- **Tasks**: Document the issue, propose reinstalling/updating the driver, write a client script, list resources used.

### Lab C — Network Problem (Intermittent Connectivity)
- **Scenario**: Network connection drops only on busy days when all computers are in use; the affected computer isn't always the same one. A new computer was recently added to the network.
- **Likely cause**: DHCP IP address pool exhaustion (not enough IPs to assign when demand is high).
- **Tasks**: Document the pattern, propose expanding the DHCP scope or reviewing IP allocation, explain to the customer in simple terms.

### Lab D — Security Problem
- **Scenario**: A laptop connects to Wi-Fi everywhere except the office. Ethernet works fine, other employees connect fine, and a new wireless router was installed yesterday.
- **Likely cause**: Cached wireless profile/security settings conflict with the new router configuration.
- **Tasks**: Document the issue, propose clearing the saved Wi-Fi profile and reconnecting/re-authenticating, write a customer explanation.

---

## 3. Scripting for Automation

### What Is a Script?
A simple text file containing commands executed line-by-line to automate repetitive tasks (diagnostics, backups, etc.). Saves significant time compared to manual execution.

### Scripting vs. Compiled Languages
- **Scripting languages** (PowerShell `.ps1`, Python `.py`, JavaScript `.js`) are **interpreted** line-by-line at runtime — easier and more flexible.
- **Compiled languages** (C, Java) are translated into machine code beforehand.

### Basic OS Commands (used inside scripts too)
| Task | Windows | Linux |
|---|---|---|
| List directory | `dir` | `ls` |
| Change directory | `cd` | `cd` |
| Make directory | `mkdir` | `mkdir` |
| Clear screen | `cls` | `clear` |
| Show/set date | `date` | `date` |
| Copy file | `copy` | `cp` |

### Variables & Environment Variables
- **Variable**: A named storage location for data.
- **Environment variable**: A special OS-level variable storing system info (username, home directory, language, etc.).
- **Common data types**:
  - `int` — integer
  - `float` — decimal number
  - `char` — single character
  - `string` — sequence of characters
  - `bool` — true/false

### Conditional Statements
- Let a script make decisions: "if X, do A; else do B."
- Use **relational operators**: equal, not equal, greater than, less than.
- Example: check the time → output "morning" or "afternoon."
- **Case statements** can group multiple conditions into categories.

### Loops
- Used to repeat the same task multiple times.
- **For loop**: repeats a set number of times.
- **While loop**: checks the condition *before* running (pre-test).
- **Do-While loop**: runs the code first, *then* checks the condition (post-test).

---

## 4. Hands-On Scripting Lab: Windows & Linux

Goal: Write scripts in three environments to display system info (computer name, OS version, CPU, memory, disk space, IP address).

### Part 1 — Windows Batch Script (`info.bat`)
Key commands:
- `echo` — print text to screen
- `ver` — show Windows version
- `wmic` — query system information (memory, disks, etc.)
- `netsh` — view/modify network configuration
- `findstr` — search for text strings in output

### Part 2 — PowerShell Script (`info.ps1`)
- Run in **PowerShell ISE** (as administrator).
- Must set execution policy (`Set-ExecutionPolicy RemoteSigned`) to allow scripts to run.
- More powerful than batch — treats system data as **objects**, enabling more precise control.
- Uses cmdlets like `Get-WmiObject`, `Get-NetIPAddress`, `Write-Output`.

### Part 3 — Linux Bash Script (`info.sh`)
- Written using a text editor (`vi`, `vim`, `nano`, `pico`, or GUI-based `gedit`).
- Key `vi` commands: `i` (insert), `a` (append), `o` (new line below), `Esc` (exit insert mode), `:w` (save), `:wq` (save & quit), `:q!` (quit without saving).
- Script starts with `#!/bin/bash` (the **shebang**) — tells the OS to run the file using the Bash interpreter.
- Must be made executable: `chmod 755 info.sh`, then run with `./info.sh`.
- Uses commands like `cat`, `grep`, `lscpu`, `df -h`, `hostname -I`.

---

## 5. Ethics, Law & Evidence Handling

- **Professionalism**: Maintain a professional demeanor with customers and colleagues at all times; follow SLA and company policy.
- **Ethical/Legal responsibilities**: Understand software licensing and applicable cyber laws when handling customer systems and data.
- **Data protection**: Sensitive data (e.g., credit card info) requires **stringent** (very strict) protection, and handling is regulated by laws like the **GDPR**, depending on data type and **jurisdiction** (the legal region whose laws apply).
- **Illegal computer/network use** can include: identity theft, sale of **counterfeit** (fake/fraudulent) goods, use of pirated software, unauthorized copying of copyrighted material, and pornography.
- **Email conduct**: Never send **unsolicited** (unrequested), **forged** (sender identity faked), or anonymous emails.
- **Evidence collection ("first response")**: Follow specific IT laws so that collected data is **admissible** (legally acceptable) as evidence in court.
- **Chain of Custody**: A documented, chronological record of who collected, stored, and had access to evidence from collection until court proceedings — proving it wasn't tampered with. A system administrator must be able to **testify** (give sworn statements) about how the evidence was gathered, stored, and accessed.

---

## Chapter Summary

1. **Professionalism & Communication** — maintain trust through professional conduct, SLA compliance, and effective handling of difficult customers.
2. **Ethics & Law** — understand licensing, cyber law, evidence-gathering procedures, and chain of custody.
3. **Scripting/Automation** — use variables, conditionals, and loops to automate repetitive administrative tasks in both Windows and Linux environments.
