# 📧 Phishing Email Analysis — Study Notes

> **Topic:** Email Header Analysis & Phishing Investigation  
> **Duration:** ~60 minutes (hands-on lab)  
> **Environment:** Virtual Machine (Ubuntu) — safe, isolated sandbox

---

## 🧠 Core Concept

Every email carries two layers of information:

| Layer | What you see | Purpose |
|---|---|---|
| **Body** | The visible message content | Communication |
| **Header** | Hidden technical metadata | Delivery routing & authentication |

Attackers exploit the fact that most users only see the body. This lab teaches you to **look deeper**.

---

## 🔑 Key Concepts

### 1. Email Header
- Think of it as the **"shipping manifest"** or **"package label"** of an email.
- Records: sender's IP address, servers the email passed through, timestamps, and routing path.
- **Why it matters:** Scammers can spoof the visible "From" name/address easily — but forging the entire header trail is much harder. This is where the truth hides.

---

### 2. SPF — Sender Policy Framework
- **Analogy:** An "Approved Sender List"
- A domain (e.g. `google.com`) publicly declares: *"Only these IP addresses are allowed to send email on our behalf."*
- When an email arrives, the receiving server checks whether the sender's IP is on that approved list.
- **If it fails:** The sender is NOT an authorized source — high likelihood of impersonation.

---

### 3. DKIM — DomainKeys Identified Mail
- **Analogy:** A "Tamper-Evident Security Seal"
- The sender attaches a unique **encrypted digital signature** to every outgoing email.
- If anyone intercepts and modifies even one character of the email in transit, the signature breaks and no longer matches.
- **If it fails:** The email was either altered in transit or sent by an untrusted source.

---

### 4. DMARC — Domain-based Message Authentication, Reporting & Conformance
- Builds on top of SPF and DKIM.
- Tells receiving servers **what to do** if SPF or DKIM checks fail (e.g. reject, quarantine, or report).
- If DKIM fails → DMARC result is also unclear/fail → email cannot be authenticated.

---

## 🛠️ Tools Used

| Tool | Purpose | URL |
|---|---|---|
| **SOGo (Mailcow)** | Webmail client — view the "victim's" inbox | `http://<IP>/SOGo/so/` |
| **MXToolbox** | Paste email headers → automatic security analysis report | [mxtoolbox.com](https://mxtoolbox.com) |
| **VirusTotal** | Upload suspicious attachments → check for malware | [virustotal.com](https://www.virustotal.com) |

---

## 🔍 5-Step Investigation Workflow

```
Step 1 → Access the Lab Environment
Step 2 → Find & Extract the Email Headers
Step 3 → Analyze Headers with MXToolbox
Step 4 → Interpret the Results
Step 5 → Draw a Conclusion
```

### Step 1: Access the Lab Environment
- Run `ip addr` in the terminal to get your VM's IP address.
- Open browser → navigate to `http://<YOUR_IP>/SOGo/so/`
- Log in as the victim: `john@exchange.com`

### Step 2: Extract Email Headers
- Open the suspicious **"Invoice Overdue"** email in the inbox.
- Click the **three-dot menu (⋮)** → select **"View Message Source"**
- Copy the entire raw header text that appears.

### Step 3: Analyze with MXToolbox
- Go to [MXToolbox Header Analyzer](https://mxtoolbox.com/EmailHeaders.aspx)
- Paste the copied header → click **"Analyze Header"**

### Step 4: Interpret the Results

| Check | Result | Meaning |
|---|---|---|
| **SPF** | ✅ Pass | Sender's IP is technically registered — not definitive proof of legitimacy |
| **DKIM** | ❌ Fail | **🚨 Red flag.** Digital seal is broken → email was tampered with or is untrustworthy |
| **DMARC** | ⚠️ Unclear | Authentication failed due to DKIM failure → cannot verify sender |
| **TLS** | ❌ Not used | Email was not transmitted over a secure/encrypted channel |

### Step 5: Conclusion
> **Verdict: PHISHING**  
> The email visually mimics a legitimate invoice, but the broken DKIM signature proves it cannot be trusted. The absence of TLS further confirms this is a non-professional, malicious sender.

---

## ⚠️ Safe Attachment Analysis (VirusTotal)
- **Never open suspicious attachments directly.**
- Upload the file to [VirusTotal](https://www.virustotal.com) → it scans with 70+ antivirus engines simultaneously.
- Returns a verdict: clean, suspicious, or malicious.

---

## 💡 Key Takeaways

1. **Visible ≠ Real** — The "From" field can be completely faked. Always dig into the headers.
2. **DKIM failure = strongest red flag** — A broken digital seal is near-definitive proof something is wrong.
3. **SPF pass alone is NOT enough** — Attackers can pass SPF while still failing DKIM/DMARC.
4. **Never open attachments** without checking VirusTotal first.
5. **All three checks matter:** SPF + DKIM + DMARC together form a reliable authentication chain.

---

## 🧩 Quick Reference: Authentication Chain

```
Email Received
      │
      ▼
   SPF Check ──► Is sender's IP on the approved list?
      │
      ▼
  DKIM Check ──► Is the digital signature intact and valid?
      │
      ▼
 DMARC Policy ──► Based on above results, accept / quarantine / reject?
```

---

*Lab environment: Virtual Machine (Ubuntu) — isolated sandbox, safe for malware interaction*  
*Tools: SOGo Webmail · MXToolbox · VirusTotal*
