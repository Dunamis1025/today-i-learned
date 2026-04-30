# TIL: Advanced Git Log Analysis & Metadata Leakage

## 1. Challenge Overview: "Blame Game"
- **Platform:** picoCTF 2024
- **Category:** General Skills
- **Goal:** Identify the specific commit or metadata containing the flag in a project with extensive history.
- **Key Learning:** Sensitive data (flags, credentials, or personal info) can be hidden not just in the code, but in the **Git commit metadata** (Author, Date, or Commit Messages).

---

## 2. Practical Workflow

### Step 1: Entry and Navigation
To perform any Git-related operations, you must be inside the directory containing the `.git` metadata folder.
```bash
unzip challenge.zip
cd drop-in
```
## 2. Efficient Searching with Pipes
When dealing with hundreds of commits, manually scrolling through `git log` is inefficient. Using the `grep` command with a specific pattern is the professional way to solve this.

- **Command Used:**
```bash
git log | grep "picoCTF{"
```

- **Why this works:** Including the opening brace `{` narrows down the search results specifically to the flag format, filtering out generic "picoCTF" mentions in emails or descriptions.

---

## 3. Findings & Flag
- **Observation:** The flag was hidden in the **Author** field of a commit, masked as an email-like identity.
- **Flag:** `picoCTF{@sk_th3_1nt3rn_d2d29f22}`
- **Hint Reference:** The challenge hinted at "who" prevented the program from working, pointing towards the author/contributor identity.

---

## 4. Technical Summary & Tips

| Feature | Command | Usage in CTF/Forensics |
| :--- | :--- | :--- |
| **Filtered Search** | `git log | grep "keyword"` | Quickly find flags in commit messages or author info. |
| **Metadata Attribution** | `git blame <file>` | Identify who changed a specific line of code. |
| **History Navigation** | `q` | Exit the `less` pager (used when logs are long). |
| **Compact View** | `git log --oneline` | View high-level project flow to spot anomalies. |

---

## 5. Security Takeaway
This challenge demonstrates a real-world vulnerability: **Metadata Leakage**. Even if the final version of the code is secure, the entire history of the repository is archived. Developers must use tools like `git-filter-repo` or `BFG Repo-Cleaner` if they accidentally commit sensitive information to a public repository.
