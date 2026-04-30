# 28. FANTASY CTF — Terminal Game & picoCTF Rules

**Platform:** picoCTF (picoGym)
**Category:** General Skills
**Difficulty:** Easy
**Points:** 10
**Solves:** 43,693

---

## Challenge Description

> Play this short game to get familiar with terminal applications and some of the most important rules in scope for picoCTF. Additional details will be available after launching your challenge instance.

**Hint:** When a choice is presented like `[a/b/c]`, choose one (e.g. `c`) and press Enter.

---

## Tools Used

- `nc` (netcat) — connect to remote server via TCP

---

## Solution

### Step 1 — Launch the instance

Click **Launch Instance** on the challenge page. Wait until the status changes from `NOT_RUNNING` to `RUNNING`. The page will display a netcat connection command, e.g.:

```
$ nc verbal-sleep.picoctf.net 59102
```

### Step 2 — Open Webshell

Go to [webshell.picoctf.org](https://webshell.picoctf.org) (or click the `>_ Webshell` button in the top-right of the picoCTF site). This opens a browser-based Linux terminal — no local setup required.

### Step 3 — Connect to the server

Paste the command from Step 1 into the Webshell and press Enter:

```bash
nc verbal-sleep.picoctf.net 59102
```

> Note: `nc verbal -sleep...` (with a space) will fail — make sure there is no space in the hostname.

### Step 4 — Play the story game

The challenge is a text-based interactive fiction game set in a futuristic world. A character named **Eibhilin** is registering for picoCTF 3025 with her AI companion **Nyx**.

Press **Enter** repeatedly to advance through the story. When a choice appears, type the letter and press Enter.

---

### Choice 1 — Account registration

```
Options:
A) *Register multiple accounts*
B) *Share an account with a friend*
C) *Register a single, private account*
[a/b/c] >
```

**Answer: `c`**

**Reason:** picoCTF rules require one account per person. Registering multiple accounts or sharing accounts is a violation that can lead to disqualification.

---

### Choice 2 — How to find the flag

```
Options:
A) *Play the game*
B) *Search the Ether for the flag*
[a/b] >
```

**Answer: `a`**

**Reason:** In CTF competitions, the intended approach is to solve challenges yourself. Searching externally for flags (e.g. looking up writeups during a live competition) goes against the spirit of the competition.

---

### Step 5 — Receive the flag

After the correct choices, the game completes automatically:

```
Playing the Game: 100% [time left: 00:00]
Playing the Game completed successfully!

"Thanks, Nyx! Here's the flag I found: picoCTF{m1113n1um_3d1710n_1e2b417a}"

"Great, you just got 10 points!" Nyx exclaims.
```

### Step 6 — Submit the flag

Copy the flag and paste it into the **Submit Flag** field on the challenge page:

```
picoCTF{m1113n1um_3d1710n_1e2b417a}
```

---

## Key Concepts Learned

| Concept | Details |
|---|---|
| `nc` (netcat) | A command-line tool for reading/writing data over TCP/UDP connections. Used to connect to CTF challenge servers. Syntax: `nc <host> <port>` |
| picoCTF account rules | One account per person. No account sharing. Violations = disqualification. |
| Writeup policy | During a live competition, do not publish solutions publicly. Wait until winners are announced. |
| CTF flag format | Flags follow the format `picoCTF{...}`. The content inside the braces is unique to each challenge. |
| picoGym vs Competition | picoGym is a non-competitive practice space. The annual competition (picoCTF 2025) ran March 7–17, 2025. After the competition ends, writeups can be published freely. |

---

## picoCTF Rules Summary (learned from this challenge)

1. **One account per person** — do not register multiple accounts
2. **No account sharing** — each participant must have their own account
3. **Solve challenges yourself** — don't look up flags during a live competition
4. **Writeup timing** — publish solutions only after winners are announced

---

## Reflection

This was the first CTF challenge I solved. Even though the difficulty was Easy and no technical hacking was required, it taught me:

- How to use `nc` to connect to a remote server
- The workflow of launching an instance and using the Webshell
- Core picoCTF rules that apply to all challenges
- What a flag looks like and how to submit it

A great starting point before tackling real technical challenges.
