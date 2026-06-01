# Study Notes: Introduction to curl — Cybersecurity Lab

> **Date:** 2025  
> **Platform:** Cybersecurity learning platform (virtual machine lab, 30 min)  
> **Role:** Junior Security Analyst  

---

## 1. What is `curl`?

`curl` (Client URL) is a **command-line tool** for sending and receiving data to/from web servers — essentially a **web browser without a graphical interface**.

| Browser | curl |
|---|---|
| Uses mouse clicks | Uses typed commands |
| Shows rendered visual pages | Shows raw data (HTML, headers, JSON) |
| User-friendly GUI | Lightweight, scriptable, precise |

**Why security analysts use it:**
- Inspect how a server responds without any browser interference
- Automate checks and tests
- Identify misconfigurations, security headers, and server infrastructure

---

## 2. Core Commands & Options

### 2-1. Fetch a web page (GET request)
```bash
curl https://example.com
```
- Default HTTP method: **GET** (read-only, no data sent)
- Returns raw **HTML** of the page

---

### 2-2. Fetch HTTP headers only
```bash
curl -I https://example.com
```
- `-I` → retrieves only the **response headers**, not the body
- Key thing to look for: **status code**

```
HTTP/1.1 200 OK
```

---

### 2-3. Verbose mode — inspect full communication
```bash
curl -v https://example.com
```
- `-v` = **verbose** → shows *everything*: connection steps, TLS handshake, headers sent and received
- Useful for diagnosing security issues, checking encryption, and seeing what the server reveals about itself

---

### 2-4. Save output to a file
```bash
curl https://example.com -o page.html
```
- `-o [filename]` → saves response body to a local file instead of printing to screen

```bash
cat page.html   # view the saved file contents
```

---

### 2-5. Send data to a server (POST request)
```bash
curl -X POST https://httpbin.org/post -d "name=David"
```
- `-X POST` → sets the HTTP method to **POST** (sends data)
- `-d "name=David"` → the **data payload** to send

**Analogy:**
- `GET` = checking out a book from a library
- `POST` = signing your name in the library's guestbook

**Sample response (JSON):**
```json
{
  "form": { "name": "David" },
  "origin": "123.45.67.89",
  "url": "https://httpbin.org/post"
}
```
- `"form"` → confirms the server received your data correctly
- `"origin"` → your public IP address

---

### 2-6. Check curl version
```bash
curl --version
```
- Confirms installed version, supported protocols (HTTP, HTTPS, FTP…), and features (SSL/TLS support)
- Security analysts verify this to ensure the tool supports encrypted connections

---

### 2-7. Test an invalid domain (error handling)
```bash
curl https://nonexistent-domain-xyz.com
```
- Returns: `Could not resolve host`
- Indicates a **DNS resolution failure** — the domain doesn't exist or can't be found

---

### 2-8. Access help & documentation
```bash
curl --help          # quick summary of common options
curl --manual        # full manual
man curl             # system manual (press Space to scroll, q to quit)
```
> **Pro tip:** Even professional security analysts look things up constantly. Knowing *how* to find the answer matters more than memorizing every flag.

---

## 3. HTTP Methods

| Method | Purpose | Analogy |
|---|---|---|
| **GET** | Retrieve data | Reading a webpage |
| **POST** | Send data to server | Submitting a form |
| **PUT** | Update existing data | Editing a record |
| **DELETE** | Remove data | Deleting a record |

Security analysts monitor HTTP methods to detect **unexpected or unauthorized requests** (e.g., a POST to a read-only endpoint may indicate an attack).

---

## 4. HTTP Status Codes

| Code | Status | Meaning |
|---|---|---|
| **200** | OK | Request succeeded — server responded correctly |
| **301 / 302** | Redirect | Resource has moved to a new URL |
| **403** | Forbidden | Access denied — you don't have permission |
| **404** | Not Found | The resource doesn't exist |
| **500** | Internal Server Error | Something broke on the server's side |

---

## 5. Reading Response Headers — Server Fingerprinting

When you run `curl -I` or `curl -v`, the response headers reveal information about the server's infrastructure.

**Example headers and what they mean:**

| Header | Example Value | Meaning |
|---|---|---|
| `Server` | `cloudflare` | Which server software/proxy is in use |
| `CF-RAY` | `abc123-SIN` | Confirms the site is behind **Cloudflare** |
| `cf-cache-status` | `HIT` | Response was served from Cloudflare's cache |
| `Last-Modified` | `Wed, 09 Aug 2023` | When the content was last updated |

---

## 6. What is Cloudflare?

Cloudflare is a **reverse proxy and security service** that sits between users and the origin web server.

```
User → [Cloudflare] → Origin Server
```

**What it does:**
- **DDoS protection** — absorbs massive attack traffic before it hits the server
- **Web Application Firewall (WAF)** — blocks malicious requests
- **Caching** — serves content from servers geographically close to the user (faster load times)
- **TLS termination** — handles HTTPS encryption

**Security implication:** If you see `CF-RAY` or `Server: cloudflare` in headers, the site is protected by Cloudflare. Direct access to the origin server is blocked — a key recon detail in security assessments.

---

## 7. Quick Reference Cheat Sheet

```bash
# Basic fetch
curl https://example.com

# Headers only
curl -I https://example.com

# Verbose (full communication log)
curl -v https://example.com

# Save output to file
curl https://example.com -o page.html

# POST request with data
curl -X POST https://httpbin.org/post -d "name=David"

# Check curl version
curl --version

# Help
curl --help
curl --manual
```

---

## 8. Key Takeaways

1. `curl` lets you communicate with web servers using raw commands — stripping away browser abstraction.
2. **GET** reads data; **POST** sends data. Understanding the difference is fundamental to web security.
3. **Status codes** are the server's answer: `200` = success, `4xx` = client error, `5xx` = server error.
4. **Headers reveal the server's identity** — always check them when assessing a target.
5. **Cloudflare** is a widely-used security layer; its presence means the origin server is shielded.
6. **Verbose mode (`-v`)** is your best debugging tool — use it to understand exactly what's happening in a connection.
7. **Professionals use documentation** — mastering `--help` and `man curl` is a skill in itself.
