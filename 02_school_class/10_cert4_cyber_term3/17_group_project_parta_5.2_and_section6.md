# Industry Project (VU23220 / ICTICT443) — Group Project Part A: Section 5.2 & Section 6

**Date:** 17 September 2026
**Context:** Thursday afternoon class group session (SPDA team). Worked on the Google Docs group report (Part A) — completed Section 5.2 and Section 6, and created three staff-training visual assets.

---

## 1. Session overview

Today's class ran straight into a group work session. Since a Webex breakout room wasn't set up in time, the team coordinated over our Discord channel instead. The focus was on filling in the empty sections of the Part A group report and dividing up remaining work.

**Task allocation agreed today:**

| Section | Owner |
|---|---|
| 3.1 WBS diagram | Mike (MS Project lead) |
| 3.5 Risk management plan | Evan |
| 5.2 Phishing campaign development process | **Me (completed today)** |
| 5.3 Landing / educational page | Mitchell (checking status) |
| 6. Phishing Awareness Training Program | **Me (completed today)** |
| 7. Project completion / handover | Team (final stage) |

Note: 3.4 Project scheduling screenshots were already done by Mike (original + reworked schedule after Andrei joined).

---

## 2. Section 5.2 — Phishing campaign development process

This section documents **how the phishing email campaign was built and which tools were used**. Key points I wrote up from my own understanding:

### Tools used
- **GoPhish** — the open-source phishing framework used to build the email template, landing page, and sending profile, and to launch/track the campaign.
- **MailHog** — a **local SMTP server**. Its role is to intercept emails GoPhish sends and keep them inside the virtual machine (VM) instead of letting them reach real inboxes. This lets us test sending/receiving safely in a sandbox, with no real users affected.
- **Shared VM (hosted by Mitchell)** — ran the whole GoPhish + MailHog environment; shared with the team via WebEx screen share.
- **WebEx** — real-time screen sharing so the team could work and troubleshoot together.
- **Google Docs / Google Drive** — shared source code, setup instructions, and Evan's target list; Mitchell downloaded these into his VM.

### Development stages
1. **Planning & target preparation** — defined the scenario (impersonating EzyTech HR with a "payroll update" email). Evan built a list of 30 fictional employees, imported into GoPhish's Users & Groups.
2. **Building components (done in parallel)** — while Evan built the email list, I built the email template, and Mitchell set up hosting.
   - Email template made in GoPhish's editor.
   - `{{.FirstName}}` tag → auto-personalises each email with the recipient's name (pulled from the target list).
   - `{{.URL}}` tag → inserts a **unique tracking link per recipient**, so GoPhish can record which specific user clicked.
   - Landing page = a fake login page shown when the user clicks the email link/button. On submit, JavaScript redirects to an educational page ("You've been phished" + awareness content). In a real campaign, submitted credentials are visible in the GoPhish dashboard.
3. **Testing & verification** — ran the campaign, checked transmission status of all 30 targets in the dashboard, verified arrival in MailHog, opened emails, clicked through to confirm the fake login → educational page flow worked end to end.

### Concepts I clarified today
- **Local SMTP server**: SMTP is the protocol for sending email. Normally a real mail server (e.g. Gmail) sends mail out to the internet. MailHog acts as a "fake post office" that catches the mail inside the VM. "Local" = only within this machine/VM. This is what keeps the test safe.
- **Parallel vs sequential work**: Sequential = one task finishes before the next starts (A→B→C). Parallel = tasks run at the same time. Our team worked in parallel (Evan on the list, me on the template, Mitchell on hosting — no one waiting on another).
- **`{{.FirstName}}` and `{{.URL}}`**: FirstName is replaced with each recipient's real name for personalisation; URL is replaced with a unique per-user tracking link so click-through can be tracked individually.
- **HTML rendering issue (documented in 5.4)**: pasting HTML into GoPhish's editor showed raw code instead of a rendered preview. Fixed by removing the header/footer portions and inserting only the body HTML in Source mode.

---

## 3. Section 6 — Phishing Awareness Training Program

An outline of the training program run after the simulated campaign, following the template (Goal / Background / Target Audience / Program components / Resources / Schedule / References).

### Key content
- **Goal**: help EzyTech staff recognise, avoid, and report phishing; build a security-aware culture. Aim to cut click-through rates and reach ≥80% reporting rate in future campaigns (consistent with the 2.3 objective).
- **Background**: the mock campaign on 30 staff showed vulnerability to **social engineering** — especially emails impersonating an internal department (our "payroll update" scenario). Framed as education, **not punishment**.
- **Target audience**: all EzyTech staff, with focus on those who clicked the link or entered credentials; accessible to non-technical staff too.
- **Program components**:
  - *Interactive Training* — modules on checking sender addresses, hovering over links before clicking, spotting urgency-based manipulation; each ends with a short quiz.
  - *Visual Aids* — posters and infographics of common phishing signs, displayed around the office and on the intranet.
  - *Simulated Phishing Campaigns* — periodic tests (like our GoPhish campaign) to measure improvement; anyone caught is directed to an educational page.
- **Resources**: GoPhish platform, the educational landing page from this project, training materials (slides/posters/infographics), completion deadlines, a designated training manager.
- **Schedule**: debrief + interactive training within 2 weeks of a campaign; refresher every 6 months; simulated campaign every quarter; results shared with management.
- **References**: ACSC phishing guidance (cyber.gov.au), GoPhish docs (docs.getgophish.com).

### Concepts I clarified today
- **Social engineering**: an attack that exploits human psychology (trust, urgency, authority) to extract information, rather than a purely technical exploit.
- **Debriefing**: a session held *after* an activity to review what happened and what was learned — here, sharing campaign results and lessons with staff after a simulation.
- **Infographic**: information presented visually (icons, diagrams) so key points can be understood at a glance, as opposed to long paragraphs of text.

---

## 4. Staff training visual assets created

Created three visual assets (via AI image generation, with content/structure I designed) to support Section 6's Visual Aids and the Part C presentation. All three carry both the SPDA (our consulting team) and EzyTech (client) branding, reflecting that SPDA produced them for the client.

1. **Poster — "STOP. THINK. REPORT."**
   - For display around the EzyTech office.
   - Summarises 5 quick checks before clicking (sender address, hover over links, urgent language, never share credentials, report to IT).

2. **Infographic — "SPOT. STOP. PHISHING."**
   - For the EzyTech intranet.
   - Explains what phishing is, common warning signs, and the 5 checks **with real examples** (e.g. lookalike domain `ezytech.com` vs `ezy-tech.com`, a fake "Urgent: Account will be suspended" email).

3. **Process flow — "From Phishing to Protection"**
   - Shows the 8-stage employee training journey: receive simulated phishing email → click link / enter details → enrolled in training → complete training → take quiz → get results → completion → stay alert & help others.
   - Chosen over a standalone quiz screen because showing the whole process is more informative and ties directly to our actual campaign flow (payroll phishing email → fake login → educational page).

**Design principle followed:** I decided the content, wording, and structure of each asset; AI was used only to visualise it — consistent with the assessment's "AI Guided Use" rule.

### Placement in the report
- Process flow → top of Section 6 (overview of how the program works).
- Poster → under *Visual Aids* (office display).
- Infographic → under *Visual Aids* (intranet).
- Each image gets a Figure number + caption, matching the convention used in the Part B pen-testing report.

---

## 5. Team / coordination notes
- **Andrei**: still not participating (missed sessions, no contribution to the shared doc). Raised the idea of flagging this to the trainer (Eddie) and updating his role in the doc — to be handled after Eddie's guidance. His originally-assigned "Presentation & QA" role in the doc will likely need revising.
- **Presentation (Part C) plan discussed**: Part A group presentation 15–20 min, everyone presents their own part (~3–4 min each), each member records and submits individually. To be tackled *after* the group doc is finished.

---

## 6. Key takeaways
- Understood **why** each GoPhish tag and tool is used, not just how to click through — able to explain the campaign flow in my own words now.
- Learned the meaning of local SMTP server, parallel vs sequential work, social engineering, debriefing, and infographic in context.
- Practised turning my own understanding into report-ready documentation, then supporting it with self-designed visual assets.
