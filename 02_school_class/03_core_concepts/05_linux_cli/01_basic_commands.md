# Linux / CLI - Basic Commands

Linux Command Line Interface (CLI) allows users to interact with the system using text-based commands.

Understanding basic commands is essential for system administration, cybersecurity, and automation.

---

# 📁 Navigation Commands

## pwd (Print Working Directory)
Shows the current directory path.

    pwd

---

## ls (List)
Lists files and directories.

    ls
    ls -l      # detailed list
    ls -a      # include hidden files
    ls -la     # detailed + hidden

---

## cd (Change Directory)
Moves between directories.

    cd /home/user
    cd ..        # go up one level
    cd ~         # go to home directory
    cd -         # go to previous directory

---

# 📄 File & Directory Management

## mkdir (Make Directory)
Creates a new directory.

    mkdir my_folder
    mkdir -p parent/child

---

## rmdir
Removes an empty directory.

    rmdir my_folder

---

## rm (Remove)
Deletes files or directories.

    rm file.txt
    rm -r folder
    rm -rf folder

⚠️ Warning: rm -rf deletes permanently

---

## cp (Copy)
Copies files or directories.

    cp file1.txt file2.txt
    cp -r folder1 folder2

---

## mv (Move / Rename)
Moves or renames files.

    mv file.txt /home/user/
    mv old.txt new.txt

---

# 📖 Viewing Files

## cat
Displays file content.

    cat file.txt

---

## less
View file page by page.

    less file.txt

---

## head / tail
Shows beginning or end of file.

    head file.txt
    tail file.txt
    tail -f log.txt

---

# 🔐 Permissions

## chmod (Change Mode)
Changes file permissions.

    chmod 755 file.sh
    chmod +x script.sh

---

## chown (Change Owner)
Changes file ownership.

    chown user:group file.txt

---

# 🔍 Searching

## find
Search for files.

    find /home -name file.txt

---

## grep
Search inside files.

    grep "text" file.txt
    grep -r "text" .

---

# 🌐 Network Commands

## ping
Tests network connectivity.

    ping google.com

---

## ip (Recommended)
Shows network configuration.

    ip a

---

## curl
Fetch data from a URL.

    curl http://example.com

---

# ⚙️ System Information

## whoami
Shows current user.

    whoami

---

## uname
Displays system information.

    uname -a

---

## top
Shows running processes.

    top

---

# 🧠 Key Tips

- Linux is case-sensitive
- Use Tab for auto-completion
- Use ↑ to reuse commands
- Be careful with rm -rf

---

# 📌 Summary

Basic CLI commands allow you to:

- Navigate the file system
- Manage files and directories
- View and search content
- Control permissions
- Monitor system and network
