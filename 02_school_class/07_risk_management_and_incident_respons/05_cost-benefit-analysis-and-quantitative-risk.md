# Session 7 — Risk-Based Security Controls & System Hardening

**Unit:** VU23219 (Manage the security infrastructure for an organisation) / VU23221 (Evaluate and test an incident response plan for an enterprise)
**Topic:** Topic 7 — Implementing Security System Controls & System Hardening

---

## 1. Cost–Benefit Analysis (CBA)

CBA is used to decide whether implementing a security control is financially justified.

**Key Costs Considered**
- Purchase or licensing costs
- Implementation and configuration time
- Ongoing maintenance and monitoring
- Training and staffing costs

**Key Benefits Considered**
- Reduced likelihood of incidents
- Reduced impact if incidents occur
- Avoided downtime and recovery costs
- Improved compliance and trust

**CBA Steps**
1. Identify and quantify the costs (capital, operational, maintenance).
2. Identify and quantify the benefits (revenue generation, cost savings, positive impacts).
3. Assign a monetary value using techniques such as **NPV**, **IRR**, or **ROI**.
4. Compare total costs vs. total benefits — implement only if benefits outweigh costs.

**Decision rule:** if the annual risk (financial exposure) is *less* than the cost of the control, the control is not worth implementing.

---

## 2. Feasibility Analysis

Feasibility analysis complements CBA by examining whether a proposed control can **realistically** be implemented and sustained, considering:

- Available resources
- Technical capability (do we have the skills/tools?)
- Staff skills
- Time constraints
- Operational impact (will it disrupt the business?)
- New risks introduced by the control itself

**Feasibility Steps**
1. Define the project scope and objectives; identify required resources.
2. Conduct a market analysis (demand, competitors, trends) — *for larger projects/investments*.

CBA + Feasibility together determine whether a control is both **cost-effective** and **practically achievable**.

---

## 3. Quantitative Risk Assessment (Formulas)

Unlike qualitative assessment (labels like High/Medium/Low), quantitative assessment expresses risk in **dollar terms**.

| Term | Definition |
|---|---|
| **AV** (Asset Value) | Estimated value of the asset based on original cost, depreciation, and replacement cost. |
| **EF** (Exposure Factor) | Expected % of damage to an asset if a risk occurs. |
| **SLE** (Single Loss Expectancy) | Expected loss in $ from **one** occurrence of the risk. |
| **ARO** (Annualised Rate of Occurrence) | Number of times the risk is expected to occur per year (e.g., once in 100 years → ARO = 0.01). |
| **ALE** (Annualised Loss Expectancy) | Expected loss in $ from a risk in any given year. |

**Formulas**
```
SLE = AV × EF
ALE = SLE × ARO
```

**Worked example**
- If implementing a new control reduces ARO of a data breach from 0.1 to 0.05, and SLE = $100,000:
```
Expected Reduction in ALE = (0.1 - 0.05) × $100,000 = $5,000
```
- If the annual cost of the control is **less than $5,000**, the organisation benefits financially from implementing it.

**Why ALE matters**
- Quantifies cyber risk in financial terms
- Enables objective comparison between different risks
- Justifies security spending / avoids overspending on low-impact risks
- Focuses resources on risks with the highest business impact

> Note: this assessment task (AT2 Part A) primarily requires a **qualitative** risk assessment — the exact quantitative figures (e.g., hardware asset values) are not mandatory, but can be included as illustrative examples if desired.

---

## 4. Qualitative Risk Assessment — Risk Matrix

**Likelihood Ratings**
| Rating | Description |
|---|---|
| Rare | May occur only in exceptional circumstances |
| Unlikely | Could occur but is not expected |
| Possible | May occur under certain circumstances |
| Likely | Expected to occur at some point |
| Almost Certain | Expected to occur frequently |

**Impact Ratings**
| Rating | Description |
|---|---|
| Insignificant | Minimal impact on operations |
| Minor | (details as per organisation's risk matrix) |
| Moderate | ... |
| Major | ... |
| Severe | ... |

A **Risk Matrix** classifies each identified risk by combining Likelihood (one axis) and Impact (the other axis) to derive an overall risk rating.

---

## 5. NIST Cybersecurity Framework (CSF) 2.0

A voluntary set of guidelines/best practices from NIST to help organisations manage and reduce cybersecurity risk.

**Six Core Functions**
1. **Govern** — Oversees and establishes cybersecurity risk management strategy
2. **Identify**
3. **Protect**
4. **Detect**
5. **Respond**
6. **Recover**

Each function has subcategories. Example — **Recover: Incident Recovery Plan Execution (RC.RP)**:

| Subcategory | Requirement | What It Means in Practice | Key Documentation |
|---|---|---|---|
| RC.RP-01 | Execute the recovery portion of the IR plan | Recovery procedures formally activated after containment/eradication | Recovery initiation approval, transition record (Respond → Recover) |
| RC.RP-02 | Recovery actions selected, scoped, prioritised, performed | Systems restored based on business impact & defined priorities | Recovery priority list, RTO/RPO definitions, Business Impact Analysis |
| RC.RP-03 | Integrity of backups/restoration assets verified before use | Backups validated, scanned, confirmed uncompromised | Backup validation checklist, malware scan results |
| RC.RP-04 | Critical mission functions & cybersecurity risk considered | Restoration decisions align with business continuity & risk tolerance | Post-incident operational plan, risk assessment updates |
| RC.RP-05 | Integrity of restored assets verified before use | Restored systems tested for functionality & security | System validation checklist, vulnerability scan results |

---

## 6. Recovery Planning: RTO & RPO

- **RPO (Recovery Point Objective):** Maximum acceptable **data loss** after an incident, measured *backward* from the moment of failure.
  - Key question: *How much data can we afford to lose?*
  - Drives backup frequency.
  - Example: RPO = 1 hour → backups must occur at least every hour.
- **RTO (Recovery Time Objective):** How quickly the system must be restored to normal operations (time-based).

An effective recovery plan should be **risk-based** and **aligned with business impact**.

---

## 7. Security Controls Recap

**Control Types:** Administrative / Logical (Preventative) / Physical
**Control Classes:** Preventative / Detective / Corrective

**Applying Controls to a Risk (worked example — customer data breach)**

| Element | Example |
|---|---|
| Risk | Customer data breach |
| Threat | Phishing attack targeting staff |
| Vulnerability | Weak passwords and no MFA |
| Impact | Financial loss, reputational damage, legal penalties |

**5-Step Control Lifecycle**
1. **Identify Risks, Threats, Vulnerabilities**
2. **Select Controls That Match the Risk** (not random controls)
   - Logical/Preventative: MFA, strong password policies
   - Administrative: security awareness training (phishing focus), least-privilege access policy updates
3. **Implement the Controls** — put into actual operation, not just documentation
   - e.g., MFA enabled on email/cloud, password complexity enforced, staff phishing training completed, access rights reviewed
   - Controls are **tested** to ensure they work as intended
4. **Add Detective and Corrective Controls** — to support detection & recovery
   - Monitoring/logging for failed logins, alerts for suspicious activity, backup testing
   - Ensures the organisation can detect, respond to, and recover from incidents — not just prevent them
5. **Review and Adjust** — controls reviewed regularly to ensure they still match the risk
   - New threats may require new controls
   - System/user changes may introduce new vulnerabilities
   - Lessons learned from incidents used to improve controls

> **Key principle:** Security controls are effective only when they are aligned to identified risks, threats, and vulnerabilities.

---

## 8. System Hardening

Techniques to secure systems by reducing vulnerabilities and limiting exposure to threats — implementing control processes so systems are protected from unauthorised access and successful attacks.

---

## Summary

| Concept | One-line takeaway |
|---|---|
| CBA | Only implement a control if benefits > costs |
| Feasibility Analysis | A control must also be practically achievable, not just cost-effective |
| SLE / ALE | Quantifies risk in $ terms: `SLE = AV × EF`, `ALE = SLE × ARO` |
| Risk Matrix | Qualitative rating via Likelihood × Impact |
| NIST CSF | Govern → Identify → Protect → Detect → Respond → Recover |
| RTO / RPO | RTO = how fast to recover; RPO = how much data loss is acceptable |
| Control Lifecycle | Identify → Select → Implement → Add Detective/Corrective → Review & Adjust |
