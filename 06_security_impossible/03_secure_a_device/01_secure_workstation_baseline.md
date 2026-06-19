# Secure a Device

Lab notes from **Security Impossible — Cyber Range**, part of the *Certificate IV: Secure a
Device* track. Each lab focuses on a hands-on Linux endpoint-hardening task, with the
commands used, the reasoning behind each step, and any debugging encountered along the way.

## Labs

| # | Lab | Topics |
|---|---|---|
| 01 | [Secure Workstation Baseline Configuration](./01_secure_workstation_baseline.md) | User/group management, PAM password policy & account lockout, SSH hardening |

## Skills Practiced

- Least-privilege user and group management (`useradd`, `groupadd`, `chmod`)
- Password policy enforcement via PAM (`pam_pwquality`)
- Account lockout on repeated failed logins (`pam_faillock`)
- SSH hardening (`sshd_config`: `PermitRootLogin`, `AllowUsers`)
- Verifying security controls using system logs (`auth.log`, `faillock`, `passwd -S`)
