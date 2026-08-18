# Session 4 – Conducting Risk Assessments & Categorising Risks

**Unit:** VU23219 / VU23221 — Manage the security infrastructure for an organisation
**Topic:** Topic 4 — Evaluate security infrastructure, assets, and conduct risk assessments

---

## 1. Threat, Vulnerability, Asset, Risk — Core Definitions

- **Threat** – any potential event/action that could cause an undesired outcome/harm.
  - Examples: zero-day exploit, untrained user with excessive privileges.
  - Threats can be **deliberate** or **accidental** (e.g. an untrained employee unintentionally causing harm).
- **Vulnerability** – a weakness a threat could exploit.
- **Asset** – anything of value to the organisation that needs protecting (hardware, software, data, people).
- **Risk** – the *potential* loss/impact/measure that exists when an identified vulnerability or threat is not mitigated. Risk is **not a certainty (not 100%)** — it's a possibility.
  - Risk is determined by **Likelihood** and **Impact** of harm occurring to an asset.
  - To assess a risk, consider: the asset at risk, the threat & actor, the vulnerability, and the harm/impact.

## 2. Evaluating Information Threats

Three questions to evaluate a threat: **Why? (motivation) / Where? (location) / Who or what? (agent)**

Three-axis threat model:
- **Agent**: Force Majeure → Technological → Human
- **Motivation**: Deliberate ↔ Accidental
- **Location**: External ↔ Internal

> Key point: **Internal threats can be more dangerous than external threats** — internal actors already know the organisation's systems and security measures in place.

### Technological Threats
Rely on technology to break through network security and exploit vulnerabilities. Often deployed alongside social engineering.
- Examples: **DoS, Man-in-the-Middle, Brute force attack**
- Causes: inadequate hardware maintenance, random component failure, natural ageing of materials, insufficient software testing/patching.

## 3. Likelihood & Impact

- **Likelihood** — probability of a threat occurring, informed by **precedent** (how often similar events have happened before).
- **Impact** — the **magnitude of harm** felt by the asset owner if compromised.
  - Dimensions of impact: Financial, Reputation, Customer, Legal/Regulatory, Management.

## 4. Why Risk Assessment Matters

Risk assessment = identifying, analysing, and evaluating potential risks, then taking steps to mitigate/manage them.

1. Helps identify vulnerabilities (via **audit**)
2. Helps prioritise security efforts (audit → gives priorities → implementation)
3. Helps comply with regulations
4. Helps make informed decisions (→ leads to security policy creation)

## 5. Risk Management Frameworks

### ISO 31000
Provides principles, framework, and process for managing risk, usable by any organisation.
- **Principles (Clause 4)** — centred on Value Creation and Protection
- **Framework (Clause 5)** — centred on Leadership and Commitment (Integration, Design, Implementation, Evaluation, Improvement)
- **Process (Clause 6)** — Scope/Context/Criteria → **Risk Assessment** (Identification → Analysis → Evaluation) → **Risk Treatment**, surrounded by ongoing Communication & Consultation and Monitoring & Review.

### NIST Risk Management Framework
Phases: **Prepare → Categorize → Select → Implement → Assess → Monitor** (ongoing, not a one-time process).
- NIST SP 800-53 is referenced as a controls catalogue.

## 6. Risk Matrix

- **Risk = Likelihood × Impact**
- 5×5 matrix: Likelihood (Rare/Unlikely/Possible/Likely/Almost Certain) × Impact (Insignificant/Minor/Moderate/Major/Catastrophic)
- Output ratings: Low / Medium / High / Critical
- This is called **qualitative risk analysis**.

## 7. Bow-Tie Diagrams

Visual risk-modelling technique showing **how** a risk works (vs. risk matrix, which shows **how big** a risk is).

**Structure:**
- **Hazard** (top) → **Event** (centre "knot")
- **Left side (causal/fault tree)**: Threats → Preventive Controls
- **Right side (consequence/event tree)**: Consequences → Mitigating/Recovery Controls

**Example threats (left side):** Phishing emails, weak/reused passwords, unpatched systems, insider misuse
**Example preventive controls:** MFA, email filtering, patch management, security awareness training
**Example consequences (right side):** Data breach, service outage, financial loss, reputational damage
**Example mitigating controls:** Incident response plan, backups & recovery, logging & monitoring, legal & regulatory response

> Tool suggestion from tutorial: [app.diagrams.net](https://app.diagrams.net/) — free online tool to build bow-tie diagrams.

## 8. Inherent Risk vs Residual Risk

- **Inherent risk** = risk that exists **before** any controls are applied (raw exposure / worst case).
- **Residual risk** = risk that **remains after** controls have been implemented. Risk can never be fully eliminated.
- **Risk Reduction = Inherent risk − Residual risk**
- The goal of risk management is **not to eliminate risk entirely**, but to reduce inherent risk to an **acceptable level** (residual risk).
- **Risk Appetite** = the amount/type of risk an organisation is willing to accept. Varies by organisation — e.g. a bank vs. a small business will have different acceptable risk levels.

## 9. Risk Mitigation — People, Process, Technology

Risk mitigation is an overall approach to prevent, reduce, and manage the severity of risk, applied across three key areas (in order of importance):
- **People** — often the weakest link but also the strongest defence when prepared. Examples: security awareness training, phishing simulations, clear accountability.
- **Process** — defines how people should behave. Examples: security policies, incident response procedures, change management processes.
- **Technology** — provides automated protection. Examples: firewalls, IDS, encryption, backups.

## 10. Security Control Types (by *what* the control is)

| Control Type | Focus | Examples |
|---|---|---|
| **Logical (Technical)** | Software/hardware controls, often invisible to users | Passwords, MFA, firewalls, encryption, IDS |
| **Physical** | Visible/tangible controls on physical movement or equipment | Locked doors, security guards, fences, CCTV, signage |
| **Administrative** | "Soft controls" — policy/procedure-based, focus on people & processes | Security policies, hiring/vetting, DR plans, training & awareness, access reviews, job rotation |

## 11. Control Classes (by *when/how* the control acts)

| Control Class | Purpose | Example |
|---|---|---|
| **Preventive** | Stop attacks before they succeed | MFA, firewalls, patch management, access controls |
| **Detective** | Identify attacks in progress or after occurrence | Logging & monitoring, IDS/IPS, SIEM, CCTV |
| **Corrective / Responsive** | Limit impact and restore normal operations after an incident | Least-privilege access, network segmentation, backups, DR plans, incident response plans |
| *(Deterrent — mentioned as a 4th category)* | Discourage an attack before it's attempted | e.g. visible security signage/cameras |

> A single control can combine type + class, e.g. MFA (Logical + Preventive), CCTV (Physical + Detective), DR plan (Administrative + Corrective).

## 12. Cost–Benefit Consideration

Controls must be proportionate to risk — avoid both under-protecting critical assets and over-engineering controls that cost more than the potential loss.

## 13. Risk Treatment Options (Risk Appetite–driven)

| Option | When Used | Example |
|---|---|---|
| **Accept** | Risk is within appetite | Minor website defacement on a low-impact site |
| **Mitigate** | Risk exceeds appetite, additional controls required | Adding MFA/monitoring for admin access |
| **Transfer** | Risk shared with a third party | Cyber insurance, cloud service providers |
| **Avoid** | Risk far above appetite | Discontinuing unsupported legacy systems |
| *(Indemnify — mentioned in the IBM video)* | Insurance/contract to cover financial loss | Cyber insurance |

## 14. Industry Context (CIA Triad varies by sector)

From the IBM "Risky Business" video referenced in class:
- **Manufacturing** → prioritises **Availability** (keeping production lines running)
- **Financial services** → prioritises **Confidentiality** (precise risk models, actuarial data, very risk-intolerant)
- **Healthcare** → prioritises **patient safety** above general confidentiality concerns

Risk analysis process (from video): Policy → Architecture → Implementation → Operation → Audit → (loops back to Risk Analysis). Key inputs: know yourself, risk tolerance, industry norms.

Quantitative analysis (numbers/spreadsheets) is valuable but shouldn't be over-relied upon; qualitative analysis (High/Medium/Low judgement) remains important.

---

## Reference Materials
- Topic 4 – Conducting Risk Assessments & Categorising Risks (course PDF)
- Bow-tie Method Tutorial (course PDF) — CRAMM mentioned as a more complex alternative approach
- IBM Technology — *"Risky Business: Strengthening Cybersecurity with Risk Analysis"* (YouTube)
- ISO 31000 official site: https://www.iso.org/iso-31000-risk-management.html
- Bow-tie diagramming tool: https://app.diagrams.net/

## Application Notes (NovaStyle Part A/B connection)
These concepts directly underpin the NovaStyle Part A risk assessment work already completed:
- Actor/Asset List → Section 4.1 (asset identification, CIA valuation)
- Bow-Tie Diagrams (4.1, 4.2) → Section 4.4 (threats/causes left, consequences right, prevention/recovery controls)
- Risk Assessment Matrix → Section 4.3 (Likelihood × Impact, 5×5 matrix)
- Controls section → Sections 4.5/4.5.2 (Preventive/Detective/Corrective, Logical/Physical/Administrative)
- Not yet incorporated: explicit **Inherent vs Residual risk** distinction and **Risk Appetite** statement for NovaStyle — worth adding to Part B.
