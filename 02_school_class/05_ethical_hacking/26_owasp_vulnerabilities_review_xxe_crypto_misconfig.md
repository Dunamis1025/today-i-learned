# 26 — OWASP Vulnerabilities Review: XXE, Cryptographic Failures, Misconfiguration & More

**Unit:** VU23222 — Expose Website Security Vulnerabilities
**Context:** Final-class review of OWASP Top 10 categories (quiz-style recap), extending the four hands-on vulnerabilities from AT2 (SQLi, Broken Auth, XSS, IDOR).

> This note captures the **concepts** reviewed in class — what each vulnerability is, how it's exploited, how it's prevented, and how a fix is verified.

---

## 1. Cryptographic Failures (Sensitive Data Exposure)

**What it is:** Failing to protect sensitive data properly — storing it in plain text, or using weak/outdated algorithms — so that a breach exposes it directly.

- **Bad practice:** storing user passwords as **plain text** in the database. If the DB is breached, every password leaks immediately.
- **Bad practice:** using weak/legacy hashing like **MD5** (fast, unsalted, easily cracked offline — as seen in the Broken Auth work with CrackStation).
- **Bad practice:** sending sensitive data over plain **HTTP** (exposed in transit), or disabling **SSL/TLS certificate validation** (opens the door to man-in-the-middle attacks).

**Prevention:**
- Encrypt sensitive data both **in transit** (TLS/HTTPS) and **at rest** (e.g. AES-256) with strong, vetted algorithms.
- Hash passwords with a **salted, slow algorithm** like **bcrypt** (or Argon2) — never plain text, never bare MD5.

---

## 2. Security Misconfiguration

**What it is:** Systems, frameworks, or apps that aren't properly hardened, or that expose things they shouldn't.

- **Classic example:** exposing a **config / settings file** (`config.json`, `.env`, etc.). These files often hold passwords, API keys, and database connection strings — leaking one hands an attacker the keys to everything.

**Prevention (secure practices, not misconfigurations):**
- Encrypt data with strong algorithms (AES-256).
- Hash passwords with bcrypt + salt.
- Use HTTPS for all client–server communication.
- Harden servers/frameworks and keep config files out of public reach.

---

## 3. XXE — XML External Entity Injection

**What it is:** A vulnerable **XML parser** processes external entity definitions instead of disabling them, letting an attacker's malicious XML reach internal resources.

- **How it's exploited:** the attacker sends a malicious XML payload that uses an external entity to **read internal server files** (e.g. `/etc/passwd`) or scan the internal network.
- **Class demo recap:** an `<!ENTITY xxe "...">` was defined and referenced with `&xxe;`, which the parser substituted into the output. A real attack swaps the harmless value for `SYSTEM "file:///etc/passwd"` to exfiltrate file contents.

**HTML vs XML (why XXE is an XML thing):**
- **HTML** = for *displaying* pages; tags are predefined (`<h1>`, `<p>`).
- **XML** = for *storing/transporting data*; you define your own tags (`<News>`, `<reportedBy>`). ENTITY is an XML feature that acts like a variable — which is exactly what XXE abuses.

**Prevention:**
- **Disable DTD (Document Type Definition) processing** and external entity loading in the XML parser — the most fundamental, reliable fix.
- Input encoding does **not** fix XXE (that's an XSS defence); MD5 hashing is irrelevant here.

**Verification:**
- Send a test XML payload that references an external entity and confirm (via logs/response) that the server **blocks it or returns an error** instead of resolving the external resource.

---

## 4. Vulnerable & Outdated Components

**What it is:** Modern apps are built from third-party libraries/frameworks. If those are **outdated**, they may carry **known, published vulnerabilities** an attacker can exploit.

- **Class demo recap:** the NuGet Package Manager in Visual Studio showed installed libraries (e.g. `Microsoft.AspNetCore.Identity`, `EntityFrameworkCore`) at v6.0.0 with **9 updates available** — outdated components that could be exploitable.

**Prevention / True statement from the review:**
- Keeping frameworks, libraries, and server software **up to date** patches known vulnerabilities and significantly reduces risk. (This is the core defence for this OWASP category.)

---

## 5. XSS types — quick classification recap

- **Stored XSS:** the malicious script is **permanently stored** on the server (DB, comments, profiles). Every user who loads that page runs it in their browser — cookies/session tokens can be stolen. (Most dangerous.)
- **Reflected XSS:** the script is carried in a URL parameter and **reflected straight back** in the response, executing immediately — but it's **not stored** on the server. Only whoever clicks the crafted link is hit.
- **DOM-based XSS:** never touches the server — client-side JavaScript handles a value (e.g. a URL parameter) unsafely and writes it into the **DOM**. (This was my AT2 search-bar finding.)
- **Not XSS:** *Local File Inclusion (LFI)* is a separate file-inclusion vulnerability, not a type of XSS.

---

## 6. SQL Injection — root cause recap

**Root cause:** **user input is not properly validated or sanitised**, and gets concatenated directly into a SQL query string, so the DB treats attacker input as commands.

- **Example payload:** `' OR '1'='1` bypasses authentication because the condition is always true.
- **Impact:** authentication bypass, data theft, or data deletion.

**Prevention:**
- Validate/sanitise all user input, and use **parameterised queries / prepared statements** so SQL commands and user data stay clearly separated.

---

## 7. HTTPS — what it does *and doesn't* do

- **True:** HTTPS encrypts data **in transit**, preventing network sniffing and tampering (man-in-the-middle).
- **False:** HTTPS does **not** make a site "completely safe from all attacks." It protects the transport channel only — it does nothing against XSS, SQL injection, IDOR, broken access control, or server misconfiguration. Those are application-logic/config flaws that live beyond the transport layer.

---

## Key takeaways
- **Encrypt everywhere:** in transit (TLS) *and* at rest (AES); hash passwords with salted bcrypt, never plain text or bare MD5.
- **Harden and hide config:** exposed `.env`/config files are a top misconfiguration.
- **XXE = disable DTD / external entities** in the parser; it's an XML-parser problem, and input encoding won't fix it.
- **Patch your dependencies:** outdated components carry known exploits.
- **Know your XSS:** Stored (persisted) vs Reflected (echoed, not stored) vs DOM-based (client-side only).
- **SQLi = unsanitised input → parameterised queries fix it.**
- **HTTPS ≠ total security:** it only protects the channel, not the application logic.
