# Ubuntu Server Lab – Certificate IV Server Management
> **Course:** Security Impossible – Cyber Range  
> **Scenario:** Deploy a secure, centrally managed file & web server for TechStart Inc. (10 users)

---

## Table of Contents
1. [Lab Overview](#lab-overview)
2. [Phase 1 – Planning & Backup](#phase-1--planning--backup)
3. [Phase 2 – Service Deployment](#phase-2--service-deployment)
4. [Phase 3 – Security & Identity Management](#phase-3--security--identity-management)
5. [Phase 4 – Validation & Testing](#phase-4--validation--testing)
6. [Key Concepts Reference](#key-concepts-reference)
7. [Command Cheat Sheet](#command-cheat-sheet)

---

## Lab Overview

### Business Requirements (TechStart Inc.)
- Secure file sharing for 10 users
- Centralized login system (reduce password sprawl)
- Internal website accessible via HTTP on port 80
- Budget: open-source preferred, downtime < 1 hour

### Tools Used
| Tool | Purpose |
|------|---------|
| `apache2` | Web server – hosts internal employee portal |
| `samba` / `smbd` | Linux-to-Windows compatible file sharing |
| `smbclient` | Samba client for testing share access |
| `slapd` | OpenLDAP server – centralized user directory |
| `ldap-utils` | LDAP management tools (`ldapadd`, `ldapsearch`) |
| `libpam-ldap` | Connects Linux login (PAM) to LDAP authentication |
| `ufw` | Uncomplicated Firewall – controls open ports |
| `tar` | Archive/compress files for backup |
| `md5sum` | Generates a checksum hash to verify file integrity |
| `setfacl` / `getfacl` | Fine-grained file permission control (POSIX ACLs) |
| `quota` | Per-user disk usage limits |
| `curl` | HTTP client – tests web server response |
| `nano` | Terminal text editor |
| `systemctl` | Manages system services (start/stop/enable) |

---

## Phase 1 – Planning & Backup

### Step 1.1 – Create Sample Data Files

```bash
sudo -i                          # Switch to root (full admin)
mkdir -p /data && cd /data       # Create /data directory and enter it

# Create employee roster CSV
cat > employee_roster.csv << EOF
Name,Email,Department
John Smith,jsmith@techstart.local,HR
Jane Doe,jdoe@techstart.local,IT
EOF

# Create a placeholder "PDF" (text file with .pdf extension)
echo "Q3 Financial Report: Revenue up 15%. Expenses: $500k." > q3_report.pdf

# Create files with specific timestamps (for backup demo)
touch -d "2025-09-15" old_file.txt
echo "Old legacy data." > old_file.txt

touch -d "2025-10-05" updated_file.pdf
echo "Updated Q4 projections." > updated_file.pdf

# Set standard read permissions on all files
chmod 644 *.*

ls -l   # Verify files
```

**Key Concepts:**
- `cat > file << EOF` — writes multi-line content directly into a file
- `touch -d` — creates a file with a manually specified date (useful for simulating old files)
- `chmod 644` — owner can read/write; group and others can only read

---

### Step 1.2 – Backup Data

```bash
sudo mkdir /backup               # Create backup directory

# Save MD5 checksum of original file (for integrity verification later)
md5sum /data/employee_roster.csv > ~/original_hash.txt

# Create compressed backup archive with today's date in the filename
sudo tar czf /backup/data-$(date +%Y%m%d).tar.gz /data

# Verify backup contents (show first 5 files)
sudo tar -tzf /backup/data-$(date +%Y%m%d).tar.gz | head -5
```

**What is MD5?**  
MD5 generates a unique "fingerprint" string from a file's contents. Even a single changed character produces a completely different hash — making it ideal for detecting file corruption or tampering.

```bash
# Restore backup to /tmp and compare hashes
cd /tmp
tar -xzf /backup/data-$(date +%Y%m%d).tar.gz
md5sum data/employee_roster.csv    # Should match original_hash.txt

cat ~/original_hash.txt            # Compare — identical = perfect backup

rm -rf /tmp/data                   # Clean up temp files
```

**`tar` flags explained:**
| Flag | Meaning |
|------|---------|
| `c` | Create a new archive |
| `x` | Extract from archive |
| `z` | Compress/decompress with gzip |
| `f` | Specify the filename |
| `t` | List archive contents without extracting |

---

## Phase 2 – Service Deployment

### Step 2.1 – Install Apache & Samba

```bash
apt update && apt install -y apache2 samba
```

**What are these?**
- **Apache** — a web server. It takes `index.html` files and serves them to browsers over HTTP
- **Samba** — allows a Linux server to share folders in a Windows-compatible way (SMB/CIFS protocol), like a network drive

```bash
# Create the internal web page
echo "<h1>Welcome to TechStart Inc.</h1><p>Employee Portal Active.</p>" \
  > /var/www/html/index.html

# Start Apache and enable it to auto-start on reboot
systemctl enable --now apache2
```

**Configure Samba** — edit `/etc/samba/smb.conf` and add at the bottom:

```ini
[shared]
path = /home/share
browseable = yes
writable = yes
valid users = @employees
```

> `valid users = @employees` means **only members of the `employees` group** can access this share. The `@` prefix denotes a group.

```bash
# Create shared folder with sticky bit
mkdir /home/share
chmod 1777 /home/share     # Sticky bit: users can only delete their own files

# Create employees group and add current user
groupadd employees
usermod -aG employees $USER

# Set Samba password for current user
smbpasswd -a $USER

# Start Samba service
systemctl enable --now smbd

# Open firewall ports
ufw allow 80     # HTTP (Apache)
ufw allow 445    # SMB (Samba)
ufw enable

# Test both services
curl localhost                                    # Should return HTML
smbclient //localhost/shared -U $USER            # Should open smb:\> prompt
```

**What is the sticky bit (`1777`)?**  
On a shared directory, the sticky bit prevents users from deleting each other's files — even if the directory is world-writable. The same mechanism is used on `/tmp`.

---

### Step 2.2 – System Updates

```bash
apt upgrade -y          # Update all installed packages to latest versions
apt autoremove -y       # Remove packages no longer needed

# Verify installed services
apache2 -v                          # Check Apache version
dpkg -l | grep samba                # Confirm Samba is installed
apt list --upgradable               # Should show nothing (fully up to date)
```

---

### Step 2.3 – Data Restoration to Share

```bash
# Create a data directory inside the share and extract backup
mkdir -p /home/share/data
cd /home/share
tar -xzf /backup/data-$(date +%Y%m%d).tar.gz

# Verify data integrity with MD5
md5sum /home/share/data/employee_roster.csv
cat ~/original_hash.txt    # Must match ✓

# Move files up one level and remove empty subdirectory
mv /home/share/data/* /home/share/
rmdir /home/share/data
ls /home/share
```

---

## Phase 3 – Security & Identity Management

### Step 3.1 – OpenLDAP Setup

**What is LDAP?**  
LDAP (Lightweight Directory Access Protocol) is a centralized user management system. Instead of creating accounts on each server separately, you create one account in LDAP and it works everywhere — single sign-on across all services.

```bash
apt install -y slapd ldap-utils

# Reconfigure LDAP interactively
dpkg-reconfigure slapd
```

**During reconfiguration, answer:**
| Prompt | Answer |
|--------|--------|
| Omit OpenLDAP server configuration? | **No** |
| DNS domain name | `techstart.local` |
| Organization name | `TechStart` |
| Admin password | `temp123` |
| Remove database on purge? | **No** |
| Move old database? | **Yes** |

```bash
# Generate a hashed password for LDAP users
slappasswd -s ICTLAB@123
# Output: {SSHA}xxxxxxxxxxxxxxxxxxxxxxxx  ← copy this hash
```

**Create LDAP user file** (`/tmp/users.ldif`):

```ldif
dn: ou=employees,dc=techstart,dc=local
objectClass: organizationalUnit
ou: employees

dn: uid=jsmith,ou=employees,dc=techstart,dc=local
objectClass: inetOrgPerson
uid: jsmith
cn: John Smith
sn: Smith
userPassword: {SSHA}YOUR_HASH_HERE

dn: uid=jdoe,ou=employees,dc=techstart,dc=local
objectClass: inetOrgPerson
uid: jdoe
cn: Jane Doe
sn: Doe
userPassword: {SSHA}YOUR_HASH_HERE
```

```bash
# Import users into LDAP
ldapadd -x -D "cn=admin,dc=techstart,dc=local" -W -f /tmp/users.ldif
# Password: temp123

# Verify user was added
ldapsearch -x -b "dc=techstart,dc=local" "(uid=jsmith)"

# Install PAM-LDAP integration (connects Linux login to LDAP)
apt install libpam-ldap
```

---

### Step 3.2 – Folder Permissions & Quotas

```bash
# Create HR-only folder and a test file
mkdir /home/share/HR
echo "HR Docs" > /home/share/HR/secret.txt

# Create hr group and set up users
groupadd hr
useradd -m -G hr,employees jdoe
echo "jdoe:temp123" | chpasswd
smbpasswd -a jdoe

useradd -m -G employees jsmith
echo "jsmith:temp123" | chpasswd
smbpasswd -a jsmith

# Set HR folder ownership (root owns it, hr group controls it)
chown -R root:hr /home/share/HR

# Set ACLs (Access Control Lists)
setfacl -m g:hr:rwx /home/share/HR        # hr group: read + write + execute
setfacl -m u:jsmith:rx /home/share/HR     # jsmith: read + execute only (no write)
```

**POSIX ACLs vs standard permissions:**  
Standard Unix permissions only support owner/group/others. ACLs allow you to set different permissions for **multiple specific users or groups** on the same file or directory.

```bash
# Install disk quota tools
apt install quota

# Scan filesystem to initialize quota database
quotacheck -avugm

# Enable quotas
quotaon -avug

# Edit /etc/fstab — add usrquota,grpquota to the /home partition line
nano /etc/fstab
# Example line:
# UUID=xxx /home ext4 defaults,usrquota,grpquota 0 2
```

---

### Step 3.3 – Login Scripts (User Environment Automation)

```bash
# Add PATH and alias defaults for all new users
echo 'export PATH=$PATH:/opt/tools' >> /etc/skel/.bashrc
echo 'alias ll="ls -la"' >> /etc/skel/.bashrc
```

**What is `/etc/skel`?**  
Files here are automatically copied to every new user's home directory when their account is created. It's a template for new user environments.

```bash
# Create auto-mount script (runs at every login)
nano /etc/profile.d/mount_share.sh
```

```bash
#!/bin/bash
if [ "$USER" = "jsmith" ] || [ "$USER" = "jdoe" ]; then
  mkdir -p ~/share
  mount -t cifs //10.11.2.4/shared ~/share -o username=$USER,password=ICTLAB@123
fi
```

```bash
# Make it executable
chmod +x /etc/profile.d/mount_share.sh

# Test by switching to a user
su - jsmith
ls ~/share     # Share directory should be created
exit
```

**What is `/etc/profile.d/`?**  
Scripts placed here run automatically for every user at login — ideal for setting up environment variables or mounting network drives without user intervention.

---

## Phase 4 – Validation & Testing

### Step 4.1 – Service Validation

```bash
# 1. Add server hostname to /etc/hosts (client-side DNS override)
nano /etc/hosts
# Add line:
# 10.11.2.4  server.techstart.local
```

```bash
# 2. Test network reachability
ping server.techstart.local
# Ctrl+C to stop

# 3. Test web server
curl http://server.techstart.local
# Expected: <h1>Welcome to TechStart Inc.</h1><p>Employee Portal Active.</p>

# If hostname doesn't resolve, test with IP directly
curl http://localhost
# Or: curl --connect-timeout 5 http://10.11.2.4
```

```bash
# 4. Add users to Samba password database
smbpasswd -a jsmith    # Password: ICTLAB@123
smbpasswd -a jdoe

# Add jsmith to employees group (required by smb.conf valid users)
usermod -aG employees jsmith
systemctl restart smbd

# 5. Test Samba file share access
smbclient //localhost/shared -U jsmith
# Password: ICTLAB@123
# Success: smb: \> prompt appears
# Type 'exit' to leave
```

**Troubleshooting Samba errors:**
| Error | Cause | Fix |
|-------|-------|-----|
| `NT_STATUS_LOGON_FAILURE` | User not in Samba password DB | Run `smbpasswd -a username` |
| `NT_STATUS_ACCESS_DENIED` | User not in `valid users` group | Run `usermod -aG employees username` |
| `mount.cifs: permission denied` | Non-root user can't mount | Expected in lab; run mount as root |

```bash
# 6. Verify UFW firewall rules
ufw status
# Should show: 80 ALLOW Anywhere, 445 ALLOW Anywhere

# 7. Verify Apache is running
systemctl status apache2
# Should show: active (running)
```

---

## Key Concepts Reference

### File Permissions

```
-rw-r--r--   1   root   root   92   Jun 22   file.txt
│││││││││    │    │      │      │     │         │
│││││││││    │    │      │      │     │         └── filename
│││││││││    │    │      │      │     └──────────── date modified
│││││││││    │    │      │      └────────────────── file size (bytes)
│││││││││    │    │      └───────────────────────── group owner
│││││││││    │    └──────────────────────────────── user owner
│││││││││    └───────────────────────────────────── link count
│└┤└┤└┤└┤
│ │ │ │ └── other permissions (r=read, w=write, x=execute, -=none)
│ │ │ └──── group permissions
│ │ └────── owner permissions
│ └──────── file type (- = file, d = directory, l = symlink)
└────────── file type indicator
```

**Permission numbers:**
| Number | Binary | Meaning |
|--------|--------|---------|
| 7 | 111 | read + write + execute |
| 6 | 110 | read + write |
| 5 | 101 | read + execute |
| 4 | 100 | read only |

### Networking

- **Port 80** — HTTP (web traffic, Apache)
- **Port 445** — SMB (Samba file sharing)
- **UFW** — a friendly frontend for `iptables`. Default policy: deny all incoming. Must explicitly allow ports.
- **`/etc/hosts`** — a local DNS override file. Maps hostnames to IPs without needing a DNS server.

### Services

```bash
systemctl start <service>       # Start now
systemctl stop <service>        # Stop now
systemctl restart <service>     # Restart
systemctl enable <service>      # Auto-start on boot
systemctl enable --now <service> # Enable AND start immediately
systemctl status <service>      # Check if running
```

---

## Command Cheat Sheet

### File & Directory
```bash
mkdir -p /path/to/dir       # Create directory (and parents if needed)
cd /path                    # Change directory
ls -l                       # List with details
cat file.txt                # Print file contents
echo "text" > file.txt      # Write text to file (overwrites)
echo "text" >> file.txt     # Append text to file
rm -rf /path                # Force delete directory and contents
mv source dest              # Move or rename
cp source dest              # Copy
chmod 644 file              # Change permissions
chown user:group file       # Change owner
```

### Backup & Integrity
```bash
tar czf archive.tar.gz /dir         # Create compressed archive
tar xzf archive.tar.gz              # Extract archive
tar tzf archive.tar.gz | head -5    # List archive contents
md5sum file > hash.txt              # Save file hash
md5sum file && cat hash.txt         # Compare hashes manually
```

### User & Group Management
```bash
useradd -m username              # Create user with home directory
usermod -aG groupname username   # Add user to group
groupadd groupname               # Create group
echo "user:pass" | chpasswd      # Set Linux password
smbpasswd -a username            # Add/set Samba password
su - username                    # Switch to user (full login)
id username                      # Show user's groups
```

### LDAP
```bash
slappasswd -s password                          # Generate LDAP password hash
ldapadd -x -D "cn=admin,dc=..." -W -f file.ldif  # Import LDAP entries
ldapsearch -x -b "dc=..." "(uid=username)"      # Search LDAP for user
dpkg-reconfigure slapd                          # Reconfigure LDAP interactively
```

### Permissions (ACL)
```bash
setfacl -m u:username:rwx /path    # Set user ACL
setfacl -m g:groupname:rx /path    # Set group ACL
getfacl /path                      # View current ACLs
```

### Samba
```bash
smbclient //host/share -U username    # Connect to Samba share
systemctl restart smbd                # Restart Samba
grep -A 20 '\[shared\]' /etc/samba/smb.conf   # View share config
```

### Network & Firewall
```bash
ufw allow 80              # Open port 80
ufw allow 445             # Open port 445
ufw enable                # Activate firewall
ufw status                # Check firewall rules
curl http://localhost      # Test web server
ping hostname             # Test network reachability
ip addr                   # Show IP addresses
```

---

*Lab completed: Certificate IV Server Management — Security Impossible Cyber Range*  
*Deployed: Apache web server · Samba file share · OpenLDAP SSO · UFW firewall · POSIX ACLs · Disk quotas · Login automation*
