# IT Essentials Study Notes — Questions 16–22

A summary of key hardware and IT fundamentals concepts covered today, including HDMI standards, BIOS, redundant power supplies, electrical units, and RAID configurations.

---

## Question 16 — HDMI 1.4 Type A Capabilities

**Question:** Which statement describes the capability of an HDMI version 1.4 type A port?

**Options:**
- It uses a 20-pin connector for delivering high-bandwidth video and audio signals.
- It can change a monitor's refresh rate to match the source device output rate.
- It supports high premium speeds of up to 48 Gbps.
- It can be used for 4K and 8K resolutions.

**"Official" Answer (per exam answer key):** *It can change a monitor's refresh rate to match the source device output rate.*

**Note / Caveat:** Strictly speaking, none of the four options are technically accurate for real-world HDMI 1.4 specs:
- HDMI Type A actually uses a **19-pin** connector, not 20-pin.
- 48 Gbps bandwidth is an **HDMI 2.1** feature (HDMI 1.4 maxes out around 10.2 Gbps).
- Variable Refresh Rate (VRR) — matching a monitor's refresh rate to the source — is also an **HDMI 2.1** feature.
- HDMI 1.4 supports **4K (typically at 30Hz)** but **does not support 8K**.

So while the exam's official key marks the "refresh rate" option as correct, this is technically a flawed/inaccurate question relative to actual HDMI specifications. For test-taking purposes, go with the "refresh rate" answer; for real understanding, recognize all four statements have factual errors.

---

## Question 17 — When to Enter BIOS Setup

**Question:** A technician has assembled a new computer and must now configure the BIOS. At which point must a key be pressed to start the BIOS setup program?

**Correct Answer:** **During the POST** (Power-On Self-Test)

**Key Points:**
- BIOS is the first software that runs when a computer powers on, before the operating system (e.g., Windows) loads.
- During POST, the manufacturer's logo screen briefly displays a prompt like "Press F2 or Del to enter Setup."
- This is the only window of opportunity to enter BIOS setup.
- **Why other options are wrong:**
  - If Windows has already started loading → too late.
  - While the computer is powered off → no input is registered.
  - After POST completes → the system has already moved on to loading the OS, missing the window.

---

## Question 18 — Advantage of a Redundant Power Supply

**Question:** What is the advantage of having a redundant power supply?

**Correct Answer:** **It allows for the replacement of the faulty power supply without loss of power to the server.**

**Key Points:**
- A redundant power supply setup means installing **two or more PSUs** in a system, commonly in servers.
- If one PSU fails, the other immediately takes over, so the system keeps running without interruption.
- This enables **hot-swapping** — replacing the failed unit while the server stays powered on and operational.
- **Core purpose:** reliability and uptime, NOT increasing total wattage, powering graphics cards, or serving as spare parts storage.

---

## Question 19 — Electrical Unit for Electron Flow

**Question:** What electrical unit refers to the number of electrons moving through a circuit per second?

**Correct Answer:** **Current**

**Key Points:**
- **Current** = the rate of electron flow through a circuit, measured in **Amperes (A)**.
- Analogy: like the volume of water flowing through a pipe — more electrons passing a point per second = higher current.
- **Comparison with related terms:**
  - **Power** — total electrical work done, measured in Watts (W)
  - **Voltage** — the "pressure" pushing electrons through the circuit, measured in Volts (V)
  - **Resistance** — opposition to current flow, measured in Ohms (Ω)

---

## Question 20 — Minimum Drives for RAID 10

**Question:** A data analyst asked a technician to protect locally stored data with RAID. What is the minimum number of drives required for RAID 10?

**Correct Answer:** **4**

**Key Points:**
- RAID 10 is a **nested RAID level** combining:
  - **RAID 0** (striping) → speed
  - **RAID 1** (mirroring) → redundancy/safety
- Structure: data is mirrored in pairs (2 drives = 1 mirrored pair), and at least **2 mirrored pairs** are striped together.
- Minimum: 2 pairs × 2 drives = **4 drives total**
- Result: high performance + high fault tolerance, but at the cost of needing more drives.

---

## Question 21 — RAID for 3 Drives with Single-Drive Failure Protection

**Question:** A technician needs to configure RAID using 3 drives, with protection if one drive fails. Which RAID level should be used?

**Correct Answer:** **RAID 5**

**Key Points:**
- RAID 5 requires a **minimum of 3 drives**.
- Data and **parity information** (used for recovery) are striped/distributed across all drives.
- If one drive fails, the data on the failed drive can be **reconstructed** using the parity data on the remaining drives.
- **Why not RAID 2/3/4:** These are older or specialized configurations rarely used today. RAID 5 is the modern standard for balancing performance and fault tolerance with 3 drives.

---

## Question 22 — Key Consideration for a Gaming Web Server

**Question:** A technician is selecting a web server to host multiple gaming applications. What is a major consideration?

**Correct Answer:** **Powerful processor**

**Key Points:**
- A server hosting multiple games must process **constant, rapid calculations** for many simultaneous users — the CPU is the "brain" handling this load.
- A weak processor would cause lag or crashes under heavy multi-game usage.
- **Why other options are wrong:**
  - **Multiple SCSI drives** — outdated storage tech, replaced by SSDs.
  - **Multiple touch screens** — irrelevant; servers are managed remotely/via command line.
  - **Optical drive (CD/DVD)** — only useful for initial installation, not for ongoing performance.

---

## Quick Reference Table

| # | Topic | Correct Answer |
|---|-------|-----------------|
| 16 | HDMI 1.4 Type A capability | "Can change refresh rate to match source" (exam key — technically debated) |
| 17 | When to enter BIOS setup | During POST |
| 18 | Redundant power supply advantage | Replace faulty PSU without losing server power |
| 19 | Unit for electron flow per second | Current (Amps) |
| 20 | Min drives for RAID 10 | 4 |
| 21 | RAID for 3 drives, 1-drive fault tolerance | RAID 5 |
| 22 | Key consideration for gaming web server | Powerful processor |
