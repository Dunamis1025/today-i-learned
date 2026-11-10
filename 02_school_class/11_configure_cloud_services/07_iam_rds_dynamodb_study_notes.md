# ICTCLD401 – Study Notes: IAM, RDS, DynamoDB and Learner Lab Operations

> Course: ICTCLD401 Configure cloud services (22603VIC), Holmesglen – Cert IV Cyber Security
> Date: 10 Nov 2026
> Scope: AWS IAM (Cloud Foundations Lab 1), Amazon RDS (Assessment 2 Part 4), NoSQL / DynamoDB basics, and how I manage resources in the AWS Learner Lab.
> Note: No passwords, key files or account secrets are included in these notes.

---

## 1. AWS IAM (Identity and Access Management)

### 1.1 What is IAM?
- IAM controls **who** can sign in (authentication) and **what** they can do (authorization) in an AWS account.
- IAM is a **global** service. It is not tied to a Region, so I do not change the Region when working in IAM.
- **By default, everything is denied.** A user can do nothing until a policy allows it.
- An **explicit Deny** always wins over an Allow.

### 1.2 Main building blocks

| Item | Meaning | Restaurant analogy |
|---|---|---|
| **User** | One person or application with its own sign-in. | A staff member with a name badge. |
| **Group** | A collection of users. Permissions are attached to the group, not to each person. | A job role, such as "Kitchen team". |
| **Policy** | A JSON document that lists what is allowed or denied. | The rule book for that role. |
| **Role** | Temporary permissions that a user, service or app can assume. | A temporary pass. |

**Best practice:** attach policies to **groups**, then add users to groups. This is easier to manage than giving permissions to each user.

### 1.3 Policy document structure (JSON)

| Element | Purpose |
|---|---|
| `Version` | Policy language version (`2012-10-17`). |
| `Statement` | A list of permission rules. |
| `Effect` | `Allow` or `Deny`. |
| `Action` | The API actions, such as `ec2:StartInstances`. A wildcard like `ec2:Describe*` matches all actions that start with `Describe`. |
| `Resource` | What the action applies to. `"*"` means all resources. |

### 1.4 Policy types
- **AWS managed policy**: created and maintained by AWS (for example `AmazonEC2ReadOnlyAccess`). I can attach it but cannot edit it.
- **Customer managed policy**: created by me and reusable.
- **Inline policy**: written directly inside one user, group or role. It belongs only to that identity.

### 1.5 Lab 1 – Introduction to AWS IAM (AWS Academy Cloud Foundations, Module 4)

| User | Group | Policy | Type | What it allows |
|---|---|---|---|---|
| user-1 | S3-Support | `AmazonS3ReadOnlyAccess` | AWS managed | View S3 buckets and objects only (`s3:Get*`, `s3:List*`, `s3:Describe*`). Cannot upload, modify or delete. |
| user-2 | EC2-Support | `AmazonEC2ReadOnlyAccess` | AWS managed | View EC2 and related resources (EC2, Auto Scaling, ELB, CloudWatch read access). Cannot start, stop or change instances. |
| user-3 | EC2-Admin | `EC2-Admin-Policy` | Inline (customer) | View EC2 information and **start and stop** instances. |

The inline policy for the EC2-Admin group:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "ec2:Describe*",
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": ["*"],
      "Effect": "Allow"
    }
  ]
}
```

**Steps I followed (summary):**
1. Check the three groups and the policy attached to each group (Permissions tab).
2. Open each policy and read the JSON (or the Summary view).
3. Add user-1, user-2 and user-3 to the correct groups, following the lab diagram (user-3 → EC2-Admin, user-2 → EC2-Support, user-1 → S3-Support).
4. Check the result on the **User groups** page (each group shows 1 user) and in each group's **Users** tab.

**IAM sign-in URL format:** `https://<account-id>.signin.aws.amazon.com/console`

**Key idea – least privilege:** give users only the permissions they need for their job, nothing more.

---

## 2. Amazon RDS (Relational Database Service) – Assessment 2 Part 4

### 2.1 What is RDS?
- A **managed** relational database service. AWS handles the server, patching, backups and basic maintenance.
- Data is stored in **tables** with a fixed structure (rows and columns) and queried with **SQL**.
- Engines include MySQL, MariaDB, PostgreSQL and others.
- Analogy: EC2 is the kitchen, RDS is a managed **storage room** that AWS keeps tidy for me.

### 2.2 Requirements for the task
- **Standard Create**, **MySQL** engine.
- Small instance size: **2 vCPU and 1 GiB RAM**.
- Use the **default VPC** and the **default security group**.
- **Public access: Yes**.

### 2.3 Connecting from an EC2 instance
1. Install the MariaDB package with the CLI on the EC2 instance (Amazon Linux 2023):
   ```bash
   sudo dnf install mariadb105-server -y
   ```
   The package list includes the client programs, so the `mysql` command becomes available.
2. Verify the installation:
   ```bash
   mysql --version
   ```
   My output showed MariaDB 10.5.29.
3. Connect to the RDS database with the endpoint, port and user name:
   ```bash
   mysql -h <rds-endpoint> -P 3306 -u admin -p
   ```
   The password is typed when prompted and is not shown on screen.
4. Success looks like the **"Welcome to the MariaDB monitor"** message and the `MySQL [(none)]>` prompt.
5. The Python web app page shows **"Database connected"**, which confirms the web server can reach the RDS database.

### 2.4 Errors I saw

| Error | Meaning | Note |
|---|---|---|
| `ERROR 1045 (28000): Access denied for user` | The database refused the login (authentication failed). | The first attempt failed and the second attempt worked. |
| `ERROR 1064 (42000): You have an error in your SQL syntax` | The database received something that is not valid SQL. | I typed a **shell command** (`mysql --version`) inside the MySQL prompt. Shell commands must be typed **outside** the MySQL prompt. |

### 2.5 Concepts to remember
- **Endpoint** = the DNS address of the database. **Port** for MySQL = **3306**.
- The client (EC2) must be allowed by the database's **security group** on port 3306.

---

## 3. NoSQL and Amazon DynamoDB (basics)

### 3.1 What is DynamoDB?
- A **NoSQL** database. Data is stored as **items** in **tables**, and items can have flexible attributes.
- Each table has a **primary key**. The **partition key** decides where the item is stored.
- Capacity can scale automatically as the number of users grows.
- It suits large amounts of unstructured or semi-structured data and unpredictable traffic spikes.

### 3.2 RDS vs DynamoDB

| | RDS (relational) | DynamoDB (NoSQL) |
|---|---|---|
| Data model | Tables with a fixed schema | Items with flexible attributes |
| Query | SQL | Key-based access (`GetItem`, `PutItem`) |
| Scaling | Mainly scale **up** (bigger server) | Scales **out** automatically |
| Best for | Orders, transactions, structured data | Large, fast-growing, flexible data |

### 3.3 Teacher's example (C# in Visual Studio)
- Table `Students` with the key `StudentID`.
- `PutItem` adds or replaces an item. `GetItem` reads an item by its key.
- **Partitioning** idea: big data is split into partitions by key, so the work is spread across many servers.

---

## 4. Recap of Assessment 2 – Parts 2 to 4 (what I built)

| Part | Topic | Key points |
|---|---|---|
| 2 | VPC | CIDR `192.168.12.0/24` split into two `/25` subnets. The **public** subnet has a route to the **Internet Gateway**. The **private** subnet has no such route, so its instance cannot reach the Internet. Tested with `ping` from both instances. |
| 3 | EC2 + EBS | Launched a Linux instance, hosted the Python web app, then attached a second **15 GiB EBS** volume: `mkdir` → `mkfs -t ext3` → `mount` → `df -h` to verify. |
| 4 | RDS | Created a MySQL RDS instance and connected from EC2 (section 2 above). |

---

## 5. Learner Lab operations (cost control and safety)

- **Stop** EC2 instances when I finish. Do **not** delete the launch template (`WebServerFactory`); it is needed later.
- **Start Lab** can set EC2 instances back to *Running*, so I check the instance states every time I start the lab.
- **RDS "Stop temporarily"** lasts at most **7 days**, then AWS restarts it automatically. A stopped database still costs **storage** money.
- Learner Lab (budget-limited) and the Cloud Foundations lab are **two separate AWS accounts**.
  - Error: *"You must first log out before logging into a different AWS account."*
  - Fix: close the other console tabs, log out using the "here" link, then click the AWS link again.
- If a console shows an explicit-deny error, the session may be stale. Close the tab and open the console again from the lab link.
- **Never** paste key files, passwords or secrets into documents, chats or GitHub.

---

## 6. Key terms

| Term | Short meaning |
|---|---|
| IAM | Controls who can do what in AWS. |
| Policy | JSON rules that allow or deny actions. |
| Inline policy | A policy stored inside one identity only. |
| Least privilege | Give only the permissions that are needed. |
| RDS | Managed relational database service. |
| Endpoint | The address used to connect to the database. |
| DynamoDB | Managed NoSQL key-value / document database. |
| Partition key | The key that decides where an item is stored. |
| EBS | Block storage (virtual hard drive) for EC2. |
| IGW | Internet Gateway; lets a VPC reach the Internet. |

---

## 7. Next steps
- **Part 5** (due 28 Nov): multi-layer web application with a **launch template**, **target group**, **load balancer** and **Auto Scaling group**, plus testing the scaling policy.
- Learn the **Elastic Load Balancer** (next class) and review DynamoDB questions for the submission.
