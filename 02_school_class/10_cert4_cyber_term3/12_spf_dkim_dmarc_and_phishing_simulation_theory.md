# SPF, DKIM, DMARC & Phishing Simulation Theory

**Date:** 2026-09-03
**Context:** VU23220 - Develop a Cyber Security Industry Project (Session covering email authentication mitigations + group breakout session troubleshooting our GoPhish campaign)

---

## 1. Email Authentication Mechanisms

### 1.1 SPF (Sender Policy Framework)

**What it does:** An email-authentication technique that prevents spammers from sending messages that appear to come from your domain.

**How it works:**
1. The sending organisation publishes an **SPF record** to their domain's DNS.
2. The SPF record lists which IP addresses / hostnames are authorised to send email on behalf of that domain.
3. When an email is sent, the receiving mail server performs an SPF lookup by querying DNS for the SPF record of the *sending domain* (specifically checks the `Return-Path` / envelope-from address, **not** the visible "From" header the user sees).
4. If the sending server's IP matches an authorised entry -> **Pass**. If not -> **Fail/Softfail**, and the message can be rejected or quarantined depending on policy.

**SPF record syntax example:**
```
v=spf1 ip4:192.168.100.11 -all
```
- `v=spf1` - version tag, always starts an SPF record.
- `ip4:192.168.100.11` - the IP authorised to send on behalf of the domain.
- `-all` - hard fail everything else not listed (strict mode). `~all` = softfail (more lenient).

**Real-world example (from a mail server's SPF processing log):**
```
Performing SPF lookup (company.com / 192.168.100.10)
Policy: v=spf1 mx ip4:[corpIP] include:mktomail.com ~all
Evaluating ip4:199.15.212.0/22: no match
Evaluating ip4:72.3.185.0/24: no match
...
```
Each IP range in the policy is checked one by one against the connecting IP; if nothing matches, the softfail (`~all`) applies and the message may be quarantined.

**Key limitation:** SPF only validates the *envelope sender* (bounce address), not the "From" header the recipient actually sees. Checking both improves phishing detection.

**Practical setup tip:** SPF is configured as a DNS TXT record at your domain registrar (e.g. GoDaddy) or DNS host. If using an on-prem mail server, include your server's IP. If using Office 365/Exchange Online, include Microsoft's authorised sending ranges.

---

### 1.2 DKIM (DomainKeys Identified Mail)

**What it does:** A different type of email authentication that verifies a message was **not altered in transit** and was genuinely sent/signed by the claimed domain (message integrity + origin authenticity), rather than just checking the sending server's identity like SPF does.

**How it works (5 steps):**
1. **Publish DKIM public key to DNS** - the sending organisation generates a public/private key pair and publishes the *public* key to their DNS as a TXT record (under a "selector", e.g. `default._domainkey.example.com`).
2. **Hashing body & headers** - when sending, the Mail Transfer Agent (MTA) takes the email body + selected headers and creates a hash (a fixed-length "fingerprint" of the content).
3. **Private key / crypto signature** - the MTA signs that hash using its **private key**, producing the `DKIM-Signature` header attached to the outgoing email.
4. **Recipient hashes** - on receipt, the recipient's mail server independently re-computes the same hash from the email body/headers it received.
5. **Recipient gets public key & compares** - the recipient looks up the sender's **public key** from DNS, uses it to decrypt/verify the signature, and compares the result to its own freshly-computed hash. If they match -> the message is authentic and unaltered.

**Public key vs private key relationship:** They are mathematically linked (generated together via a cryptographic algorithm, "like brothers - one can't exist without the other"). Private key signs -> only the matching public key can verify that signature. The public key is, by design, freely available to anyone (published in DNS); it cannot be used to derive the private key (this is what makes it secure - reversing it is computationally infeasible).

**Limitations:**
- DKIM does **not** encrypt email content - it only verifies integrity/authenticity.
- A spammer can still set up valid DKIM on their *own* domain - DKIM proves the email came from that domain, it doesn't prove that domain isn't malicious.

**Real-world analogy used in class:** SSL/TLS certificates on websites work the same way - a Certificate Authority (CA) is the trusted third party vouching that a public key belongs to a given domain, similar to how a government ID is trusted because a third party (government) issued it.

---

### 1.3 DMARC (Domain-based Message Authentication, Reporting & Conformance)

**What it does:** DMARC ties SPF and DKIM together. It lets a domain owner publish a policy telling receiving mail servers what to do with messages that claim to be from their domain but fail SPF and/or DKIM alignment - and it provides reporting so domain owners can monitor abuse of their domain.

**How it works:**
1. The organisation publishes a **DMARC record** to DNS.
2. When mail arrives, the receiving server checks SPF alignment, then checks DKIM (verifies public/private key match), then consults the domain's DMARC record to decide what to do with messages that failed either check.
3. Based on the domain's declared policy, the message is either delivered, quarantined, or rejected. Aggregate/forensic reports are also sent back to the domain owner.

**DMARC record syntax example:**
```
v=DMARC1; p=reject; pct=100; rua=mailto:postmaster@dmarcdomain.com; ruf=mailto:postmaster@example.com
```

| Tag | Purpose |
|---|---|
| `v` | Protocol version (always `DMARC1`) |
| `p` | Policy for the organisational domain: `none` / `quarantine` / `reject` |
| `sp` | Policy for subdomains |
| `pct` | Percentage of messages subjected to the policy/filtering |
| `adkim` | DKIM alignment mode (`s` = strict, `r` = relaxed) |
| `aspf` | SPF alignment mode |
| `rua` | Mailto address for **aggregate** reports (periodic summary of pass/fail stats) |
| `ruf` | Mailto address for **forensic** reports (details on individual failed messages) |

**Types of DMARC Policy:**
- **Monitor (`p=none`):** No effect on delivery. Just sends reports so you can see who's sending mail claiming to be from your domain. Good first step when rolling out DMARC.
- **Quarantine (`p=quarantine`):** Failing messages go to spam/junk; passing messages go to the primary inbox.
- **Reject (`p=reject`):** Failing messages are not delivered at all.

**Recommended rollout approach:** Start with `p=none` to monitor/collect reports -> once confident nothing legitimate is being blocked, escalate to `quarantine` -> then `reject`.

**Real-world example (DMARC aggregate report table, simplified):**

| Source IP | Count | Disposition | DKIM | SPF | Header.From | Result |
|---|---|---|---|---|---|---|
| (various) | 1 | none | fail | fail | altn.com | fail |
| (various) | 16 | none | pass | pass | altn.com | pass |
| (various) | 1 | quarantine | fail | fail | altn.com | fail |

This shows how a domain owner can see, per sending source, how many messages passed/failed and what action was actually taken.

---

### 1.4 SPF vs DKIM vs DMARC - Quick Comparison

| | SPF | DKIM | DMARC |
|---|---|---|---|
| Verifies | Which servers/IPs may send on behalf of the domain | Message wasn't altered + genuinely signed by the domain | Ties SPF + DKIM together, sets enforcement policy, and provides reporting |
| Checks | Envelope-from / Return-Path | Digital signature (hash + public/private key) | Alignment of SPF & DKIM results with the visible "From" domain |
| Weakness alone | Doesn't check the visible From header a user sees | Doesn't stop a spammer using a legitimately-DKIM-signed domain they own | Depends on SPF/DKIM being configured correctly underneath it |

---

## 2. Phishing Simulation Program Theory

### 2.1 Purpose of Phishing Simulations
Designed to teach the recipient to:
- **Identify** phishing communications.
- **Report** phishing attempts (direct reporting is considered the most important outcome).

> **Important ethical principle:** *"It is not the goal to embarrass or single out workers, but to educate these employees to tighten up the attack surface of the organisation."* Results should never be used to shame or call out specific individuals - findings should be reported in aggregate.

Secondary purposes:
- Quality control / measuring an organisation's overall security posture.
- Verifying whether staff have been sufficiently educated to recognise a phishing attempt.

### 2.2 Common Themes of Campaigns
- **Financial Services:** invoice payments, app store purchases.
- **Personal Social Media:** retail/shopping, delivery of packages.
- **Office communications:** files from scanner/cloud service/fax, internal social media notifications.
- **Technology based communications:** authentication-related (login, password reset, account access alerts).

### 2.3 Signs of a Phishing Email - Sophistication Ratings

| Rating | Characteristics |
|---|---|
| **Low** | Misspelled words, poor grammar, link unrelated to stated purpose, generic/duplicate content sent to multiple recipients, common links reused for unrelated purposes. |
| **Medium** | Some visual clues (grammar/spelling/graphics), plausible work context, specific & appropriate recipients, links/graphics that look correct without verification. |
| **High** | Perfect and visually appropriate email/subject/recipients/context, correct branding (colour scheme, logo, layout, footer), obfuscated link destinations, invokes strong emotional response to hinder detection, may use double-barrel or Business Email Compromise (BEC) techniques. |

### 2.4 Who to Notify Before the Campaign
Identify required stakeholders first:
- CISO / CIO
- Threat Management Team (e.g. an internal Incident Response / Threat Detection team)
- Legal representative (if applicable)

Provide them with:
- A copy of the email that will be sent (PDF/image).
- A copy of the education/landing page recipients will see.
- Brief details: From name & email, subject line, dates the simulation runs, and guidance on how staff should be told to respond if asked "is this a phishing test?"
- Schedule of the campaign timing.

### 2.5 Analyse Results (Post-Campaign)
After the campaign concludes, key metrics to collect:
- Number of employees susceptible (clicked link / entered details / opened attachment) **and did NOT report**.
- Number of employees susceptible **and DID report**.
- Number of employees who did NOT open/click and did NOT report.
- Number of employees who did NOT click and DID report (ideal outcome).
- Total number of emails sent.

Present as a table or visual chart (bar/pie chart etc.).

### 2.6 Potential Risk Analysis Template

| Risk | Likelihood | Impact | Risk Rating | Priority | Recommendations |
|---|---|---|---|---|---|
| Employees not able to identify phishing emails | Almost Certain | Moderate | Extreme | 1 | Implement a phishing simulation education program; implement stronger email blocking controls |
| No capability for employees to easily report phishing emails | Almost Certain | Moderate | Extreme | 1 | Implement a one-click reporting tool (e.g. KnowBe4); scale incident management team for increased reports |
| High-profile employees targeted for social engineering | Likely | Moderate | High | 2 | Identify key targets and profile; develop targeted monitoring/education for high-profile targets |
| Employees unaware of their role/responsibility | Possible | Minor | Moderate | 3 | Develop a compliance training module for employees |

> Tip for report writing: assume the report may be read by non-technical stakeholders (CEO, board, HR, legal) - avoid heavy jargon, or explain technical terms simply.

### 2.7 Best Practice
- Target employees with simulations **at least monthly** (though in practice this may be excessive for smaller teams - quarterly is a reasonable alternative).
- Plan simulation content **at least 3 months ahead** for large organisations (to allow time to whitelist links/domains etc.).
- Spread email delivery randomly over the course of a month rather than sending all at once.
- Create a **baseline** (easy/medium/hard) to determine where the organisation currently sits in terms of detecting phishing.
- Re-run similar difficulty levels later to confirm improvement in detection and reporting.
- **Reinforcement:** education is required *outside* the simulation process too - e.g. develop a phishing knowledge pack the incident response team can send to victims after the fact.

### 2.8 Common Baiting Tactics
- Notification from a help desk/system administrator (e.g. "mailbox storage limit reached").
- Advertisement for weight loss/hair growth/fitness (malware/virus delivery vector).
- Attachment labelled "invoice" or "shipping order" (often ransomware).
- Notification from a credit card company about an "unauthorised transaction" (credential harvesting).
- Fake account on a social media site mimicking a legitimate person/business (quiz/survey data harvesting).

### 2.9 Protect Yourself: Refuse the Bait
**STOP. THINK. CONNECT.**
- Before you click, look for common baiting tactics.
- If the message looks suspicious or too good to be true, treat it as such.
- Install and maintain antivirus software on all devices.
- Use email filters to reduce spam and malicious traffic.

---

## 3. Group Session: GoPhish Campaign Walkthrough (Mitchell's VM)

**Context:** During today's breakout session, the team walked Mitchell through the step-by-step GoPhish + MailHog guide (built earlier in the week) on his own VM, sharing his screen so the whole team could follow along and troubleshoot together in real time.

### 3.1 Issue Encountered: HTML Escaping in GoPhish Email Template Editor

**Symptom:** After copying the HTML email template code and pasting it into GoPhish's CKEditor-based Email Template field, clicking "Source" to preview showed the raw escaped code (e.g. `&lt;div style="..."&gt;`) instead of a rendered email.

**Root cause:** The HTML code was pasted directly into the rich text (WYSIWYG) editing mode **without clicking "Source" first**. CKEditor treated the pasted content as plain text and automatically escaped the HTML special characters (`<`, `>`, `&`) to prevent it being interpreted as markup.

**Fix:** Clear the content, click the **Source** button first to switch into source-code editing mode, then paste the same HTML code. This time the content is inserted as raw HTML rather than plain text. Clicking Source again then correctly previews the rendered email (EzyTech logo, styled button, formatted text all displaying properly).

**Takeaway for future GoPhish use:** Always click **Source** *before* pasting HTML into the Email Template or Landing Page editor - never paste directly into the default rich text view.

This has been documented as **Test Case #2** in Section 5.4 Verification of our AT2 report.

### 3.2 Outcome
By the end of the session, all team members had:
- Created their own GoPhish campaign using the shared step-by-step guide.
- Verified the landing page rendered correctly.
- Confirmed all 30 target emails were received in MailHog.
- Reviewed campaign statistics in the GoPhish dashboard.

---

## Key Terms Glossary
- **MTA (Mail Transfer Agent):** Software responsible for sending/receiving/routing email between servers.
- **Envelope sender / Return-Path:** The technical "bounce" address used internally between mail servers, distinct from the "From" address a user sees.
- **Hash:** A fixed-length fingerprint generated from data; even a tiny change in the input produces a completely different hash, making it useful for verifying data integrity.
- **Public/Private key pair:** Two mathematically linked cryptographic keys; data signed/encrypted with one can only be verified/decrypted with the other. The private key is kept secret; the public key can be shared freely.
- **WYSIWYG editor:** "What You See Is What You Get" - a rich text editor that shows formatted content as it will appear, as opposed to raw source code.
