# VU23220 – Cyber Security Industry Project
## Study Notes: Session 1–2 (Phishing & Project Management Fundamentals)

**Course:** VU23220 – Develop and carry out a cyber security industry project
**Related unit:** ICTICT443 – Work collaboratively in the ICT industry
**Institution:** Holmesglen TAFE
**Date:** 30 July 2026

---

## 1. Phishing — Core Concepts

### 1.1 Definition
Phishing is the fraudulent practice of sending messages that impersonate a reputable
source in order to trick individuals into revealing personal information such as
passwords, credit card numbers, or financial details.

### 1.2 Types of Phishing
| Type | Description |
|---|---|
| **Mass Scale Campaigns** | Most common attack type. Attackers hold large email databases; may make initial contact via phone call or social media. |
| **Whaling** | Targets high-value individuals (CEOs, personal assistants) to induce a click or action. |
| **Spear Phishing** | Personalised / customised messages, often used for Business Email Compromise (BEC). |
| **Vishing** | Voice phishing — same social-engineering tactics delivered by phone call instead of email. |
| **Smishing** | Phishing delivered via SMS/text message. |

### 1.3 Recognising a Phishing Email — Red Flags
- Sender domain doesn't match the organisation it claims to represent (spoofing).
- Misspelled/near-identical domains (**typosquatting**), e.g. `mazoncanada.ca` instead of `amazon.com`.
- Generic, non-personalised greetings ("Dear Client").
- Message invokes fear or urgency (e.g. "your account will be suspended in 48 hrs").
- Requests to verify personal/financial information or passwords.
- Poor grammar/spelling (though AI tools like ChatGPT are now improving attacker grammar,
  making detection harder).
- Suspicious embedded links — hovering over the link reveals a different destination
  than the displayed text (a major red flag).
- Unexpected attachments, especially non-`.txt` file types.

### 1.4 Social Engineering Techniques
- **Typosquatting** – a type of URL hijacking using a near-identical but incorrect
  domain name (e.g. `professormessor.com` vs. `ProfessorMesser.com`).
- **Pretexting** – lying / inventing a false scenario to extract information
  (e.g. "Hi, we're calling from Visa regarding an automated payment...").
- Attackers exploit human tendency to be helpful and to act quickly under urgency.

### 1.5 Dissected Real-World Example (Fake Amazon Email)
- Sender: `management@mazoncanada.ca` — missing "A" in Amazon, not a legitimate domain.
- Greeting: "Dear Client" — generic, non-personalised.
- Displayed link text looked like `amazon.com`, but hovering revealed the real
  destination: `redirect.kereskedj.com`.

### 1.6 Impacts of Phishing — Corporate
**Reputational Damage**
- Brands are fundamentally built on trust.
- Public disclosure of a breach damages perception among employees, partners, and
  customers, and can significantly reduce market value.
- Companies have a responsibility to notify affected customers **immediately** once a
  breach is confirmed — not "tomorrow," not "next week." Incident response teams
  should act first, and stakeholders should be briefed.

**Intellectual Property (IP) Loss**
- Trade secrets, R&D, customer lists, and formulas can be compromised.
- For tech, defence, or pharmaceutical firms, a single leaked patent/design can
  represent millions or billions of dollars in sunk research costs.

### 1.7 Mitigation & Reporting
- Suspicious emails must be **reported**, not simply deleted or ignored.
- Standard handling flow: report → flag → quarantine → analyse.
- IT departments generally do **not** automatically monitor personal inboxes for
  phishing — employees must forward suspicious emails to IT/security teams
  themselves (check company policy/TSD website for the correct process).
- Technical mitigation techniques mentioned for the next session: **SPF, DKIM, DMARC**
  (email authentication protocols), and general "email mitigation techniques."

### 1.8 Real-World Case Studies Discussed
- **Amazon phishing email** (missing letter in domain, fake Amazon suspension notice).
- **Rackspace-spoofed phishing email** sent from an iCloud address, demanding email
  "confirmation" within 48 hours.
- **Linkt (Australian toll company) SMS scam** — fake "unpaid toll" text messages
  leading to a convincing fake payment site; a real, personally experienced example
  discussed in class (recovery took ~6 months, including closing bank accounts).
- **Origin Energy data breach (July 2026)** — confirmed ~900,000 current/former
  customers affected; exposed PII (name, address, DOB, phone, partial financial
  details). Shared live in class as a real-time example of a corporate breach and
  the reputational-damage discussion.
- **Optus and Telstra** — referenced as other major Australian companies affected by
  past breaches/outages, tying back to the "loss of customers/trust" discussion.
- Nigerian Prince / "419" advance-fee scam — referenced as a classic historical
  phishing example.
- Fake job-offer scam (shared by a classmate) — fraudulent "sales position" that
  required sending customers to a fake Shopify page; used to harvest credit card
  information.

---

## 2. Introduction to Project Management (IT Project Management, 7th Ed. — K. Schwalbe)

### 2.1 What Is a Project?
> "A temporary endeavor undertaken to create a unique product, service, or result."
> (PMBOK Guide, 5th Ed., 2012)

- Operations = ongoing work to sustain the business (not a project).
- Projects end when objectives are met or the project is terminated.

### 2.2 Project Attributes
A project:
- Has a unique purpose
- Is temporary
- Is developed using **progressive elaboration** (increasing detail over time)
- Requires resources from various areas
- Should have a primary customer or **sponsor** (provides direction and funding —
  in this course, the sponsor/client role is played by the lecturer)
- Involves uncertainty

### 2.3 The Triple Constraint
Successful project management means meeting all three goals simultaneously, while
satisfying the project sponsor:
- **Scope**
- **Time**
- **Cost**

### 2.4 Project Management Framework
- **10 Knowledge Areas**: Integration, Scope, Time, Cost, Quality, Human Resource,
  Communications, Risk, Procurement, Stakeholder Management.
- **Project Portfolio**: multiple projects (Project 1, 2, 3, 4…) managed together
  toward enterprise success.

### 2.5 Project Stakeholders
Sponsor, project manager, project team, support staff, customers, users, suppliers,
and even opponents to the project.

### 2.6 Tools & "Super Tools"
- **Super tools** (high use + high impact on success): task-scheduling software,
  scope statements, requirements analyses, lessons-learned reports.
- **Widely-used tools that improve project outcomes**: progress reports, kick-off
  meetings, **Gantt charts**, change requests.
- Gantt charts visualise weekly/periodic progress and milestones (example shown
  using Microsoft Project 2010).
- Additional referenced techniques: network diagrams, critical path analysis,
  critical chain scheduling, cost estimates, earned value management.

### 2.7 What Helps Projects Succeed (Standish Group, "CHAOS Activity News," 2011)
1. User involvement
2. Executive support
3. Clear business objectives
4. Emotional maturity
5. Optimizing scope
6. Agile process
7. Project management expertise
8. Skilled resources
9. Execution
10. Tools and infrastructure

### 2.8 Suggested Skills for Project Managers
- Project Management Body of Knowledge (PMBOK)
- Application area knowledge, standards, and regulations
- Project environment knowledge
- General management knowledge and skills
- Soft skills / human relations skills (leadership, listening, integrity, trust,
  verbal communication, team-building, conflict resolution, critical thinking,
  balancing priorities)

**Key discussion point:** To become a good leader/manager, one should first be a
good team player/follower. Balancing priorities and neutrality during team
disagreements were emphasised as important soft skills.

---

## 3. Assessment Task 2 — Cyber Security Industry Project (Practical Task)

### 3.1 Deliverables (End Result)
As clarified in class, the final deliverables are:
1. **Penetration testing** activity
2. **Setting up a testing environment**
3. **Presenting** the results to the class (can be recorded via PowerPoint or
   delivered live)

### 3.2 Suggested Pen-Testing Report Structure
1. Executive Summary
2. Scope of Engagement (target: VulnHub "Basic Pentesting 1" VM)
3. Testing Methodology
4. Rules of Engagement
5. Host Discovery – Red Team Activity
6. Port and Service Enumeration – Red Team Activity
7. Vulnerability Identification – Red Team Activity
8. Exploitation – Red Team Activity
9. Privilege Escalation – Red Team Activity
10. Post-Exploitation – Blue Team Activity (incl. Indicators of Compromise, IOCs)
11. Findings and Risk Ratings – Blue Team Activity (CVSS-based)
12. Recommendations – Blue Team Activity
13. Conclusion & Appendices (screenshots, logs, evidence)

### 3.3 Group Work Expectations
- Group work with individual accountability — the lecturer explicitly stated:
  **contribution should be roughly equal among group members.** If a group member
  is not participating, students are encouraged to notify the lecturer directly.
- Roles within the group are self-organised, not assigned by the lecturer
  (technical work, admin/documentation, diagrams, etc.), based on individual
  strengths.
- The assessment has two components:
  - **Project Management Report** (group work)
  - **Technical Aspect / Part B** (individual work — students are expected to
    attempt this independently before asking for help)

### 3.4 Timeline
- 18 total sessions in the unit.
- Assessment Task 2 due around **Session 16**.
- Part A target: complete before the mid-term break (approx. 3rd week of September).
- If submitted early (e.g. by Session 15), attendance for remaining sessions before
  the due date is not mandatory.

---

## 4. Practical Setup — GoPhish + MailHog (Simulated Phishing Environment)

### 4.1 Purpose
Build a safe, isolated testing environment to simulate phishing campaigns without
sending real emails externally:
- **GoPhish** — open-source tool to create and launch simulated phishing campaigns.
- **MailHog** — a fake SMTP mail server that intercepts test emails locally instead
  of sending them to real inboxes.

### 4.2 Installation Steps (Linux / Kali VM)
1. Download GoPhish from the official GitHub releases page.
2. Extract the zip file to a folder.
3. Make the `gophish` file executable (`chmod +x gophish`) — only needed once.
4. Run `./gophish`. The terminal log provides:
   - Username: `admin`
   - A randomly generated temporary password
   - Dashboard URL: `https://127.0.0.1:3333`
5. Log into the dashboard, accept the browser security warning, and set a new
   password on first login (the temporary password becomes obsolete afterward).
6. Download MailHog from its GitHub releases page (separate step, still pending).
7. Make MailHog executable and run it — log provides SMTP server info and a
   dashboard URL.
8. Configure GoPhish's "Sending Profile" to use MailHog's SMTP server, then send a
   test email from GoPhish to confirm the two tools are connected.

### 4.3 Progress So Far
- ✅ GoPhish successfully installed and dashboard login completed
  (Campaigns, Users & Groups, Email Templates, Landing Pages, Sending Profiles
  are all visible).
- ⏸️ MailHog installation — not yet started (next step for a future session).
- VM can be safely shut down: stop GoPhish first via `Ctrl+C` in its terminal, then
  shut down the VM normally (or use "Suspend" to preserve the current session state
  for next time).
- To resume GoPhish later:
  ```bash
  cd ~/Downloads/gophish-v0.12.1-linux-64bit
  ./gophish
  ```

---

## 5. Key Takeaways / Personal Reflection
- Real-world relevance: a personal experience with a fake **Linkt** toll-payment SMS
  scam (paid without hesitation while working as a delivery driver; took ~6 months
  and closing all accounts to fully recover) directly illustrated the urgency-based
  social engineering tactics covered in class.
- The **Origin Energy breach**, confirmed just two days before this class, served as
  a live, real-time case study reinforcing the "notify customers immediately" and
  reputational-damage lessons.
- Practical hands-on setup (GoPhish) reinforced theoretical phishing concepts by
  showing how simulated phishing campaigns are actually built and tested by
  security professionals/organisations for staff awareness training.
