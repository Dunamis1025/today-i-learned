# Local AAA Authentication for Console and VTY (SSH) Access

**Course:** 22603VIC – Certificate IV in Cyber Security
**Unit:** VU23218 – Implement Network Security Infrastructure for an Organisation
**Module:** 7 – AAA (Authentication, Authorization, Accounting)
**Date:** 2026-08-13

---

## 1. AAA Fundamentals

**AAA** stands for the three pillars of access control on network devices:

- **Authentication** – verifying *who* you are (username/password, certificates, etc.)
- **Authorization** – determining *what* you're allowed to do once authenticated (privilege levels, command restrictions)
- **Accounting** – logging *what you actually did* (for auditing/troubleshooting)

### Multi-Factor Authentication (MFA) — 5 factors
1. **Something you know** – password, PIN
2. **Something you have** – token, smart card, phone
3. **Something you are** – biometrics (fingerprint, face)
4. **Somewhere you are** – geolocation-based access
5. **Something you do** – behavioral biometrics (typing pattern, gesture)

### Federation & SSO
- **Federation** – trust relationship between multiple organizations/systems allowing shared authentication across domains.
- **SSO (Single Sign-On)** – one login grants access to multiple independent systems without re-authenticating each time.

### Local AAA vs Server-Based AAA
| Type | Where credentials live | Example |
|---|---|---|
| **Local AAA** | Device's own local username database | `username` command on the router itself |
| **Server-Based AAA** | Centralized external server | RADIUS, TACACS+ |

Local AAA doesn't scale well (each device has its own account list), so larger networks typically move to server-based AAA (covered briefly today, hands-on lab assigned as self-paced follow-up: 7.4.9).

---

## 2. Lab Topology (Packet Tracer 7.2.6)

```
PC-B --- S2 --- R2 --- S3 --- PC-C
                / \
              R1   R3
               |
               S1 --- PC-A
```

| Device | Interface | IP Address | Notes |
|---|---|---|---|
| R1 | G0/1 | 192.168.1.1/24 | connects to PC-A via S1 |
| R1 | S0/0/0 (DCE) | 10.1.1.2/30 | link to R2 |
| R2 | G0/0 | 192.168.2.1/24 | connects to PC-B via S2 |
| R2 | S0/0/1 (DCE) | 10.2.2.1/30 | link to R3 |
| R3 | G0/1 | 192.168.3.1/24 | connects to PC-C via S3 |

Pre-configured (given, not part of today's task):
- `enable secret`: `ciscoenpa55`
- OSPF with MD5 authentication, key `MD5pa55`

---

## 3. Part 1 — Local AAA for Console Access

### Step 1: Create a local user account
```
R1(config)# username Admin1 secret admin1pa55
```
- `secret` (vs `password`) stores the password **hashed**, not in plaintext, in the running-config.

### Step 2: Enable AAA and define the authentication method
```
R1(config)# aaa new-model
R1(config)# aaa authentication login default local
```
- `aaa new-model` switches the router from legacy line-password auth to the AAA framework.
- `aaa authentication login default local` creates a **method list** named `default` (unnamed lists are auto-applied everywhere) that authenticates logins against the **local** username database.

### Step 3: Apply the method to the console line
```
R1(config)# line console 0
R1(config-line)# login authentication default
```
- Legacy: `line console 0` + `password X` + `login` → single shared password, no per-user identity.
- AAA way: `login authentication <method-list-name>` → requires **username + password**, tied to a specific method list.

### Step 4: Verify
- Exiting and reconnecting to the console now prompts for **Username** *and* **Password** (previously password-only).
- Confirmed working: login as `Admin1` / `admin1pa55` → dropped into `R1>`.

---

## 4. Part 2 — Local AAA for VTY Lines (SSH)

### Why SSH instead of Telnet?
VTY lines are accessed **remotely over the network**, unlike the console (direct physical cable). Telnet sends credentials in **plaintext** — vulnerable to sniffing. SSH encrypts the session, so VTY access is hardened by requiring SSH only.

### Step 1: Domain name + RSA key pair (required for SSH)
```
R1(config)# ip domain-name netsec.com
R1(config)# crypto key generate rsa
How many bits in the modulus [512]: 1024
```
- The domain name is used to auto-generate the key's label: `R1.netsec.com`.
- `crypto key generate rsa` creates an **asymmetric key pair**:
  - **Public key** – used to encrypt / verify, safe to share.
  - **Private key** – stays on the router only (marked *non-exportable*), used to decrypt.
- Generating this key pair automatically enables the SSH server on the router (log: `%SSH-5-ENABLED: SSH 1.99 has been enabled`).
- Alternative one-line syntax used by the instructor: `crypto key generate rsa general-keys modulus 1024` (same result, no interactive prompt).

### Step 2: Named method list for VTY
```
R1(config)# aaa authentication login SSH-LOGIN local
```
- Same concept as `default`, but explicitly named `SSH-LOGIN` so it can be applied only to VTY, separately from console.

### Step 3: Apply to VTY lines + restrict transport
```
R1(config)# line vty 0 4
R1(config-line)# login authentication SSH-LOGIN
R1(config-line)# transport input ssh
```
- `line vty 0 4` selects **5 virtual terminal lines** (0–4) → up to 5 simultaneous remote sessions.
- `login authentication SSH-LOGIN` ties these lines to the SSH-LOGIN method list.
- `transport input ssh` **blocks Telnet**, allowing only SSH connections in.

### Step 4: Verify from PC-A
```
PC> ssh -l Admin1 192.168.1.1
Password: admin1pa55
```
- `-l Admin1` = "login as Admin1"
- Successful login returns the `R1>` prompt on PC-A — confirms encrypted remote access works end-to-end.

---

## 5. Saving the Configuration

```
R1# copy running-config startup-config
```
- Copies the active (running) config to NVRAM (startup-config) so it survives a reboot.
- Tip from a classmate: prefer `copy run start` over relying on the configuration register — if the config register is set wrong, a reload could wipe changes; `copy run start` just persists whatever is currently running, regardless of register state.
- Also remember to save the actual Packet Tracer `.pka` file.

---

## 6. Quick Command Reference

```
! Local AAA — Console
username Admin1 secret admin1pa55
aaa new-model
aaa authentication login default local
line console 0
 login authentication default

! Local AAA — VTY / SSH
ip domain-name netsec.com
crypto key generate rsa           ! choose 1024 bits when prompted
aaa authentication login SSH-LOGIN local
line vty 0 4
 login authentication SSH-LOGIN
 transport input ssh

! Save config
copy running-config startup-config
```

---

## 7. Preview — Server-Based AAA (next self-paced task: 7.4.9)

Introduced conceptually today; full hands-on left as homework.

```
aaa new-model

tacacs server Server-T
 address ipv4 192.168.1.100
 single-connection
 key TACACS-Pa55w0rd
 exit

radius server SERVER-R
 address ipv4 192.168.1.101 auth-port 1812 acct-port 1813
 key RADIUS-Pa55w0rd
 exit

aaa authentication login default group tacacs+ group radius local-case
```

- Defines a **fallback chain**: try TACACS+ server first → if unreachable, try RADIUS server → if that also fails, fall back to the local username database.
- Server-based AAA centralizes credential management across many devices instead of maintaining separate local accounts on each one.

**Homework:** Packet Tracer 7.4.9 – Configure Server-Based Authentication with TACACS+ and RADIUS (self-paced, follow-up guide provided: *Step-by-step How to configure AAA_TACACS_RADIUS_Access Guide*).

---

## Key Takeaways
- `aaa new-model` is the master switch that turns on AAA framework.
- Method lists (`default` or custom-named) define *how* to authenticate; applying them to a line (`login authentication <list>`) defines *where* that rule is enforced.
- `secret` > `password` for storing credentials (hashed vs plaintext).
- Console = physical/local trust boundary; VTY = remote, so it needs encryption (SSH) + explicit method list.
- RSA key pair is mandatory before SSH can function on an IOS device.
- Local AAA doesn't scale — server-based AAA (TACACS+/RADIUS) is the enterprise-grade next step.
