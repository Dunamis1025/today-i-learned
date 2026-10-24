# NovaStyle Brute Force Scenario Brief & Group Coordination Workflow

> **Unit:** VU23219 Manage the security infrastructure for an organisation / VU23221 Evaluate and test an incident response plan
> **Type:** Group assignment coordination notes — Section 5.1 (Steps 1–5), CIRP exercise on fictional company "NovaStyle"
> **Date:** 24 Oct 2026

---

## 1. Context

Our group's assignment (Section 5.1 of the CIRP template) requires each member to independently write one step of the incident response lifecycle (Step 1: Detection, Step 2: Containment/Eradication, Step 4: Recovery, Step 5: Lessons Learned) for a fictional incident at "NovaStyle." Per **Section 1.2**, our group's assigned incident type is fixed as **brute force attack**, independent of whatever attack type the school's own "Simulation Week" exercise demonstrates — each group in the class picked a different scenario (brute force, DDoS, SQL injection, etc.), so our only constraint is internal consistency across our own four steps.

**Problem identified:** if each member invents their own details for timeline, affected systems, and detection method, the four independently-written steps won't logically connect when merged (e.g. Step 2's containment actions wouldn't match Step 1's detection trigger). This is a coordination/documentation-consistency problem common to any group-authored incident response exercise, not just this assignment.

**Solution:** write a single shared "scenario skeleton" — a short reference document establishing one timeline and one set of facts — *before* anyone starts drafting their individual step, so all four steps reference the same underlying incident.

---

## 2. The Scenario Brief (content)

**NovaStyle Brute Force Attack — Scenario Brief**

### Timeline
- **Day 0, 02:14am** — Automated script begins repeated login attempts against the NovaStyle admin login page (`/admin/login`), cycling through common username/password combinations.
- **Day 0, 02:40am** — Attempts shift target to several customer accounts on the main storefront login.
- **Day 0, 06:10am** — IT Security Lead reviews overnight authentication logs (routine morning check) and notices an unusually high number of failed logins from a single IP range, concentrated on the admin login page.
- **Day 0, 06:25am** — One admin account shows a successful login after ~400 failed attempts — event escalates to incident.

### Scope
- **Systems affected:** NovaStyle e-commerce platform (admin login + customer storefront login)
- **Accounts affected:** 1 admin account compromised; ~15 customer accounts targeted but not breached

### Detection trigger (→ feeds Step 1)
- Authentication logs show repeated failed logins from a narrow IP range, followed by one success
- No MFA was enabled on the admin account (key finding carried through to Step 5)

### Containment / eradication actions (→ feeds Step 2)
- Lock compromised admin account, force password reset
- Block/rate-limit offending IP range at the firewall/WAF
- Preserve authentication logs as evidence

### Recovery actions (→ feeds Step 4)
- Reissue admin credentials, enable MFA before reactivating account
- Monitor login logs for 72 hours post-incident
- Confirm no unauthorised changes were made during the compromised window

### Lessons learned prompts (→ feeds Step 5)
- No MFA on privileged accounts
- No account lockout threshold on admin login page

Each section is explicitly labelled with which assignment Step it feeds, so whoever is writing that step has a ready-made factual anchor rather than having to invent scope/timeline details themselves.

---

## 3. Coordination workflow used

1. **Drafted the brief as a shared skeleton, explicitly framed as editable.** The brief was introduced with language making clear it's a first-draft starting point, not a locked decision — inviting pushback/edits rather than presenting it as final, since the person who writes it first can otherwise end up unintentionally dictating the rest of the group's work.
2. **Explained the *why*, not just the *what*, when sharing it.** Rather than just posting the brief, the message explained the underlying reasoning: if everyone works from the same facts upfront, the four independently-written steps will naturally line up into one consistent story when merged later, instead of each person filling gaps differently and the group having to reconcile contradictions afterward (e.g. Step 2 listing a containment action for a vulnerability Step 1 never mentioned detecting).
3. **Posted to the team channel (Discord) in English**, matching the language the group already communicates in, even though the member drafting it is a native Korean speaker — translating a shared reference document into another language for the team would have added friction/confusion rather than clarity, since the deliverable itself (the written CIRP steps) needs to be in English anyway.
4. **Restructured the Discord message for readability.** Initial draft was one long unbroken paragraph-plus-list; revised to: a short framing message + the structured brief content below it, so a busy reader can skim rather than being faced with a wall of text.
5. **Also published the brief as a standalone file (not just a chat message).** Chat messages scroll away and are easy to lose track of; a separate file lets any member reopen it anytime mid-task to check how the scenario flows, without having to scroll back through Discord history.
   - Built as a `.docx` (via the `docx` npm library), verified visually by rendering to PDF/JPEG before sharing.
   - Uploaded to the group's shared Google Drive folder, where another member (Mike) had already independently added it under a cleaner filename (`Skeleton Scenario - NovaStyle Brute Force Attack.docx`) — the earlier duplicate created directly in personal Drive (not the shared folder) was deleted once the shared-folder copy was confirmed as the canonical version, to avoid two conflicting "latest" files.
6. **Identified a permissions gap in Discord:** the "Pin Message" option didn't appear in the right-click context menu for the message containing the timeline. This is because pinning requires the **"Manage Messages"** permission in Discord, which this account's role in the class server doesn't have — only the server owner (Mike) can pin messages here. Resolution: ask Mike directly to pin the timeline message so it stays easily discoverable at the top of the channel rather than getting buried.

---

## 4. Key takeaways

1. **Shared source-of-truth documents prevent downstream merge conflicts in collaborative writing**, the same way a shared schema or interface contract prevents integration bugs in collaborative coding — the earlier the group agrees on shared facts, the less rework later.
2. **Framing a first draft as "editable, not final" matters for group buy-in.** Whoever writes the shared reference document first has outsized influence on the group's direction by default; explicitly inviting revisions keeps the document a group artifact instead of one person's unilateral decision.
3. **Explaining *why* a process exists (not just announcing the process) improves compliance.** A plain instruction ("use this timeline") is more likely to be skipped or misapplied than one paired with the reasoning for why consistency matters.
4. **Match communication artifacts to the team's actual working language**, even when a translation might be more comfortable for the individual drafting it — introducing a second language into shared team documentation can create confusion rather than remove it.
5. **Long chat messages have a half-life.** For anything a team will need to reference repeatedly over multiple days, a persistent file (and ideally a pinned reference point) beats a chat message, which inevitably scrolls out of view.
6. **Platform permission models (e.g. Discord's "Manage Messages" permission) can silently block expected UI actions** — when a menu option is simply missing rather than greyed out, the likely cause is a role/permission gap, not a bug.
