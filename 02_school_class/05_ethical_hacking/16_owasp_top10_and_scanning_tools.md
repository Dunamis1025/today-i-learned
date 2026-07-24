# Network & Web Security Quiz — Study Notes

> Semester: Fall 2026 (2026-2학기)
> Topics: DNS, HTTP, OSI/TCP-IP model, Firewalls, OWASP Top 10, Security Scanning Tools

---

## 1. DNS & Web Fundamentals

### Q1. What component translates human-readable domain names into IP addresses?
**Answer: DNS Server**

A DNS server acts like an internet phone book. When you type a website address like `google.com`, it translates that readable name into the numeric IP address your computer needs to find the site.

### Q2. What component of a web server handles incoming client requests and delivers web pages?
**Answer: HTTP Server**

It acts like a receptionist that receives requests from users wanting to view a website and delivers the appropriate web pages back to them.

### Q3–Q4. HTTP request example (`GET /doc/test.html`)
- **Requested webpage:** `/doc/test.html` — the first line of the HTTP request (`GET /doc/test.html`) tells the server which file path the browser is asking for.
- **HTTP operation:** `GET` — the command used to ask the web server to fetch and retrieve data or a webpage.

### Q5. Primary role of the DNS resolver/recursor
**Answer: d) Translating human-readable domain names into IP addresses**

The resolver takes the website address you type and manages the *entire lookup process* to get the correct numeric IP address your computer needs.

#### 🔍 Deep dive: What is a DNS Resolver / Recursive Server?
Think of it as **"the errand-runner who does the lookup for you."** When a client asks "what's the IP for google.com?", it can't query the whole DNS hierarchy itself, so it delegates that job to a **recursive resolver** (e.g., an ISP's server, or public resolvers like Google's `8.8.8.8` or Cloudflare's `1.1.1.1`).

DNS is structured in layers:
1. **Root server** – "I don't know, but ask the `.com` server."
2. **TLD server** (`.com` server) – "I don't know the exact answer, ask google.com's authoritative server."
3. **Authoritative server** – "Here's the actual IP address!"

The resolver performs this multi-step querying **recursively** on the client's behalf and returns just the final answer. It typically **caches** results so repeated lookups are instant.

| Party | Role |
|---|---|
| Client (user's computer) | Just asks the resolver for the address |
| **DNS Resolver (Recursive Server)** | Does all the hopping between root → TLD → authoritative servers |
| Authoritative server | Holds the actual final answer (the IP) |

---

## 2. OSI / TCP-IP Model

### Q6. TCP/IP layer equivalent to OSI's Data Link + Physical layers
**Answer: d) Network Interface Layer**

It combines the bottom layers of the OSI model to handle physical transmission of data and hardware-level connections between devices.

### Q8. OSI layer responsible for logical addressing and routing
**Answer: b) Network Layer**

It acts like the postal service of a network — determining the best path for data to travel across networks and managing logical addresses like IP addresses.

### Q9. Which OSI layer does HTTP belong to?
**Answer: b) Layer 7 – Application Layer**

It operates at the very top layer, where user applications like web browsers interact directly with the network to request and display web pages.

### Q13. Firewall layer needed to inspect HTTP traffic
**Scenario:** You have a basic firewall that only understands IP addresses and port numbers, but need extra protection for a company web server running over HTTP.
**Answer: d) Layer 7 – Application Layer**

Because HTTP operates at the highest level where browsers and servers exchange data, the firewall must function at the application layer to properly inspect and understand this content.

---

## 3. Firewalls & Sandboxing

### Q11. Primary function of sandboxing in firewall operations
**Answer: b) Isolating files or executables in a separate environment**

It runs suspicious files or programs in a safe, isolated virtual space first, to test whether they contain malware or malicious code before they can affect the real system.

### Q12. Firewall type typically managed by a security service provider that can track internal network activity
**Answer: c) Cloud-based firewalls**

Operates on external cloud servers managed by a third-party security provider, allowing companies to monitor internal network traffic and receive security management remotely without physical hardware.

---

## 4. OWASP Top Ten

### Q14. What is the latest version of the OWASP Top Ten?
**Quiz answer: b) OWASP Top 10 2021**

> ⚠️ **Update note (as of July 2026):** This answer was correct when the course material was written, but **OWASP has since released a newer edition — OWASP Top 10:2025** — announced in November 2025 at the OWASP Global AppSec Conference (Washington, D.C.), with the final version released in January 2026. Key changes include:
> - Two new categories: **Software Supply Chain Failures** and **Mishandling of Exceptional Conditions**
> - **SSRF absorbed into Broken Access Control**
> - **Security Misconfiguration** moved up from #5 (2021) to **#2**
> - Shift in philosophy from listing *symptoms* (e.g., "Sensitive Data Exposure") to *root causes* (e.g., "Cryptographic Failures")
>
> For exam/quiz purposes tied to this course, **2021 remains the expected answer** unless the instructor has explicitly updated materials — but in real-world / current-knowledge terms, **2025 is now the correct, current answer.**

#### 🔍 Deep dive: What is OWASP?
**OWASP (Open Worldwide Application Security Project)**, formerly "Open Web Application Security Project," is a nonprofit, volunteer-driven international community focused on improving web application security. It publishes free research, tools, and guidelines — the most famous being the **"OWASP Top 10,"** a ranked list of the most critical web application security risks.

### Q15. Which of the following is NOT one of the OWASP Top Ten risks?
**Answer: a) Secure Network Configuration**

Cryptographic failures, insecure design, and broken access control are all official OWASP Top Ten risks, but "secure network configuration" itself is not one of the listed categories.

### Q16. Primary purpose of the OWASP Top Ten
**Answer: a) To provide a standard awareness document for developers and web application security**

It serves as a standard reference guide to raise awareness among developers and security professionals about the most critical security vulnerabilities in web applications.

### Q17. OWASP risk pertaining to compromised user accounts, tokens, or session identifiers
**Answer: b) Broken Authentication**

Occurs when authentication and session management functions are implemented incorrectly, allowing attackers to compromise passwords, keys, or session tokens and assume the identities of other users.

> 📝 **Vocabulary note — "pertains to":** means *"relates to"* or *"is connected with."* "Which risk pertains to X" = "which risk is associated with / concerns X." It's a more formal synonym for "relates to."

### Q18. OWASP risk allowing attackers to exploit external entities in an XML document
**Answer: d) XML External Entities (XXE)**

Occurs when poorly configured XML parsers process malicious XML input containing external references, allowing attackers to access internal files, read sensitive data, or perform internal network scanning.

#### 🔍 Deep dive: XML, Markup, and XXE

**Markup** means annotating plain text with tags to indicate meaning or structure (e.g., `<name>John</name>` tells a computer "this is a name," unlike plain text `John`, which has no inherent meaning to a machine).

**XML (eXtensible Markup Language)** is a markup language for structuring and exchanging data. Unlike HTML, which has a fixed set of predefined tags (`<div>`, `<p>`, etc.), XML is **"eXtensible"** — meaning users can freely define their own tag names (`<user>`, `<price>`, anything). It's widely used for data exchange between services, config files, SOAP APIs, and document formats (e.g., the internal structure of `.docx`/`.pptx` files).

**SOAP (Simple Object Access Protocol)** is a messaging protocol that formats its request/response messages as XML — an older but still common standard in enterprise/financial systems (as opposed to modern JSON-based REST APIs). Because it's XML-based, SOAP APIs are a classic target for XXE attacks.

**Anatomy of an XXE payload:**
```xml
<!DOCTYPE foo [
  <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
<foo>&xxe;</foo>
```
- `<!DOCTYPE foo [ ... ]>` — defines a DTD (Document Type Definition). `foo` is just an arbitrary root tag name (like using `foo`/`bar` as placeholder variable names in code) — in a real attack it would be whatever tag the target API actually expects.
- `<!ENTITY xxe SYSTEM "file:///etc/passwd">` — declares an entity named `xxe` whose value is defined as the contents of the server's `/etc/passwd` file. `SYSTEM` tells the parser to fetch an external resource; `file://` specifies reading a local file on the server.
- `<foo>&xxe;</foo>` — the actual document body. When the parser encounters `&xxe;`, it substitutes it with the entity's value — i.e., the full contents of `/etc/passwd` get injected into the document.

**Parser:** A program that reads and interprets a given file format (XML, JSON, code, etc.) into a structure the computer can work with. An "XML parser" reads XML and resolves entities like `&xxe;`. The vulnerability exists when the parser is configured (by default, in many older libraries) to allow external entity resolution — securely configured parsers disable this feature entirely.

---

## 5. Security Testing Tools

### Q19. Primary function of DIRB (Directory Buster)
**Answer: b) It looks for existing and/or hidden web objects.**

Acts as a web scanner that runs a dictionary-based attack against web servers to locate hidden or unlinked directories, files, and pages.

### Q20–Q21. Nikto
**Q20 Answer: b) Scanning web applications for security threats**
**Q21 Answer: b) SQL injection and other vulnerabilities**

Nikto is a web vulnerability scanner that thoroughly checks web servers for potential security issues, dangerous files, outdated software, misconfigurations, and flaws such as SQL injection.

#### 🔍 Deep dive: What is SQL Injection?
**SQL (Structured Query Language)** is used to query/manipulate data in a database. A login form, for example, typically runs a query like:
```sql
SELECT * FROM users WHERE username = 'entered_id' AND password = 'entered_password';
```

**SQL Injection** happens when an attacker enters malicious SQL syntax into an input field (login box, search bar, URL parameter) instead of normal data, causing the database to behave unintendedly.

**Classic example:** entering `' OR '1'='1` into a username field turns the query into:
```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '...';
```
Since `'1'='1'` is always true, the attacker may log in **without knowing any valid password.**

**Risks:** authentication bypass, full data exfiltration (personal info, password hashes), unauthorized data modification/deletion, and in severe cases, server takeover.

**Root cause:** developer code inserts user input directly into a SQL query string instead of treating it strictly as data.

**Defense:** use **Prepared Statements** / **parameterized queries**, which ensure user input is always treated as a literal value, never as executable SQL.

### Q22–Q23. nmap
**Q22 Answer: b) Scanning a network's IP addresses and ports**
**Q23 Answer: c) Open ports and services**

nmap is a powerful network discovery tool used to scan IP addresses, detect active hosts, and determine open ports/services and running software or OS, helping identify unnecessarily exposed or misconfigured pathways.

### Q24–Q25. Burp Suite
**Q24 Answer: c) Security testing of web applications**
**Q25 Answer: a) Proxy**

Burp Suite is an integrated platform for web application security testing — intercepting, analyzing, and modifying HTTP traffic, and scanning for vulnerabilities. Its **Proxy** tool specifically sits as a middleman between the browser and server, allowing traffic interception, inspection, and modification.

### Q30. Tool for testing security of web browsers and extensions
**Answer: d) BeEF**

A penetration testing tool focused specifically on the web browser, allowing security professionals to assess browser vulnerabilities and client-side security posture.

---

## 6. Authentication, Authorization & Accounting (AAA)

### Q26. Process of granting or denying a user access to resources
**Answer: b) Authorization**

The security process that determines whether an *already-authenticated* user has permission to access a specific file, application, or system resource.

### Q27. Process of tracking a user's activity while accessing network resources
**Answer: c) Accounting**

Refers to tracking user activities, resource consumption, and login sessions for auditing, billing, and security monitoring purposes.

---

## 7. Web Application Architecture & Client-side Security

### Q28. What makes up the client component in web application server architecture?
**Answer: b) JavaScript, HTML, CSS**

These are the core technologies used to build, style, and add interactive features to the user-facing interface inside a web browser.

### Q29. What attacks does Content-Security-Policy (CSP) help prevent?
**Answer: c) Cross-site scripting (XSS) and other attacks**

CSP restricts which scripts and resources can be loaded/executed on a webpage, effectively blocking malicious code injections like XSS.

---

## Quick Vocabulary Reference

| Term | Meaning |
|---|---|
| **Markup** | Tagging plain text to indicate structure/meaning |
| **XML** | eXtensible Markup Language — user-definable tags for structuring/exchanging data |
| **Entity (XML)** | A reusable value placeholder within XML, similar to a variable |
| **External Entity** | An XML entity that references an external resource (file/URL) |
| **XXE** | Attack exploiting external entity resolution to read server files / probe internal networks |
| **SQL Injection** | Injecting SQL syntax via user input to manipulate database queries |
| **Parser** | A program that reads and interprets a file format into a usable structure |
| **Pertains to** | Formal synonym for "relates to" / "is connected with" |
| **SOAP** | XML-based web service messaging protocol |
| **Prepared Statement** | Parameterized SQL query that treats user input strictly as data, preventing injection |
