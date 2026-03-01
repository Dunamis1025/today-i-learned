🐧 Linux CLI File & Permission Practice

(Hands-on Practice Log – File System & Permission Management)

📌 Purpose of This Practice

This exercise was completed using Linux CLI (no GUI tools allowed).

The goal was to:

Understand Linux file system navigation

Create directories and files

Write content into files

Manage file permissions using numeric mode

Verify results using CLI commands

Understand how ownership and permission structure works

This is foundational knowledge for Cyber Security and System Administration.

🗂 Step-by-Step Commands and Detailed Explanation
1️⃣ Check Current Working Directory
pwd
What it does:

pwd stands for Print Working Directory

It shows the current directory path

Why I used it:

To confirm I was inside my home directory before creating new folders.

2️⃣ Create a New Directory Inside Home
mkdir ~/work
Breakdown:

mkdir = make directory

~ = home directory

~/work = create a folder named "work" inside home

Result:

A new folder called work was created.

3️⃣ Move Into the Work Directory
cd ~/work
Breakdown:

cd = change directory

This moves the terminal into the work folder

Why important:

All new folders and files will now be created inside work.

4️⃣ Create Multiple Directories at Once
mkdir public shared temp
What it does:

Creates three directories:

public

shared

temp

Important:

Linux allows creating multiple directories in one command.

5️⃣ Create Empty Files
touch public/file1.txt
touch shared/file2.txt
What touch does:

Creates an empty file

If file exists → updates timestamp

If file does not exist → creates new file

6️⃣ Write Content Into Files
echo "this is file 1" > public/file1.txt
echo "this is file 2" > shared/file2.txt
Breakdown:

echo prints text

> redirects output into a file

> overwrites existing content

Important Concept:

> replaces content

>> would append content

7️⃣ Set File Permissions (Numeric Mode)
🔐 For file1.txt
chmod 664 public/file1.txt
🔐 For file2.txt
chmod 640 shared/file2.txt
📖 Understanding chmod Numeric System

Linux permission numbers:

Number	Meaning
4	Read (r)
2	Write (w)
1	Execute (x)

They are added together.

664 means:

Owner: 6 → 4 + 2 → Read + Write
Group: 6 → Read + Write
Others: 4 → Read only

Result:

rw-rw-r--
640 means:

Owner: 6 → Read + Write
Group: 4 → Read only
Others: 0 → No permission

Result:

rw-r-----
8️⃣ Verify Directory Structure and Permissions
ls -lR ~/work
Breakdown:

ls = list

-l = long format (shows permissions, owner, size, date)

-R = recursive (shows subdirectories)

Why important:

This confirms:

File existence

Folder structure

Permission settings

9️⃣ Verify File Content
cat public/file1.txt
cat shared/file2.txt
What cat does:

Displays file content inside terminal.

Used to confirm:

Text was written correctly

Redirection worked properly

🔎 Additional Recommended Commands (For Deeper Understanding)

These were not required but are important for mastery.

Check Current User
whoami

Shows which user is currently logged in.

Check User ID and Groups
id

Shows:

UID

GID

Group memberships

Important for understanding permission behavior.

Check Detailed File Information
stat public/file1.txt

Shows:

File size

Permissions

Last modified time

Owner and group

More detailed than ls -l.

Symbolic Mode Permission Example

Instead of numeric:

chmod u+rw,g+r,o-r shared/file2.txt

Meaning:

u = user

g = group

o = others

= add permission

= remove permission

This is more readable but numeric mode is faster in exams.

🧠 Key Concepts Learned

Linux file system is hierarchical

~ represents home directory

Permissions are divided into:

Owner

Group

Others

Numeric permission system (4+2+1)

Redirection operator > overwrites

Recursive listing helps verify structure

CLI is powerful and precise

🎯 Why This Is Important for Cyber Security

Understanding permissions helps with:

Preventing unauthorized access

Hardening Linux systems

Identifying misconfigurations

Managing secure environments

Auditing file access control

Incorrect permissions can lead to:

Data leakage

Privilege escalation

System compromise

📌 Final Reflection

This practice reinforced:

Confidence using Linux CLI

Understanding permission structure

Writing and verifying system-level changes

Working without GUI tools

This is foundational knowledge for:

Cyber Security

System Administration

Linux Server Management

Penetration Testing

✅ Practice Completed Using CLI Only

No GUI tools were used.
All tasks were completed and verified through terminal commands.
