# Cloud Computing & Virtualization — Study Notes

## 1. Cloud Service Models

| Model | What It Provides | Example Use Case |
|-------|-----------------|------------------|
| **IaaS** (Infrastructure as a Service) | Raw computing infrastructure — servers, storage | Renting virtual servers |
| **PaaS** (Platform as a Service) | Development tools & environment on the cloud | Distributed dev teams sharing the same coding platform |
| **SaaS** (Software as a Service) | Ready-to-use software applications over the internet | Email, Office 365, LMS tools |
| **ITaaS** | IT services delivered as a business model | Managed IT support |

> **Q1 Key Point:** A global software company using a shared cloud-based dev environment → **PaaS**, because it provides the platform/tools without requiring local setup.

---

## 2. Cloud Deployment Models

| Model | Who Uses It |
|-------|------------|
| **Public Cloud** | Anyone; shared over the internet |
| **Private Cloud** | One specific organization; fully isolated |
| **Community Cloud** | Multiple organizations sharing common goals (e.g., a professional association) |
| **Hybrid Cloud** | Mix of private + public |

> **Q11:** An international engineering association sharing research → **Community Cloud**
> **Q16:** Services dedicated to a specific organization → **Private Cloud**

---

## 3. Cloud Computing — Key Characteristics

- Access applications **anywhere, anytime, on any device** via the internet
- **No need to own or manage hardware** — the provider handles it
- Connect through an **ISP** (Internet Service Provider)
- **Pay-as-you-go** — only pay for what you use
- **Elastic scaling** — instantly increase or decrease capacity as needed

> **Q19:** Core trait of cloud computing → device/location-independent access
> **Q17 (small company):** Three advantages of moving to the cloud:
> 1. No concern about handling growing storage/processing demands in-house
> 2. Only pay for what you use
> 3. Scale capacity up or down as needed

---

## 4. Cloud vs. Virtualization — Key Difference

| | Virtualization | Cloud Computing |
|---|---|---|
| **What it separates** | OS from underlying hardware | Application from hardware |
| **Core concept** | Run multiple virtual OSes on one physical machine | Deliver IT services over the internet on demand |
| **Relationship** | Foundational technology | Built on top of virtualization |

> **Q10:** Virtualization separates the OS from hardware; cloud computing separates the application from hardware.
> **Q13:** Cloud computing and virtualization are **NOT** the same thing — **False**.

---

## 5. Virtualization — Advantages

- Run **multiple operating systems simultaneously** on one PC
- **Cost savings** — fewer physical machines needed
- Reduces hardware, power, and maintenance expenses

> **Q2:** Two advantages of PC virtualization → multiple OSes + cost savings

### Business Challenges Solved by Virtualization (in Data Centers)
- **Power & air conditioning** — fewer physical servers = less electricity and cooling needed
- **Physical footprint** — less floor space required in the data center

> **Q6:** Two challenges overcome → power/cooling costs + physical space

---

## 6. Hypervisors

A **hypervisor** is software that creates and manages virtual machines (VMs) on a host computer.

### Type 1 — Bare-Metal Hypervisor
- Installed **directly on hardware** (no host OS needed)
- Very fast, stable, and efficient
- Used in **enterprise data centers**

### Type 2 — Hosted Hypervisor
- Installed **on top of an existing OS** (e.g., Windows, macOS)
- Easier to set up, less efficient
- Used for **personal/testing environments**

> **Q8:** Type 1 characteristic → installed directly on a server
> **Q15:** Mac user installs Windows VM → **Type 2** hypervisor
> **Q20:** Most common hypervisor type in data centers → **Type 1**
> **Q7:** Type 2 does NOT have direct hardware access, is NOT ideal for enterprise, and DOES require management software

---

## 7. Hypervisor — Main Function

> **Q12:** A hypervisor **creates and manages multiple VM instances** on a host machine.

---

## 8. Virtualization — Use Cases

### Security Research (Q18)
Studying viruses and worms in a **virtualized sandbox**:
- Completely isolated from the host machine and real network
- If something goes wrong, simply reset or delete the VM
- No risk of infecting actual systems

### Running Unsupported Applications (Q21)
If an app doesn't run on your current OS:
- Create a **Virtual Machine** with a compatible OS inside your existing computer
- Runs the app in an isolated "guest" environment without changing your main system

### Remote Learning (Q23)
Providing a uniform hands-on Windows environment to remote learners:
- **Virtual Desktop Infrastructure (VDI)** — each learner gets the same full Windows environment hosted on a server, accessed remotely

### Learning Management System / Hosted App (Q4)
A small college wants a hosted LMS without building infrastructure:
- **SaaS solution (e.g., Office 365)** — software is managed by the provider, accessed over the internet

---

## 9. Disaster Recovery with Virtualization (Q5)

**Live Migration** — the ability to move a running VM from one physical server to another instantly, without service interruption.

- Protects against hardware failure
- Minimizes downtime during data center issues

---

## 10. Software-Defined Networking (SDN) (Q14)

- Centrally controls the entire network through **software** instead of configuring each device manually
- Automatically and rapidly **reconfigures network topology** as conditions change
- Makes networks **flexible and highly responsive**

---

## 11. Cloud Computing — Technology That Enables Anywhere Access (Q9)

> **Answer: Cloud Computing**
> Stores data on remote internet servers so users can access it from any device, anywhere, anytime.

---

## 12. Hardware Troubleshooting (Q22)

**Loud clicking noise from a computer → Check the Hard Drive (HDD) first**

- Inside an HDD, a read/write arm physically moves across magnetic platters
- Repetitive clicking = the arm is failing → known as the **"Click of Death"**
- This is a critical warning: **back up data immediately**

---

## Quick Reference Summary

| Topic | Key Answer |
|-------|-----------|
| Global dev team sharing tools | PaaS |
| Specific org cloud | Private Cloud |
| Shared-goal group cloud | Community Cloud |
| Anywhere access technology | Cloud Computing |
| Cloud vs. Virtualization | Different concepts |
| Hypervisor in data centers | Type 1 (Bare-Metal) |
| Mac + Windows VM | Type 2 Hypervisor |
| Hypervisor's job | Create & manage VMs |
| Virus lab safety | Virtualized sandbox |
| Disaster recovery method | Live Migration |
| Flexible network tech | SDN |
| Uniform remote learning env | VDI |
| Hosted LMS solution | SaaS (Office 365) |
| Clicking computer noise | Hard Drive failure |
| Cloud advantages (small biz) | No hardware worry, pay-as-you-go, elastic scaling |
| Virtualization advantages | Multiple OSes, cost savings |
| Data center challenges solved | Power/cooling, physical space |
