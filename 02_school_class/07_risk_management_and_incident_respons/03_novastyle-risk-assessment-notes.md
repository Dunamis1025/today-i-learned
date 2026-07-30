# NovaStyle Risk Assessment — Report Structure Notes

Study notes explaining *why* each section of the NovaStyle e-commerce risk
assessment (Part A) is structured the way it is, and how the sections feed
into one another.

## Overview: How the sections connect

```
Sections 2–3   Who is involved, what needs protecting, who can access what
     ↓
Section 4      Turn that into concrete incident scenarios (Bow-Tie Diagrams)
     ↓
Sections 5–6   Score and rank those scenarios (Risk Matrix, Risk Register)
     ↓
Sections 7–8   Group risks into categories, confirm ratings
     ↓
Section 9      Controls to prevent incidents + vendor tools
     ↓
Section 10     Recovery plan for when prevention fails anyway
```

The report is essentially two halves: **Section 9 is "stop it from
happening"**, and **Section 10 is "survive it if it happens anyway."** The
final step of Section 10 (Post-Incident Review) loops back and updates the
Risk Register and Controls — so the whole thing is a cycle, not a one-time
exercise.

---

## 2. Actor List & Information Asset List

Before assessing risk, you need to define **who is involved (Actors)** and
**what needs protecting (Assets)**. Without this baseline, you can't
meaningfully ask "who could threaten what."

### 2.1 Actor List

| Category | Actors | Why they matter |
|---|---|---|
| Internal Staff | Order processing, customer support, IT admin, warehouse staff | Log directly into company systems; risk = credential misuse |
| External Partners | Payment gateway, cloud hosting provider, courier, software vendors | Not employees, but connected to systems; risk = *their* security failure becomes *our* problem |
| Customers | Online shoppers entering payment/personal info | Risk = becoming victims if their data leaks |
| Other Physical Actors | Visitors, couriers entering the office/warehouse | No system login, but physical access; risk = theft/intrusion |

### 2.2 Information Asset List

| Category | Assets | Why they matter |
|---|---|---|
| Digital Assets | Customer DB, payment/transaction data, e-commerce website, order management system, cloud accounts | Vulnerable to hacking/data breaches |
| Physical Assets | Office/warehouse building, staff laptops/mobile devices, network equipment, on-site servers | Vulnerable to theft/physical intrusion |

**Purpose:** This section is the raw material for Section 3 (who accesses
what) and, eventually, the Bow-Tie diagrams and Risk Register. It's the prep
work, not the analysis itself.

---

## 3. Actor-to-Asset Access Mapping

This section cross-references the Actor list and Asset list: **who accesses
which asset, at what permission level, and what's concerning about that
combination.** The general pattern across the table is:

> **The stronger the access, the weaker the control around it.**

- **IT/Systems administrator** — Full/Admin access to everything, but **no
  evidence of MFA enforcement**. Because this one account can touch
  everything, it's flagged as a **single point of failure**.
- **Order processing staff** — Read/Write (limited) access via **mobile
  devices**, which increases exposure to **phishing/credential theft**.
- **Customer support staff** — Handles sensitive customer data directly,
  making them a target for **social engineering**.
- **Payment gateway provider** — External limited access via API; the
  company relies on this vendor's security, but the current policy shows
  **no contractual security requirements** for them.
- **Cloud hosting provider** — External limited access; manages the
  underlying infrastructure the website runs on.
- **Customers** — Self-data only, via the front-end platform; relatively
  low risk since access is naturally restricted.
- **Visitors/Couriers** — Physical access only; **no CCTV or strict access
  control**, creating a device-theft risk.

This mapping is what later populates the "vulnerability" causes on the left
side of the Bow-Tie diagrams (Section 4) — e.g., "weak employee passwords"
and "no MFA" trace directly back to the admin account row here.

---

## 4. Bow-Tie Diagrams

A Bow-Tie diagram is shaped like a bow tie: a central **Event** (the
incident) with **causes/prevention on the left** and
**consequences/recovery on the right**.

- **Left (Before/Prevention):** root causes + the controls that stop them
- **Center:** the actual incident
- **Right (After/Recovery):** consequences + the response that mitigates them

### 4.1 Unauthorised Access to Customer & Payment Data
- **Causes:** weak employee passwords, unpatched software, unsecured
  network configuration
- **Prevention:** MFA, patch management, network segmentation
- **Consequences:** regulatory fines, reputational damage, financial loss
- **Recovery:** incident response, notification, cyber insurance

### 4.2 Physical Break-In / Device Theft
- **Causes:** no CCTV, no motion sensors/after-hours detection, devices
  left unsecured (no lockers)
- **Prevention:** CCTV installation, access control, alarm system
- **Consequences:** data breach from stolen devices, hardware
  loss/replacement cost, business disruption
- **Recovery:** remote wipe, asset insurance, backup recovery

### Why Sections 2–3 had to come first
The left-side causes in these diagrams (weak passwords, unpatched software,
unsecured network) are lifted straight from the vulnerabilities identified
in Section 3. The right-side consequences (regulatory fines, reputational
damage) exist *because* Section 2 defined the customer database as a
protected asset. In short: **you can't draw a plausible incident scenario
until you know who has access to what, and where the gaps are.** The
Bow-Tie diagrams compress the scattered findings from Section 3 into
coherent scenarios that Section 6 (Risk Register) will then quantify.

---

## 5. Risk Assessment Matrix

This is where the qualitative scenarios from Section 4 get converted into
**numbers**: `Likelihood × Impact = Risk Score`.

### 5.1 Likelihood Scale

| Score | Level | Meaning |
|---|---|---|
| 1 | Rare | Only in exceptional circumstances (e.g. once every few years) |
| 2 | Unlikely | Could occur at some point (e.g. once a year) |
| 3 | Possible | Might occur every few months |
| 4 | Likely | Will probably occur monthly |
| 5 | Almost Certain | Expected weekly or continuously |

### 5.2 Impact Scale

| Score | Level | Meaning |
|---|---|---|
| 1 | Negligible | Minimal disruption, no data/financial loss |
| 2 | Minor | Small operational impact, brief downtime |
| 3 | Moderate | Noticeable disruption, limited data exposure |
| 4 | Major | Significant breach/outage, regulatory attention |
| 5 | Severe | Large-scale breach, major fines, business-threatening |

### 5.3 Risk Rating Matrix

Multiply Likelihood × Impact to get a score, then map it to a band:

| Band | Score range | Meaning |
|---|---|---|
| **Low** | 1–3 | Don't need to worry much |
| **Medium** | 4–7 | Needs some management |
| **High** | 8–14 | Needs priority attention |
| **Extreme** | 15–25 | Needs immediate top-priority action |

**Why this matters:** budget and time are limited, so the company can't
treat every risk equally. This matrix is a **prioritization tool** — deal
with red (Extreme) first, green (Low) can wait. Every risk from the
Bow-Tie diagrams gets an L and I score here, and those numbers flow
directly into the L/I/Rating columns of Section 6.

---

## 6. Detailed Risk Register

This is the **centerpiece deliverable** of the report — all prior analysis
(Actors, Assets, Bow-Tie, Matrix) compressed into one table of 9 concrete
risks. Each row tells a mini-story:

> **[Actor]** can exploit **[Vulnerability]** to carry out **[Threat]**
> against **[Asset]**, resulting in **[Impact]**. This scores **L × I =
> Rating**.

### Notable entries

- **#1 (Extreme, 16):** External attacker exploits outdated, unpatched
  e-commerce software → data breach, service disruption, regulatory
  exposure. L4 × I4.
- **#2 (Extreme, 16):** Weak passwords + no MFA → brute-force/credential
  attacks on admin accounts → unauthorized access to systems and order
  data. L4 × I4.
- **#4 (Extreme, 15):** No reliable/tested backup plan → ransomware or
  system failure causes **permanent data loss**. L3 × I5 — likelihood is
  moderate but impact is worst-case, driving the extreme rating.
- **#6 and #8** are explicitly footnoted as **physical security
  vulnerabilities** (unsecured devices; no CCTV/motion sensors/after-hours
  detection) — distinct in nature from the cyber risks (#1–5, 7).
- **#9** is the **downstream consequence** of the other 8 risks —
  regulatory investigation and fines following a breach, under
  non-compliance with data privacy regulations (e.g. GDPR). Note the Actor
  here is "NovaStyle (organisation) / Regulator" rather than an external
  attacker — this row captures the company's own regulatory exposure, not
  a direct attack.

### Why organize it this way
1. **Priorities are visible at a glance** — the color-coded Rating column
   immediately shows what needs attention first.
2. **Every claim is justified** — instead of "this is risky," the table
   states *why* (Vulnerability) and *what happens* (Impact), which makes
   it defensible to management/auditors.
3. **It feeds directly into Sections 7 and 9** — the risk numbers (#1–9)
   are referenced again in the category grouping and in the control plan.

---

## 7. Risk Categories for Security Infrastructure

Groups the 9 individual risks into 8 broader categories. For example,
risks #6 (device theft) and #8 (break-in) are different scenarios but both
fall under **Physical Security / Endpoint Security**.

| Risk Category | Related Risks | Description |
|---|---|---|
| Application / Software Security | 1 | Outdated, unpatched, or vulnerable software |
| Access Control / Identity Management | 2 | Weak authentication and account access controls |
| Network Security | 3 | Insecure network configuration, lack of segmentation |
| Business Continuity / Backup & Recovery | 4 | Ability to recover data/operations after an incident |
| Data Protection | 5 | Inadequate protection (e.g. encryption) of sensitive data |
| Physical Security / Endpoint Security | 6, 8 | Inadequate physical safeguards for premises and devices |
| Security Awareness / Human Factor | 7 | Insufficient staff training on security practices |
| Compliance / Legal | 9 | Non-compliance with data privacy regulations |

**Why bother categorizing?** Saying "we have 9 risks" is less actionable
for management than saying "we have gaps across 8 domains." Similar-nature
problems can be budgeted for and solved together (e.g., one physical
security upgrade addresses both #6 and #8).

---

## 8. Risk Ratings

This section is intentionally brief — it's a **confirmation pointer**, not
new analysis. The actual work of assigning Likelihood/Impact scores
happened in Section 6, using the scale defined in Section 5.3. Section 8
exists mainly to satisfy a report-structure requirement ("show the risk
ratings") by explicitly pointing back: *"see the shaded Rating column in
Section 6."*

- **Section 7:** classify the risks into categories
- **Section 8:** confirm "ratings were assigned per Section 5.3, see
  Section 6" — a formality, not a new deliverable

---

## 9. Controls, Monitoring & Vendor Evaluation

This is where the report finally answers **"so how do we actually stop
this?"** — the first appearance of concrete solutions.

### 9.1 Control Measures & Monitoring Plan

For each of the 9 risks, the table defines:
- **Control Measure** — the specific action to take
- **Control Type** — the nature of the response
- **Monitoring & Review Plan** — how often it's checked
- **Owner** — who's accountable

#### Control Types explained
- **Preventive** — stops the incident from happening at all (e.g. password
  policy, encryption)
- **Detective** — notices an incident quickly (e.g. CCTV, monitoring)
- **Corrective** — mitigates damage after the fact (e.g. backup restore,
  remote wipe)

Most controls in the table are **Preventive** — reflecting the principle
that preventing an incident is cheaper and more effective than fixing it
afterward.

#### Example mappings
- **#1** (unpatched software) → monthly patch cycle + automated
  vulnerability scanning
- **#2** (weak passwords/no MFA) → strong password policy + MFA
  enforcement
- **#6** (device theft) → lockable storage + MDM enrollment with
  remote-wipe capability

#### Why the Owner varies
- Mostly **IT Administrator** (technical fixes)
- **#6:** IT Administrator + Office Manager (device management is IT;
  lockers/physical storage is facilities)
- **#7:** HR + IT Administrator (staff training involves HR)
- **#8:** Office Manager (CCTV/access control is a facilities matter)
- **#9:** Management/Compliance Lead (legal/regulatory issues sit at
  leadership level)

This makes accountability explicit so nothing falls into a "whose job is
this?" gap.

### 9.2 Vendor Product Evaluation

Rather than building everything in-house, three existing products were
selected to affordably cover the highest-rated risks:

| Product | Category | Key Features | Why it fits NovaStyle |
|---|---|---|---|
| **Wazuh** (open-source SIEM) | Security monitoring / threat detection | Free; log collection & correlation; intrusion/file-integrity detection; real-time alerting | Low-cost, covers Risks #1, #2, #3, #7 without a large licensing budget — this is the same Wazuh used in the TSOC Lab simulation exercises |
| **Qualys VMDR** | Vulnerability & patch management | Continuous scanning; automated risk scoring; patch prioritization | Gives an ongoing, quantifiable risk score for unpatched software (Risk #1) |
| **Microsoft Intune** | Mobile Device Management (MDM) | Device enrollment, encryption enforcement, remote wipe, compliance policies | Directly addresses Risk #6; integrates with the Microsoft 365 the company already uses |

**Overall flow of Section 9:** Section 6 identifies and scores 9 risks →
Section 9.1 assigns a specific action, type, review cadence, and owner to
each → Section 9.2 recommends actual tools to implement those actions.
Section 9 is where **theory (risk analysis) turns into practice (concrete
action plan).**

---

## 10. Security Recovery Plan

If Section 9 is "stop it from happening," Section 10 is "survive it when
it happens anyway." It complements the Incident Response Plan (IRP) from
Part B.

### 10.1 Recovery Objectives (RTO / RPO)

Two key disaster-recovery terms:

- **RTO (Recovery Time Objective)** — the maximum acceptable time to
  restore a system after an incident ("how fast do we need to be back
  up?")
- **RPO (Recovery Point Objective)** — how much data (in time) can be lost
  in the worst case, determined by backup frequency ("how recent does our
  restore point need to be?")

| System / Data | RTO | RPO |
|---|---|---|
| E-commerce website / order management system | 4 hours | 1 hour (near-continuous transaction logging) |
| Customer database (personal & payment info) | 8 hours | 24 hours (daily encrypted backup) |
| Internal network / admin systems | 24 hours | 24 hours |
| Employee devices / endpoints | 48 hours (replace/reimage) | N/A (no critical local data) |

**Analogy:** RTO = "how long until the shop reopens," RPO = "how far back
does our last saved record go, so we know what's unrecoverable."

The website gets the tightest RTO because it's directly tied to revenue.
The customer DB has a looser RTO but relies on daily backups (RPO) to
limit data loss — directly linked to the Risk #4 control (automated
encrypted backups) from Section 9.1.

### 10.2 Recovery Phases (6-Stage Incident Response, ~NIST lifecycle)

1. **Preparation** — maintain tested backups, updated contact lists, an
   accessible offline copy of the IRP/recovery plan, confirmed
   vendor/support contacts. Happens *before* any incident.
2. **Detection & Containment** — confirm the incident via monitoring
   alerts (e.g. Wazuh); isolate affected systems/accounts; disable
   compromised credentials.
3. **Eradication** — remove malware/unauthorized access, apply emergency
   patches, reset potentially affected passwords, close the exploited
   vulnerability.
4. **Recovery & Restoration** — restore from the most recent clean backup,
   validate data integrity, bring systems back online in a **staged
   manner: internal systems first, then the customer-facing site** — a
   deliberately cautious sequencing.
5. **Validation & Return to Operations** — verify functionality and
   security controls, monitor closely for 24–48 hours, confirm with
   stakeholders before declaring normal operations resumed.
6. **Post-Incident Review** — document root cause, timeline, and response
   effectiveness; **feed lessons learned back into the Risk Register and
   Controls (Sections 6 and 9)**; report to management and notify
   affected parties where required.

### 10.3 Backup & Restoration Procedure

- Daily **encrypted** backups of the customer DB and order management
  system, stored **both on-site and in a separate cloud location**
  (redundancy against a single point of failure).
- Before any restore, the backup is **scanned for malware first** —
  restoring an infected backup would undo the recovery.
- Restoration happens in an **isolated/staging environment first**,
  verified, then promoted to production.
- A **full restore test is performed quarterly** to confirm the process
  actually works and to keep the RTO/RPO targets realistic (rather than
  aspirational).

### 10.4 Return-to-Operations Checklist

A final gate before declaring "back to normal" — essentially a condensed
summary of the 6 recovery phases:

- [ ] Affected systems patched/reconfigured to remove the original
      vulnerability
- [ ] Monitoring tools (e.g. Wazuh) show no further suspicious activity
- [ ] All affected passwords/credentials reset
- [ ] Staff, management, and (where required) customers/regulators
      notified
- [ ] Risk register, controls, and recovery plan updated with lessons
      learned

---

## Big-picture takeaway

The report forms a **closed loop**, not a one-off checklist:

```
Identify who/what (2–3) → Model scenarios (4) → Score & rank (5–6)
     → Categorize (7–8) → Prevent (9) → Recover (10)
     → Post-Incident Review feeds back into Risk Register & Controls
```

Sections 9 and 10 together form a complete security management cycle:
**prevention** for the common case, and **recovery** for when prevention
inevitably fails somewhere. The explicit feedback loop in step 6 of
Section 10.2 is what keeps the whole assessment a living document rather
than a static, one-time report.
