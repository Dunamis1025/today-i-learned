# PC Troubleshooting – Key Concepts Summary

> Based on 7 exam-style Q&A covering CompTIA A+ / IT Support fundamentals.

---

## Q1 – Burning Smell from a Computer

**Answer: Power Supply Unit (PSU)**

| Component | Why it's NOT the answer |
|-----------|------------------------|
| CPU | Generates heat but rarely burns unless cooling fails entirely |
| Hard Drive | Fails with noise or stops working; rarely burns |
| RAM | Overheating to the point of burning is very uncommon |

**Key Point:** The PSU converts AC power from the outlet to DC power for all components. An internal electrical fault or overload causes the PSU to burn, producing a distinctive electrical smell — making it the most common source.

---

## Q2 – When Does a Technician Research Online or in a Manual?

**Answer: "Test the Theory to Determine the Cause"**

### 6-Step Troubleshooting Process (CompTIA A+)

1. **Identify the problem** – Gather symptoms
2. **Test the theory to determine the cause** ← Research happens here
3. **Establish a plan of action** – Plan the fix
4. **Implement the solution** – Execute the fix
5. **Verify full system functionality** – Confirm it works
6. **Document findings, actions, and outcomes** – Record everything

**Key Point:** Research (internet/manual) is done during Step 2 to form and validate a theory about the root cause.

---

## Q3 – What to Back Up Before Troubleshooting a Customer's PC

**Answer: Two items must be backed up (choose two)**

- ✅ **Internet Explorer Favorites** – Personal bookmarks that cannot be recovered from media
- ✅ **Customer-created documents** – Personal files (photos, work files) that are irreplaceable

| Item | Back Up? | Reason |
|------|----------|--------|
| Hard disk driver files | ❌ | Can be reinstalled from manufacturer |
| BIOS system files | ❌ | Usually not modified; not user data |
| Windows OS files | ❌ | Can be reinstalled from original media |
| IE Favorites | ✅ | Personal and irreplaceable |
| Customer documents | ✅ | Personal and irreplaceable |

**Key Point:** Prioritize data that is **unique to the user** and cannot be reinstalled or downloaded again.

---

## Q4 – After Installing an Updated Video Driver, What's Next?

**Answer: Log (document) the previous and current driver version numbers**

**Scenario:** Employee reports distorted display → Technician downloads and installs latest GPU driver.

| Option | Why it's wrong |
|--------|----------------|
| Schedule next checkup | Not the immediate priority |
| Open video editing software to test | Unnecessary for basic verification |
| Move GPU to another slot | Only needed if software fix fails |

**Key Point:** After implementing a fix, the next step per troubleshooting methodology is **documentation** — recording what versions were changed and what actions were taken.

---

## Q5 – After Applying a Possible Solution, What Comes Next?

**Answer: Verify full system functionality and apply maintenance procedures**

### Post-Solution Flow

```
Apply Solution
      ↓
Verify Full System Functionality + Apply Preventive Measures
      ↓
Document Findings, Causes, and Outcomes
```

**Key Point:** Do **not** jump straight to documentation. First confirm the fix actually worked across the entire system, then document.

- "Test another solution" and "Find other causes" are only for when the fix **fails**.

---

## Q6 – After Renewing Antivirus License and Updating, What's Next?

**Answer: Run a full virus scan on the computer**

**Scenario:** Antivirus couldn't update due to expired license → Technician renews license and completes update.

| Option | Why it's wrong |
|--------|----------------|
| Download antivirus from another vendor | Issue is already resolved |
| Review Event Viewer for last update time | Redundant; update was just completed |
| Record new license number in the log | Important, but not the immediate priority |

**Key Point:** The system was **unprotected** during the period the license was expired. A full scan is required to ensure no threats were introduced during that vulnerability window.

---

## Q7 – PC Slows Down After Installing Video Editing Software + HDD LED Constantly Flashing

**Answer: Add more RAM**

**Root Cause Analysis:**

```
Insufficient RAM
      ↓
OS uses hard disk as "virtual memory" (paging/swap)
      ↓
HDD is constantly read/written → LED flashes non-stop
      ↓
System becomes very slow
```

| Option | Why it's wrong |
|--------|----------------|
| Replace HDD with faster model | Doesn't fix the root cause (lack of RAM) |
| Replace GPU with DVI output | Unrelated to performance; DVI is a display connector type |
| Upgrade to faster CPU | Doesn't address memory paging bottleneck |

**Key Point:** Constant HDD LED activity after installing memory-intensive software is a classic symptom of **RAM shortage causing excessive paging**. Adding RAM eliminates the need for virtual memory swapping.

---

## Quick Reference – CompTIA A+ Troubleshooting Steps

| Step | Action |
|------|--------|
| 1 | Identify the problem |
| 2 | Test the theory to determine the cause *(research here)* |
| 3 | Establish a plan of action |
| 4 | Implement the solution |
| 5 | Verify full system functionality + preventive measures |
| 6 | Document findings, actions, and outcomes |

---

## Key Vocabulary

| Term | Definition |
|------|------------|
| PSU (Power Supply Unit) | Converts wall outlet AC power to DC for PC components |
| Virtual Memory / Paging | Using HDD space as overflow RAM when physical RAM is full |
| Driver | Software that lets the OS communicate with hardware |
| HDD Activity LED | Indicator light that flashes when the hard drive is being accessed |
| Troubleshooting | Systematic process of diagnosing and resolving technical problems |
