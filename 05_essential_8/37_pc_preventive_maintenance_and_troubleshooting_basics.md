# PC Preventive Maintenance & Troubleshooting — Study Notes

## 1. Preventive Maintenance Overview

Preventive maintenance means checking and caring for a computer **before** problems happen — similar to changing a car's oil before the engine fails.

**Why it matters:**
- Reduces hardware/software issues, equipment failures, and downtime
- Lowers repair costs and extends hardware lifespan
- Improves data protection and system stability

**How maintenance plans are decided** (based on environment and usage):
- **Location:** Computers in dusty environments (e.g., construction sites) need more frequent cleaning
- **Usage:** High-traffic systems (e.g., school networks) need more frequent malware scans and cleanup of unwanted files

---

## 2. Managing Dust

Dust blocks airflow → causes overheating → leads to component failure.

**Cleaning methods:**
- **External:** Wipe the case regularly with a clean cloth; apply cleaner to the cloth, not directly onto the device
- **Internal:** Use compressed air, an anti-static vacuum, and a lint-free cloth

**Compressed air safety:**
- Keep the can **upright** (tilting can release liquid that damages parts)
- Keep a safe distance from sensitive components

**Critical fan-cleaning rule:** When blowing air on a fan, **hold the blades still by hand**. Letting the fan spin freely from the air can damage the motor or generate excess voltage.

---

## 3. Internal Component Inspection Checklist

| Component | What to Check |
|---|---|
| **CPU Fan & Heat Sink** | Fan spins freely, power cable secure, fan turns when powered on |
| **RAM** | Modules seated properly, retaining clips locked |
| **Storage (HDD/SSD)** | Cables firmly connected, no loose jumpers, no unusual rattling/grinding sounds |
| **Screws & Cards** | Remove loose screws (risk of short circuit); ensure cards (e.g., GPU) are secured; slot covers in place |
| **Cables** | No bent/broken pins, not pinched or overly bent |
| **Power Devices** | Power strips, surge protectors, UPS working properly with clear ventilation |
| **Keyboard/Mouse** | Clean with compressed air, including the mouse sensor |

---

## 4. Environmental Considerations

For optimal performance, keep the computer in a clean environment with proper airflow.

- **Airflow:** Don't block the vents — leave clearance around the case
- **Temperature:** 7°C – 32°C (45°F – 90°F)
- **Humidity:** 10% – 80%

Note: Recommendations vary by manufacturer — check the product manual for special environments.

---

## 5. Software Preventive Maintenance

| Task | Purpose |
|---|---|
| **Updates** | Keep OS, programs, and drivers current for security, compatibility, and performance |
| **Security Scans** | Update antivirus/antimalware definitions and run scans regularly |
| **Cleanup** | Uninstall unused programs to free space and resources |
| **Disk Optimization** | Scan for errors and defragment to maintain speed |

---

## 6. Required Tools for PC Preventive Maintenance (4 Tools)

✅ **Correct answers:**
1. **Screwdriver** — to open the case and secure/remove internal parts
2. **Lint-free cloth** — wipes dust without leaving fibers or scratches
3. **Anti-static wrist strap** — prevents static discharge from damaging sensitive components
4. **Compressed air can** — blows dust out of hard-to-reach areas

❌ **Why others are wrong:**
- **Hammer:** Too rough for precision electronics
- **Cotton swabs:** Leave lint that can interfere with connections
- **Industrial vacuum cleaner:** Too powerful suction + generates static, risky for PC parts

---

## 7. Introduction to Troubleshooting

Troubleshooting is a **systematic, logical process** — not random guessing.

**Key principles:**
- **Systematic approach:** Isolate variables, test components in logical order
- **Data protection comes first:** Some repairs (OS reinstall, drive replacement) risk data loss. If data is lost due to negligence, the technician/company may be **held liable**

**Before starting any repair, verify backups:**
- When was the last backup?
- What data does it include?
- Is the backup file valid/not corrupted?

**If there's no backup and one can't be made:**
- Have the customer sign a **Liability Release Form** before starting work
- This form confirms the customer understands the risks, grants permission to proceed, and protects the technician if data is lost

---

## 8. The 6-Step Troubleshooting Process

1. **Identify the problem** — ask the customer questions and observe symptoms
2. **Establish a theory of probable cause** — make an educated guess (e.g., "Is the cable loose?")
3. **Test the theory** — verify the guess (e.g., swap the power cable); if wrong, go back to step 2
4. **Establish a plan of action and implement the solution** — once confirmed, fix it
5. **Verify full system functionality and implement preventive measures** — confirm the fix works and prevent recurrence
6. **Document findings, actions, and outcomes** — record the problem and solution for future reference

---

## 9. Step 1 in Detail: Identify the Problem

### Customer Communication Etiquette
- Avoid technical jargon
- Be professional — never blame or talk down to the customer
- Ask clear, direct questions

### Information to Gather
- **Customer details:** name, contact info, address
- **Device specs:** manufacturer, model, OS, network environment
- **Problem description:**
  - *Open-ended questions* — "What happened when it failed?" (get the big picture)
  - *Closed-ended questions* — "Does it power on?" (narrow down the cause)
- **Hardware indicators:** error messages, beep sequences, LED patterns

### Key Technical Concepts
- **Beep Codes:** Patterns of beeps during POST signal specific hardware failures — record the pattern and check the manufacturer's manual
- **POST (Power-On Self-Test):** The system's self-check at startup. If it stops here, suspect hardware failure or a setup error
- **BIOS:** If the system halts right after power-on, check BIOS settings to confirm hardware is detected
- **Diagnostic Tools:** Manufacturer-provided diagnostic software is often the most reliable way to pinpoint issues

### Documentation
Record every detail gathered — small clues often become the key to solving complex issues, and notes help future repairs.
