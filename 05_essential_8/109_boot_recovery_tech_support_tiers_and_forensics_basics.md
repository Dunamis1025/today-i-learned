# IT Support & Security — Study Notes

*Topics covered: boot recovery, technical support tiers, digital forensics, PII, and security best practices.*

---

## 1. BOOTMGR Missing Error

**Symptom:** `BOOTMGR is missing` appears after POST (Power-On Self-Test) — the system can't find the Windows Boot Manager, the file responsible for starting Windows.

**Correct fixes:**
- **Restore BOOTMGR via Windows Recovery Environment (WinRE)** — built-in recovery tools automatically detect and replace missing/corrupted boot files. This is the primary, go-to fix.
- **Run `bootrec /fixboot`** — executed from Command Prompt within WinRE; rewrites the boot sector (the disk area that tells the computer how to load the OS).

**Why not other options?** Disk checks / virus scans address different problems (disk errors, malware) — they don't fix a broken/missing boot file.

---

## 2. Level One vs. Level Two Technicians

| | Level 1 | Level 2 |
|---|---|---|
| Role | First point of contact; basic troubleshooting, intake, documentation | Deeper technical expertise; complex/urgent issue resolution |
| Handles "down calls" (system completely non-functional) | No — escalates | **Yes** — faster resolution due to expertise |
| Typical tasks | Answer calls, gather basic info, create tickets | Gather diagnostic data (logs, tools), remotely update drivers/software, apply direct technical fixes |

**Key idea:** Level 1 = gatekeeper/intake. Level 2 = specialist who diagnoses and repairs what Level 1 can't.

---

## 3. Escalation & Customer Communication

**Scenario:** A Level 1 tech (e.g., Chad) gets a frustrated customer with an issue he can't solve.

**Correct actions:**
1. **Escalate to Level 2** — hand off to someone with the right expertise.
2. **Document the reason for the call + create a support ticket** — ensures continuity so Level 2 can pick up immediately without re-asking everything.

**Separate scenario — customer can't follow verbal instructions:**
- Best action: **offer an alternative format**, e.g., emailed step-by-step instructions with illustrations.
- Rationale: people process information differently; switching format (not just repeating) is the professional fix.

---

## 4. Chain of Custody (Digital Forensics)

**Definition:** A chronological record of who handled a piece of evidence, when, where it was stored, and what was done to it — from discovery until it's presented in court.

**Requirement to prove chain of custody:** **Proper documentation procedures.**

**Why it matters:** Complete, unbroken documentation proves evidence wasn't tampered with, altered, or contaminated — preserving:
- **Integrity** (evidence is trustworthy)
- **Admissibility** (the evidence can legally be accepted/used in court)

Without solid documentation, even strong evidence can be ruled **inadmissible**.

---

## 5. Personally Identifiable Information (PII)

**Best definition:** Data collected by businesses to distinguish the identities of individuals.

**Examples:** full name, national ID / SSN, email address, phone number.

**Distinction:** Unlike generic/anonymous tracking data (e.g., website behavior analytics), PII can directly identify a specific person — which is why it's treated as high-priority from a security standpoint.

---

## 6. Credentials & UAC — Security Best Practice

**Scenario:** IT technician modifying system files on a laptop triggers a **UAC (User Account Control)** prompt requiring a password.

**Correct action:** Call the employee and have them **come to the IT department in person** to enter their own credentials.

**Why:**
- A technician should **never** ask for or receive a user's password over the phone or email — this resembles a phishing/social engineering red flag.
- Passwords are private; only the account owner should enter them.
- Having the employee enter it in person preserves password integrity and complies with standard security policy.

---

## Key Vocabulary

| Term | Meaning |
|---|---|
| **Admissibility** | Whether evidence is legally acceptable for use in court |
| **Credentials** | Login information (username, password, certificates) used to prove identity/access |
| **Chain of Custody** | Documented history of evidence handling from collection to court |
| **PII** | Personally Identifiable Information — data that identifies a specific individual |
| **UAC** | User Account Control — Windows security prompt requiring authorization for system-level changes |
| **Escalation** | Passing an issue from a lower support tier to a higher, more specialized one |
