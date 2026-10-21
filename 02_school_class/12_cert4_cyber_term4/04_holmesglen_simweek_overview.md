# Holmesglen Simulation Week — Web App Pentest Overview (Concept Summary)

**Date:** 20 October 2026
**Context:** Holmesglen Institute, VU23219/VU23221 (Cert IV Cyber Security), "Simulation Week" hands-on activity — a controlled, lab-only exercise against a deliberately vulnerable practice web app on an isolated host-only network.

## What the exercise covered

The activity walked through a full attack lifecycle against a lab target, mirroring the stages in MITRE ATT&CK:

1. **Reconnaissance / Discovery** — identifying live hosts and open services on the private lab subnet, then fingerprinting the web application's technology stack and enumerating hidden/unlinked paths.
2. **Initial Access** — the login form was vulnerable to a classic SQL injection authentication bypass, letting an attacker log in without valid credentials.
3. **Privilege Escalation** — the authenticated session used a JSON Web Token (JWT) signed with a symmetric secret (HS256). The app's own source left a clue that effectively exposed how the secret was stored, illustrating a common real-world mistake: treating encoding (e.g. Base64) as if it were encryption. Once the signing secret is known, an attacker can forge tokens with elevated claims.
4. **Impact** — the forged admin session exposed an in-app admin console that could issue commands to simulated IoT/industrial devices over Modbus, a protocol with no built-in authentication — demonstrating how a web-app compromise can cascade into control of connected physical/IoT systems.

## Key takeaways

1. **Error-based reconnaissance matters.** Deliberately triggering errors or unexpected input reveals a lot about how a backend is built, which shapes what to try next.
2. **Classic injection bypasses still work when input isn't parameterised.** A boolean-based SQL injection doesn't need real credentials — it just needs a query structure that can be forced true.
3. **Encoding is not encryption.** Developers sometimes mistake Base64 (or similar encoding) for a security control. It isn't — it's trivially reversible and provides no confidentiality.
4. **Symmetric JWT signing is only as strong as the secret.** If the signing secret leaks, anyone can forge arbitrary claims (e.g. privilege escalation from a normal user to admin) without ever needing the original password.
5. **IoT/industrial protocols often have no authentication by default.** Once an attacker has network access (here, via the compromised admin console), unauthenticated protocols like Modbus let them directly manipulate connected devices.
6. **Full attack chains map cleanly onto MITRE ATT&CK stages**: Reconnaissance → Discovery → Initial Access → Privilege Escalation → Impact. This framing is useful for structuring incident response documentation (e.g. Tools/Techniques/Procedures, Attack Scenarios, Successful Breach Points sections of an assessment report).

## Why this matters for defenders

- Input validation and parameterised queries prevent the injection class of bugs entirely.
- Secrets (JWT signing keys, API keys, etc.) should never be stored in client-reachable code, comments, or source — use a secrets manager / environment-level secret store.
- Segment and authenticate OT/IoT protocols (e.g. Modbus) separately from general IT networks; don't assume network-level access implies authorised access.
- Principle of least privilege on admin interfaces reduces the blast radius if any single account is compromised.

*(Note: this write-up intentionally omits exact payloads, secret values, and reproducible commands used in the lab exercise, since the underlying vulnerable app and lab setup are reused for other students' assessments.)*
