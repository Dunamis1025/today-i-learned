# VU23222 – Expose Website Security Vulnerabilities
## Assessment Task 2, Part 1: Knowledge Questions – Summary

---

### Question 1 – Client-Server Model & 3-Tier Architecture

The client-server model is how the web works. The user requests something through a browser on their device, and the server processes that request and sends back a webpage. As web apps grow and become more complex, managing everything in one place gets messy. That is why a 3-tier architecture is used to separate concerns:

- **Presentation Tier**: What the user sees and interacts with in the browser (HTML/CSS), e.g. a product page on Amazon.
- **Application Tier**: The middle layer. When a user clicks something, the request goes to the server, where the application tier handles background processing such as checking stock or calculating totals. It sits between the browser and the database.
- **Data Tier**: Where the actual data resides (user accounts, product lists) in a database.

Separating the application into tiers makes maintenance easier if one part goes down or needs an upgrade. It also enhances security — even if the frontend or application layer is compromised, the core database is not directly exposed.

---

### Question 2 – HTTP Protocol Structure and Operation

HTTP (Hypertext Transfer Protocol) is the foundational protocol for communication on the web. It operates on a request-response model using a client-server architecture. The browser acts as the client and sends an HTTP request to the web server.

1. **Request**: The client sends a message containing a request line (method + target URL), headers with metadata, and sometimes a message body.
2. **Processing**: The server receives and processes the request, interacting with databases or internal logic if necessary.
3. **Response**: The server sends back a status code (e.g. 200 OK, 404 Not Found), response headers, and a payload (HTML, images, JSON).

HTTP is **stateless** — each request-response pair is independent, and the server does not remember previous requests from the same client. This is why cookies and sessions are used to remember users.

---

### Question 3 – Function and Role of HTTP Headers

HTTP headers are "additional information" (metadata) exchanged between client and server — similar to the details written on the outside of a parcel rather than its contents (sender, receiver, item type, shipping instructions).

Main roles of headers:
1. **Controlling Communication and Settings**: Tell the server what data formats the client accepts, what browser is used, and whether the connection should stay alive.
2. **Security and Authentication**: Transmit authorization details or use cookies to maintain sessions.
3. **Caching and Performance Optimization**: Allow browsers to use cached files instead of downloading the whole page every time.

---

### Question 4 – Common HTTP Headers Explained

- **User-Agent**: Identifies the client (browser, OS, device) so the server can deliver a compatible layout (mobile/desktop).
- **Host**: Specifies the domain being requested; distinguishes between multiple sites hosted on one server IP.
- **Cookie**: Stored data the client sends back to the server to remember login states or preferences.
- **Set-Cookie**: Used by the server to instruct the client to store a value as a cookie (e.g. a session ID after login).
- **Authorization**: Carries credentials (passwords, tokens, API keys) needed to access a protected resource.
- **Content-Type**: Indicates the media type of the data being exchanged (e.g. `application/json`, `text/html`).
- **Cache-Control**: Directs how long content should be cached by the browser to reduce repeat server requests.
- **Server**: Provides software details about the web server that handled the request (e.g. Apache, Nginx).

---

### Question 5 – HTTP Security Headers

- **X-Frame-Options**: Prevents the site from being embedded in `<frame>`/`<iframe>`/`<object>` elements on other sites, blocking Clickjacking attacks.
- **Content-Security-Policy (CSP)**: Strictly controls which external sources (scripts, images, stylesheets) can be loaded, using a whitelist approach (allowing only pre-approved sources, blocking everything else). This prevents execution of untrusted scripts and helps stop Cross-Site Scripting (XSS).
- **Strict-Transport-Security (HSTS)**: Forces the browser to communicate only via HTTPS. Even if a user tries `http://`, the browser upgrades the request to `https://`, preventing Man-in-the-Middle (MitM) attacks.

---

### Question 6 – OWASP Secure Headers Project (OSHP) and oshp-validator

**OSHP**: An open-source project providing guidelines and tools to help developers/administrators properly configure HTTP security headers (HSTS, CSP, X-Frame-Options, etc.).

**oshp-validator**: A validation tool that checks whether HTTP security response headers comply with OSHP recommendations. It is a standalone, portable testing suite that lets users define and run tests without requiring complex coding knowledge, helping administrators identify missing or misconfigured headers.

*(Note: verified via OWASP's official GitHub — it is a Venom-based test suite for validating header configurations against OSHP recommendations, not a simple URL-scanning web tool.)*

---

### Question 7 – Role of the OWASP Framework

OWASP (Open Worldwide Application Security Project) is a globally recognized, open-source authority guiding secure web application development and testing in three key areas:

1. **Standards and Guidelines**: e.g. the OWASP Top 10, which highlights the most critical risks to prioritize.
2. **Development and Testing Tools**: e.g. OWASP ZAP (Zed Attack Proxy), used to test, scan, and identify vulnerabilities.
3. **Security Awareness and Culture**: OWASP fosters a global security community sharing best practices and threat intelligence, helping build a strong security culture industry-wide.

---

### Question 8 – Website Vulnerabilities and Their Impact

**Website Vulnerabilities**: Security flaws or weaknesses in a web application's code, design, or configuration that attackers can exploit for unauthorized access or malicious actions. For example, a login form vulnerable to SQL Injection could let an attacker bypass the password check and exfiltrate the entire user database.

**Impact on Users**:
- Data breaches (passwords, credit card numbers, personal records)
- Financial/personal harm from phishing or malware
- Account takeover, leading to privacy violations

**Impact on Organizations**:
- Financial loss and regulatory fines (e.g. GDPR)
- Reputational damage and loss of customer trust
- Operational disruption from downtime, leading to legal liability

---

### Question 9 – OWASP Top Ten & OWASP Top 10 API Security Risks

**OWASP Top Ten**: A globally recognized standard awareness document highlighting the 10 most critical web application security risks, ranked by real-world frequency and impact (e.g. Broken Access Control, Security Misconfiguration, Injection). It gives developers and security teams a roadmap for prioritizing threats.

**OWASP Top 10 API Security Risks**: A specialized project focused on the top 10 vulnerabilities unique to APIs, which power modern web, mobile, and cloud architectures. Reflecting the 2023 update, it addresses API-specific flaws such as Broken Object Level Authorization (BOLA) and Broken Object Property Level Authorization (BOPLA).

*(Note: category names updated to reflect current OWASP standards — "Broken Authentication"/"Security Misconfigurations" are 2017-era terms; "Excessive Data Exposure" was merged into BOPLA in the 2023 API Top 10.)*

---

### Question 10 – SQL Injection

**How it works**: Occurs when a web application takes user input (e.g. login form, search bar) and includes it directly in backend database queries without proper sanitization or validation. Attackers inject malicious SQL syntax (e.g. `' OR '1'='1`), tricking the database into executing the statement in an unintended way — allowing authentication bypass or exfiltration/modification/deletion of data.

**How it can be tested**:
- **Manual Testing**: Inputting special characters or SQL syntax (`'`, `OR 1=1`, `UNION SELECT`) into vulnerable-looking fields or URL parameters, checking for leaked error messages, unauthorized login, or exposed data.
- **Automated Testing**: Using specialized scanners like SQLmap or interception proxies like Burp Suite to systematically send payloads and detect vulnerabilities.

---

### Question 11 – Cross-Site Scripting (XSS)

**How it works**: An attacker injects malicious scripts (typically JavaScript) into a trusted website. Other users' browsers execute the script, trusting it because it comes from a trusted site — allowing attackers to steal session cookies, hijack accounts, or expose sensitive information. Example: a comment field that fails to filter input, allowing a payload like `<script>alert('XSS')</script>` to execute for every visitor.

**How to prevent it**:
- **Output Encoding**: Encoding user-supplied data (e.g. `<` → `&lt;`) so browsers treat it as text, not executable code.
- **Input Validation and Sanitization**: Cleaning incoming data to strip dangerous tags/scripts before processing or storage.
- **Content Security Policy (CSP)**: Restricting where scripts can be loaded from and blocking unauthorized inline script execution.

---

### Question 12 – Insecure Direct Object References (IDOR)

**Definition**: An access control vulnerability where a web application exposes internal implementation objects (database keys, filenames, user IDs) directly in user input or URLs without proper authorization checks. Example: `example.com/account?id=1001` — if the server doesn't verify the logged-in user is authorized to view record 1001, an attacker can simply change the parameter to access another user's data.

**Why it's dangerous**:
- **Unauthorized Data Exposure**: Attackers can harvest sensitive personal, financial, or internal data.
- **Low Barrier to Exploitation**: No advanced tools needed — just modifying a parameter value.
- **Large-Scale Data Harvesting**: Predictable/sequential IDs allow automated enumeration of thousands of records.
- **Privilege Escalation & Account Takeover**: Can allow unauthorized data modification or account hijacking.

---

### Question 13 – Browser Exploitation Framework (BeEF)

**Definition**: A powerful, open-source penetration testing tool focused specifically on web browsers. Unlike tools targeting server-side or network infrastructure, BeEF assesses client-side security by using browsers as an entry point.

**Use in penetration testing**:
- **Browser Hooking**: Testers "hook" a target browser by having a user visit a compromised page or click a malicious link, establishing a persistent connection between the browser and the BeEF server.
- **Client-Side Command Execution**: Once hooked, testers can run commands remotely — launching further exploits, capturing keystrokes, stealing session cookies, or pivoting to scan internal network resources.

---

### Question 14 – Common Vulnerability Testing Tools

- **Nikto**: A web server vulnerability scanner focused on the server itself — checks for dangerous files, outdated software, risky CGI scripts, and misconfigurations.
- **DIRB**: A web content scanner using brute-force to discover unlinked directories and files (e.g. hidden admin panels or backup files) that Nikto's server-focused scan wouldn't find.
- **Burp Suite**: The go-to interception proxy for hands-on web testing — intercepts, inspects, and modifies HTTP/HTTPS traffic in real time, supporting both manual exploitation and automated scanning.
- **SAST (Static Application Security Testing)**: "White-box testing." Analyzes source code or binaries without executing the program, catching flaws early — before code is deployed.
- **DAST (Dynamic Application Security Testing)**: "Black-box testing," in contrast to SAST. Tests a running, deployed application by simulating real-world external attacks (e.g. SQL Injection, XSS) to find runtime vulnerabilities.

---

## References

**Question 6 — oshp-validator**
- OWASP, "www-project-secure-headers" GitHub repository — https://github.com/OWASP/www-project-secure-headers
- OWASP, "oshp-validator" subproject — https://github.com/oshp/oshp-validator

**Question 9 — OWASP Top Ten & API Security Top 10**
- OWASP Foundation, "OWASP Top Ten Web Application Security Risks" — https://owasp.org/www-project-top-ten/
- OWASP Foundation, "OWASP Top 10:2021" — https://owasp.org/Top10/2021/A00_2021_Introduction/
- OWASP Foundation, "OWASP API Security Project" — https://owasp.org/www-project-api-security/

**Question 13 — BeEF**
- BeEF Project, official site — https://beefproject.com/
- StationX, "How to Use the BeEF Hacking Tool" — https://www.stationx.net/beef-hacking-tool/

---

*Generative AI (Claude, Anthropic) was used to assist with verifying technical accuracy, researching current OWASP standards, and refining the wording of written responses. All final answers reflect the learner's own understanding and were written in their own words.*
