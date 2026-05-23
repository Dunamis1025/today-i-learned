# Computer Hardware Study Notes

> Study session covering input/output devices, ESD prevention, power supplies, and hardware connectors.

---

## 1. Input vs. Output Devices

### Definitions

| Term | Definition |
|------|------------|
| **Output Device** | A device that receives processed data from a computer and presents it to the user (visual, audio, or physical form). |
| **Input Device** | A device used to send data or control signals into a computer. |

### Device Classification

| Device | Type | Reason |
|--------|------|--------|
| Headphones | ✅ Output | Converts audio signals from the computer into sound for the user. |
| Monitor | ✅ Output | Displays visual data (text, images) processed by the computer. |
| Printer | ✅ Output | Converts digital data into a physical hard copy on paper. |
| Fingerprint Scanner | ❌ Input | Captures biometric (biological) data and sends it to the computer. |
| Mouse | ❌ Input | Sends cursor movement and click data to the computer. |
| Keyboard | ❌ Input | Sends keystroke data to the computer. |

---

## 2. KVM Switch

### What It Is

A **KVM switch** stands for **Keyboard, Video (Monitor), Mouse**. It is a hardware device that allows a single set of input/output peripherals (one keyboard, one monitor, one mouse) to control **multiple computers or servers**.

### Use Case

- Commonly used by **network administrators** to manage multiple servers without needing separate peripherals for each machine.
- Saves physical space in server rooms and reduces equipment costs.

### Why Other Options Are Incorrect

| Option | Why It's Wrong |
|--------|---------------|
| Touch screen monitor | Acts as a combined I/O device but cannot switch control between multiple computers. |
| PS/2 hub | An older connector standard for keyboards/mice; no video signal or server-switching capability. |
| USB switch | Shares USB peripherals between computers but does **not** handle video (monitor) signals. |
| UPS (Uninterruptible Power Supply) | Provides battery backup power during outages; unrelated to peripheral management. |

---

## 3. Biometric Identification Device

### Definition

A **biometric identification device** identifies users based on unique physical or behavioral characteristics, such as:

- Voice patterns
- Fingerprints
- Facial recognition
- Iris scanning

### Key Point

> A device that identifies users **by their voice** is classified as a **biometric identification device**.

### Why Other Options Are Incorrect

| Option | Why It's Wrong |
|--------|---------------|
| KVM switch | Controls multiple computers; no user identification capability. |
| Scanner | Converts physical documents/images into digital files; not for biometric analysis. |
| Digitizer | A graphics tablet for hand-drawing input; unrelated to identity verification. |

---

## 4. ESD (Electrostatic Discharge) Prevention

### What Is ESD?

**ESD (Electrostatic Discharge)** is the sudden flow of static electricity between two objects. In a hardware context, static built up on a person's body can discharge into sensitive electronic components, causing **permanent, invisible damage** to circuits.

### How to Prevent ESD

#### ✅ Correct Method: Work on a Grounded Antistatic Mat

- Antistatic mats have a **conductive surface** that provides a safe path for static electricity to be **drained to the ground**.
- Prevents charge from accumulating and discharging into components.
- Often used in combination with an **antistatic wrist strap**.

#### ❌ Incorrect Methods (and Why)

| Method | Why It Does NOT Prevent ESD |
|--------|----------------------------|
| Moving cordless phones away | Phones cause RF interference, not ESD. |
| Keeping computer plugged into a surge protector | Surge protectors guard against power-line voltage spikes, not human static discharge. (Best practice: **unplug** before opening.) |
| Lowering humidity in the work area | Lower humidity = **more** static buildup. Higher humidity actually helps dissipate static charges. |

---

## 5. How Internal Components Are Protected from ESD Inside a Computer

### Correct Answer: Grounding via Attachment to the Case

- The **metal chassis (case)** of a computer acts as a **common ground**.
- When components (motherboard, drives, PSU) are **screwed into the metal case**, any stray static charges are safely channeled through the mounting points into the chassis and dissipated.
- This is a built-in, passive ESD protection mechanism in all properly assembled desktops.

### Why Other Options Are Incorrect

| Option | Why It's Wrong |
|--------|---------------|
| Unplugging after use | A safety habit for users, not an inherent ESD protection mechanism for components. |
| Using plastic or aluminum cases | Plastic is an **insulator** (no ground path). Aluminum can conduct, but just using a certain material doesn't protect components — the **physical grounding connection** is what matters. |
| Using multiple fans | Fans provide **thermal cooling**, not ESD protection. |

---

## 6. Power Supply Form Factors

### Key Form Factors

| Form Factor | Used In | Notes |
|-------------|---------|-------|
| **ATX12V** | Modern desktop / gaming PCs | Current industry standard; delivers stable 12V power directly to the CPU and high-draw components. |
| EPS12V | Servers / Workstations | Higher-end specification for professional systems requiring extreme stability. |
| ATX | General motherboard/case sizing | Term describes form factor broadly; ATX12V is the specific PSU standard. |
| AT | Obsolete (pre-mid-1990s) | Completely outdated; incompatible with modern hardware. |

### Key Takeaway

> When replacing a power supply in a **high-end gaming PC**, look for the **ATX12V** form factor — it is the universal standard for modern desktop power supplies.

---

## 7. PCIe Power Connector (6/8-pin)

### What It Is

The **6/8-pin PCIe power connector** is a cable that runs directly from the power supply to high-power internal components.

### Primary Use

- Supplies **additional power to graphics cards (GPUs)**.
- The PCIe slot on the motherboard alone cannot provide enough wattage for high-end GPUs, so this connector bridges the gap directly from the PSU.

### Why Other Options Are Incorrect

| Option | Why It's Wrong |
|--------|---------------|
| Connecting disk/optical drives | Those use **SATA power connectors** (flat, wider shape). |
| Connecting legacy floppy drives | Floppy drives used small **4-pin Berg (mini-Molex) connectors**. |

---

## Summary Table

| Topic | Key Concept |
|-------|-------------|
| Output Devices | Headphones, Monitor, Printer |
| Input Devices | Keyboard, Mouse, Fingerprint Scanner |
| KVM Switch | One set of peripherals → controls multiple computers/servers |
| Biometric Device | Identifies users via biological traits (voice, fingerprint, face) |
| ESD Prevention | Use grounded antistatic mat; higher humidity helps |
| Internal ESD Protection | Components grounded via metal chassis attachment |
| PSU Form Factor (Gaming PC) | ATX12V |
| 6/8-pin PCIe Connector | Delivers extra power to GPUs |
