# Rail Network Privilege Escalation Lab — T SOC Simulation Week

**Course:** VU23222 — Expose Website Security Vulnerabilities
**Date:** 25 August 2026
**Environment:** Holmesglen T SOC (Railway Control Cybersecurity Exercise)
**Role:** Red Team

## Overview

Full attack chain against a simulated railway control web application
(`Holmesglen LEGO Town`, Node.js/Express, port 3000), starting from
unauthenticated access and ending in remote control of physical IoT/rail
devices via Modbus. The same activity was also observed from the Blue Team
side (Wazuh SIEM) to confirm detection.

## Attack Chain

### 1. Reconnaissance

```bash
nmap -p 3000 10.12.237.0/24 10.12.239.0/24      # host discovery on target subnets
nmap -sC -sV 10.12.237.200                       # service/version detection
whatweb 10.12.237.200:3000                       # fingerprinting -> Node.js Express
dirb http://10.12.237.200:3000/ /usr/share/wordlists/dirb/common.txt
```

- Confirmed target: `10.12.237.200:3000`, running Node.js Express.
- `dirb` revealed hidden paths: `/admin`, `/user`, `/vendor`, `/css`.
- `/admin` redirected to `/login.html` when unauthenticated.

### 2. Authentication Bypass — SQL Injection

- Login form was vulnerable to classic SQLi. Injecting a single quote
  (`test'`) in the username field returned a raw SQL syntax error,
  confirming the input was concatenated directly into the query.
- Payload used:

  ```
  Username: test' OR 1=1 --
  Password: (any)
  ```

- Result: authenticated as a standard user (`dave`, role: `user`) without
  valid credentials.

### 3. Sensitive Data Exposure — Leaked JWT Secret

- Viewed page source (`view-source:`) of the authenticated `/user` page.
- Found a developer comment left in the HTML:

  ```html
  <!--
  Dave, the JWT secret needs changing, bGV0bWVpbjEyMw==
  it's less secure now that you put it as a note in the html
  Don't worry Dave, I encoded it, nobody will be able to read it now
  -->
  ```

- The string was Base64-encoded (not encrypted). Decoded via CyberChef
  ("From Base64"):

  ```
  bGV0bWVpbjEyMw==  ->  letmein123
  ```

### 4. Privilege Escalation — JWT Forgery

- Retrieved the session JWT from `document.cookie` / DevTools → Storage →
  Cookies.
- Decoded payload (jwt.io):

  ```json
  {
    "id": 1,
    "username": "dave",
    "role": "user",
    "iat": 1787622343,
    "exp": 1787629543
  }
  ```

- Modified `role` to `"admin"` and re-signed the token (HS256) using the
  leaked secret `letmein123`.
- Replaced the `token` cookie value in the browser with the forged JWT.
- Reloaded `/admin` → access granted. Obtained an interactive **admin
  terminal** (`admin[dave]@LEGO:/root$`).

### 5. IoT / ICS Manipulation — Modbus (modpoll)

- Admin terminal exposed limited commands, including `modpoll`.
- Used `modpoll` (Modbus TCP client) to write directly to PLC holding
  registers on the rail control PLC (`10.0.10.11`, port 502):

  ```bash
  # Track switch: OFF -> ON (discrete/coil value)
  modpoll -m tcp -p 502 -r 40001 -t 0 10.0.10.11 1

  # Motor speed: change register value (32-bit)
  modpoll -m tcp -p 502 -r 40003 -t 4 10.0.10.11 50
  ```

- Verified changes reflected live on the "Field Device Status" panel of the
  user dashboard (Track Switch State: ON, Motor Speed updated).
- Demonstrates that a web-layer vulnerability chain (SQLi → JWT forgery)
  can escalate into direct control of physical/industrial equipment when
  Modbus is exposed without authentication or encryption.

## Blue Team Validation (Wazuh SIEM)

- Logged into Wazuh (`https://10.12.237.42/`) and queried
  `wazuh-alerts-*` for `admin access granted to dave` and Modbus commands.
- Confirmed detection of every step performed as Red Team:

  ```
  rule.description: Lego-app: privilege escalation - admin access granted to dave
  rule.level: 15 (critical)
  data.username: dave
  data.input: modpoll -m tcp -p 502 -r 40003 -t 4 10.0.10.11 50
  rule.mitre.tactic: Defense Evasion, Lateral Movement
  rule.mitre.technique: Application Access Token
  rule.mitre.id: T1550.001
  ```

- All Modbus write commands were logged as
  `unauthorized Modbus write command executed by dave via privileged...`.

## Root Causes / Vulnerabilities Identified

| # | Vulnerability | Location | Impact |
|---|---|---|---|
| 1 | SQL Injection | `/login.html` | Authentication bypass |
| 2 | Sensitive data exposure (hardcoded secret, Base64 mistaken for encryption) | HTML source comment | JWT secret compromise |
| 3 | Broken access control / privilege escalation | JWT `role` claim, no server-side re-validation | Full admin takeover |
| 4 | Unauthenticated Modbus/ICS interface | Port 502, PLC `10.0.10.11` | Unauthorized physical device control |

## Key Takeaways

- Base64 is encoding, **not** encryption — never rely on it to hide secrets.
- JWTs are only as strong as the secrecy of their signing key; a leaked
  secret allows an attacker to mint arbitrary valid tokens.
- Client-side role claims must always be re-validated server-side against
  a trusted source (e.g. a database), not trusted at face value from the
  token.
- Industrial control protocols like Modbus TCP have no built-in
  authentication — network segmentation and access control are essential
  when these systems are reachable from IT networks.
- The full kill chain (SQLi → secret leak → JWT forgery → privilege
  escalation → ICS manipulation) was independently confirmed by SIEM logs,
  reinforcing the value of detection/monitoring even when prevention
  fails at one layer.
