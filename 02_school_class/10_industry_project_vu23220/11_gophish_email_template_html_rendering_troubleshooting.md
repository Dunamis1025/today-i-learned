# GoPhish Email Template & Landing Page HTML Rendering Troubleshooting

## Context

While building out a phishing simulation campaign in GoPhish (SMTP delivery handled by MailHog, see `10_gophish_smtp_troubleshooting.md`), I ran into two separate issues while setting up the **Email Template** and **Landing Page** components. Both issues came from misunderstanding how GoPhish's editor and templating engine actually work under the hood. This doc captures the root causes, the fixes, and the underlying concepts so I don't repeat the same mistakes.

Stack involved: GoPhish (self-hosted), MailHog (local SMTP catcher), Ubuntu VM (VMware Workstation), Firefox.

---

## Background: How GoPhish templating works

GoPhish supports a small set of template variables that get substituted per-recipient at send time:

| Variable | Substituted with |
|---|---|
| `{{.FirstName}}` | Recipient's first name from the imported Users & Groups list |
| `{{.URL}}` | The unique phishing link for that recipient, pointing at the campaign's Landing Page (host/port taken from the campaign's URL field, plus a unique `rid` per recipient) |
| `{{.Tracker}}` | An invisible 1x1 tracking pixel `<img>` tag, used to record "Email Opened" events |

These are **not** literal HTML — they're placeholders GoPhish's Go template engine resolves at send time, per recipient.

A critical early mistake: I initially built an email template by taking a real, already-sent test email exported from MailHog and reusing its raw source as the "template." That source had already had the template variables *resolved* into a literal value, e.g.:

```html
<a href="http://127.0.0.1?rid=ZJi4CWP">Confirm My Details</a>
```

Reusing this as the template meant every future recipient's email pointed at the exact same hardcoded IP and rid, instead of getting their own dynamic `{{.URL}}`. This surfaced as a real bug for a teammate: when they ran the same campaign from their own VM, the link in the email still pointed at *my* VM's `127.0.0.1`, which (from their machine) resolved to nothing useful — appearing instead to redirect somewhere unrelated once combined with other environment differences.

**Fix:** replace all resolved values with their template tags before pasting into GoPhish:
- `http://127.0.0.1?rid=ZJi4CWP` → `{{.URL}}`
- `<img src="http://127.0.0.1/track?rid=ZJi4CWP" style="display:none">` → `{{.Tracker}}`
- Hardcoded recipient name → `{{.FirstName}}`

**Why this matters conceptually:** `127.0.0.1` (localhost) always resolves to "this machine," so it's correct and safe to hardcode in places where GoPhish is talking to itself (e.g. the Sending Profile's SMTP host, `127.0.0.1:1025` for MailHog). It's *not* safe to hardcode in content that gets sent externally and needs to reference "wherever this campaign's server actually is" — that has to stay a template variable so it resolves correctly regardless of which machine is running the campaign.

---

## Issue 1: Email Template renders as raw code instead of a formatted email

### Symptom
After pasting HTML into the GoPhish Email Template editor (a CKEditor-based rich text editor) and saving, opening the resulting email in MailHog showed the literal HTML source as plain text in the message body, instead of a rendered email with the logo, styled button, etc.

### Root cause
The HTML I pasted included a full document structure:

```html
<html>
<head>
	<title></title>
</head>
<body>
  <div>...actual email content...</div>
</body>
</html>
```

GoPhish's template editor expects only the **body content** — not a full HTML document. When a full `<html>/<head>/<body>` document is pasted into the CKEditor Source view and saved, the editor's underlying parser treats the outer structural tags as invalid/out-of-place content for what it expects to be a content fragment, and ends up storing them in an escaped form (i.e. `<` and `>` get converted to `&lt;` and `&gt;`) rather than as live markup. The result: when the email is later rendered, the browser/mail client displays literal tag text instead of interpreting it as HTML.

### Fix
Strip out `<html>`, `<head>`, `<title></title>`, `<body>`, and the closing `</body></html>` tags. Paste **only** the inner content, starting from the first real content element (in this case a `<div>`):

```html
<div style="font-family: Arial, Helvetica, sans-serif; max-width: 600px; ...">
  ...
</div>
<p>{{.Tracker}}</p>
```

### Verification step (now part of my standard workflow)
Before clicking Save on any Email Template or Landing Page:
1. Click the **Source** button in the CKEditor toolbar to toggle out of raw-source mode.
2. Confirm the editor now shows a **rendered preview** (logo, styled text, buttons) rather than visible tag text.
3. Only then save.

If raw code is still visible after toggling out of Source mode, the paste has gone wrong somewhere (usually: `<html>`/`<body>` tags left in, or pasted while not in Source mode in the first place, causing the rich text editor to mangle the markup on the way in).

---

## Issue 2: Landing Page had the same failure mode, for a different reason

### Symptom
Same visual result as Issue 1 (raw code shown instead of a rendered login form) — but this HTML file did **not** contain `<html>/<head>/<body>` tags. It was already just a content fragment: a `<div id="loginView">`, a `<div id="educationView">` (initially hidden), and a `<script>` block toggling between the two on form submit.

### Root cause
Since the tag-stripping fix from Issue 1 didn't apply here, the actual cause was simpler: the code had been pasted **before** switching the editor into Source mode. Pasting rich HTML directly into the WYSIWYG view (rather than the raw Source view) causes CKEditor to interpret and partially escape/mangle the markup during paste, rather than storing it as-is.

### Fix
Always click **Source** first, *then* paste the code into the now-visible raw text area, *then* toggle Source off again to confirm it renders correctly, before saving.

### General rule going forward
> **Click Source → Paste → Toggle Source off to preview → confirm it looks right → Save.**

This applies to both Email Templates and Landing Pages in GoPhish's editor, and is probably true of any CKEditor-based tool.

---

## Key concepts reinforced by this troubleshooting

1. **Template engines vs. literal strings** — a "template" should contain placeholders, not resolved output. Copying a resolved example instead of the source template is a classic trap when trying to reverse-engineer a format from an example.
2. **localhost (`127.0.0.1`) is host-relative, not a fixed address** — it always means "this machine," which makes it correct for machine-to-machine config on the same host (e.g. SMTP host in a Sending Profile) but incorrect for anything meant to be portable across machines/recipients (e.g. a link inside an email body).
3. **Tracking pixels** — `{{.Tracker}}` works by embedding an invisible 1x1 image whose URL points back at the GoPhish server. When a recipient's mail client renders the email and fetches that image, the request itself (independent of the image being visible) is what GoPhish logs as an "opened" event.
4. **Rich text editors (CKEditor) are not neutral pass-throughs for HTML** — pasting HTML directly into the visual (WYSIWYG) editing surface is not equivalent to pasting it into the raw source view. The editor will sanitize/escape/restructure markup differently depending on which mode it's pasted into, and a full document (`<html>...</html>`) is treated differently from a fragment.
5. **Always verify visually before trusting a save** — the fastest way to catch a broken template is to toggle the Source view off immediately after pasting, before saving, and eyeball whether it looks like a real page or a wall of tags.

---

## Quick reference: correct paste procedure for GoPhish Email Templates / Landing Pages

1. Open the template/page editor, go to the **HTML** tab.
2. Click **Source** to enter raw HTML mode.
3. Paste HTML **content only** (no `<html>`, `<head>`, `<body>` wrapper tags).
4. Click **Source** again to preview the rendered result.
5. Confirm it visually matches the intended design.
6. Save.
