# 29_Commitment_Issues.md

## 🚩 Challenge Overview
- **Challenge Name:** Commitment Issues
- **Category:** General Skills
- **Point of Interest:** Git version control forensics

## 🚧 Troubleshooting & Lessons Learned
This challenge was a perfect example of why "deleted" doesn't mean "gone" in a Git-managed project. I encountered several hurdles that made this more than a simple `cat` exercise:

1.  **Directory Confusion:** The `unzip` process extracted files into a directory named `drop-in/`, not the expected `challenge/`.
2.  **Commit State Awareness:** The "add flag" commit actually removed the flag content in the same breath. Attempting to `cat flag.txt` at the current HEAD returned an empty file because the "current" state was the "deleted" state.
3.  **Hash Volatility:** Re-extracting the challenge ZIP changed the commit hashes, reminding me to always verify the current state with `git log` before running commands.

## 🛠 Command Deep Dive
These are the specific commands I used to navigate the history and recover the data:

| Command | Why I used it |
| :--- | :--- |
| `git log --oneline` | To find the specific commit where the flag was mentioned. |
| `git show HEAD` | To see the "diff" (difference) of the current commit. This revealed the flag in red (`-`), showing it had been written and then deleted. |
| `git checkout <hash>` | To move the HEAD to a previous state to inspect the file structure at that specific time. |
| `git grep "pico" $(git rev-list --all)` | A "nuclear option" to search for the string "pico" across every single commit ever made in this repo. |
| `git diff <hash1> <hash2>` | To compare the starting state with the "add flag" state to see exactly what changed. |

## 💡 Final Solution
1.  Navigate to the source: `cd drop-in`.
2.  Inspect the commit history: `git log --oneline`.
3.  Examine the most recent commit's changes: `git show 3899edb` (or `git show HEAD`).
4.  The flag was found as a deleted line in the diff: `picoCTF{s@n1t1z3_9539be6b}`.

## 📝 Reflection
As a former chef, I know that even if you wipe the counter, you might find crumbs in the cracks. Git is the same—the metadata and commit history are the "cracks" where sensitive information often hides. In cybersecurity, we call this **Information Exposure through Version Control**.
