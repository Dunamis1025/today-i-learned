# Cloud Computing Concepts and AWS Services: Study Notes

Study notes covering cloud technology standards, hardware and software, service models, cost models, core AWS services, scaling, databases, storage and the shared security responsibility model.

---

## 1. Industry Technology Standards in Cloud Computing

| Standard | What it is | Why it matters |
|---|---|---|
| **Virtualization** | A hypervisor abstracts physical hardware (CPU, memory, storage, network) into multiple isolated virtual machines (VMs). | Enables resource pooling, scalability and better hardware utilisation. It is the foundation of cloud computing. |
| **Open Virtualization Format (OVF)** | An open, vendor-neutral file format (by DMTF) for packaging and distributing VMs. A package contains an XML descriptor and disk images. | Lets a VM move between hypervisors and clouds, which avoids vendor lock-in. |
| **Single Sign-On (SSO)** | Log in once and access multiple services (e.g. SAML, OAuth, OpenID Connect). | Better user experience and centralised account management. |
| **Multi-factor authentication (MFA)** | Two or more factors: something you **know** (password), **have** (phone, token) and **are** (biometrics). | A stolen password alone is not enough to log in. |
| **Identity Federation** | A trust arrangement between organisations so one identity can access services across domains. | Users reuse an existing identity (e.g. "Sign in with Google"). |
| **VXLAN** | Encapsulates Layer 2 Ethernet frames in UDP packets to build overlay networks over a Layer 3 network. | About 16 million segments (vs 4,096 VLANs), ideal for multi-tenant data centres. |
| **NFV (Network Functions Virtualization)** | Replaces dedicated network hardware (firewalls, routers, load balancers) with software on standard servers. | Lower cost, less space, faster deployment, easy scaling. |
| **IPsec (Internet Protocol Security)** | A protocol suite that authenticates and encrypts each IP packet. | Secures data in transit, widely used for VPNs between company networks and the cloud. |

**Key distinctions**
- **SSO vs Identity Federation:** SSO is "one login for many apps". Federation is "trust between different organisations".
- **SSO + MFA:** SSO is convenient but is a **single point of failure** if the account is compromised. MFA protects that single login.
- **OVF vs VMware:** VMware is a hypervisor (a program). OVF is a file format that makes VMs portable between programs.
- **VXLAN vs NFV:** VXLAN virtualises the *network itself* (overlay). NFV virtualises *network devices' functions* as software.

---

## 2. Hardware and Software Used in the Cloud

### Hardware
| Hardware | Key points | Examples |
|---|---|---|
| **Servers** | High-performance, reliable, scalable machines with multiple CPUs, fast networking and large memory. | Dell, HP, Lenovo |
| **Networking equipment** | Switches, routers and load balancers connect servers and users. A stable network is essential because many servers communicate at once. | Cisco, Juniper, Arista |
| **Storage devices** | SSD (fast) vs HDD (cheaper, larger). Data is replicated across locations, so one failure does not lose data. | Dell EMC, NetApp, Pure Storage |
| **GPUs** | Thousands of simple parallel cores, ideal for AI training, video editing and scientific computing. Rented on demand in the cloud. | NVIDIA, AMD |

### Software
| Software | Key points | Examples |
|---|---|---|
| **Operating systems** | Industry-standard OSs manage cloud infrastructure. | Linux, Windows Server |
| **Virtualization software** | Divides one physical server into multiple VMs. | VMware ESXi, Microsoft Hyper-V, KVM |
| **Containerization software** | Packages an app with everything it needs into a lightweight container. Lighter and faster to start than VMs. | Docker, Kubernetes (orchestration) |
| **DBMS** | Stores, retrieves and protects data, keeping it consistent when many users read and write at once. | MySQL, PostgreSQL, Oracle, SQL Server, MongoDB |

**VM vs container:** a VM is a complete house. A container is a flat that shares the building's facilities, so it is lighter and starts faster.

---

## 3. Cloud Service Models: IaaS, PaaS, SaaS

| Model | Provider manages | User manages | Analogy | Examples |
|---|---|---|---|---|
| **IaaS** | Hardware, virtualization | OS, applications, data | Rent an empty kitchen | Amazon EC2, Azure Virtual Machines |
| **PaaS** | + OS, development tools | Applications, data | Shared kitchen with tools ready | Google App Engine, Heroku |
| **SaaS** | + the whole application | Data, access | Order at a restaurant | Google Workspace, Microsoft 365, Dropbox |

- **IaaS:** maximum flexibility and control, but the most to manage.
- **PaaS:** developers focus on code. The platform scales automatically.
- **SaaS:** nothing to install, accessible anywhere, usually a monthly subscription.

---

## 4. Cloud Cost Models and Economics

| Model | How it works | Price | Commitment | Interruption risk | Best for |
|---|---|---|---|---|---|
| **Pay-as-you-go (On-Demand)** | Pay only for what you use | Highest unit price | None | None | Short-term or unpredictable workloads |
| **Reserved Instances** | Commit for 1 or 3 years for a discount | Much cheaper | 1 to 3 years | None | Steady, predictable workloads |
| **Spot Instances** | Rent the provider's spare capacity | Cheapest (up to about 90% off) | None | **Yes**, can be reclaimed | Interruption-tolerant jobs (data analysis, testing) |

**Economic ideas**
- **CapEx to OpEx:** no large upfront hardware purchase. Cost becomes an ongoing operating expense.
- **Elasticity:** scale up and down with demand and pay only for what is used.
- **Volume discount logic:** committing to usage lowers the price (Reserved).
- **Spare capacity:** the provider earns from idle resources. Prices follow supply and demand (Spot).

---

## 5. AWS Pricing Models: EC2 vs RDS

| Pricing model | Amazon EC2 | Amazon RDS |
|---|---|---|
| On-Demand | Yes | Yes |
| Reserved Instances | Yes (up to about 72% off) | Yes (up to about 69% off) |
| Savings Plans | Yes (Compute and EC2 Instance plans, more flexible than RIs) | **Database Savings Plans** (1-year term) |
| Spot Instances | **Yes** (up to about 90% off) | **No** |

- **EC2** = Elastic Compute Cloud (virtual servers). **RDS** = Relational Database Service (managed relational DB).
- **Why no Spot for RDS?** A database that shuts down suddenly can cause data problems.
- AWS now recommends Savings Plans over Reserved Instances for new commitments because they are more flexible. Discounts vary by service and time, so always say "up to".

---

## 6. Core AWS Services

| Service | Function | Key points |
|---|---|---|
| **EC2** | Rentable virtual servers | Choose CPU, memory and OS. Launch in minutes. Pay for what you use. |
| **Application Load Balancer (ALB)** | Distributes incoming web traffic across EC2 servers | Prevents overload and sends traffic only to **healthy** servers. |
| **Auto Scaling group** | Adds or removes servers automatically as demand changes | Replaces failed servers. Keeps performance and saves cost. |
| **CloudWatch** | Monitors metrics (e.g. CPU), collects logs, raises alarms | Alarms can trigger Auto Scaling. |
| **S3** (Simple Storage Service) | Near-unlimited object storage | Durable (replicated), pay for what you use. Used for images, backups and sharing. |
| **VPC** (Virtual Private Cloud) | Your own isolated virtual network in AWS | Define IP ranges, subnets and security rules. Decide which servers face the internet. |

**How they work together:** VPC is the private network. EC2 servers run the app. ALB spreads traffic across them. CloudWatch watches load and triggers an alarm. Auto Scaling adds or removes servers. S3 stores files.

---

## 7. Scaling, Machines and Databases

### Vertical vs horizontal scaling
| | Vertical (scale up) | Horizontal (scale out) |
|---|---|---|
| What | Upgrade one server (more CPU or memory) | Add more servers |
| Pros | Simple | Almost unlimited growth, fault tolerant |
| Cons | Hardware limit, single point of failure | Needs a load balancer to distribute requests |

### Physical vs virtual machines
| | Physical | Virtual |
|---|---|---|
| What | A real hardware server for one user | A server created by dividing hardware with software |
| Pros | Full control and performance | Launched in minutes, lower cost, efficient |
| Cons | Expensive, slow to set up | Slight performance overhead |

### Relational vs data warehouse vs NoSQL
| Type | Purpose | Structure | Example |
|---|---|---|---|
| **Relational** | Accurate transactions (orders, banking) | Tables with relationships | Amazon RDS |
| **Data warehouse** | Large-scale analysis and reporting of historical data | Integrated historical data | Amazon Redshift |
| **NoSQL** ("not only SQL") | Flexible, high-volume storage that scales out easily | No fixed tables | Amazon DynamoDB |

### Self-hosted vs managed vs cloud-native databases
| Type | Who operates it | Pros | Cons | Example |
|---|---|---|---|---|
| **Self-hosted** | You | Full configuration freedom | You handle updates, backups and troubleshooting | A database installed on your own server |
| **Managed** | Cloud provider | Less workload | Less configuration freedom | Amazon RDS |
| **Cloud-native** | Cloud provider, designed for the cloud from the start | Automatic scaling, highly reliable | Possible vendor lock-in | Amazon Aurora, DynamoDB |

*Analogy: self-hosted = shop and cook yourself, managed = meal kit, cloud-native = order at a restaurant.*

---

## 8. Cloud Storage Options

| Type | How it works | Pros | Cons | Best for | AWS example |
|---|---|---|---|---|---|
| **Block** | Data in fixed-size blocks, attached to a server like a hard disk | Very fast, low latency | Usually one server at a time, costly | OS and databases | Amazon EBS |
| **Object** | Each file stored as an object with a name tag, accessed over the internet | Near-unlimited, low cost | Slower, objects replaced as a whole | Photos, videos, backups | Amazon S3 |
| **Archive** | Rarely used data kept long term | Lowest cost, long retention | Retrieval takes minutes to hours and may cost extra | Compliance records, old backups | S3 Glacier |
| **Network file system** | Many servers share the same folders over a network | Folder structure, concurrent access | Slightly slower than block, costlier than object | Shared documents and files | Amazon EFS |

**Block vs object:** block is like the hard disk (C: drive) attached to a computer. Object is like Google Drive or Dropbox.

---

## 9. Shared Security Responsibility Model

**Definition:** cloud security is shared between the cloud **vendor** and the **customer**. A perfect system can still be breached by a careless user, and a careful customer can still be affected by a weak vendor system. Each side must know its boundary.

| Party | Responsible for | Examples |
|---|---|---|
| **Vendor** (AWS, Azure) | Security **of** the cloud | Data-centre physical security, servers, network devices, virtualization |
| **Business** (customer organisation) | Security **in** the cloud | Data encryption, access permissions, security configuration, OS patching (in IaaS) |
| **User** (employee) | Their own accounts and behaviour | Strong passwords, MFA, avoiding phishing, following policy |

**Responsibility shifts by service model:** moving from IaaS to PaaS to SaaS, the vendor takes on more and the business takes on less. **The user's responsibility never goes away.**

*Analogy: vendor = building management, business = tenant locking the door, user = family and guests protecting the keys.*

---

## Quick Reference: Common Pitfalls

- **Relational** (not "relationship") database. **NoSQL** is one word.
- **Scale out** (horizontal) = add servers. **Scale up** (vertical) = upgrade one server.
- Spot Instances exist for **EC2 but not RDS**.
- OVF is a **file format**, not a program.
- Keep terms consistent: **vendor / business / user**.
