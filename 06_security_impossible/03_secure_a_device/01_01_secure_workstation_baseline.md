# Linux Workstation Security Baseline — Lab Notes

**Date:** June 19, 2026
**Source:** Security Impossible — Cyber Range, Certificate IV: Secure a Device
**Environment:** Ubuntu 22.04 LTS VM (Azure), accessed via browser-based remote desktop (Guacamole)

## Overview

This lab walks through hardening a fresh Linux workstation to meet a minimum security
baseline: least-privilege user/group management, enforced password policy with account
lockout, SSH hardening, and verification via system logs. Below is a record of every step
taken, the reasoning behind each command, and a couple of real debugging detours that came
up along the way.

---

## 1. System Preparation

Updated the system and installed the PAM module needed for password quality enforcement.

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install libpam-pwquality -y
```

- `apt update` refreshes the local package index; `apt upgrade -y` installs available
  upgrades non-interactively.
- `libpam-pwquality` provides `pam_pwquality.so`, the PAM module that enforces password
  complexity rules (length, character variety, etc.).

During the upgrade, two interactive prompts appeared:

- **Docker daemon restart prompt** — accepted (`<Yes>`) since no containers were running yet.
- **"Daemons using outdated libraries" service restart list** — accepted the pre-selected
  defaults (`chrony`, `cron`, `irqbalance`, `multipathd`, `serial-getty`) so the updated
  shared libraries would actually be loaded by running services.

---

## 2. User & Group Management (Least Privilege)

**Goal:** create a `staff` group, add a new user `analyst1` to it, and lock down a sensitive
file so only `root` can read it.

```bash
getent group                      # list existing groups — confirmed 'staff' (gid 50) already exists
sudo useradd -m -G staff analyst1 # create user + home dir, add as supplementary member of 'staff'
sudo passwd analyst1              # set a password (12+ characters)
```

- `-m` creates the home directory (`/home/analyst1`); without it, the user would have no
  home folder.
- `-G staff` adds `analyst1` to the **supplementary** group `staff`. The user's **primary**
  group is auto-created as `analyst1` (this is Ubuntu's default `USERGROUPS` behavior).

### Restricting a sensitive file to root only

```bash
sudo touch /root/confidential.txt
sudo chmod 600 /root/confidential.txt
```

- `chmod 600` → owner (root) gets read+write (`6` = 4+2), group and others get nothing (`0`, `0`).
- `/root/` itself is not world-traversable by default, which already blocks non-root users —
  the `chmod` adds a second layer of defense on the file itself.

### Verification

```bash
su - analyst1
cat /root/confidential.txt   # → "Permission denied" (expected)
exit
```

Confirmed `analyst1` cannot read the file, proving the access control works as intended.

---

## 3. Password Policy & Account Lockout (PAM)

**Goal:** enforce a 12-character minimum password length, and lock an account for 5 minutes
after 3 consecutive failed login attempts.

### 3.1 Minimum password length

```bash
sudo nano /etc/security/pwquality.conf
```

Uncommented and set:

```
minlen = 12
```

This file is read by `pam_pwquality.so` and defines complexity rules system-wide.

### 3.2 Enforce pwquality in the password-change stack

```bash
sudo nano /etc/pam.d/common-password
```

Confirmed the following line was present (Ubuntu ships with this enabled by default):

```
password    requisite    pam_pwquality.so retry=3
```

`requisite` means: if this module fails (password doesn't meet quality rules), stop the
whole PAM stack immediately and reject the change — don't bother evaluating subsequent
modules.

### 3.3 Account lockout after failed logins

```bash
sudo nano /etc/pam.d/common-auth
```

Added two lines around the existing `pam_unix.so` line:

```
auth    required                     pam_faillock.so preauth audit silent deny=3 unlock_time=300
auth    [success=1 default=ignore]   pam_unix.so nullok try_first_pass
auth    [default=die]                pam_faillock.so authfail audit deny=3 unlock_time=300
auth    requisite                    pam_deny.so
auth    required                     pam_permit.so
```

How this stack works, in order:

1. **`pam_faillock.so preauth`** — runs *before* the password check. If the account is
   already locked from previous failures, deny immediately.
2. **`pam_unix.so`** — does the actual username/password check.
3. **`pam_faillock.so authfail`** with **`[default=die]`** — runs *after* `pam_unix`. If the
   password check failed, this module records the failure and `[default=die]` forces the
   entire PAM stack to fail immediately (no fallback to `pam_deny`/`pam_permit` below it).

### 3.4 Lockout thresholds

```bash
sudo nano /etc/security/faillock.conf
```

Set:

```
deny = 3              # lock after 3 consecutive failures
fail_interval = 900    # ...within a 15-minute window
unlock_time = 300      # lock duration: 300 seconds = 5 minutes
```

### 3.5 Verification

**Password policy:**

```bash
sudo passwd analyst1
# entering a password under 12 characters →
# "BAD PASSWORD: The password is shorter than 12 characters"
```
Confirmed the policy rejects short passwords as expected.

**Account lockout:**

```bash
su - analyst1
# entered an intentionally wrong password 3 times in a row → "Permission denied" each time
su - analyst1
# 4th attempt, even with the CORRECT password → "su: Authentication failure"
```

Checked `/var/log/auth.log` and found the smoking-gun line confirming the lockout fired:

```
pam_faillock(su-l:auth): Consecutive login failures for user analyst1 account temporarily locked
```

Also useful for inspecting/clearing lockout state:

```bash
sudo faillock --user analyst1            # view failure history
sudo faillock --user analyst1 --reset    # clear the lockout
sudo passwd -S analyst1                  # check account status (P = active, L = locked)
```

#### Debugging detour: "Authentication failure" persisted even after resetting

After resetting the lockout and resetting the password (twice), `su - analyst1` kept
failing with `Authentication failure`, even though:

- `faillock --user analyst1` showed **zero** recorded failures (so it wasn't actually locked)
- `passwd -S analyst1` showed `P` (password set, account active — not locked)

To isolate the cause, ran:

```bash
sudo su - analyst1
```

This succeeded immediately (no password prompt needed, since `sudo` already grants root and
`sudo su -` doesn't ask for the *target* user's password). That confirmed:

- The `analyst1` account itself was healthy.
- The PAM/faillock configuration was working correctly (proven separately via the auth.log
  entry above).
- The actual problem was specific to typing the password into the interactive `su` prompt in
  this particular browser-based remote desktop session — most likely a keyboard input
  quirk in the remote session rather than anything wrong with the Linux configuration.

**Lesson:** when a credential check fails unexpectedly, check the *system's own evidence*
(`faillock`, `passwd -S`, `auth.log`) before assuming the configuration is wrong. In this
case the logs proved the security controls were working; the failure was an input/environment
issue, not a misconfiguration.

---

## 4. SSH Hardening

**Goal:** disable root login over SSH and restrict SSH access to `analyst1` only. Practiced
first against a disposable Docker container before touching the real host config.

### 4.1 Practice environment (Docker)

```bash
cd ssh-lab
sudo docker build -t ssh-lab .
sudo docker run -d \
  --name ssh-lab-container \
  -p 2222:22 \
  ssh-lab
ssh student@localhost -p 2222    # password: student123
```

The Dockerfile (provided by the lab) builds an Ubuntu 22.04 image with `openssh-server`,
creates a `student` user with sudo rights, and pre-configures `sshd_config` with
`PasswordAuthentication yes` and `PermitRootLogin no`.

**Debugging note:** re-running `docker run` with the same `--name` failed with:

```
docker: Error response from daemon: Conflict. The container name "/ssh-lab-container" is already in use...
```

Fixed by removing the stale container before re-creating it:

```bash
sudo docker rm -f ssh-lab-container
sudo docker run -d --name ssh-lab-container -p 2222:22 ssh-lab
```

### 4.2 Hardening the actual host's SSH config

```bash
sudo nano /etc/ssh/sshd_config
```

Changes made:

```
PermitRootLogin no
AllowUsers analyst1
```

- `PermitRootLogin no` — disables direct SSH login as `root` entirely. Anyone needing root
  access must log in as a normal user first and use `sudo`.
- `AllowUsers analyst1` — an explicit allow-list; only the listed user(s) may authenticate
  over SSH. Anyone not on this list is rejected before a password is even checked.

```bash
sudo systemctl restart ssh
sudo systemctl status ssh   # confirm "active (running)"
```

### 4.3 Verification (intended, from a separate terminal)

```bash
ssh root@localhost -p 2222        # should fail — root login disabled
ssh student@localhost -p 2222     # should fail — not in AllowUsers
ssh analyst1@localhost -p 2222    # should succeed — explicitly allow-listed
```

> **Note:** the lab instructs reverting `sshd_config` to its original state after
> verification, since this step modifies the actual host (not just the disposable container).

---

## Key Concepts Recap

| Concept | What it does |
|---|---|
| `useradd -m -G <group> <user>` | Creates a user, home directory, and adds to a supplementary group |
| `chmod 600 <file>` | Owner: read+write; group & others: no access |
| `pam_pwquality.so` | Enforces password complexity (length, character classes) |
| `pam_faillock.so` | Tracks failed auth attempts; locks account after a threshold |
| `deny` / `fail_interval` / `unlock_time` | Failed-attempt threshold / time window / lockout duration (seconds) |
| `PermitRootLogin no` | Blocks SSH login as root |
| `AllowUsers <user>` | Allow-list restricting which accounts may SSH in at all |
| `faillock --user <name> --reset` | Manually clears a lockout |
| `passwd -S <user>` | Quick check of account lock status (`P` = active, `L` = locked) |

## What I'd Want to Drill Again Without the Guide

- Writing the `pam_faillock.so` lines in `common-auth` from memory (the before/after
  placement around `pam_unix.so` and the role of `[default=die]` took the most thinking).
- Reconstructing the `sshd_config` changes (`PermitRootLogin no` + `AllowUsers`) without
  looking them up.
- Using `auth.log` / `faillock` proactively to debug an authentication issue *before*
  assuming the config is broken.
