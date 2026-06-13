# PC Troubleshooting & Preventive Maintenance — Study Notes

---

## 1. Troubleshooting: Identifying the Problem

The **first step** in troubleshooting is to gather as much information as possible from both the customer and the computer before attempting any fix.

### Customer Conversation Etiquette
- Ask **direct questions** to collect information efficiently.
- Avoid **industry jargon** — use plain language.
- Never **talk down to** or insult the customer.
- Never **accuse the customer** of causing the problem.

### Information to Gather

| Category | Details |
|---|---|
| **Customer Info** | Company name, contact name, address, phone number |
| **Computer Config** | Manufacturer, model, OS, network environment, connection type |
| **Problem Description** | Open-ended questions for details → closed-ended (yes/no) to confirm |
| **Technical Indicators** | Error messages, beep sequences, LED status, POST behavior |

### Question Types

**Open-Ended Questions** — Let the customer explain freely (what/how):
- "What problems are you experiencing with your computer or network?"
- "What were you doing when the problem was identified?"
- "What software has recently been installed on the computer?"
- "What hardware changes have recently been made to the computer?"

**Closed-Ended Questions** — Require a yes/no answer to confirm specifics:
- "Can you reproduce the problem?"
- "Are you currently logged into the network?"
- "Have you recently changed your password?"
- "Has anyone else used your computer recently?"
- "Have you received any error messages on your computer?"

### Documentation & Diagnostics
- **Document everything** in a work order, repair log, or journal — small details often lead to solutions.
- **Beep codes** during POST indicate specific hardware failures — record and research them.
- **BIOS settings** — If the system stops after POST, check settings against motherboard documentation.
- **Diagnostic tools** — Use software or manufacturer-provided tools to diagnose hardware issues.

---

## 2. Key Troubleshooting Tools (Windows)

| Tool | Purpose |
|---|---|
| **Event Viewer** | Logs system/software errors — tracks what happened, when, severity, source, Event ID, and logged-in user |
| **Device Manager** | Shows all configured devices; flags issues with icons (⚠️ yellow triangle = problem, ❌ red X = disabled/missing, ↓ arrow = disabled) |
| **Task Manager** | Displays running apps and background processes; lets you close unresponsive programs and monitor CPU, memory, disk, and network usage |

---

## 3. Cable-Related Issues Inside a PC

Two common cable problems inside a PC:

- **Crimping** — Cables that are squeezed, bent, or deformed, disrupting signal transmission.
- **Bent pins** — Metallic pins inside a connector become crooked, preventing proper connection with a port or device.

---

## 4. Preventive Maintenance: Benefits

Regular preventive maintenance on desktop PCs provides three key benefits:

1. **Longer equipment life** — Cleaning dust and performing checkups prevents overheating and extends component lifespan.
2. **Fewer security breaches** — Regular updates and system checks reduce vulnerability to cyberattacks.
3. **Less computer downtime** — Issues are identified and resolved before causing critical failures.

---

## 5. Environment-Specific Maintenance Concerns

**Scenario:** A mining employee uses a laptop underground in a mine.

The three biggest maintenance concerns in this environment are:

| Factor | Why It Matters |
|---|---|
| **Dust** | Mine environments are heavily dusty; dust entering the laptop can cause overheating and hardware failure |
| **Humidity** | High underground humidity can corrode internal components and cause electrical issues |
| **Dirty keyboard** | Frequent use in a dirty environment causes rapid contamination of the keyboard |

---

## 6. ESD (Electrostatic Discharge) Safety

**Scenario:** A technician forgot their anti-static mat and considered working in socks instead, since there was no carpet.

**Answer: FALSE — This is NOT acceptable.**

- Working in socks **increases** static electricity generation due to friction.
- Static discharge can **permanently damage** computer components.
- Always use proper ESD protection (**anti-static mat** or **wrist strap**), regardless of time constraints.

---

*Topic: CompTIA A+ / IT Support Fundamentals — Troubleshooting & Preventive Maintenance*
