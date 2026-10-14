# AWS Cloud Fundamentals — Study Notes (Questions 1–15)

> Study notes on core AWS concepts: compute, storage, networking, security, and automation.
> Format per topic: **Key idea → Explanation → Example → Exam tip → Simple English sentences**.

---

## Table of Contents

1. [Quick Overview (Q1–Q15)](#1-quick-overview-q1q15)
2. [Core Services: EC2, S3, EBS, VPC (Q1–Q5, Q7)](#2-core-services-ec2-s3-ebs-vpc-q1q5-q7)
3. [Public IP (Q6)](#3-public-ip-q6)
4. [S3 Bucket (Q8)](#4-s3-bucket-q8)
5. [Security Group (Q9)](#5-security-group-q9)
6. [S3 vs EBS: Object vs Block Storage (Q10–Q11)](#6-s3-vs-ebs-object-vs-block-storage-q10q11)
7. [S3 Objects and Metadata (Q12)](#7-s3-objects-and-metadata-q12)
8. [CIDR Notation (Q13)](#8-cidr-notation-q13)
9. [Shared Responsibility Model (Q14)](#9-shared-responsibility-model-q14)
10. [EC2 Launch Template (Q15)](#10-ec2-launch-template-q15)
11. [Key Vocabulary](#11-key-vocabulary)
12. [Self-Check Questions](#12-self-check-questions)
13. [Big Picture Summary](#13-big-picture-summary)

---

## 1. Quick Overview (Q1–Q15)

| Q | Topic | Core Concept | Easy English |
|---|-------|--------------|--------------|
| 1 | EC2 | Virtual servers | EC2 runs virtual servers. |
| 2 | S3 | File storage | S3 stores files. |
| 3 | VPC | Private network | VPC creates private networks. |
| 4 | EBS | Disk storage | EBS provides disk storage. |
| 5 | S3 | Static website files | S3 stores website files. |
| 6 | Public IP | Internet communication | A public IP is used for internet communication. |
| 7 | EBS | Operating system files | EBS stores OS files. |
| 8 | S3 Bucket | Container for objects | A bucket stores objects. |
| 9 | Security Group | Virtual firewall | A Security Group controls traffic. |
| 10 | S3 vs EBS | Object vs block storage | S3 stores objects. EBS provides disks. |
| 11 | EBS | Persistent storage | EBS retains data after EC2 stops. |
| 12 | S3 Object | Data + metadata | An object contains data and metadata. |
| 13 | CIDR | IP address range | CIDR represents IP address ranges. |
| 14 | Shared Responsibility | AWS + customer security | AWS and customers share security responsibilities. |
| 15 | Launch Template | Reusable configuration | A launch template stores reusable EC2 settings. |

---

## 2. Core Services: EC2, S3, EBS, VPC (Q1–Q5, Q7)

| Service | Full Name | What It Does | Analogy |
|---------|-----------|--------------|---------|
| **EC2** | Elastic Compute Cloud | Runs virtual servers (compute) | The computer |
| **S3** | Simple Storage Service | Stores files as objects | A cloud file locker |
| **EBS** | Elastic Block Store | Provides disk (block) storage for EC2 | The computer's hard drive |
| **VPC** | Virtual Private Cloud | Creates an isolated private network in AWS | Your own private network |

**Key points**
- **EC2** is where applications and operating systems run.
- **EBS** holds the EC2 instance's operating system files and data (like a hard drive).
- **S3** stores files such as images, backups, and **static website files** (HTML, CSS, JS, images).
- **VPC** defines the network (IP range, subnets) in which resources such as EC2 live.

> **Easy English:** EC2 runs servers. EBS gives them disks. S3 stores files. VPC connects them in a private network.

---

## 3. Public IP (Q6)

- A **public IP address** is reachable from the internet.
- It allows a resource (e.g., a web server on EC2) to **communicate with the internet**.
- A **private IP** is used only inside the VPC.

> **Easy English:** A public IP is used for internet communication.

---

## 4. S3 Bucket (Q8)

- A **bucket** is a **container** in S3 that holds **objects** (files).
- Bucket names must be globally unique across AWS.

```
S3 (service)
 └── Bucket (container)
      └── Object (data + metadata)
```

> **Easy English:** A bucket stores objects.

---

## 5. Security Group (Q9)

- A **Security Group** acts as a **virtual firewall** for AWS resources such as EC2 instances.
- It **controls inbound and outbound traffic** using rules (protocol, port, source/destination).
- Example: allow **SSH (port 22)** only from your own IP, and **HTTP (port 80)** from anywhere.

> **Security reminder:** Allowing SSH from *everyone* (`0.0.0.0/0`) is a common misconfiguration and a customer responsibility (see Q14).

> **Easy English:** A Security Group controls traffic.

---

## 6. S3 vs EBS: Object vs Block Storage (Q10–Q11)

| Feature | Amazon S3 | Amazon EBS |
|---------|-----------|------------|
| Storage type | **Object** storage | **Block** storage |
| Used for | Files, backups, static websites, media | Disks for EC2 (OS, databases) |
| Attached to EC2? | No (accessed over the network/API) | Yes (acts like a hard drive) |
| Data unit | Object (data + metadata) | Fixed-size blocks |

**Persistence (Q11):** EBS volumes are **persistent** — data is retained even after the EC2 instance is stopped (unlike temporary instance store storage).

> **Easy English:** S3 stores objects. EBS provides disks. EBS retains data after EC2 stops.

---

## 7. S3 Objects and Metadata (Q12)

**Question:** Which storage service stores files and any metadata related to the file as objects in a container?
**Answer: Amazon S3** (EC2 = compute, EBS = block storage, VPC = network).

### Explanation
- **S3** is an **object storage** service.
- Objects are stored inside **buckets**.
- Each **object** contains **file data + metadata**.
- **Metadata = data about data.** It describes the file rather than being the file's content.

### Example

```
Bucket: my-photos
 └── Object: holiday.jpg
      ├── File data:  the actual photo
      └── Metadata:
           ├── Content-Type:   image/jpeg
           ├── Content-Length: 2 MB
           └── Last-Modified:  (time of last change)
```

> Note: Camera details and shooting date (**EXIF data**) can be embedded *inside* the image file itself. S3 metadata (e.g., Content-Type, Content-Length) is separate information that S3 manages for the object.

### Relationship to remember
**S3 (service) → Bucket (container) → Object (data + metadata)**

### Why metadata matters in IT and cyber security
Metadata appears often in security work (e.g., file properties, timestamps, forensic investigation), so understanding "data about data" is a valuable general concept.

### Easy English
- Amazon S3 is an object storage service.
- S3 stores objects inside buckets.
- An object contains data and metadata.
- Metadata is information about data.

> **One sentence to remember:** *"Amazon S3 stores objects in buckets. Each object contains data and metadata."*

---

## 8. CIDR Notation (Q13)

**Question:** A range of IP addresses for an AWS VPC is represented by which notation?
**Answer: Classless Inter-Domain Routing (CIDR) notation.**

### Explanation
CIDR shows **an IP address and the size of its network** together.

```
192.168.1.0/24
│           └── Prefix length: number of network bits
└── Network address
```

- IPv4 addresses have **32 bits**.
- `/24` means the **first 24 bits are the network part**; the remaining **8 bits are host addresses**.
- Number of addresses = **2^(32 − prefix)**.
- `/24` is equivalent to subnet mask **255.255.255.0**.

### Prefix comparison

| CIDR | Subnet Mask | Network bits | Host bits | Total IPv4 addresses |
|------|-------------|--------------|-----------|----------------------|
| /16 | 255.255.0.0 | 16 | 16 | 65,536 |
| /24 | 255.255.255.0 | 24 | 8 | 256 |
| /28 | 255.255.255.240 | 28 | 4 | 16 |

**Rule:** The **larger the prefix number, the fewer addresses** in the network.

### AWS-specific note
In an AWS subnet, **5 IP addresses are reserved by AWS** (network address, VPC router, DNS, future use, and broadcast). So a `/24` subnet has 256 − 5 = **251 usable addresses**.

### Why the other answers are wrong
- **Classful notation** — the older class A/B/C system; CIDR replaced it.
- **Binary notation** — writes addresses in 1s and 0s; does not express a range with a prefix.
- **Dotted-decimal notation** — the format of an address like `192.168.1.10`; does not itself show the network range.

### Easy English
- CIDR stands for Classless Inter-Domain Routing.
- CIDR notation represents a range of IP addresses.
- AWS VPC uses CIDR blocks to define IP address ranges.
- For example, `192.168.1.0/24` contains 256 IP addresses.
- The number after the slash is the network prefix length.

> **One sentence to remember:** *"AWS VPC uses CIDR notation to define IP address ranges."*

---

## 9. Shared Responsibility Model (Q14)

**Question:** Which statement best describes the AWS shared responsibility model?
**Answer:** Security responsibilities are distributed between **AWS (Security *of* the Cloud)** and the **customer (Security *in* the Cloud)**.

### Who is responsible for what?

| | **AWS — Security OF the Cloud** | **Customer — Security IN the Cloud** |
|---|---|---|
| Focus | The cloud infrastructure itself | What the customer puts and configures in the cloud |
| Examples | Physical data center security, servers and hardware, core network infrastructure, virtualization layer | Customer data, IAM users and permissions, Security Group rules, OS patching on EC2 |

### Example
AWS secures the data center where your EC2 server runs. But if you set a weak administrator password or open SSH to the whole internet, that misconfiguration is **your** responsibility.

### Analogy: apartment building
- **Landlord (AWS):** building structure, shared facilities, main entrance.
- **Tenant (customer):** locking their own door, managing keys, protecting valuables.

> **The exact split depends on the service.** With EC2 the customer manages the OS; with fully managed AWS services, AWS manages more of the stack.

### Why the other options are wrong

| Option | Why it is wrong |
|--------|-----------------|
| a) AWS is fully responsible for all security, including customer data | Customers are responsible for their own data and configuration |
| b) Customers are solely accountable for AWS infrastructure | AWS is responsible for the physical infrastructure |
| c) Responsibilities are shared (of vs. in the cloud) | **Correct** |
| d) AWS provides optional security tools | Partly true, but not the definition of the model |

### Easy English
- AWS uses a shared responsibility model.
- AWS is responsible for security **of** the cloud.
- Customers are responsible for security **in** the cloud.
- AWS protects the physical infrastructure.
- Customers protect their data and manage access permissions.

> **Sentences to remember:**
> - *"AWS is responsible for security OF the cloud."*
> - *"Customers are responsible for security IN the cloud."*

---

## 10. EC2 Launch Template (Q15)

**Question:** What is the primary benefit of using an Amazon EC2 launch template?
**Answer: (b) It stores reusable configuration parameters for launching EC2 instances.**

### Explanation
A **Launch Template** is a saved "form" of settings used to create EC2 instances. Instead of re-entering the same settings every time, you reuse the template.

Typical contents:
- **AMI** (Amazon Machine Image / operating system)
- **Instance type** (e.g., `t3.micro`)
- **Security Group**
- **EBS storage** (e.g., 20 GB)
- **Key pair** (for SSH)

```
Launch Template: my-web-server-template
   AMI: Ubuntu Linux | Type: t3.micro | SG: web-server-sg | EBS: 20 GB
        │
        ├──► EC2 #1
        ├──► EC2 #2
        └──► EC2 #3     (all with identical configuration)
```

**Benefits:** saves time, reduces configuration errors, keeps servers consistent.

### Analogy: recipe
- Recipe = Launch Template
- Ingredients and settings = AMI, instance type, Security Group
- Finished dish = EC2 instance

### Why the other options are wrong

| Option | Related AWS feature | Description |
|--------|---------------------|-------------|
| a) Automatic scaling | **EC2 Auto Scaling** | Adjusts the number of servers based on demand |
| b) Reusable configuration | **EC2 Launch Template** | **Correct** — stores reusable settings |
| c) Monitoring and logging | **Amazon CloudWatch** | Metrics and logs for performance |
| d) Encryption | **AWS KMS / EBS encryption** | Protects data at rest and in transit |

### Launch Template vs Auto Scaling
They are **different features that work together**:
- **Launch Template** defines **what** to launch (the configuration).
- **Auto Scaling** decides **when and how many** to launch or remove.

Example: when website traffic increases, Auto Scaling launches new EC2 instances using the settings stored in the Launch Template.

### Easy English
- An EC2 Launch Template stores configuration settings.
- We can reuse these settings to launch EC2 instances.
- A launch template can include an AMI, instance type, and security group.
- It saves time and reduces configuration errors.
- We can use one template to launch multiple EC2 instances.

> **One sentence to remember:** *"An EC2 Launch Template stores reusable configuration settings for launching EC2 instances."*

---

## 11. Key Vocabulary

| English | Meaning (Korean) | Notes |
|---------|------------------|-------|
| Object | 객체 | Data + metadata in S3 |
| Metadata | 메타데이터 | Data about data |
| Container | 컨테이너 | A bucket is a container |
| Bucket | 버킷 | S3 container |
| Related to | ~와 관련된 | "metadata related to the file" |
| Contain | 포함하다 | "An object contains data and metadata." |
| CIDR | 클래스 구분 없는 도메인 간 라우팅 | Classless Inter-Domain Routing |
| Notation | 표기법 | |
| Range | 범위 | "a range of IP addresses" |
| Prefix | 접두부 | Number after the slash |
| Subnet mask | 서브넷 마스크 | /24 = 255.255.255.0 |
| Represent / Define | 나타내다 / 정의하다 | |
| Shared | 공유된, 공동의 | |
| Responsible for | ~에 책임이 있는 | "AWS is responsible for physical security." |
| Infrastructure | 인프라 | |
| Permission | 권한 | |
| Launch | 실행하다 | |
| Template | 템플릿 | |
| Configuration | 구성, 설정 | |
| Reusable | 재사용 가능한 | Key word in Q15 |
| Primary benefit | 주요 장점 | |

---

## 12. Self-Check Questions

1. **Which service provides virtual disks for EC2?**
   Amazon S3 / **Amazon EBS** / Amazon VPC → **Amazon EBS**
2. **Which AWS feature acts as a virtual firewall?**
   **Security Group** / S3 Bucket / Launch Template → **Security Group**
3. **What is the main purpose of a Launch Template?**
   Monitor performance / **Store reusable EC2 settings** / Create an IP address range → **Store reusable EC2 settings**

### Practice answering in English
- *What is an object in Amazon S3?* → An object contains file data and metadata. Amazon S3 stores objects in buckets.
- *What is CIDR notation?* → CIDR is a notation used to represent a range of IP addresses.
- *What is the Shared Responsibility Model?* → AWS and customers share security responsibilities. AWS secures the cloud; customers secure what they put in the cloud.
- *What is the main benefit of an EC2 Launch Template?* → We can save and reuse configuration settings to launch EC2 instances.

---

## 13. Big Picture Summary

```
VPC (private network, defined by a CIDR block)
 ├── Security Group (virtual firewall)
 └── EC2 instance (virtual server, launched from a Launch Template)
      └── EBS volume (persistent disk: OS and data)

S3 (object storage)
 └── Bucket → Object (data + metadata)

Security: AWS secures the cloud; the customer secures what is in the cloud.
```

**Next step:** Re-take all 15 questions without looking at the answers, reading the English question and choosing the answer yourself.
