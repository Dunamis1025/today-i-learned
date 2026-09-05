# VU23222 — Communicating Security Findings to a Non-Technical Audience
### From Technical Exploitation to Executive Reporting & Presentation

This session focused not on finding new vulnerabilities, but on **translating already-discovered technical findings into a report and presentation suitable for a non-technical business audience** (e.g. a company owner/client) — a core real-world skill for any security professional.

---

## 1. Mini Report — "Report Web Application Vulnerabilities" (Activity, pre-submission to main Assessment)

Completed a separate, shorter Brightspace activity that summarises three vulnerabilities (SQL Injection, Broken Authentication, IDOR) in a formal, business-appropriate report format, ahead of pasting the same approved content into the final Assessment Task 2 submission.

**Report structure:**
- **Executive Summary** — 3–5 non-technical sentences per vulnerability, written in formal (not conversational) English, explaining what was found and why it matters, without jargon.
- **Scope & Test Environment** — target, tools, and lab authorisation statement.
- **Technical Issues & Risk Assignment table** — Title / Risk / Reproduction Steps / Remediation Steps for each vulnerability, using numbered steps and paragraph breaks for readability.
- **Presentation and Sign-off** — formal declaration that findings were presented to the "client" (assessor).

**Key writing lesson learned:** the difference between **spoken/casual English** (used for rehearsing or explaining verbally) and **formal written English** (used in the report) — e.g. removing filler words ("so", "I mean"), replacing first-person narrative ("I found") with passive/objective phrasing ("it was discovered"), and avoiding repeated articles/verbs that are natural in speech but incorrect in writing.

**Concepts clarified during report writing (in plain terms, for non-technical readers):**
- **Parameterised query / prepared statement**: comparable to a fixed hospital intake form — the structure is locked, and user input only fills in blank fields, so it can never alter the form (or SQL statement) itself.
- **Server-side vs client-side validation**: client-side (browser) checks can be bypassed entirely by sending requests directly to the server; only server-side validation is a real security control.
- **Escaping**: marking special characters (e.g. an apostrophe in "O'Brien") so they are treated as literal text rather than being misinterpreted as command syntax.
- **ORM framework**: lets developers avoid writing raw SQL by hand, automatically applying parameterisation/escaping and reducing injection risk.
- **Token (JWT)**: functions like a temporary access keycard issued after login — no need to re-enter credentials, but if it stores sensitive data insecurely (e.g. a password hash), stealing the token can expose that data too.
- **Salted, slow hash algorithms (bcrypt/Argon2)**: deliberately slow down each password check (e.g. 0.1s → 0.3s) — negligible for one legitimate login, but a massive cumulative delay for an attacker trying thousands of password guesses, making brute-force attacks impractical.
- **UUID vs sequential ID**: comparable to replacing simple, predictable hotel room numbers (1, 2, 3...) with long, random, unguessable codes — prevents an attacker from predicting another user's resource identifier.

---

## 2. Executive Presentation — Slide Deck for a Non-Technical Stakeholder

Built a full presentation (using Gamma AI + a custom-designed opening slide) reporting the same three vulnerabilities to an audience assumed to have **no technical background** (the assessor role-playing as a company owner/client).

### Key structural decision: BLUF, not narrative storytelling
Initially considered a TED-Ed-style narrative/curiosity-driven structure, but deliberately rejected it in favour of **BLUF (Bottom Line Up Front)** — the standard structure used in executive/military/security briefings: state the critical risk first, then explain cause and fix, rather than building suspense. Rationale: a busy executive wants the headline risk immediately, not a "reveal" — a curiosity-driven structure risks frustrating a time-constrained audience ("why isn't this getting to the point?").

**Slide flow used:**
1. **Opening/Hook** — striking title slide ("Juice Shop: One Click Away From Being Hacked") with a bold visual, presenter name/ID, and subject code.
2. **Problem overview** — three-box summary of all three vulnerabilities in plain language, before naming them technically.
3. **Per-vulnerability sections (×3)** — each following the same rhythm:
   - Plain-language explanation of the flaw + real screenshot evidence
   - Demonstrated impact (what an attacker could actually do)
   - Real-world consequence analogy or case study (e.g. the 2022 Optus data breach, used as a cautionary real-world parallel — verified against primary sources rather than trusting an AI-generated fact uncritically)
   - Plain-language remediation, reinforced with a simple visual analogy (hospital form, keycard, hotel room numbers)
4. **Summary slide** — reused the three-vulnerability box layout from earlier (for audience recall), with severity ratings and a call to action for the development team.
5. **Closing slide** — "Thank you" + sources.

**Non-technical communication techniques applied:**
- Complex evidence screenshots (e.g. a raw JWT payload) were *not* shown in full — instead, the relevant field (e.g. `password`) was cropped, enlarged, and paired with a plain-language caption, while the full original screenshot was kept small as supporting evidence only.
- Verified that any real-world breach example cited (Optus) was fact-checked against a primary source (Wikipedia / news article) rather than taken at face value from an AI summary, to avoid presenting an unverified claim as fact to an audience.
- Iteratively translated every line of the Korean voice-over script into English, refining from conversational/spoken English into a natural presentation register (correcting article errors, verb-form mistakes like "automate" vs "automated", and run-on repeated words — common artefacts of composing English scripts in real time).

---

## 3. English Technical Writing — Recurring Grammar Patterns Corrected

Through iterative translation of the presentation script, the following recurring English patterns were identified and corrected:
- **automate (verb) vs automated (adjective)** — "an automated tool", not "the automate tool".
- **Articles with "every"** — never "the every"; just "every customer's account".
- **"affect" takes no preposition** — "affect the code", not "affect to the code".
- **"Because ~ so ~" is invalid in English** (unlike Korean) — use one connector only: "Because A, B" or "A, so B".
- **"whether ~" construction** for expressing "confirms whether X is true or not" — e.g. "checks whether the user is the real owner", cleaner than "checked the this account is logged in or not".
- **"as + adjective + as" comparison** — useful for analogies, e.g. "as easy as finding your own hotel room".
- **Proper nouns require capitalisation** — "Juice Shop", not "juice shop".

---

## 4. Submission Logistics

- Final submission package: mini-report (Word doc), presentation slide deck (PPTX), and a recorded video presentation (delivered via PowerPoint's built-in recording feature, after Webex's cloud-recording workflow proved difficult to locate/verify reliably in time).
- A Google Drive backup link was included in the submission comments as a fallback in case of file download issues — good practice for high-stakes submissions with large video files.

---

## Key Takeaway

Finding a vulnerability and *explaining why it matters to someone who doesn't code* are two different skills. This session's core lesson: technical accuracy must be preserved in the formal report, while the presentation layer requires translating that accuracy into plain analogies (forms, keycards, hotel rooms) — without ever letting the simplification introduce factual inaccuracy (e.g. still fact-checking the Optus breach example before using it).
