# ICTCLD401 – Session 3 Study Notes (EBS, Snapshots, S3, Launch Templates)

> Date: 27 Oct 2026 · Course: Cert IV in Cyber Security · Unit: ICTCLD401 Configure Cloud Services
> Environment: AWS Academy Learner Lab (us-east-1, N. Virginia)
> These are my own study notes. No credentials, account IDs, or personal data are included.

---

## 1. Lab setup and cost basics

- **Learner Lab** is a free sandbox with a **$50 credit budget**. Starting the lab itself costs almost nothing; running resources (EC2, RDS) consume credit.
- A session lasts **4 hours**. When it ends, resources are **retained**, but running EC2 instances are **stopped**.
- After a restart, an EC2 instance gets a **new public IPv4 address**. Old URLs stop working.
- Clean-up habit: stop or terminate unused instances, delete unused volumes and snapshots, and empty then delete test S3 buckets.

## 2. Compute basics refresher

| Concept | Meaning |
|---|---|
| RAM | Volatile working memory; cleared when power is off |
| Disk (SSD/HDD) | Non-volatile storage; keeps data without power |
| `t3.micro` | EC2 instance type: 2 vCPU, 1 GiB RAM, free-tier eligible |
| Instance type | Determines CPU and RAM. Storage is a separate resource (EBS) |

- HDDs store data on **tracks** and **sectors** using magnetic particles; **formatting** creates the file-system structure on top.
- Linux disk names: `sda`, `sdb` (classic); on AWS Nitro instances they appear as `nvme0n1`, `nvme1n1`, ... Names differ, the disk is the same.

## 3. Amazon EBS (Elastic Block Store)

- EBS = virtual hard drive attached to a single EC2 instance (block storage).
- Every EC2 instance gets a default **8 GiB root volume**, which cannot be resized during the standard launch wizard.
- **Rule 1:** a volume and its instance must be in the **same Availability Zone (AZ)**.
- A volume is an **independent resource**: creating it does not make the instance aware of it. It must be **attached**.
- Region = city, AZ = separate data-centre building (e.g. `us-east-1c`).

### Add a second 15 GiB drive – full workflow

1. EC2 → Elastic Block Store → **Volumes → Create volume** (15 GiB, AZ = instance AZ, tag `Name=EBS2`).
2. **Actions → Attach volume** → select the instance and device name (e.g. `/dev/sdf`).
3. Verify in the instance **Storage** tab: two volumes (8 GiB root + 15 GiB new).
4. Connect with **EC2 Instance Connect** (browser terminal, no SSH keys needed).
5. Inspect disks, then format and mount:

```bash
lsblk                                   # list block devices; find the new 15G disk
sudo mkdir /mnt/data-store              # create the mount point
sudo mkfs -t ext3 /dev/sdf              # format (make file system) - DESTROYS existing data
sudo mount /dev/sdf /mnt/data-store     # mount the disk to the folder
df -h                                   # confirm 15G mounted on /mnt/data-store
```

### Command reference

| Command | Purpose |
|---|---|
| `lsblk` | List block devices (read-only, safe) |
| `mkfs -t <fs> <device>` | Create a file system (format). Use ext3/ext4/xfs. **Wipes the disk** |
| `mkdir` | Make a directory |
| `mount <device> <dir>` | Attach a formatted disk to a folder |
| `df` / `df -h` | Show disk free space; `-h` = human readable |
| `cd ~` | Go to the home directory |

- `df .` output is in **KB**; divide by 1024 twice to get GB (8,310,764 KB ≈ 7.9 GB).
- `lost+found` is created automatically by the file system for recovering file fragments after corruption.
- **Journaling** (ext3/ext4/xfs): changes are logged before being written so the file system can recover after a crash.
- Evidence tip: submit **result** screenshots (attached volume, `df -h` output), not just configuration screens.

### File permissions

- Creating a file in `/mnt/data-store` failed with **Permission denied**, because the folder was created with `sudo` and is owned by root.
- Fix used in class: `sudo chmod 777 /mnt/data-store`.
- Permission digits: **r = 4, w = 2, x = 1**. Three digits = owner / group / others.

| Mode | Meaning |
|---|---|
| 777 | Everyone: read, write, execute (**insecure** for production) |
| 755 | Owner full; others read + execute |
| 644 | Owner read + write; others read |
| 400 | Owner read only (e.g. private keys) |

- Better practice: `sudo chown ec2-user /mnt/data-store`, or least-privilege modes.
- Note: `sudo echo "x" > file` fails because the redirect `>` runs outside sudo; use `echo "x" | sudo tee file`.

## 4. EBS Snapshots (backup and restore)

- A **snapshot** is a point-in-time backup of an EBS volume. It stores only **used data** (15 GiB volume → ~373 MiB snapshot).
- Snapshots are stored redundantly across multiple locations, so they survive the loss of one volume.
- Restore flow:
  1. Write test data (`hello.txt`) on `EBS2`.
  2. **Create snapshot** from `EBS2` (status: Pending → Completed).
  3. **Create volume from snapshot** → `EBS3` (same size, **same AZ** as the instance).
  4. Attach `EBS3` (e.g. `/dev/sdg`).
  5. Create a new folder and **mount only** (`sudo mount /dev/sdg /mnt/data-store2`).
  6. `ls` / `cat hello.txt` confirms the data was restored.
- **Do not run `mkfs` on a volume restored from a snapshot**: it already has a file system and `mkfs` would erase the data.
- "Fast snapshot restore" showed an authorization error in Learner Lab; it is a permission limit and can be ignored.
- Snapshots cost money; create them when needed and delete when finished.

### EBS vs EFS

| | EBS | EFS |
|---|---|---|
| Attached to | One instance (same AZ) | Many instances |
| Type | Block storage | Network file system |
| Cost | Lower | Higher |

## 5. Amazon S3 (Simple Storage Service)

- S3 = **object storage**, independent of any server (like OneDrive/Google Drive for applications).
- Files are called **objects**; containers are **buckets**. Not tied to an AZ or a single instance; many servers/users can share a bucket.
- **Bucket naming rules:** globally unique, lowercase letters, numbers and hyphens only.
- Creating a bucket: S3 → Create bucket → name → (optionally disable *Block all public access* and acknowledge the warning) → Create.
- Upload: bucket → Upload → Add files. A prefix such as `public/` acts like a folder.
- Object identifiers:
  - S3 URI: `s3://<bucket>/public/<file>`
  - ARN: `arn:aws:s3:::<bucket>/public/<file>`
  - Object URL: `https://<bucket>.s3.us-east-1.amazonaws.com/public/<file>`

### Making objects publicly readable

Two layers must both allow access:

1. **Block public access** must be turned off (outer door).
2. A **bucket policy** must grant read access (permission slip). Without it, the Object URL returns **AccessDenied**.

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": ["s3:GetObject"],
      "Resource": ["arn:aws:s3:::<BUCKET-NAME>/*"]
    }
  ]
}
```

- Replace `<BUCKET-NAME>`. For least exposure, scope the resource to `arn:aws:s3:::<BUCKET-NAME>/public/*`.
- The console showed an access-analyzer "Unexpected error" (Learner Lab lacks that permission); the policy still saved successfully.
- Clean-up order: delete bucket policy → **Empty** bucket (type `permanently delete`) → **Delete** bucket. A non-empty bucket cannot be deleted.

### Why S3 beats EC2 for public static assets

- No server to run or patch; objects served directly over HTTPS.
- Near-unlimited, durable storage; pay only for what is stored/transferred.
- Scales automatically; many servers can share the same assets.

## 6. Launch Templates and User Data

- A **launch template** is a saved instance configuration (AMI, instance type, security group, key pair, storage, user data). Launching from it skips the long wizard.
- Changing a template creates a **new version**; old versions are kept. Use **Actions → Set default version** to choose which version new launches use.
- New instances launched from a template are **not named automatically**: add a `Name` tag (e.g. `WebServer_new`).
- **User data** is a bash script that runs **once, at first boot**. Editing a template does not change instances that are already running.

### What the user-data script does

1. Updates packages and installs Python 3, pip, unzip, wget.
2. Installs Flask and `mysql-connector-python`.
3. Downloads and unzips the sample Python web app from GitHub.
4. Runs `setup.py` to write values into `config.ini` (port, **S3 `base_url`**, database endpoint/user/password).
5. Registers the app as a **systemd service** (`my_python_app.service`) and enables/starts it.

- In Python/shell scripts, `#` starts a **comment**. To activate a config line, **remove the `#`** and replace placeholders such as `<base url string>`.
- Tip: edit the script in a text editor first, then paste it into the User data box.

### Verification result and troubleshooting

- Instructor's instance showed **"Static content server is configured"** with the S3 base URL.
- My instance showed **"not available. Fallback to EC2 local images"** even though:
  - template version 2 contained the correct `base_url` line,
  - `config.ini` and `cloud-init-output.log` showed `base_url` updated to my S3 bucket,
  - the S3 image URL opened correctly in a browser.
- Next steps to try: `sudo systemctl restart my_python_app.service`, then reload the page; test with `curl -I <S3 image URL>`.
- "EC2 Server status not available. Check database connection" is expected until the RDS database exists (Part 4).
- `SendSSHPublicKey failed` on EC2 Instance Connect is a transient lab error: retry. A **stopped** instance has no public IP and cannot be connected to.

## 7. Key takeaways

1. EBS volumes live in one AZ and attach to one instance; attach → format → mount is the required sequence.
2. Always verify the device name with `lsblk` before running `mkfs`.
3. Snapshots back up used data; volumes created from snapshots are already formatted – mount only.
4. S3 is global-namespace object storage; public access needs both the setting change **and** a bucket policy.
5. Launch templates are versioned; user data runs once at first boot.
6. Avoid `chmod 777` and public buckets outside of labs; clean up resources to save credit.
7. Do not keep credentials in plain-text notes.

## 8. Suggested repo layout

```
ictcld401-notes/
├── README.md
├── session3-ebs-s3-launch-templates.md   # this file
└── scripts/
    ├── userdata.sh
    └── s3-public-read-policy.json
```
