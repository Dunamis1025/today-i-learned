# GoPhish & MailHog Phishing Simulation Setup — VU23220 Industry Project

**Unit:** ICTICT443 / VU23220 — Work Collaboratively in the ICT Industry / Develop and Carry Out a Cyber Security Industry Project
**Context:** AT2 Cyber Security Group Project — Team SPDA (Thursday Afternoon)
**Date:** 20 August 2026

## Overview

This session covered setting up a full phishing simulation pipeline using **GoPhish** (campaign management) and **MailHog** (local SMTP mail catcher) on an Ubuntu VM (VMware Workstation), and building a custom landing page with credential capture and an educational redirect.

---

## 1. Environment Setup

### Tools used
- **GoPhish** (`v0.12.1-linux-64bit`) — open-source phishing framework for creating and tracking simulated phishing campaigns
- **MailHog** — a local fake SMTP server + web UI that catches outgoing test emails without sending them externally
- **VMware Workstation** — Ubuntu VM as the isolated lab environment

### Running the services
```bash
cd ~/gophish
sudo ./gophish
```
- Admin dashboard: `https://127.0.0.1:3333`
- Phishing server (serves landing pages/emails to "victims"): `http://0.0.0.0:80`

```bash
cd ~/Downloads   # or wherever MailHog binary was placed
sudo ./MailHog
```
- SMTP listener: `0.0.0.0:1025`
- Web dashboard: `http://0.0.0.0:8025`

### Verifying services are running
```bash
netstat -putln
```
Confirmed both `127.0.0.1:3333` (GoPhish) and `:8025` / `:1025` (MailHog) were in `LISTEN` state before proceeding.

---

## 2. GoPhish Campaign Components

A GoPhish campaign requires four components to be configured before it can launch:

| Component | Purpose |
|---|---|
| **Sending Profile** | SMTP config GoPhish uses to send the phishing emails |
| **Email Template** | The phishing email content sent to targets |
| **Landing Page** | The page a target sees after clicking the email link |
| **Users & Groups** | The target list (name/email/position) |

### 2.1 Sending Profile
- Name: arbitrary (e.g. `MailHog Test`)
- **Host: `127.0.0.1:1025`** ← critical field, must point at MailHog's SMTP port
- From: any address (e.g. `payroll@ezytech.com`)
- Username/Password: left blank (MailHog doesn't require auth)
- Ignore Certificate Errors: checked (local self-signed setup)

**Common failure point:** a typo in the Host field (e.g. `1-7.001:1025` instead of `127.0.0.1:1025`, or leaving it as `0.0.0.0` instead of the loopback address) causes every target's campaign status to show **"Error"** instead of "Sent". Always double-check this field character-by-character after saving.

### 2.2 Email Template
- Subject example: *"Action Required: Confirm Your Bank Details for Payroll Update"*
- Envelope Sender: `payroll@ezytech.com`
- Body written in HTML, using GoPhish template variables:
  - `{{.FirstName}}` — personalizes the greeting per target
  - `{{.URL}}` — GoPhish auto-generates a unique tracking link per recipient; this is what links the email to the landing page and enables click tracking
- Demonstrates classic phishing psychology: urgency ("payment may be delayed"), impersonation of an internal team (HR/Payroll), a plausible pretext (system upgrade requiring re-confirmation of bank details)
- "Add Tracking Image" left enabled (adds an invisible pixel used to detect email opens)

### 2.3 Landing Page (custom-built)
Built a landing page in two stages:

**Stage 1 — static "You've Been Phished" page**
A simple educational message shown after the click, explaining:
- This was a simulated phishing exercise
- What red flags should have been noticed (sender address, urgency language, hovering over links, unsolicited credential requests)

**Stage 2 — combined login form + auto-redirect (final version)**
Combined a fake login form (Employee ID / Password) with the education page in a single HTML file:
- Form fields: `name="username"`, `name="password"` — required so GoPhish's data-capture engine recognizes and logs the submitted values
- On submit, JavaScript intercepts the form (`e.preventDefault()`), sends the data via `fetch()` as a normal POST to the same URL (so GoPhish still captures it exactly as a native form submission would), then swaps the visible content from the login view to the "You've Just Been Phished!" education view — no page navigation, so no separate "Redirect to" URL is needed
- GoPhish settings enabled: **Capture Submitted Data** and **Capture Passwords** (with the caveat that GoPhish stores captured credentials in **plaintext**, an important point for the project report on why this is risky in real deployments)

### 2.4 Users & Groups
- Group name: e.g. `EZYTech`
- Populated via **Bulk Import Users** using a CSV (columns: First Name, Last Name, Email, Position)
- 30 fictional targets used for the test campaign

---

## 3. Launching and Verifying the Campaign

### Launch sequence
1. Campaigns → New Campaign
2. Select Email Template, Landing Page, Sending Profile, Group
3. URL field: `http://127.0.0.1` (points at the local GoPhish phishing server)
4. Launch Date left as default (current time) — **do not manually edit the calendar widget unless intentionally scheduling for later**, as this can cause targets to sit in "Scheduled" state indefinitely
5. Click Launch Campaign → confirm

### Full pipeline verification (Results dashboard)
GoPhish tracks each target through five sequential stages:

| Stage | What it confirms |
|---|---|
| Email Sent | SMTP handoff to MailHog succeeded |
| Email Opened | Tracking pixel loaded (target opened the email) |
| Clicked Link | Target clicked the unique `{{.URL}}` link |
| Submitted Data | Target submitted the login form (credentials captured) |
| Email Reported | Target reported the email as phishing (not natively supported by GoPhish — requires a separate integration, e.g. a custom script or plugin) |

**End-to-end test performed:**
1. Opened MailHog Inbox (`127.0.0.1:8025`), confirmed all 30 emails arrived with the expected sender/subject
2. Opened one email, clicked the "Confirm My Details" link
3. Landing page loaded correctly (login form)
4. Submitted a dummy username/password
5. Page auto-transitioned to the "You've Just Been Phished!" education screen
6. Returned to the GoPhish campaign results page — confirmed the target's status progressed through Clicked Link → Submitted Data, and the dashboard counters (Email Opened / Clicked Link / Submitted Data) incremented accordingly
7. Expanded the target's row to view the **Timeline** — GoPhish logs a full audit trail per recipient (timestamp, OS, browser) for each Sent/Opened/Clicked/Submitted event, including a "Replay Credentials" option

---

## 4. Troubleshooting Log

| Symptom | Cause | Fix |
|---|---|---|
| VM has no internet / terminal unusable | VMware NAT/DHCP service conflict, often triggered by switching networks (e.g. home Wi-Fi ↔ school Wi-Fi) | Restart VMware's NAT and DHCP services (or reset via Virtual Network Editor → Restore Defaults / re-select VMnet8 and apply) |
| MailHog dashboard (`127.0.0.1:8025`) unreachable | MailHog process not running in that VM | Run `sudo ./MailHog` from the correct directory; confirm via `netstat -putln` that port 8025/1025 are LISTEN |
| Email Template HTML editor shows blank content | Toggling the "Source" button back and forth between rich-text and code view corrupted the rendering | Click "Source" once, paste the raw HTML, and avoid re-toggling before saving |
| All 30 campaign targets show status **"Error"** | Sending Profile's SMTP Host field had a typo (not exactly `127.0.0.1:1025`) | Corrected the Host field, then used GoPhish's **Copy Campaign** feature to quickly relaunch with identical settings instead of rebuilding from scratch |

---

## 5. Key Takeaways

- A phishing campaign's credibility depends on exploiting the "weakest link" in any security system — people — via urgency, impersonation, and pretexts that mimic normal business communication.
- GoPhish's `{{.URL}}` template variable is the mechanism that ties email → click tracking → landing page together per recipient; nothing works without it.
- Captured credentials in GoPhish are stored **unencrypted** — a deliberate teaching point about why real organizations must never build test tooling this way for production use.
- Debugging campaign delivery issues should follow a consistent order: (1) confirm GoPhish and MailHog processes are both running, (2) confirm the Sending Profile's SMTP host/port exactly matches MailHog's listener, (3) confirm the landing page and email template are correctly saved, (4) only then investigate network/VM-level issues.
- GoPhish does not natively track "Reported" phishing emails — this requires a custom/external solution, which is a known limitation to flag in the project report.

---

## Suggested next steps for the group project
- Document click/open/submission rates as part of the AT2 report deliverable
- Decide as a team whether to build a custom "Email Reported" tracking mechanism
- Finalize/standardize the Sending Profile and Landing Page across all team members' VMs so results are reproducible
