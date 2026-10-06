# Cloud Fundamentals & Launching My First EC2 Instance

- **Date:** 2026-10-06 (Session 1)
- **Unit:** ICTCLD401 – Configure Cloud Services
- **Platform:** AWS Academy Learner Lab (Region: `us-east-1`, N. Virginia)

---

## 1. Key Takeaways (TL;DR)

- **Cloud computing** = renting computing resources (CPU, memory, storage, networking) over the internet instead of buying and owning hardware.
- **Three deployment models:** Public, Private, Hybrid.
- **Multi-tenancy** = multiple customers share the same physical hardware, but are **logically isolated**.
- **Elasticity** = scale resources up and down on demand (a strength of public cloud).
- **Region** = a geographic location with AWS data centers. Our lab only works in **us-east-1 (N. Virginia)**, even though we are in Australia.
- **EC2 instance** = a virtual machine (VM) running in an AWS data center. To create one you choose: **OS (AMI)**, **hardware (instance type)**, **key pair**, plus network/storage settings.
- **Cost control matters:** the Learner Lab has a **$50 budget**. Always **terminate** instances and **end the lab** after use.

---

## 2. Why Cloud Computing?

### Benefits discussed
- **Uninterrupted service:** you are not dependent on a single data center.
- **Avoids single-point-of-failure risk.** Relying on one data center is dangerous because of:
  1. **Natural disasters** (e.g. earthquake).
  2. **Human error** (mistakes by staff).
  3. **Events outside your control** (power, network, third parties).
- **No duplication of hardware:** instead of every team buying its own computers, resources are shared.
- **Pay for what you use** (billed per hour for many services).

---

## 3. Cloud Deployment Models

| Model | Who can use it | Hardware | Key features |
|---|---|---|---|
| **Public cloud** | Anyone (open to all customers) | Shared (multi-tenancy) | Elasticity, no hardware purchase, provider (e.g. AWS) handles stability and security |
| **Private cloud** | One organization only | Dedicated, **not shared** | No other tenants can access your CPU/memory; limited elasticity |
| **Hybrid cloud** | Mix of both | Public + Private | Combine the strengths of each |

### Public cloud
- "Where everybody can access."
- Instead of buying a computer for each computation need, you **share CPU and memory** with other customers on the same hardware.

### Private cloud
- Resources (CPU, memory) are **not shared** with anyone. Nobody else can access them.
- Typical example: a company gives employees **virtual machines** (e.g. VMware-based) that they access over the internet. If a physical laptop breaks, the employee gets a VM and keeps working because code/data lives in a central repository.
- Trade-off: you **do not get elasticity** (cannot scale on demand easily).

### Hybrid cloud
- Combine **some public features** with **private** security.
- **Example architecture:**
  - **Application server → Public cloud** (needs elasticity).
  - **Database server → Private cloud** (contains **sensitive information**).

---

## 4. Multi-Tenancy (Shared Tenancy)

- **Tenancy = sharing.** In public cloud, many customers (tenants) share the same hardware at the same time.
- Think of it as tenants in the same building.
- Security is still maintained because of **logical isolation (logical boundaries)**:
  - Your files may sit in the same physical memory/disk as another customer's, yet **neither can see the other's data**.
  - **Example:** Amazon **S3 buckets** – one user's bucket cannot interact with another user's bucket, even though the underlying hardware is shared.
- AWS guarantees the **stability and security** of the shared infrastructure.
- Historical contrast: 10–20 years ago each team needed separate hardware for computation.
- Reminder: no hardware, no computer. Software/platforms run on top of hardware, and as customers we are **tenants inside a VM on a physical host**.

---

## 5. Cloud Resources

A **resource** is anything you create and use in the cloud, for example:
- Virtual machines
- Databases
- Hard disks (storage volumes)
- Load balancers
- Auto scaling groups
- VPCs (virtual private clouds)

---

## 6. AWS Global Infrastructure & Regions

- AWS has data centers in many places worldwide (North America, South America, Europe, Middle East, Africa, Asia Pacific, Australia & New Zealand).
- Australia has **Sydney** and **Melbourne** regions.
- **Our lab runs in `us-east-1` (N. Virginia).** The Learner Lab only grants access to this one region/data center.
- Physical distance does not matter much: we remote into a machine in the U.S. over the internet with good bandwidth.
- Big idea: *"I do not need to physically own or visit the computer. I create a Windows laptop in Virginia and use it from Melbourne."*

---

## 7. AWS Academy Learner Lab

### Getting access
1. Accept the **Course Invitation** email from AWS Academy.
2. Choose **Create My Account** (Canvas), set a password, accept the terms.
   - The marketing-contact checkbox and personal email are optional.
   - Store the password in a password manager.
3. Go to **Modules → AWS Academy Learner Lab → Launch AWS Academy Learner Lab**.
4. Scroll to the bottom and **agree** to the terms.
5. Click **Start Lab**.

### Lab status indicator (traffic-light analogy)
| Color | Meaning |
|---|---|
| Red | Lab is off (the "shutter" is closed) |
| Yellow/Orange | Lab is starting |
| **Green** | Lab is ready |

- **First start takes longer** because AWS builds your environment; later starts are faster.
- Clicking **AWS** (when green) opens the **AWS Management Console**.

### Important limits
- **Budget: $50 USD.** If you exceed it, you lose access and your work.
- **Session length: 4 hours** by default (timer shown). Starting again resets the timer.
- At the end of a session, **EC2 instances are shut down automatically**, but other resources (e.g. **RDS**) keep running.
- Some services (e.g. **Elastic Load Balancer**, **NAT gateway**) can **keep charging between sessions**; delete them when finished.
- Only a **restricted set of AWS services** is available.
- Resources persist across sessions until you delete them.
- The instructor shared a story of a student account that went over $50 and could not open the lab, so **budget discipline is important**.

### Network note
- School networks may block certain ports/traffic. If a connection fails, switch to **mobile data/hotspot** (a personal laptop also helps).
- Mac users need the **Windows App** (Microsoft Remote Desktop) from the App Store for RDP.

---

## 8. Amazon EC2 (Elastic Compute Cloud)

- **EC2** = "Elastic Compute Cloud" (two C's). It is the AWS service for creating and running **virtual machines**.
- An **instance** = one virtual machine (like one laptop).
- Open it from the console search bar: type **EC2**.
- On the EC2 dashboard, **Instances (running)** shows how many VMs you have. **Launch instance** creates a new one.

### Launch instance – settings chosen today
| Setting | Choice | Notes |
|---|---|---|
| **Name** | `MyWindowsServer` | Just a label; the system does not know the purpose |
| **AMI (OS image)** | **Microsoft Windows Server 2025 Base** | Default is Linux, so you must select **Windows** (a light-blue highlight confirms) |
| **Instance type (hardware)** | **t3.micro** | 2 vCPU, 1 GiB memory, Free tier eligible |
| **Key pair** | New RSA key pair `MyWinkey` (`.pem`) | Downloaded automatically; keep it safe |
| **Network settings** | Defaults (default VPC, auto-assign public IP, RDP allowed) | Details covered next week |
| **Security group** | Default "launch-wizard" | Equivalent to a **firewall**; to be covered next week |
| **Storage** | 30 GiB, gp3 (EBS) | Free tier covers up to 30 GiB |
| **File systems** | None | EFS/S3 Files not supported on Windows |

### Concepts to remember
- **AMI (Amazon Machine Image):** template with the operating system and software for the instance. Choosing the OS = "choosing which software the laptop comes with".
- **Instance type:** the **hardware spec** (CPU, memory). Larger types cost more (priced per hour).
- **Key pair:** a public/private key pair. The private key (`.pem`) is used to **decrypt the initial Windows administrator password**. If you lose the key and password, you lose access to the instance.
- **Security group:** a cloud firewall controlling inbound/outbound traffic (same idea a network engineer calls a firewall).
- **EBS (Elastic Block Store):** the instance's virtual hard disk (covered in more detail in Session 3).
- Create **only one** instance to avoid unnecessary cost.
- The instructor walked through everything with a "buy a laptop" analogy: choose the OS, choose the hardware, set up access, then launch. In the cloud this takes a few clicks and the machine appears in a data center in Virginia.

---

## 9. Instance Status Checks (3/3 checks passed)

After launching, the instance state becomes **Running**, but it takes a few minutes for **Status check** to go from *Initializing* to **3/3 checks passed**.

| # | Check | What it verifies |
|---|---|---|
| 1 | **System status check** | AWS infrastructure: networking and the physical host/power are healthy |
| 2 | **Instance status check** | The **operating system** is healthy and reachable |
| 3 | **EBS check** | The attached **storage volume** is healthy |

Meaning: the machine is up, running, and healthy.

Useful details on the instance **Details** tab:
- **Public IPv4 address / Public DNS:** used to connect from the internet.
- **Private IPv4 address:** used inside AWS's network.
- **Instance state, instance type, availability zone** (e.g. `us-east-1a`).

Note: **ping (ICMP)** does not work by default; it requires a security group rule that allows ICMP. This will be covered later.

---

## 10. Connecting to the Windows Instance (RDP)

**RDP = Remote Desktop Protocol**, which lets you control another computer's desktop remotely.

### Method 1: RDP shortcut file
1. Select the instance → **Connect → RDP client** tab (not "In web browser").
2. **Download remote desktop file** (`.rdp`). It already contains the machine address and username.
3. Click **Get Windows password**.
4. **Upload private key file** (`.pem`) → **Decrypt password**.
5. Copy the password and **save it securely** (do not lose it).
6. Open the `.rdp` file → accept the warning → enter **Administrator** + the password.
7. The Windows Server desktop appears; the top bar shows the remote address.

### Method 2: Remote Desktop Connection app (manual)
1. Search for **RDP** in Windows → open **Remote Desktop Connection**.
2. Enter the **Public DNS** (or public IP) in the **Computer** field.
3. Enter username **Administrator** and the decrypted password.

### Differences between methods
- **RDP file:** machine name and username are pre-filled; you only supply the password.
- **Manual app:** knows nothing; you provide the address, username and password.

### Troubleshooting tips
- Username must be exactly **Administrator**.
- Paste the password carefully (no extra characters or spaces).
- Make sure you connect to **your** instance's DNS/IP.
- If the school network blocks the connection, switch to **mobile hotspot**.
- Public DNS/IP can change after stopping/starting an instance.
- Do **not** change the Windows password, because the "Get Windows password" tool cannot recover a changed password.
- Do **not** delete default resources such as the **`vockey`** key pair (created by AWS Academy).

---

## 11. Cleaning Up (Very Important)

1. Close the RDP window.
2. In EC2 → **Instances**: select the instance → **Instance state → Terminate (delete) instance** → confirm.
   - **Warning:** terminating deletes the instance and its root EBS volume. Data is lost and the action cannot be undone.
3. The state goes **Shutting-down → Terminated** (it may still appear in the list for a while).
4. In the Learner Lab page, click **End Lab** (the "shutter" closes; the dot turns red).
5. Key pairs do not cost money and can be kept.

Result: **Used $0 of $50** shows the lab cost was negligible because everything was cleaned up.

---

## 12. Summary of Today's Workflow

1. Joined AWS Academy and launched the Learner Lab.
2. Started the lab and opened the AWS console in `us-east-1`.
3. Opened EC2 and launched a **Windows Server 2025** instance (`t3.micro`).
4. Created a **key pair** (`MyWinkey.pem`).
5. Waited for **3/3 status checks**.
6. Decrypted the **administrator password** with the private key.
7. Connected with **RDP**.
8. **Terminated** the instance and **ended the lab**.

---

## 13. Terminology Cheat Sheet

| Term | Meaning |
|---|---|
| Cloud computing | On-demand computing resources over the internet |
| Public / Private / Hybrid cloud | Shared / dedicated / mixed |
| Multi-tenancy | Many customers share hardware with logical isolation |
| Elasticity | Scale resources up or down as needed |
| Region | Geographic area with AWS data centers (e.g. `us-east-1`) |
| Availability Zone | Data center location within a region (e.g. `us-east-1a`) |
| EC2 | AWS virtual machine service |
| Instance | One virtual machine |
| AMI | OS/software template for an instance |
| Instance type | Hardware size (e.g. t3.micro) |
| Key pair | Public/private keys used to decrypt the Windows password |
| Security group | Cloud firewall for an instance |
| EBS | Virtual hard disk for an instance |
| VPC | Virtual private network in the cloud |
| RDP | Remote Desktop Protocol |
| Terminate | Permanently delete an instance |
| S3 | Object storage service (buckets) |
| PII | Personally Identifiable Information (security concept mentioned) |

---

## 14. Exam / Revision Notes

- The instructor stressed that definitions like **public cloud, private cloud, hybrid cloud, multi-tenancy, elasticity** are **knowledge questions** likely to appear in assessments.
- Be able to explain **why hybrid cloud** puts the database in private and the app server in public.
- Be able to explain **how shared hardware is still secure** (logical boundaries, S3 bucket example).
- Know the **EC2 launch steps** and the **3 status checks**.
- Know the **cost-control rules** (budget, terminate, end lab, delete ELB/NAT).

## 15. Next Week

- Networking fundamentals (read the provided networking material before the next session).
- Security groups (firewall), VPC and network settings.
- EBS storage (Session 3).

---

*Note: These notes were reconstructed from the live class captions and my own hands-on lab work. Sensitive information (passwords, instance IDs, IP addresses, account IDs) has been intentionally left out.*
