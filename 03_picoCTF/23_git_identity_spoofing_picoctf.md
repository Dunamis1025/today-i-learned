# 📝 Today I Learned: 2026-04-10

## 🚩 Challenge: picoCTF - MY GIT
**Category:** General Skills / Git Exercise
**Difficulty:** Easy (Technical perspective), Medium (Infrastructure perspective)

---

### 1. Learning Objective
The primary goal of this challenge was to understand how **Git identity configurations** work and how they can be exploited through **identity spoofing (Impersonation)** if proper authentication mechanisms (like GPG signing) are not enforced.

---

### 2. Technical Concepts

#### A. Git Identity Spoofing (Impersonation)
In Git, the `user.name` and `user.email` configurations are metadata attached to a commit. By default, Git does not verify if the person committing is actually who they claim to be in the config.
* **The Exploit:** By changing the local config to match a privileged user (e.g., `root`), a user can bypass simple server-side identity checks that rely solely on commit metadata.
* **Key Commands:**
  `git config user.name "root"`
  `git config user.email "root@picoctf"`

#### B. SSH Connectivity & Dynamic Ports
Working with on-demand cloud instances (like picoCTF's webshell/instances) introduces infrastructure-level hurdles.
* **Issue:** `Connection refused` on a specific SSH port.
* **Root Cause:** The instance might have timed out, or the specific port was closed/changed upon restarting.
* **Solution:** Restarting the instance to assign a new valid port and updating the SSH connection string accordingly.

---

### 3. Step-by-Step Resolution

1. **Initialize Environment:** Clear previous failed attempts to ensure a clean workspace.
   `rm -rf challenge`

2. **Clone the Repository:** Connect to the remote server using the assigned SSH port.
   `git clone ssh://git@foggy-cliff.picoctf.net:53594/git/challenge.git`
   *(Note: Use the password `1a03c9e3` when prompted.)*

3. **Perform Identity Spoofing:** Modify local Git settings to impersonate the `root` user.
   `cd challenge`
   `git config user.name root`
   `git config user.email root@picoctf`

4. **Create and Commit:** Create the required file and commit it with the spoofed identity.
   `touch flag.txt`
   `git add flag.txt`
   `git commit -m "add flag"`

5. **Push and Capture Flag:** Push the changes to the master branch.
   `git push origin master`
   **Resulting Flag:** `picoCTF{1mp3rs0n4t4_g17_345y_367122f4}`

---

### 4. Troubleshoot & Reflections
* **Infrastructure Sensitivity:** Even if the commands are correct, network issues or server-side instance states can cause fatal errors (e.g., `Connection refused`). Methodical troubleshooting of the connection string is a core skill.
* **Security Implication:** This exercise highlights why **GPG signing** is essential in professional environments to prevent unauthorized users from committing code under an administrator's identity.
* **Persistence:** Despite technical inconsistencies with the tools (AI and Server), staying focused on the objective led to the successful capture of the flag.

---

### 5. Summary of Commands Used
* `git clone`: Clones the remote repository via SSH.
* `git config`: Sets the identity for the current repository.
* `git add / commit`: Stages and records the changes.
* `git push`: Sends local commits to the remote server.
* `rm -rf`: Forcefully removes a directory to reset the environment.
