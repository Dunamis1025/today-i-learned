# ICTCLD401 – Session 6: Target Group, Application Load Balancer, Auto Scaling Preview and IaaS / PaaS / SaaS

> Course: ICTCLD401 Configure cloud services (22603VIC), Holmesglen – Cert IV Cyber Security
> Date: 17 Nov 2026
> Environment: AWS Academy Learner Lab (us-east-1, N. Virginia)
> Scope: Assessment 2 Part 5 (multi-layer web application), a preview of Auto Scaling, and the cloud service models.
> Note: No account IDs, ARNs, DNS names, instance IDs, key files or passwords are included in these notes.

---

## 1. Big picture

Goal of Part 5: build a **multi-layer web application** where several identical EC2 servers sit behind one load balancer.

```
Browser  ──HTTP:80──▶  Application Load Balancer  ──HTTP:8080──▶  Target group  ──▶  EC2 x3 (Flask app)
```

Restaurant analogy (with the instructor's "suitcase"):

| Cloud part | Analogy |
|---|---|
| Launch template | A **recipe card** (the "factory") that builds identical kitchens |
| EC2 instance | One **kitchen** |
| Target group | A **suitcase** that holds the kitchens the load balancer may use |
| Load balancer | The **host / coordinator** who sends each customer to a kitchen |
| Auto Scaling group (next week) | An **automatic manager** that adds or removes kitchens |

Order of work: security group → launch template → 3 instances → target group → load balancer → verify → (next week) Auto Scaling.

---

## 2. Security group

- The same security group from Part 3 is reused (default VPC).
- New rule for this session: **Custom TCP 8080**, because the Flask app listens on port 8080.
- The instructor said **do not delete the security group or the launch template**. Both are reused next week.
- Lab convenience only: the load balancer and instances share one security group with wide-open rules.
- Best practice (my own note, not from class): use a separate security group for the load balancer (allow 80/443 from the internet) and let the instances accept 8080 **only from the load balancer's security group**.

---

## 3. Launch template as a "factory"

- **Launch instance from template** with quantity 3 creates **three identical instances at once**. Nothing is configured by hand on each server.
- The template stores: AMI (Amazon Linux 2023), instance type (`t3.micro`), key pair (`vockey`), security group, 8 GiB storage and **User data** (script that installs and starts the app at first boot).
- Use the **latest / default version** of the template. The instructor was careful about this.
- After launching, wait until the status checks pass (for example `3/3 checks passed`). A new instance may need a refresh before it appears in the list.
- Security: User data can contain database details. **Hide User data / Advanced details in screenshots.**

---

## 4. Target group

Settings that **cannot be changed after creation** (immutable):

| Setting | Value used | Notes |
|---|---|---|
| Target type | **Instances** | Other types: IP addresses, Lambda function, Application Load Balancer |
| Protocol | **HTTP** | Do **not** use TCP. An Application Load Balancer only works with HTTP/HTTPS (instructor) |
| Port | **8080** | The port the app listens on |
| IP address type | IPv4 | |
| VPC | Default VPC | Must be the same VPC as the instances |
| Protocol version | HTTP1 | |

**Health check** (defaults seen in class): protocol HTTP, path `/`, port = traffic port, healthy after **5** consecutive successes, unhealthy after **2** failures, timeout **5 s**, interval **30 s**, success code **200**.

**Register targets:**
1. Select all running instances.
2. Confirm the port is **8080**.
3. Click **Include as pending below**, then **Create target group**.
4. Add a `Name` tag.

**Health status meanings**

| Status | Meaning |
|---|---|
| Healthy | Passed health checks, receives traffic |
| Unhealthy | Failed health checks, gets no traffic |
| **Unused** | The target group is **not attached to any load balancer yet** |
| Initial | Registration in progress, health checks starting |
| Draining | Being removed, finishing existing requests |

- Right after creation the instructor's target group showed **0 Healthy / 0 Unhealthy / 3 Unused**. This is normal. What matters is **0 Unhealthy**.
- Once a load balancer is attached, targets move to Healthy. Briefly seeing Initial or Unhealthy right after registering is possible.

---

## 5. Application Load Balancer (ALB)

Settings I used:

| Setting | Value |
|---|---|
| Type | Application Load Balancer |
| Scheme | Internet-facing |
| IP address type | IPv4 |
| VPC | Default VPC (same as the target group) |
| Availability Zones | At least **2** required (I selected all 6) |
| Security group | The web app security group (default one removed) |
| Listener | **HTTP:80 → forward to the target group (100%)** |
| IPAM pool | Left unchecked |
| Tag | `Name` tag |

- **State flow:** *Provisioning* (a few minutes) → **Active**. The ALB then checks the target group and its machines (instructor's "tough guy" load balancer: it does not trust anything until it checks).
- **Access:** open the load balancer's **DNS name** with **`http://`** (not `https`). Port 80 is the listener port, so no `:8080` is needed.
- **Details tab** shows: type, scheme, state (Active), VPC, Availability Zones and subnets, **load balancer ARN**, DNS name. The **Listeners and rules** tab shows HTTP:80 → target group.
- Careful: the ARN in the **Listeners** table is the **listener** ARN (`listener/app/...`). The **load balancer** ARN (`loadbalancer/app/...`) is under **Details**.

---

## 6. Verifying the application (Task 5.2)

- Open the DNS name in the browser and **refresh**. The page shows the **Instance ID, local IP and public IP** of the instance that handled the request. Different IDs prove the load balancer forwards requests to different EC2 instances.
- Which instance answers is decided by the load balancer. The instructor said it is "not under my control": a refresh may sometimes show the same instance. Using different browsers or windows helps to see all of them.
- At this stage the app shows *"S3 static content is not available"* and *"EC2 server status is not available. Check the database connection"*. This is **expected** for Part 5.

**Troubleshooting (instructor's explanations)**

| Symptom | Meaning |
|---|---|
| **502 Bad Gateway** | The load balancer has no machine to connect to |
| **503 Service Unavailable** | No **healthy** targets can serve the request |
| Targets not reachable | Check VPC / subnets / Availability Zones, protocol HTTP, port 8080 and the security group |

**Evidence rules for the assessment**
- Show the **final result**, not the wizard steps ("I want the results, nothing else").
- For each resource, show the **list view with the resource highlighted (red box)** plus the **Details tab**, with as much information as possible.
- For 5.2, show the browser **URL bar** and the **Instance ID / Public IP**, and at least **two running instances** in the instances list. The public IP on the page should match the instance list.
- Use the Snipping Tool.

---

## 7. Auto Scaling preview (full session next week)

- The instructor stopped all of his instances live to show a "trailer for next week's movie": when machines fail, an **Auto Scaling group** can create replacements automatically.
- **Horizontal scaling:** add more machines when traffic is high (for example up to a maximum of 10) and remove machines when traffic is low.
- Why it matters:
  1. Service continues **without interruption**.
  2. Users get the **same speed** even when traffic grows.
  3. A single machine would be overloaded when many requests arrive.
- Terms for the assignment (Tasks 5.3 and 5.4): **Minimum, Desired and Maximum capacity**, **scaling policy**, **scale out** (add instances) and **scale in** (remove instances). I will confirm the details when we build it next week.
- The Auto Scaling group uses the **launch template** and connects to the **load balancer / target group**.
- Next week the instructor wants us to **repeat today's build by ourselves** (informal assessment). Screenshots may be replaced then.

---

## 8. Cloud service models: IaaS, PaaS and SaaS

The instructor drew a **9-layer stack** and marked which layers the cloud provider manages.

| # | Layer | Instructor's pizza analogy |
|---|---|---|
| 1 | Application | Finished pizza |
| 2 | Data | Ingredients |
| 3 | Runtime | Chef |
| 4 | Middleware | Kitchen services / environment |
| 5 | Operating system | Kitchen services / environment |
| 6 | Virtualization | Kitchen services / environment |
| 7 | Server | Kitchen services / environment |
| 8 | Storage | Kitchen services / environment |
| 9 | Networking | Kitchen services / environment |

(The pizza picture helps understanding. For exams, use the technical wording instead.)

**Who manages what**

| Layer | IaaS | PaaS | SaaS |
|---|---|---|---|
| Application | **Me** | **Me** | Provider |
| Data | **Me** | **Me** | Provider |
| Runtime | **Me** | Provider | Provider |
| Middleware | **Me** | Provider | Provider |
| Operating system | **Me** | Provider | Provider |
| Virtualization | Provider | Provider | Provider |
| Server | Provider | Provider | Provider |
| Storage | Provider | Provider | Provider |
| Networking | Provider | Provider | Provider |

- **SaaS (Software as a Service):** the provider manages everything. I only use the software. Examples from class: **Microsoft 365**, **Salesforce**.
- **PaaS (Platform as a Service):** I manage only my **application and data**. The **platform** = runtime + middleware + OS + virtualization + server + storage + networking, given by the provider. Demo: an **ASP.NET** web app (built in Visual Studio) was **published to Azure App Service**; the runtime stack (.NET LTS) is selected when creating the app service, and no server maintenance is needed.
- **IaaS (Infrastructure as a Service):** the provider gives **virtualization, servers, storage and networking**. I install and manage the **OS, middleware, runtime, data and application**. **Infrastructure** in every cloud means these four layers. Examples: **Amazon EC2** and Azure **Virtual Machines**. Demo: on a Windows virtual machine, **IIS** (a Microsoft web server, not an AWS product) was configured to host a site. This is what we do with EC2 and Flask.
- **Middleware** = the connectivity layer. The **database** is a different thing (instructor).
- Extra note (my own, to verify): AWS has PaaS-style services such as Elastic Beanstalk. In this unit we mainly use EC2, which is IaaS.

**Quick self-check**
1. Which layers does the customer manage in PaaS? → Application and data.
2. Which model gives the most control? → IaaS. Which gives the least work? → SaaS.
3. Is EC2 IaaS, PaaS or SaaS? → IaaS.

---

## 9. Cost and clean-up lessons (Learner Lab)

- The lab allows **9 running EC2 instances at once**. Unused instances should be **Stopped, not Terminated** (Terminate cannot be undone).
- A **load balancer is billed per hour while it exists** and has **no Stop option**. It can only be kept or deleted.
- **RDS** can be **Stopped temporarily**, but it may **start again automatically after up to 7 days** (to verify). Stopped EC2 and RDS still keep some storage cost.
- **Public IPv4 addresses can change** after Stop → Start (no Elastic IP). Instance IDs stay the same.
- When the lab session ends, resources are kept. After **Start Lab**, check EC2 and RDS states and stop anything that restarted.
- Do **not** delete the security group or the launch template.

---

## 10. Key takeaways and next-week checklist

- Launch template → identical instances → target group (HTTP, 8080) → ALB (listener HTTP:80) → test with the DNS name over `http://`.
- 502 = no machine to connect to; 503 = no healthy target. Target group status **Unused** just means it is not attached to a load balancer yet.
- Evidence = final result screens: list with red box + Details tab, URL bar and Instance ID visible.
- IaaS: I manage OS and above. PaaS: I manage application and data. SaaS: I manage nothing.

Next week:
- [ ] Check that the load balancer and target group still exist; check RDS did not restart.
- [ ] Start instances only when needed.
- [ ] Build the Auto Scaling group: Minimum / Desired / Maximum capacity and a scaling policy.
- [ ] Test scale out and scale in and capture the logs (Task 5.4).
- [ ] Fill in the ARN table (target group, load balancer, launch template, Auto Scaling group).
