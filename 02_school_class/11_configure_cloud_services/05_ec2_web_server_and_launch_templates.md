# ICTCLD401 – Session 3: Hosting a Web App on EC2, User Data and Launch Templates

> Date: 2026-10-20 | Unit: ICTCLD401 Configure cloud services | Environment: AWS Academy Learner Lab (us-east-1, N. Virginia)

## 1. Big picture

Goal of the session: create a Linux EC2 instance, install a web server environment, host a Python (Flask) application, reach it from a browser, then **automate the whole process** with *User data* and a *Launch template*.

Laptop analogy used by the instructor:

| Laptop | AWS equivalent |
|---|---|
| Buy a laptop | Launch an EC2 instance |
| Install runtime/framework (.NET, Flask) | Set up the web server environment |
| Write/copy your code onto it | Deploy the application code |
| Publish it with a domain | Access via public IP/DNS (+ optional domain) |

A **server** is software that is always running and *listening* for requests (via a socket), responds to the client, then waits again. Frameworks (Flask for Python, .NET for C#) provide this plumbing so we do not code sockets by hand.

## 2. Assessment context (Assessment 2 – Build and Configure Cloud Services)

- Part 3 requirements: Linux, Free Tier AMI, 8 GB disk, host the Python app from GitHub (`qiaoli116/ictcld401-python-app`).
- 3.1 Screenshots of the instance showing **OS, CPU, memory, hard drive**.
- 3.2 Browser screenshot with **IP address and port** visible in the URL.
- 3.3 Attach a 15 GB EBS volume, format and mount it via CLI (**covered next week**).
- Submission is split into three dated parts in Brightspace; students gave feedback that one final submission would be clearer (suggested compromise: optional interim submissions with feedback + single final deadline).
- Keep multiple backups of the Word document (USB, cloud, email).

## 3. Learner Lab basics

1. Open AWS Academy → Learner Lab → Modules → *Launch AWS Academy Learner Lab* → **Start Lab**.
2. Wait for the AWS indicator to turn **green**, then click **AWS** to open the console.
3. Session length is ~4 hours; budget is **$50**. Exceeding it destroys the environment.
4. When the timer ends, resources persist but running EC2 instances are stopped. RDS keeps running and costing money, so delete what you do not need.
5. Always check the region is **us-east-1**.
6. **End Lab** when finished.

## 4. Security group (the instance firewall)

- Created **before** the instance: `WebAppSecurityRules` (default VPC).
- **Inbound** = traffic coming *into* the server (this is what we configure). **Outbound** = traffic leaving the server (left as allow-all).
- Rules used in class (lab convenience only): All ICMP-IPv4, SSH (22), All TCP, source `0.0.0.0/0`.
  - `0.0.0.0/0` = anywhere on the internet.
  - ICMP enables `ping`.
- **Security note:** allowing all TCP from anywhere is not production practice. In real systems open only required ports (e.g., 22 from a trusted IP, 8080 for the app).
- Rules can be edited later (Edit inbound rules → Save rules). Add a `Name` tag to find it easily.
- Do **not** delete this security group; it is reused.

## 5. Launching the EC2 instance

Four key choices (plus storage):

1. **OS / AMI:** Amazon Linux 2023 (Free tier eligible).
2. **Hardware:** `t3.micro` – 2 vCPU, 1 GiB memory (Free tier eligible).
3. **Access credentials:** key pair **`vockey`** (pre-created in Learner Lab – no need to create a new one; name is case-sensitive).
4. **Security group:** select existing → `WebAppSecurityRules`.
5. **Storage:** 8 GiB gp3 root volume (`/dev/xvda`).

Notes:
- Default VPC is used for this session (custom VPC was last week).
- Wait for **Status check 3/3 (or 2/2) passed** before connecting.
- Public IPv4 changes if an instance is stopped/started; use the current one.
- Keep instance count low – each running instance consumes credits.

### Where to find 3.1 evidence
- Instances → select instance → **Details** (AMI name, Platform details = OS).
- **Storage** tab (8 GiB volume).
- Instance Types page / instance type detail (vCPUs 2, Memory 1 GiB).
- Highlight evidence with red boxes and add a short caption.

## 6. Connecting and installing the web server (manual method)

Connect: Instances → Connect → **EC2 Instance Connect** (browser terminal, user `ec2-user`). SSH from Linux/Mac/Windows 10-11 also works (`.pem` key; `.ppk` is only needed for PuTTY). Last week's Windows server used **RDP** (Remote Desktop Protocol – GUI) instead of SSH (text commands).

```bash
sudo yum update -y                                   # always patch the OS first
sudo yum install -y python3 python3-pip unzip wget   # runtime + tools
sudo pip3 install --upgrade pip
sudo pip3 install flask mysql-connector-python       # web framework + MySQL driver
wget https://github.com/qiaoli116/ictcld401-python-app/archive/refs/heads/main.zip
unzip main.zip
mv ictcld401-python-app-main WebServer
cd WebServer
python3 app.py                                       # starts Flask on port 8080
```

Observations:
- pip warning about running as root and an "Cannot uninstall pip" error are harmless here.
- App listens on **port 8080**. Open `http://<public-ip>:8080` (use **http**, not https).
- Do not press Ctrl+C in that terminal – it stops the server (`python3 app.py` is a foreground process).
- Warnings on the page are expected at this stage: S3 static content and database (RDS) are not configured yet (Part 4/5).
- Files downloaded with `wget` live on the **EC2 instance**, not the student's laptop.

## 7. Troubleshooting notes

| Symptom | Cause / Check |
|---|---|
| `ERR_CONNECTION_TIMED_OUT` | Check the Flask process is actually running (this was one classmate's cause), then security group/port, then local network |
| Page will not load | Wrong/old public IP, `https://` instead of `http://`, missing `:8080` |
| Works for others but not you | VPN, ISP port blocking, CGNAT (some ISPs block inbound/non-standard ports) |
| Cannot delete security group/VPC | Still attached to a resource |
| Terminate menu greyed out | Already-terminated instances selected – filter by `Instance state = running` |

Lesson: diagnose in order – **process running → port/security group → network path**.

## 8. Automation with User data

*User data* is a script that runs **once at first boot** (bootstrap), so no manual SSH is needed. Paste it in **Advanced details → User data** (plain text; leave "already base64 encoded" unchecked). Paste through Notepad first to avoid hidden formatting.

Script structure (same commands as manual setup):
1. `#!/bin/bash` shebang.
2. `yum update`, install Python/pip/unzip/wget, pip install Flask + MySQL connector.
3. `wget` the app zip, `unzip`, rename to `python-app`.
4. Commented lines (`#`) for `setup.py` config (port, S3 base URL, DB endpoint, port 3306, user, password) – uncommented later for Part 4/5.
5. Create a **systemd service** (`/etc/systemd/system/my_python_app.service`) with `Restart=always`.
6. `systemctl daemon-reload`, `start`, `enable` – app starts now and after every reboot.

Result: launching an instance with this script brought the web app up automatically at `http://<public-ip>:8080`.

## 9. Launch templates ("the factory")

A **launch template** stores instance settings so identical servers can be created repeatedly – and is what **Auto Scaling groups** use in Part 5.

Created `WebServerFactory` (version 1) containing:
- Name and version description
- AMI: Amazon Linux 2023
- Instance type: t3.micro
- Key pair: vockey
- Security group: `WebAppSecurityRules`
- Storage: 8 GiB
- Advanced details → **User data** script
- Subnet / Availability Zone left as *Don't include* (Auto Scaling decides later)

Usage: Launch templates → Actions → **Launch instance from template** → set *Number of instances* (e.g., 5) → **Launch instance**. Five identical servers started and each served the app automatically (each page shows a different Instance ID / Public IP).

Pitfall observed: clicking Launch twice created two batches (10 instances). Check *Instances* with the `running` filter before relaunching.

Do **not** delete the launch template or security group – needed for Part 5.

## 10. Public vs private IP

- **Public IP/DNS:** reachable from the internet (browser → web server).
- **Private IP** (e.g., `172.31.x.x`, shown as "Local IP"): reachable only inside the VPC. Used for server-to-server traffic such as web server ↔ database, load balancer ↔ targets, public-subnet EC2 ↔ private-subnet EC2 (last week's Part 2). Servers in a private subnet have no public IP.

## 11. Clean-up ("always leave a clean plate")

- Terminate all instances after use (Instance state → Terminate). Verify EC2 dashboard shows **0 running instances**.
- **Keep:** security groups (default + `WebAppSecurityRules`), default VPC, route table, internet gateway, launch template.
- **End Lab** at the end of the session.

## 12. Background concept: how a CPU works (instructor's whiteboard)

- **Clock / cycles per second (Hz):** CPU works on a repeating high/low signal; more cycles per second = faster.
- **Registers (AX, BX, CX, DX):** very fast storage inside the CPU where data is loaded from memory.
- **ALU (Arithmetic Logic Unit):** performs calculations on register values.
- **32-bit vs 64-bit:** amount of data handled per cycle; 64-bit moves more data per cycle and addresses a far larger **address space** (memory is accessed via buses).
- Relevance: `t3.micro` = 2 vCPU, `x86_64` (64-bit) architecture.

## 13. Key takeaways

1. Environment (OS + runtime/framework) first, then application code on top.
2. Security group = instance firewall; Inbound controls who can reach the server.
3. User data automates setup; launch templates make servers repeatable and are the foundation of Auto Scaling.
4. Troubleshoot methodically and verify the service is running before blaming the network.
5. Control cost: terminate unused resources, keep reusable ones (security group, template).

## 14. Next steps

- Complete 3.1 and 3.2 evidence in the Word document (done) and keep backups.
- **Next week:** 3.3 – attach a 15 GB EBS volume, format and mount via CLI; then Part 4 (RDS) and Part 5 (target group, load balancer, launch template, Auto Scaling).
