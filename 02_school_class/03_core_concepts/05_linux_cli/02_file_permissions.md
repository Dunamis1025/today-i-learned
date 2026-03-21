# Linux File Permissions

Linux file permissions control who can access a file or directory and what actions they can perform.

This is a fundamental concept in:
- system administration
- cybersecurity
- access control

---

## Why File Permissions Matter

Without proper permissions:
- sensitive data can be exposed
- unauthorized users can modify files
- malicious users may execute harmful files
- systems become less secure

With proper permissions:
- important files are protected
- users only get the access they need
- accidental changes are reduced
- system security becomes stronger

---

## Basic Permission Groups

In Linux, permissions are assigned to 3 categories:

- user (u) = the owner of the file
- group (g) = users in the same group
- others (o) = everyone else

So Linux always asks:

1. What can the owner do?
2. What can the group do?
3. What can everyone else do?

---

## Basic Permission Types

There are 3 basic permission types:

- r = read
- w = write
- x = execute

Meaning:

- read (r)
  - for a file: allows viewing the contents
  - for a directory: allows listing the names inside

- write (w)
  - for a file: allows modifying the contents
  - for a directory: allows creating, deleting, or renaming files inside

- execute (x)
  - for a file: allows running the file as a program or script
  - for a directory: allows entering the directory with cd

---

## Example of a Permission String

Example:

-rwxr-xr--

Let’s break it down:

- first character: file type
- next 3 characters: owner permissions
- next 3 characters: group permissions
- last 3 characters: others permissions

So:

- = regular file
rwx = owner can read, write, execute
r-x = group can read and execute
r-- = others can only read

---

## File Type Symbol

The first character shows the file type:

- = regular file
d = directory
l = symbolic link

Examples:

-rw-r--r--  regular file
drwxr-xr-x  directory
lrwxrwxrwx  symbolic link

---

## File Permissions vs Directory Permissions

This is very important because permissions behave differently for files and directories.

### File permissions

For a file:

- r = read the file
- w = edit or overwrite the file
- x = run the file

Example:
If a script has x permission, it can be executed.

### Directory permissions

For a directory:

- r = list directory contents
- w = add, remove, or rename files in the directory
- x = enter the directory or access items inside it

Important:
A directory usually needs x permission to be usable.

Example:
If a directory has r but not x, you may be able to see names, but you cannot enter it properly.
If a directory has x but not r, you may enter it if you already know exact file names, but you cannot list everything easily.

---

## Numeric Permission Values

Linux permissions can also be written as numbers.

Each permission has a value:

- r = 4
- w = 2
- x = 1

Add them together:

- 7 = 4 + 2 + 1 = rwx
- 6 = 4 + 2 = rw-
- 5 = 4 + 1 = r-x
- 4 = 4 = r--
- 3 = 2 + 1 = -wx
- 2 = 2 = -w-
- 1 = 1 = --x
- 0 = no permission

Example:

755 means:
- owner = 7 = rwx
- group = 5 = r-x
- others = 5 = r-x

644 means:
- owner = 6 = rw-
- group = 4 = r--
- others = 4 = r--

---

## Common Permission Modes

Here are common examples:

- 777 = rwxrwxrwx
  - everyone can do everything
  - very dangerous in most cases

- 755 = rwxr-xr-x
  - owner can do everything
  - others can read and execute
  - common for scripts and directories

- 700 = rwx------
  - only owner has access
  - good for private directories

- 644 = rw-r--r--
  - owner can read and write
  - others can only read
  - common for normal files

- 600 = rw-------
  - only owner can read and write
  - good for sensitive files

---

## Viewing Permissions

Use this command to view permissions:

ls -l

Example output:

-rw-r--r-- 1 yunho staff 120 Mar 21 10:30 notes.txt

Meaning:
- -rw-r--r-- = permission string
- 1 = link count
- yunho = owner
- staff = group
- 120 = file size
- Mar 21 10:30 = last modified date
- notes.txt = file name

---

## chmod Command

chmod means change mode.
It is used to change permissions.

There are 2 common ways to use chmod:

1. symbolic mode
2. numeric mode

---

## chmod in Symbolic Mode

Basic format:

chmod who operator permission filename

Parts:
- who = u, g, o, or a
- operator = +, -, =
- permission = r, w, x

Meanings:
- u = user
- g = group
- o = others
- a = all

Operators:
- + = add permission
- - = remove permission
- = = set exact permission

Examples:

chmod u+x script.sh
Adds execute permission for the owner.

chmod g-w file.txt
Removes write permission from the group.

chmod o+r file.txt
Adds read permission for others.

chmod a-x file.txt
Removes execute permission from everyone.

chmod u=rw file.txt
Sets owner permission to read and write only.

---

## chmod in Numeric Mode

Examples:

chmod 755 script.sh
chmod 644 notes.txt
chmod 700 private_folder
chmod 600 secret.txt

These are faster and very common in Linux administration.

---

## chown Command

chown means change owner.

It changes the owner or group of a file.

Examples:

chown yunho file.txt
Changes the owner to yunho.

chown yunho:staff file.txt
Changes owner to yunho and group to staff.

chown -R yunho:staff my_folder
Changes owner and group recursively for a directory and everything inside it.

Note:
Usually changing ownership requires sudo.

Example:

sudo chown yunho:staff file.txt

---

## chgrp Command

chgrp means change group.

Example:

chgrp staff file.txt

This changes only the group owner.

---

## Practical Examples

### Example 1: Make a script executable

chmod 755 backup.sh

Meaning:
- owner can read, write, execute
- group can read and execute
- others can read and execute

This is common for shell scripts.

### Example 2: Protect a private key

chmod 600 id_rsa

Meaning:
- only owner can read and write
- nobody else can access it

This is important because SSH private keys must be restricted.

### Example 3: Secure a private folder

chmod 700 my_private_folder

Meaning:
- only owner can enter, read, and modify it

### Example 4: Normal text file

chmod 644 notes.txt

Meaning:
- owner can read and edit
- others can only read

---

## Important Security Warnings

### Avoid chmod 777

Example:

chmod 777 file.txt

This gives:
- read
- write
- execute

to everyone.

Why this is dangerous:
- anyone can modify the file
- malware or attackers may abuse it
- it breaks the principle of least privilege

Use 777 only in very rare and controlled situations, if ever.

### Principle of Least Privilege

This means:
Give users only the minimum permission they need.

This is a core cybersecurity principle.

Example:
If someone only needs to read a file, do not give write permission.
If a script does not need public access, do not give it to everyone.

---

## Recursive Permission Changes

Sometimes you want to change permissions for an entire directory.

Example:

chmod -R 755 my_folder

- -R means recursive
- this applies changes to the folder and everything inside it

Be careful with recursive changes.
They can accidentally expose many files.

---

## Default Permissions and umask

When a new file or directory is created, Linux uses default permissions, then reduces them using umask.

Typical defaults:
- files start from 666
- directories start from 777

Then umask removes some permissions.

Example:
If umask is 022:

- file becomes 644
- directory becomes 755

You can check umask with:

umask

This is useful in Linux administration and security hardening.

---

## Special Permissions

Linux also has special permissions.

### SUID

SUID allows a file to run with the permissions of the file owner.

Example:
If a file is owned by root and has SUID, another user may run it with root-level owner permissions for that file process.

Numeric value:
- 4 in front of normal permissions

Example:
4755

### SGID

SGID on a file:
- runs with the group’s permissions

SGID on a directory:
- new files inside inherit the directory’s group

Numeric value:
- 2 in front

Example:
2755

### Sticky Bit

Used mainly on directories.

It means:
Users can create files, but only the file owner can delete their own file.

Common example:
- /tmp

Numeric value:
- 1 in front

Example:
1777

These special permissions are more advanced but important to know.

---

## How Permissions Appear in Real Life

Examples:

-rw-r--r--   normal text file
-rwxr-xr-x   executable script
drwxr-xr-x   normal directory
drwx------   private directory

You should practice reading these quickly.

---

## Quick Command Summary

View permissions:
ls -l

Change permissions using symbols:
chmod u+x file.sh

Change permissions using numbers:
chmod 755 file.sh

Change owner:
chown user file.txt

Change owner and group:
chown user:group file.txt

Change group only:
chgrp group file.txt

Recursive permission change:
chmod -R 755 my_folder

---

## Beginner-Friendly Memory Tips

Remember:

- r = read
- w = write
- x = execute

And:

- 4 = read
- 2 = write
- 1 = execute

So:
- 7 = rwx
- 6 = rw-
- 5 = r-x
- 4 = r--

Easy way to remember:
read is strongest basic viewing permission,
write changes things,
execute runs or enters.

---

## Common Mistakes

### Mistake 1: Giving execute to normal text files
Not every file needs x permission.

### Mistake 2: Using 777 too easily
This is insecure.

### Mistake 3: Confusing file permissions with directory permissions
x means run for files, but enter for directories.

### Mistake 4: Forgetting ownership
Even if permissions look correct, wrong ownership can still cause access problems.

---

## Why File Permissions Matter in Cybersecurity

File permissions are important in cybersecurity because:

- they help protect confidential data
- they reduce unauthorized access
- they limit attacker movement
- they enforce least privilege
- they protect scripts, keys, configs, and logs

Bad permissions can lead to:
- privilege abuse
- data leaks
- accidental deletion
- easier exploitation by attackers

So file permissions are one of the first layers of defense in Linux security.

---

## Final Summary

Linux file permissions decide:
- who can access a file or directory
- what actions they can perform

Main permission groups:
- user
- group
- others

Main permission types:
- read
- write
- execute

Important commands:
- ls -l
- chmod
- chown
- chgrp

Common safe examples:
- 644 for normal files
- 755 for scripts and directories
- 600 for sensitive files
- 700 for private directories

Always follow:
the principle of least privilege

---

## Key Takeaway

Linux file permissions are a basic but essential security feature.

If you understand permissions well, you can:
- manage files safely
- protect sensitive data
- avoid common Linux mistakes
- build stronger cybersecurity habits
