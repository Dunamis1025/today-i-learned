# Virtualization & Cloud Computing — Study Notes
> Cert IV in Cyber Security | CCNA Prep | Module 9 Summary

---

## 1. Virtualization

### What Is It?
Virtualization is a technology that allows **a single physical computer to run multiple independent virtual machines (VMs)** that share the same underlying hardware. It is the **foundation of cloud computing**.

### Key Terminology

| Term | Definition |
|------|-----------|
| **Host Computer** | The physical machine the user controls |
| **Host OS** | The operating system installed on the host computer |
| **Guest OS** | The OS running inside a virtual machine |
| **Virtual Machine (VM)** | A software-based computer that exists within a physical computer |
| **Hypervisor (VMM)** | Software that creates, manages, and allocates resources to VMs |

### Why Virtualization Replaced Traditional Servers

Traditional model = **one server per application** — highly inefficient:
- **Wasted resources** — servers sit idle most of the time
- **Single point of failure** — one server down = service down
- **Server sprawl** — more services = more physical machines = more cost + space

Virtualization fixes this by consolidating multiple workloads onto fewer physical machines.

### Benefits of Server Virtualization

| Benefit | Description |
|---------|-------------|
| Better use of resources | Hardware is fully utilized instead of sitting idle |
| Less physical space | Fewer physical servers needed |
| Reduced costs | Lower energy, maintenance, and infrastructure costs |
| Faster provisioning | New VMs can be deployed in minutes, not weeks |
| Improved disaster recovery | VMs can be copied/moved between hardware platforms easily |
| Support for legacy software | Old OS/apps can run inside a VM on modern hardware |
| Less energy consumed | Fewer machines = lower power and cooling bills |

---

## 2. Hypervisors

### Type 1 — Bare Metal
- Installed **directly on the hardware**, no host OS required
- Used in **data centers and enterprise server environments**
- More efficient, better performance, more secure
- Examples: **VMware vSphere, Oracle VM Server, Microsoft Hyper-V (Server)**

### Type 2 — Hosted
- Installed **on top of an existing OS** (like Windows or macOS)
- Used for **personal/client-side virtualization**, testing, labs
- Easier to set up, but slightly less efficient
- Examples: **VMware Workstation, VirtualBox, Microsoft Virtual PC**

> **Your setup:** VMware on Windows running Linux + Windows 11 + Windows Server = **Type 2 hypervisor**
>
> **Web-based hacking labs (e.g., Security Impossible):** You're accessing a VM hosted on a remote server that uses a **Type 1 hypervisor** — that's cloud computing in action.

### System Requirements for Running VMs
- **CPU** — must support virtualization (Intel VT-x or AMD-V), more cores = better
- **RAM** — host OS needs its own memory + each VM needs its own allocation
- **Storage** — each VM requires significant disk space (SSD recommended)
- **Network** — VMs share the host's physical NIC via virtual network adapters

> ⚠️ VMs are still vulnerable to malware. Always install antivirus, apply updates, and enable firewalls inside each VM.

---

## 3. Cloud Computing

### What Is It?
Cloud computing delivers **computing services — software, platforms, and infrastructure — over the internet on demand**. It is built on top of virtualization technology.

> Without virtualization, modern cloud computing would not be possible.

### 5 Essential Characteristics (NIST Definition)

| Characteristic | Meaning |
|----------------|---------|
| **On-demand self-service** | Users can provision resources instantly without human intervention from the provider |
| **Broad network access** | Available over the internet via heterogeneous devices (phones, tablets, laptops) |
| **Resource pooling** | Provider pools resources and dynamically assigns them to multiple users (multi-tenant) |
| **Rapid elasticity** | Resources can scale up or down automatically based on demand |
| **Measured & metered service** | Usage is tracked and billed accurately — pay only for what you use (transparency for both sides) |

---

## 4. Cloud Service Models

### SaaS — Software as a Service
- **What you get:** A finished, ready-to-use application
- **Who manages everything:** The provider
- **You just:** Use it via a browser or app
- **Examples:** Gmail, Office 365, Google Docs, YouTube Premium, Netflix, Claude, Gemini, Notion, GitHub (core features)
- **Analogy:** Staying in a hotel — everything is provided

### PaaS — Platform as a Service
- **What you get:** A development environment (OS, tools, runtime)
- **Who manages infrastructure:** The provider
- **You manage:** Your application code and data
- **Examples:** Google App Engine, Heroku, AWS Elastic Beanstalk
- **Analogy:** Renting a furnished house — you do the interior design

### IaaS — Infrastructure as a Service
- **What you get:** Raw virtual hardware — servers, storage, networking
- **You manage:** Everything from the OS upward
- **Examples:** AWS EC2, Microsoft Azure VMs, Google Compute Engine, DigitalOcean
- **Analogy:** Renting an empty plot of land — you build your own house

### ITaaS — IT as a Service
- An extension of IaaS where the provider delivers **comprehensive IT operations** — training, licensing, provisioning, support
- Useful for small businesses that want to fully outsource their IT department

### Quick Comparison

| Model | User Manages | Provider Manages | Best For |
|-------|-------------|-----------------|----------|
| SaaS | Nothing | Everything | End users |
| PaaS | App + Data | Infrastructure + OS + Runtime | Developers |
| IaaS | OS + Apps + Data | Physical hardware + Virtualization | IT admins / architects |
| ITaaS | Nothing | All IT operations | Small businesses |

---

## 5. Cloud Deployment Models

| Model | Who Can Access | Example |
|-------|---------------|---------|
| **Public Cloud** | Anyone over the internet | Gmail, YouTube |
| **Private Cloud** | One specific organization only | Internal company intranet, internal budget system |
| **Community Cloud** | Group of organizations with shared goals | Government agencies sharing a bidding platform |
| **Hybrid Cloud** | Combination of two or more models | Gov website: public info (public) + internal data (private) |

---

## 6. Software Defined Networking (SDN)

### What Is It?
SDN is a modern networking approach that **uses software to control network infrastructure**, replacing rigid, hardware-dependent traditional models.

### SDN Architecture — 3 Layers

```
┌─────────────────────────────────┐
│        Application Layer        │  ← Business logic, traffic policies
├─────────────────────────────────┤
│   Northbound API (upward link)  │
├─────────────────────────────────┤
│         Control Layer           │  ← SDN Controller (the "brain")
├─────────────────────────────────┤
│  Southbound API (downward link) │
├─────────────────────────────────┤
│       Infrastructure Layer      │  ← Physical/virtual switches, routers, firewalls
└─────────────────────────────────┘
```

| Layer | Role |
|-------|------|
| **Application Layer** | Defines how traffic is prioritized and handled |
| **Control Layer** | Houses the SDN Controller — sends instructions to hardware below |
| **Infrastructure Layer** | Physical and virtual devices that actually move the data |
| **Northbound API** | Connects SDN Controller ↔ Application Layer |
| **Southbound API** | Connects SDN Controller ↔ Infrastructure Layer |

### SD-WAN Benefits
- Simplifies complex network architectures
- Enables automation of network management tasks
- Integrates advanced security (encryption, firewalls)
- Reduces costs by centralizing control instead of managing scattered physical devices

---

## 7. Cloud vs. Data Center

| | Data Center | Cloud Computing |
|-|-------------|----------------|
| **What it is** | A physical facility housing servers and hardware | A service model for accessing shared computing resources over the internet |
| **Analogy** | A physical library building | A digital book lending service accessible anywhere |

---

## 8. Practical Lab — Installing Linux in a VM (VirtualBox)

### Steps Overview
1. Download and install **Oracle VirtualBox**
2. Download **Ubuntu Desktop** ISO image
3. Create a new VM in VirtualBox (allocate RAM, CPU, storage)
4. Boot the VM and install Ubuntu
5. Install **Guest Additions** for better screen resolution and usability
6. Explore the GUI — open a browser, terminal emulator, and installed apps

### Minimum Requirements
- RAM: 2 GB minimum (4 GB recommended)
- Free disk space: 10 GB minimum per VM

### Linux vs. Ubuntu
- **Linux** = a family of operating systems (like "Windows" as a category)
- **Ubuntu** = a specific distribution (distro) within the Linux family
- Other distros: Fedora, Debian, Kali Linux (used in cybersecurity)

---

## 9. Key Exam Questions — Quick Reference

| Question | Answer |
|----------|--------|
| What hypervisor type is VMware Workstation? | Type 2 |
| What hypervisor type is VMware vSphere? | Type 1 |
| What cloud model does Gmail represent? | Public Cloud |
| What cloud model is an internal budget system? | Private Cloud |
| What service model is Netflix/YouTube Premium? | SaaS |
| What service model is Heroku? | PaaS |
| What service model is AWS EC2? | IaaS |
| What technology underpins cloud computing? | Virtualization |
| What does "decoupling" mean in virtualization? | Separating the OS from the physical hardware |
| What cloud model combines two or more types? | Hybrid Cloud |
| What characteristic ensures pay-per-use billing? | Measured & Metered Service |
| What hypervisors suit enterprise server consolidation? | Oracle VM Server, VMware vSphere |
| What cloud service handles IT operations end-to-end? | ITaaS |

---

## 10. Real-World Examples You Already Know

| Service You Use | Cloud Category |
|----------------|---------------|
| Claude (Anthropic) | SaaS |
| Gemini (Google) | SaaS |
| YouTube Premium | SaaS |
| Netflix | SaaS |
| Notion | SaaS |
| GitHub (core) | SaaS |
| Google Drive / OneDrive | SaaS |
| VMware on your PC | Type 2 Hypervisor (client-side virtualization) |
| Hacking labs via browser | Cloud (Type 1 backend) + SaaS delivery |

---

*Last updated: June 2026 | Cert IV Cybersecurity — Module 9*
