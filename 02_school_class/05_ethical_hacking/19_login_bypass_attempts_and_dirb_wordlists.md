# 19 — Login Bypass Attempts & Dirb Wordlists (Simulation Week Rehearsal)

This document covers a local rehearsal session for Holmesglen Simulation Week, done ahead of the real activity day. The goal was to practice Checkpoint 1 (Discovery) and Checkpoint 2 (Enumeration and Exploitation) against a locally-hosted copy of the target web app ("Holmesglen LEGO Town") before doing it for real on the school network.

## Setup Recap

- **Attacker machine:** Kali Linux, IP `192.168.233.130`
- **Target machine:** Fedora Linux running the web app on port `3000`, IP `192.168.233.129`
- Both machines were on the same private virtual network (a "Host-Only" network), meaning they could talk to each other but not reach the internet — a safe, isolated sandbox for practicing.

## Core Concepts Explained Simply

### What is an IP address?

Think of an IP address like a house address, but for a computer on a network. `192.168.233.129` is the "address" of the target Fedora machine — it's how the Kali machine knows where to send its requests.

### What is a port?

If the IP address is the building, the port number is the specific door/room inside it. Port `3000` is the specific "door" where the web app is listening for visitors. A web server can have many apps running on different ports at once, each with its own door.

### What is JSON?

JSON (JavaScript Object Notation) is just a simple, structured way of writing data using curly braces `{ }`. For example:

```json
{"username": "admin", "password": "1234"}
```

This is like filling out a form with labeled fields (`username`, `password`) instead of just writing plain text. Many websites use JSON to send data back and forth between the browser and the server.

### What does "POST" mean?

When a browser talks to a web server, it usually does one of two things:
- **GET** — "Show me this page" (like opening a webpage to read it)
- **POST** — "Here's some data, please do something with it" (like submitting a form)

Logging in is a POST request: the browser sends the username and password to the server and asks it to check them.

## Checkpoint 1 — Discovery (Completed)

Two tools were used to find the target and learn what it was running:

- **nmap** — scans a network to find live machines and open ports. Think of it like knocking on every door in a hallway to see which ones answer.
- **whatweb** — once a web port is found, this tool "reads the sign on the door" — it tells you what software/framework is running behind that page (in this case, Express, a Node.js framework), and grabs the page title.

Result: found the login page at `http://192.168.233.129:3000/login.html`, confirmed via its title: "Holmesglen LEGO Town Login".

## Checkpoint 2 — Enumeration and Exploitation (Attempted, Not Solved in Rehearsal)

### Finding hidden pages with Dirb and wordlists

Not every page on a website has a visible link pointing to it. Some pages exist but are only reachable if you know (or guess) the exact URL — like a room in a building with no sign on the door.

**Dirb** is a tool that automates guessing. It takes a **wordlist** (a big text file full of common page/folder names like `admin`, `backup`, `config`) and tries each one against the target, checking whether a real page exists at that address.

Three wordlists were tried, in increasing size:

| Wordlist | Approx. word count | What it means |
|---|---|---|
| `common.txt` | ~4,600 | The "default" list — quick, common names only |
| `big.txt` | ~20,000 | A bigger list — more names, takes longer, more thorough |
| `directory-list-2.3-medium.txt` | ~219,000 | Extremely large — dirb warned this would take too long and refused to run without a special override flag |

**Result:** All three attempts (well, the two that actually completed) found the same six pages: `/admin`, `/Admin`, `/ADMIN`, `/css`, `/user`, `/vendor`. A bigger wordlist did not reveal anything new. This taught an important lesson: **more brute-force isn't always the answer** — sometimes a hidden page simply isn't there, and the real vulnerability lies elsewhere (e.g. in how the login logic itself handles input).

### Understanding HTTP status codes seen during testing

- **200 OK** — "Here's the page you asked for, no problem."
- **301 / 302 (Redirect)** — "That's not the real address, go here instead." This is exactly what happened when visiting `/admin` without logging in — the server redirected to the login page instead of showing admin content. This is actually a **good sign for the developer** — it means the admin page is properly protected.
- **404 / "Cannot GET"** — "That page doesn't exist here at all." Seen when trying `/register` and `/api/users` — these simply weren't real endpoints on this app.

### Trying to bypass the login form

The login form's own code (viewed via the page source) revealed exactly how it worked: it sends `{ username, password }` as JSON to `/login`, and the server replies with a `role` field that decides whether you're treated as an admin or a normal user.

Several classic bypass techniques were attempted:

1. **SQL Injection** — a technique where malicious input like `' OR '1'='1` is used to trick a database query into always returning "true," effectively logging in without knowing the real password. This only works if the app uses a SQL database (like MySQL) *and* builds its queries by directly pasting in user input without protection.
   - *Result: Failed.* The app likely isn't using raw SQL string-building, or it sanitizes input properly.

2. **NoSQL Injection** — similar idea, but aimed at NoSQL databases (like MongoDB), which use special operators such as `$ne` ("not equal to") or `$gt` ("greater than"). Sending `{"password": {"$ne": ""}}` instead of a normal string is an attempt to trick the check into "any password that isn't blank" — which is almost always true.
   - *Result: Failed.* The server appears to check that `username` and `password` are actual text (strings) before processing them, and rejects anything that's a JSON object instead — a solid defensive practice.

3. **Guessing default credentials** (`admin` / `admin`) — sometimes test or demo apps leave an easy default login in place.
   - *Result: Failed.*

4. **Omitting a field entirely** (sending only `username`, no `password` key at all) — testing whether the server crashes or behaves unexpectedly when a required field is simply missing.
   - *Result: Failed* — same generic error message every time.

5. **Checking for other hidden endpoints** that might leak data or offer another way in, like `/register` (a signup page) or `/api/users` (a possible "list all users" API).
   - *Result: Neither existed.*

### Key takeaway from this checkpoint

Every failed attempt returned the exact same error message: `{"error":"Invalid username or password"}`. A consistent, generic error message across every kind of failed attempt is actually a sign of **good security practice** by the developer — it doesn't give attackers any extra clues about *why* something failed, which makes guessing much harder.

## Reflection & Next Steps

This rehearsal target was not successfully bypassed using standard techniques. Two theories going into the real Simulation Week activity:

1. The real target (on the school network) may behave differently, or hints will be provided on the day.
2. The activity documentation groups **Checkpoint 3 (JWT — JSON Web Tokens)** right after login bypass, which raises the possibility that admin access is meant to be gained through JWT manipulation rather than a traditional login bypass. This is worth revisiting once JWT concepts (how tokens are structured, stored, and signed) have been studied.

**Next checkpoints to prepare for:**
- **Checkpoint 3:** Learn how JWTs work — their structure (header, payload, signature), how they're stored (usually in cookies or browser storage), and how tools like CyberChef can decode/re-sign them.
- **Checkpoint 4:** Learn Modbus basics and the `modpoll` tool for sending commands to simulated IoT devices.
