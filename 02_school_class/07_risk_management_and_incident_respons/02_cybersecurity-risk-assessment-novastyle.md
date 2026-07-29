# Cybersecurity Risk Assessment — Study Notes

> Personal study notes from working through a Risk Assessment assignment (VU23219/VU23221 – *Manage the Security Infrastructure for an Organisation* / *Evaluate and Test an Incident Response Plan*). Covers risk management frameworks, bow-tie analysis, risk registers, and how to build a full risk assessment report from scratch.

---

## 1. Core Risk Management Frameworks

### 1.1 ISO 31000
An international standard providing principles and guidelines for risk management. It defines a repeatable cycle:

```
Identify → Analyze → Evaluate → Treat → Monitor → Communicate
```

Key structural elements:
- **Principles** (Clause 4) — e.g. integrated, structured, customised, inclusive, dynamic, best available information, human/cultural factors, continual improvement.
- **Framework** (Clause 5) — Leadership & commitment → Design → Implementation → Evaluation → Improvement.
- **Process** (Clause 6) — Scope/Context/Criteria → Risk Assessment (Identification, Analysis, Evaluation) → Risk Treatment, wrapped by ongoing *Communication & Consultation* and *Monitoring & Review*, all captured through *Recording & Reporting*.

### 1.2 NIST SP 800-37 Rev. 2 — Risk Management Framework (RMF)
Purpose-built for information systems and organisations. Described as **Comprehensive, Adaptable, Repeatable, Measurable**.

**7 Steps:**
1. **Prepare** — get the organisation ready to manage risk
2. **Categorize** — classify system/information based on impact (see NIST SP 800-60)
3. **Select** — choose applicable security/privacy controls (see NIST SP 800-53)
4. **Implement** — deploy and document controls
5. **Assess** — verify controls are working as intended
6. **Authorize** — a senior official makes a risk-based go/no-go decision
7. **Monitor** — continuously track control effectiveness and emerging risk

### 1.3 Bow-Tie Analysis
A visual risk tool that maps the pathway from **causes → event → consequences**, with **barriers/controls** placed on both sides.

```
[Cause 1] ─┐                                    ┌─ [Consequence 1]
[Cause 2] ─┼─[Preventive Controls]→ (EVENT) →[Recovery Controls]─┼─ [Consequence 2]
[Cause 3] ─┘                                    └─ [Consequence 3]
```

- **Left side (Prevention / "Before")** — potential causes/threats, with preventive controls (e.g. MFA, patch management, training) sitting between causes and the event.
- **Center** — the single top/adverse event.
- **Right side (Recovery / "After")** — potential consequences/outcomes, with recovery/corrective controls (e.g. incident response, notification, insurance) between the event and outcomes.

Useful because it separates **prevention** (reduce likelihood) from **recovery** (reduce impact) in one diagram — good for both the risk register and for informing the control plan.

**Practical tool note:** [draw.io](https://app.diagrams.net) has no dedicated "bow-tie" shape library — it's built from basic shapes:
- Two large **triangles** (wedges) facing each other, resized via the *Arrange* tab (set Width/Height directly for a clean wedge instead of a default equilateral triangle)
- A **circle/ellipse** in the middle for the top event
- **Rounded rectangles** for causes/consequences, layered on top of the triangles
- **Arrows** connecting causes → event → consequences
- Gradient fills (Style tab → Fill → Gradient) make it look like professional infographics
- Text colour is edited under the **Text** tab (not the *Style* tab, which only controls fill/line)

---

## 2. Structuring a Risk Assessment Report

A practical two-part structure that maps well to most assignment/marking guides:

```
■ High Level Analysis
  1. Business goals + security baseline + configuration/change management
  2. Actor list & Information asset list
  3. Actor-to-Asset access mapping
  4. Bow-tie diagram(s) for key adverse events

■ Risk Assessment and Ratings
  5. Risk assessment matrix (Likelihood × Impact)
  6. Detailed risk register (Actor / Asset / Threat / Vulnerability / Impact / Rating)
  7. Risk categories
  8. Risk ratings (derived from the matrix)
  9. Controls, monitoring plan & vendor evaluation
  10. Security recovery plan
```

### 2.1 Actors — what the term actually means
"Actor" ≠ a person in a film. In risk/security analysis, an **actor** is any person, group, or system that interacts with or affects the organisation's assets. Typical categories:

| Category | Examples |
|---|---|
| Internal staff | Order processing, customer support, IT admin, warehouse staff |
| External partners | Payment gateway, cloud hosting provider, couriers, software vendors |
| Customers | End users placing orders / providing personal data |
| Other physical actors | Visitors, delivery couriers physically entering the premises |

The key analytical step isn't just listing actors — it's evaluating **whether their actual work habits align with security policy** (e.g. staff using personal mobile devices for system access without MFA = a gap between stated policy and real behaviour).

### 2.2 Assets
Split into:
- **Digital assets** — databases, websites, order management systems, cloud accounts
- **Physical assets** — buildings, devices, network hardware, on-site servers

### 2.3 Actor-to-Asset Access Mapping
A table cross-referencing each actor with the assets they can reach, their access level (e.g. Read/Write limited, Full/Admin, External limited, Physical-only), and analytical notes tying back to real vulnerabilities (e.g. "No CCTV — policy Section 9 omits adequate physical security measures").

---

## 3. Risk Assessment Matrix (Qualitative 5×5)

### 3.1 Likelihood Scale
| Rating | Level | Description |
|---|---|---|
| 1 | Rare | Once every few years |
| 2 | Unlikely | ~once a year |
| 3 | Possible | Every few months |
| 4 | Likely | Monthly |
| 5 | Almost Certain | Weekly / continuous |

### 3.2 Impact Scale
| Rating | Level | Description |
|---|---|---|
| 1 | Negligible | No real disruption |
| 2 | Minor | Small cost / brief downtime |
| 3 | Moderate | Limited data exposure, moderate cost |
| 4 | Major | Significant breach/outage, regulatory attention |
| 5 | Severe | Large-scale breach, major fines, business-threatening |

### 3.3 Combining into a Rating
`Risk Score = Likelihood × Impact`, then banded:

| Score | Rating |
|---|---|
| 1–3 | Low |
| 4–7 | Medium |
| 8–14 | High |
| 15–25 | Extreme |

This produces a standard 5×5 heat-map matrix that every individual risk can be plotted against.

---

## 4. Detailed Risk Register

Each row documents **one risk end-to-end**, with all fields needed for both the matrix and the control plan:

| Field | Purpose |
|---|---|
| Actor | Who/what triggers or is involved in the risk |
| Asset | What is being threatened |
| Threat | The event/action that could cause harm |
| Vulnerability | The specific weakness that enables the threat |
| Impact (description) | What happens if it occurs |
| Likelihood (L) | 1–5, from Section 3.1 |
| Impact (I) | 1–5, from Section 3.2 |
| Rating | L × I, banded per Section 3.3 |

**Important:** don't forget to explicitly call out **physical security vulnerabilities** as their own risk entries (e.g. unsecured devices, missing CCTV/motion sensors) — these are commonly a separate, required marking criterion distinct from pure cyber risk.

### Risk Categories
Once the register exists, group risks into categories for reporting clarity, e.g.:
`Application/Software Security · Access Control/Identity Management · Network Security · Business Continuity/Backup & Recovery · Data Protection · Physical/Endpoint Security · Security Awareness/Human Factor · Compliance/Legal`

---

## 5. Controls, Monitoring & Vendor Evaluation

For each risk, define:
- **Control measure(s)** — what will actually be done
- **Control type** — Preventive / Detective / Corrective
- **Monitoring & review plan** — how often and by whom this control is checked (weekly log review, quarterly audits, annual policy review, etc.)
- **Owner** — who is accountable

### Vendor product evaluation
Pick tools that plausibly support **risk monitoring or risk rating**, matched to the highest-priority risk categories, e.g.:

| Vendor | Category | Why it fits |
|---|---|---|
| **Wazuh** (open-source SIEM) | Security monitoring / log & threat detection | Free — good for small businesses; covers ongoing detection risks |
| **Qualys VMDR** | Vulnerability & patch management | Automated risk scoring directly supports the "unpatched software" risk |
| **Microsoft Intune** | Mobile Device Management (MDM) | Enforces encryption/remote wipe — addresses unsecured mobile device risk |

---

## 6. Security Recovery Plan

Distinct from an Incident Response Plan (which is about detection/containment/communication) — a recovery plan focuses on **getting systems and data back to normal operation**.

### 6.1 RTO / RPO
- **RTO (Recovery Time Objective)** — how quickly a system must be restored
- **RPO (Recovery Point Objective)** — how much data loss (measured in time) is tolerable, i.e. how far back the last usable backup can be

Different systems can have different targets (e.g. the customer-facing website needs a much shorter RTO than an internal admin tool).

### 6.2 Recovery Phases
A simple six-phase structure:
1. **Preparation** — backups tested, contacts/documentation ready
2. **Detection & Containment** — confirm incident, isolate affected systems
3. **Eradication** — remove the root cause (malware, compromised accounts, unpatched flaw)
4. **Recovery & Restoration** — restore from clean backup, stage before going live
5. **Validation & Return to Operations** — confirm systems are clean and stable before declaring "all clear"
6. **Post-Incident Review** — document lessons learned, update the risk register and controls

### 6.3 Backup & Restoration Procedure
Good practice pattern: backups stored **both on-site and off-site/cloud**, scanned for malware before restoration, restored to a staging/isolated environment first, and **tested periodically** (e.g. quarterly) — otherwise the RTO/RPO targets are just theoretical numbers.

---

## 7. General Lessons Learned

- **A risk register is the hub** — actors, assets, and controls all connect back to it; build it after the actor/asset/access work is done, so it can reference real, specific vulnerabilities rather than generic ones.
- **Bow-tie diagrams are a visualization, not a separate analysis** — the causes/consequences should come directly from risks already identified elsewhere in the assessment, not be invented separately.
- **Policy documents are often deliberately generic** — a short, vague internal policy (e.g. "changes are performed as required") is itself evidence of a control gap and can be cited directly as justification for a risk.
- **Consistency matters** — same terminology, same rating scale, and same actor/asset names should be used across every section, since assessors mark for internal consistency, not just correctness of each section in isolation.
- **AI-assisted drafting vs. academic integrity** — tools can help structure tables, generate scaffolding, and explain frameworks, but any prose/analysis meant to demonstrate personal understanding should be reviewed, personalised, and (where required) explicitly disclosed as AI-assisted.

---

## 8. Quick Reference — Formulas & Legends

```text
Risk Score = Likelihood (1–5) × Impact (1–5)

1–3   → Low
4–7   → Medium
8–14  → High
15–25 → Extreme
```

```text
Bow-Tie structure:
Causes --[Preventive Controls]--> TOP EVENT --[Recovery Controls]--> Consequences
```

---

*Notes compiled while completing a cybersecurity risk assessment assignment. For personal study reference only.*
