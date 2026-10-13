# Session 6: Subnetting, Amazon VPC and EC2 in a Custom VPC

> Date: 2026-10-13 | Unit: ICTCLD401 Configure Cloud Services | Instructor: Jefi Varghese
> Environment: AWS Academy Learner Lab (budget: $50, region: N. Virginia / us-east-1)

## 1. Overview

Today covered the networking basics needed for cloud design, then applied them hands-on by building a custom **Amazon Virtual Private Cloud (VPC)**, launching EC2 instances into it, verifying connectivity, and cleaning everything up.

- The VPC content is not assessed on its own, but it is the foundation for **Assessment Two, Part 2** (build and verify a VPC and EC2 instances).
- The unit is graded **Satisfactory / Not Yet Satisfactory** (no exam). Assessment One is knowledge questions; Assessment Two is "Build and Configure Cloud Services".

## 2. Networking Fundamentals

### 2.1 Why subnet? (Subnetting)

Subnetting splits one large network into smaller networks. Analogy used in class: a campus with many buildings and hundreds of rooms. One flat network means every lookup disturbs everyone; separate buildings (subnets) are easier to manage.

Benefits:
1. **Redundancy / fault isolation**: a problem (e.g. ransomware, maintenance) in one subnet does not affect the others.
2. **Less unnecessary traffic**: a router sends traffic only toward the subnet that holds the destination.
3. **Faster lookups / better performance**: smaller search space (compared to how B+ trees speed up database search).
4. **Easier administration**: each subnet can be managed independently.

### 2.2 IP addresses and octets

- An IPv4 address has **4 octets x 8 bits = 32 bits**, written in dotted decimal (e.g. `192.168.12.0`).
- Always write each octet with 8 binary digits (pad with leading zeros).

### 2.3 Decimal to binary (divide by 2)

Repeatedly divide by 2 and read the remainders **from bottom to top**.

| Decimal | Binary |
|---|---|
| 192 | 11000000 |
| 168 | 10101000 |
| 12 | 00001100 |
| 0 | 00000000 |

So `192.168.12.0` = `11000000.10101000.00001100.00000000`.

### 2.4 CIDR notation and prefix length

- `/24` = **Classless Inter-Domain Routing (CIDR)** prefix: the first 24 bits are fixed (the **network ID**); the remaining bits identify hosts.
- Old class-based terms (Class A/B/C) are outdated; think "how many bits are fixed".
- `192.168.12.0/24` gives 8 host bits = 256 addresses.

### 2.5 Splitting a network

Borrowing bits from the host portion creates more, smaller subnets:

| Prefix | Borrowed bits | Subnets | Addresses per subnet |
|---|---|---|---|
| /24 | 0 | 1 | 256 |
| /25 | 1 | 2 | 128 |
| /26 | 2 | 4 | 64 |

Rule: **borrowed bits = n gives 2^n subnets**. The total address space stays the same; each subnet just gets smaller.

## 3. Amazon VPC Concepts

**VPC (Virtual Private Cloud)** = a logically isolated virtual network inside AWS that you control.

Design used in class (private example range):

```
AWS Cloud
└── VPC 192.168.12.0/24
    ├── Public subnet  192.168.12.0/25    -> Internet Gateway (two-way)
    └── Private subnet 192.168.12.128/25  -> NAT Gateway (outbound only)
```

| Component | Purpose |
|---|---|
| **Public subnet** | Reachable from the internet (route to an Internet Gateway) |
| **Private subnet** | Not reachable directly from the internet |
| **Internet Gateway (IGW)** | Two-way door between the VPC and the internet |
| **NAT Gateway** | Placed in the public subnet; lets private instances reach out (e.g. updates) but blocks inbound connections |
| **Route table** | Tells traffic where to go (public -> IGW, private -> NAT) |
| **Availability Zone (AZ)** | Separate data-centre area in a region; one AZ used in the lab |

Analogy from class: a private subnet is like reaching out of a window to pick coconuts from a tree, while nobody outside can walk in.

### Other concepts

- **DHCP** assigns IP addresses automatically within the subnet range; a normal IP can change after a stop/start.
- **Elastic IP** = a static public IP that does not change; unattached or unused ones can cost money.
- **Security group** = **instance-level** firewall. **Network ACL (NACL)** = **subnet-level** firewall.
- Private IP is used inside the VPC; public IP is needed to reach an instance from the internet.

## 4. Hands-on Lab (Steps)

### 4.1 Security group

1. VPC console -> Security groups -> Create security group.
2. Name `MySecurityGroup`, description "Security Group rules" (default VPC at first).
3. Inbound rules: **All ICMP-IPv4, All TCP, SSH**, source `0.0.0.0/0` (lab only, not for production).
4. Outbound rules: default **All traffic**.
5. Add a tag `Name` (key) with a value (tags are what make the name column show in the console).
6. Later: **VPC associations -> Associate VPC** to link the security group to `MyVPC`.

Common mistake seen: putting the inbound rules in the **Outbound** section.

### 4.2 Create the VPC ("VPC and more")

1. VPC -> Create VPC -> **VPC and more**.
2. Name tag `MyVPC`, IPv4 CIDR `192.168.12.0/24` (type it manually; pasting can fail).
3. AZs: 1, public subnets: 1, private subnets: 1.
4. Customize subnet CIDRs: public `192.168.12.0/25`, private `192.168.12.128/25`.
5. NAT gateway: **Regional**; VPC endpoint (S3 gateway) and DNS options left at defaults.
6. Create VPC and wait for all workflow steps (NAT activation takes the longest).
7. Check the **Resource map**: 2 subnets, route tables, Internet gateway, NAT gateway.

Notes:
- **Do not delete the default VPC.**
- If creation fails in N. Virginia, retry or fall back to defaults (10.0.0.0/16).

### 4.3 Launch EC2 instances (public subnet)

Settings:
- AMI **Amazon Linux 2023**, type **t3.micro** (free tier eligible), key pair **vockey** (provided by the lab, do not create or share keys).
- Network settings -> Edit: VPC `MyVPC-vpc`, **public subnet**, **Auto-assign public IP = Enable**, security group **Select existing -> MySecurityGroup**.
- Storage 8 GiB gp3, no file systems. Names: `PublicEC2#1`, `PublicEC2#2`.
- Wait for **3/3 status checks passed** (network, OS, hardware healthy).

Important: when editing network settings, auto-assign public IP can flip to Disabled; turn it back on, otherwise the instance cannot be reached.

A **private instance** (demo only, not required for the assessment) uses the private subnet with auto-assign public IP **Disabled**.

### 4.4 Connect and verify

- Connect with **EC2 Instance Connect** (browser terminal, user `ec2-user`). School Wi-Fi can block SSH (the instructor used a hotspot).
- Commands used:
  - `ifconfig` -> confirm the private IP is inside the public subnet range
  - `ping www.google.com.au` (stop with Ctrl+C) -> confirm internet access through the IGW (0% packet loss)
- Evidence for the assessment: instance details (public and private IP visible), `ifconfig` output, `ping` output, each highlighted with a red box.

Observations:
- Public instances respond to ping and can be accessed; instances in the private subnet cannot be reached directly from outside.
- Closing the browser tab only ends the session; the instance keeps running and billing.

## 5. Cleanup (Cost Control)

Order used:
1. EC2 -> select instances -> **Terminate** (Stop is not enough for cost cleanup; Terminate deletes).
2. VPC -> **NAT gateways** -> delete (billed hourly, slowest step).
3. **Elastic IPs** -> release any left.
4. **Delete VPC** (select only your VPC, type `delete`); subnets, route tables and IGW are removed together.
5. Learner Lab -> **End Lab**.

Notes:
- The security group can stay (no cost); deleting it fails until it is disassociated from the VPC.
- Keep budget for next week; the lab environment can be recreated at any time.
- If an assessment screenshot is still missing, capture it **before** deleting resources.

## 6. Assessment Two Notes

- Structure: Section A knowledge questions (13); Section B build tasks in 5 parts (access, VPC, EC2, RDS, multi-layer web app and reflection).
- Part 2 evidence: VPC, two subnets, Internet gateway; then two EC2 instances showing private IP, public IP and internet access, each with a short explanation **in my own words**.
- Screenshot tips from the instructor:
  - Highlight only the relevant part with a red box.
  - Show resource names and IDs so the work is identifiable as mine; account or login details are not needed.
  - Do not over-crowd the answer cells.
- Generative AI may help with editing but not write full answers; AI use must be acknowledged in the document.
- Part 3 (hosting a web app, attaching a second EBS volume) was not covered today.

## 7. Key Takeaways

- Subnetting = performance + isolation + manageability; **n borrowed bits = 2^n subnets**.
- VPC = my own isolated network; **public subnet -> IGW, private subnet -> NAT**.
- Security group (instance) vs NACL (subnet).
- Always enable public IP for public-subnet instances, and always **clean up NAT, Elastic IPs and instances** to protect the budget.

## 8. Glossary

| Term | Meaning |
|---|---|
| VPC | Virtual Private Cloud |
| CIDR | Classless Inter-Domain Routing (prefix notation such as /24) |
| IGW | Internet Gateway |
| NAT | Network Address Translation |
| AZ | Availability Zone |
| DHCP | Dynamic Host Configuration Protocol |
| ICMP | Protocol used by ping |
| SSH | Secure Shell, remote Linux access (port 22) |
| EC2 | Elastic Compute Cloud (virtual servers) |
