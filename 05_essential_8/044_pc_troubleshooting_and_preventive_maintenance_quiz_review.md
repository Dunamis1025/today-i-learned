# PC Troubleshooting & Preventive Maintenance — Study Guide (Q8–Q25)

> A concise reference covering core concepts from CompTIA A+ / IT fundamentals exam questions.

---

## Table of Contents

1. [Preventive Maintenance](#preventive-maintenance)
2. [Troubleshooting Process (6-Step Model)](#troubleshooting-process-6-step-model)
3. [Hardware Diagnostics](#hardware-diagnostics)
4. [Customer & Technician Best Practices](#customer--technician-best-practices)
5. [Documentation](#documentation)
6. [Quick Reference Cheat Sheet](#quick-reference-cheat-sheet)

---

## Preventive Maintenance

### Q8 — Primary Benefit of Preventive Maintenance
**✅ Correct: Extends the life of components**

Regular maintenance (removing dust, ensuring proper cooling, keeping firmware updated) prevents hardware damage and keeps parts functioning longer.

| Option | Why It's Wrong |
|---|---|
| Assists software development | Unrelated to hardware maintenance |
| Enhances troubleshooting processes | PM prevents problems; it doesn't improve post-failure repair |
| Simplifies PC use | Maintenance doesn't change how the OS or software works |

---

### Q9 — Preventive Maintenance at a Construction Site
**✅ Correct: Remove dust from intake fans**

Construction sites are extremely dusty. Dust-clogged fans reduce airflow, causing overheating and hardware failure. Cleaning intake fans is the most critical PM task in this environment.

| Option | Why It's Wrong |
|---|---|
| Reformat and reinstall | Too drastic; this is a repair procedure, not routine PM |
| Audit all installed software | Software audits don't protect hardware from dust |
| Install forensic tracking software | Security task, unrelated to physical hardware PM |

---

### Q16 — Three Benefits of Computer Preventive Maintenance *(choose 3)*
**✅ Correct answers:**
- **Extension of the life of components** — Cleaning and upkeep prevents premature wear
- **Improvement in data protection** — Routine backups and checks keep data safer
- **Reduction in the number of equipment failures** — Catching issues early prevents full breakdowns

**❌ Incorrect options:**
- *Elimination of the need for repairs* — PM reduces failures but doesn't eliminate all repairs
- *Time savings for technicians* — Not a primary benefit
- *Improvement in RAM access time* — Hardware speed is not improved by cleaning or maintenance

---

## Troubleshooting Process (6-Step Model)

### The Standard 6 Steps (Memorize This!)

```
Step 1 → Identify the Problem
Step 2 → Establish a Theory of Probable Cause
Step 3 → Test the Theory
Step 4 → Establish a Plan of Action & Implement the Solution
Step 5 → Verify Full System Functionality (+ Preventive Measures if applicable)
Step 6 → Document Findings, Actions, and Outcomes
```

---

### Q14 — Which Step Is Being Used? *(helpdesk checking power cables)*
**✅ Correct: Implement a Solution (Step 4)**

The technician is actively guiding the user to check power cables and lights — this is implementing a solution, not just identifying or planning.

| Option | Why It's Wrong |
|---|---|
| Verify system functionality | This comes after the fix, not during |
| Establish a theory | That would be guessing causes, not acting |
| Establish a plan of action | Planning comes before acting |
| Identify the problem | Already done — the problem (won't turn on) is known |

---

### Q15 — What Is the Next Step After Verifying with the Customer?
**✅ Correct: Document the findings, actions, and outcomes (Step 6)**

After verifying the fix works and the customer confirms resolution, the final step is always documentation.

---

### Q20 — What Comes After Applying a Manufacturer-Recommended Solution?
**✅ Correct: Verify the solution and confirm full system functionality (Step 5)**

Applying a solution doesn't mean the job is done. You must confirm everything works before closing out.

---

### Q23 — During Which Step Does the Technician Demonstrate the Fix to the Customer?
**✅ Correct: Verify Full System Functionality (Step 5)**

During verification, the technician shows the customer that the problem is resolved and the system works as expected.

---

## Hardware Diagnostics

### Q11 — PC Won't Boot, RAM Was Reseated and Now Works
**✅ Correct: RAM modules were not seated firmly**

RAM that isn't fully inserted into its slot causes a poor connection and prevents booting. Removing and reinserting ensures a proper connection — no hardware replacement needed.

| Option | Why It's Wrong |
|---|---|
| Doesn't match PC specs | Incompatible RAM wouldn't work in the second PC either |
| Has bad blocks (bad memory) | Faulty RAM would have failed in the second PC too |
| Inserted backwards | RAM is keyed; it can't physically go in backwards |

---

### Q12 — Best Way to Check if a CPU Fan Is Spinning
**✅ Correct: Visually inspect the fan while the power is ON**

Watching the fan spin in real-time is the safest and most accurate method.

| Option | Why It's Wrong |
|---|---|
| Spin blades with a finger | Can damage the motor or bearings |
| Listen for sound | Sound alone can't confirm adequate speed |
| Use compressed air to spin it | Can over-rev the motor and cause damage |

---

### Q13 — Hard Drive LED Not Working, PC Functions Normally
**✅ Correct: The hard drive LED cable has come loose from the motherboard**

Since the PC works fine, the issue is isolated to the front-panel indicator light. A disconnected header cable is the most probable cause.

| Option | Why It's Wrong |
|---|---|
| Data cable malfunction | Would cause errors, corruption, or boot failure |
| BIOS needs update | BIOS issues affect boot/hardware, not a single LED |
| PSU not providing enough voltage | Would cause shutdowns or instability, not just one dead LED |

---

### Q18 — PC Takes a Long Time to Boot; BIOS Re-Detects Hardware Every Time
**✅ Correct: Replace the CMOS battery**

The CMOS battery (a small coin cell on the motherboard) powers the chip that stores BIOS settings. After ~4 years, it discharges and the BIOS "forgets" hardware info, forcing a full detection scan on every boot. A new battery fixes this.

| Option | Why It's Wrong |
|---|---|
| Start with last known good config | OS-level fix; doesn't address BIOS memory loss |
| Launch Device Manager | OS-level; can't stop the BIOS POST hardware scan |
| Reset BIOS via CMOS jumper | Would erase settings, making the problem worse |

---

### Q25 — Workstation Freezes After 5 Minutes of Use Every Time
**✅ Correct: CPU is overheating**

A consistent freeze after a fixed period of use is a classic sign of thermal throttling or thermal shutdown. As the CPU runs, heat accumulates and triggers a protective lockup around the 5-minute mark.

| Option | Why It's Wrong |
|---|---|
| Hard disk failing | Disk issues cause slow speeds or read errors, not timed freezes |
| RAM malfunctioning | RAM errors usually produce immediate BSODs or crashes |
| PSU failing | Would cause sudden shutdowns or reboots, not consistent freezes |

---

## Customer & Technician Best Practices

### Q10 — Purpose of Documenting Customer Info in a Work Order
**✅ Correct: To use the information to aid in solving the problem**

Customer-reported symptoms help technicians understand and diagnose issues faster and more accurately.

---

### Q19 — Problem Beyond Technician's Knowledge Level
**✅ Correct: Gather as much information as possible and escalate the problem**

Escalation is the professional response. Collect all details, then pass the ticket to a higher-level technician or specialist.

| Option | Why It's Wrong |
|---|---|
| Try to fix it anyway | Could make the problem worse |
| Ask customer to call back later | Poor customer service |
| Tell customer to call the manufacturer | Deflects responsibility unprofessionally |

---

### Q21 — First Thing to Do Before Troubleshooting a Customer's Computer
**✅ Correct: Perform a data backup**

Before any repair work, always back up the customer's data. Any work could accidentally cause data loss.

---

### Q22 — Liability Release Form (When Backup Is Not Possible)
If a backup cannot be made, the liability release form must include **all three** of the following:

1. **Permission** to work on the computer without a current backup
2. **Release from liability** if data is lost or corrupted
3. **Description of the work** to be performed

---

### Q24 — Where to Find Error Logs for System/User/Software Issues
**✅ Correct: Event Viewer**

Windows Event Viewer logs all errors, warnings, and informational events generated by the system, users, and applications. It's the primary diagnostic tool for tracking down the cause of software or OS problems.

| Option | Why It's Wrong |
|---|---|
| Device Manager | Shows hardware status only |
| BIOS | Contains hardware config; not an error log |
| Vendor diagnostic tools | Proprietary tools for specific hardware tests |

---

## Documentation

### Q17 — What Should Be Documented After Fixing a Problem?
**✅ Correct: Everything that was done to try to solve the problem**

A complete record includes:
- The problem description
- All attempted solutions (including failed ones)
- The successful resolution

This provides a full history for future reference and helps other technicians facing the same issue.

---

## Quick Reference Cheat Sheet

### 6-Step Troubleshooting Model
| Step | Action |
|---|---|
| 1 | **Identify the problem** |
| 2 | **Establish a theory of probable cause** |
| 3 | **Test the theory** |
| 4 | **Establish a plan & implement the solution** |
| 5 | **Verify full system functionality** *(show customer the fix works)* |
| 6 | **Document findings, actions, and outcomes** |

### Key Rules to Remember
| Rule | Detail |
|---|---|
| Before any repair | Always **back up data** first |
| Can't back up? | Get a signed **liability release form** |
| Problem out of your depth? | **Escalate** with full details |
| CPU freeze after ~5 min | Think **overheating** |
| PC won't boot, RAM works elsewhere | **Reseat the RAM** |
| BIOS forgets settings (old PC) | Replace the **CMOS battery** |
| LED not working, PC runs fine | Check the **front-panel header cable** |
| Never spin a fan manually | Could **damage the motor** |
| Best fan check method | **Visual inspection** while powered on |
| Error logs location (Windows) | **Event Viewer** |
| Document how much? | **Everything** — failures and successes |
