# [picoCTF] SUDO MAKE ME A SANDWICH - Writeup

## Challenge Description
- **Category:** General Skills
- **Difficulty:** Easy
- **Challenge:** The goal is to read the `flag.txt` file, which is restricted to the root user. The challenge focuses on understanding `sudo` permissions and privilege escalation through misconfigured binary permissions.

## Key Concepts

### 1. SSH (Secure Shell)
- Used the command `ssh -p <port> ctf-player@<host>` to connect to the remote challenge server.
- The `-p` flag specifies the **Port** number required for the connection.

### 2. Sudo & Permissions
- **Sudo (Substitute User DO):** Allows a permitted user to execute a command as the superuser (root).
- **sudo -l:** A crucial command used to list the allowed (and forbidden) commands for the invoking user.



## Step-by-Step Solution

### Step 1: Connecting to the Server
After launching the instance, I connected via SSH and entered the provided password.
```bash
ssh -p 51708 ctf-player@green-hill.picoctf.net
# Password: deebe023
```

### Step 2: Checking Privileges
Once logged in as ctf-player, I checked which commands I could run with sudo privileges without a password.

```bash
sudo -l
```

## Output:
(ALL) NOPASSWD: /bin/emacs
This indicated that I could run the emacs text editor as root without needing a password.

### Step 3: Exploiting Misconfiguration
Since I didn't have permission to use cat on flag.txt, I used the allowed emacs binary to open the file with root privileges.

```bash
sudo emacs /home/ctf-player/flag.txt
```

### Step 4: Retrieving the Flag
Inside the Emacs editor, the flag was displayed. After copying the flag, I exited Emacs using Ctrl+x followed by Ctrl+c.

## Conclusion
This challenge demonstrates a common Privilege Escalation vector where a user is granted sudo access to a powerful binary (like a text editor). Because editors can open and read any file on the system, giving them sudo access is equivalent to giving full root access to the sensitive files.
