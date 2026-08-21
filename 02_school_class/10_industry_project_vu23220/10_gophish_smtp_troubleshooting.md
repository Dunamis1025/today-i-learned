# GoPhish + MailHog SMTP Delivery Troubleshooting

## Context

During Assessment Task 2 (Cyber Security Industry Project), our team ran a simulated
phishing campaign using GoPhish (campaign management) and MailHog (local fake SMTP
server) inside individual VMware Workstation VMs. While one team member's VM worked
correctly, replicating the same setup on a teammate's VM initially failed, with all
30 campaign targets returning an `Error` status instead of `Email Sent`.

This document summarizes the debugging process and the root cause, for reference in
future labs or by other team members setting up the same stack.

## Symptom

- Campaign launched in GoPhish (`Campaigns > [campaign name]`)
- All target rows in the results table (`Details`) showed a red **Error** status
- MailHog's inbox (`http://127.0.0.1:8025`) showed **0 messages received**, meaning
  GoPhish never successfully connected to the SMTP server at all

## Investigation Steps

1. **Ruled out scheduling issues.** Initially suspected the campaign's Launch Date
   had been accidentally changed. Confirmed campaigns showing `Scheduled` (not yet
   fired) are a separate, normal state — not an error. Once the scheduled time
   passed, targets flipped to `Error`, confirming the failure was in delivery, not
   timing.

2. **Checked the Sending Profile.** In GoPhish, a Sending Profile
   (`Sending Profiles` in the sidebar) defines the outbound SMTP connection GoPhish
   uses to relay mail — this is the most common point of failure for local test
   setups.

3. **Used "Send Test Email."** Every Sending Profile has a built-in test button.
   This isolates the SMTP connection from the rest of the campaign (templates,
   groups, landing pages) and is the fastest way to confirm whether the profile
   itself is broken, without re-running a full 30-target campaign each time.

4. **Found the actual misconfiguration.** The Host field was set to:

   ```
   0.0.0.0:1025
   ```

   instead of:

   ```
   127.0.0.1:1025
   ```

## Root Cause

`0.0.0.0` is a **bind address** — it's what a server (MailHog, in this case) uses to
say "listen on all available network interfaces." It is *not* a valid destination
address for a client to connect to. When GoPhish tried to open an SMTP connection to
`0.0.0.0:1025`, the connection failed silently from GoPhish's perspective, resulting
in the `Error` status for every target.

This is an easy mistake to make because MailHog's own startup log commonly prints:

```
[HTTP] Binding to address: 0.0.0.0:8025
[SMTP] Binding to address: 0.0.0.0:1025
```

Seeing `0.0.0.0` in MailHog's own log and copying it directly into GoPhish's Sending
Profile Host field is a natural but incorrect assumption — the log describes what
address MailHog *listens on*, not what address a client should *connect to*.
For a client (GoPhish) connecting to a server running on the **same machine**, the
correct destination is always `127.0.0.1` (localhost) or the machine's actual LAN IP
— never `0.0.0.0`.

## Fix

Changed the Sending Profile Host field from `0.0.0.0:1025` to `127.0.0.1:1025`,
saved the profile, and re-launched the campaign.

## Verification

| Check | Before fix | After fix |
|---|---|---|
| Campaign status (30 targets) | All `Error` | All `Email Sent` |
| MailHog inbox count | 0 messages | 31 messages received |
| Email subject visible in MailHog | N/A | "Payroll: Action Required: Confirm Your Bank Details for Payroll Update" |

## Key Takeaways

- **`0.0.0.0` vs `127.0.0.1`**: `0.0.0.0` means "any interface" and is only ever
  correct on the *server/listening* side of a connection. On the *client/connecting*
  side, always use a real, routable address — `127.0.0.1` for localhost, or the
  actual IP for a remote host.
- **GoPhish's per-target "Error" status has no visible error text by default in the
  results table** — the practical way to debug it is to isolate the Sending Profile
  with "Send Test Email" rather than repeatedly relaunching the full campaign.
- **Cross-checking MailHog's inbox count (not just GoPhish's status column)** is a
  useful independent signal: if MailHog shows 0 received messages, the problem is
  almost certainly upstream at the SMTP connection/Sending Profile level, not in the
  email template or landing page.
- **Copying a value from one tool's log output into another tool's config field is
  risky** without understanding what that value represents (bind address vs.
  connection address) — the same string can be correct in one context and invalid
  in another.

## References

- GoPhish documentation: https://docs.getgophish.com/user-guide/building-your-first-campaign
- MailHog GitHub: https://github.com/mailhog/MailHog
