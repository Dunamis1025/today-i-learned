# Networking Fundamentals — Study Notes

> Based on Cisco Networking Academy (CCNA Introduction) practice questions.

---

## 1. The Internet

**Definition:** A massive global system formed by interconnecting countless smaller networks worldwide, enabling devices everywhere to communicate and share information.

**Key distinction:**
| Network Type | Who Can Access | Analogy |
|---|---|---|
| **Internet** | Everyone, globally | Public town square |
| **Intranet** | Internal employees only | Private living room |
| **Extranet** | Authorized external partners (suppliers, customers) | Invited guest room |

- Home users access the **Internet** for online shopping.
- Companies use an **Extranet** to give secure access to suppliers, customers, and collaborators.

---

## 2. ISP & WISP

### ISP (Internet Service Provider)
An organization that enables individuals and businesses to connect to the Internet (e.g., KT, SK Broadband, LG U+, Comcast, AT&T).

### WISP (Wireless Internet Service Provider)
Provides internet access via **wireless signals** instead of physical cables.
- **Best use case:** Rural or remote areas where laying cable infrastructure is impractical (e.g., farms, mountains).

---

## 3. Network Devices

### Router
- Acts as the **traffic police / GPS** of a network.
- **Function:** Determines the best path for data packets to travel across internetworks to reach their destination.

### End Devices
Devices that users interact with directly (computers, smartphones, laptops).

**Two key roles:**
1. **Originate data** — they are the starting point for data flowing through the network.
2. **Interface between humans and the network** — keyboard, screen, and touch input connect people to the digital world.

---

## 4. Internet Connection Types

| Connection Type | Requires Physical Cable to Building? |
|---|---|
| DSL | ✅ Yes |
| Dedicated Leased Line | ✅ Yes |
| Dialup | ✅ Yes |
| **Cellular (LTE/5G)** | ❌ No — uses cell tower signals |
| **Satellite** | ❌ No — uses signals from space |

> **Exam tip:** Cellular and Satellite are the two options that do **not** require a physical cable run to the building.

---

## 5. Key Network Characteristics

### Scalability (확장성)
The ability of a network to **grow quickly** to support new users and applications **without degrading performance** for existing users.

**Two characteristics of a scalable network:**
- Uses **modular devices** that allow for expansion (like LEGO blocks — plug in more capacity as needed).
- **Grows in size without impacting existing users** — like a restaurant adding tables without disturbing current diners.

### Fault Tolerance (내결함성)
The ability of a network to **continue operating** even when a component (cable, device) fails.

- The network reroutes traffic through alternative paths automatically.
- Users experience only a **brief interruption**, not a total outage.
- *Example: A fiber cable is accidentally cut on campus → students experience only a very short service interruption.*

---

## 6. Modern Networking Trends

### BYOD (Bring Your Own Device)
Employees use their **personal devices** (laptops, smartphones) to access company network resources.

**Key impact:** Provides **flexibility** in *where* and *how* users access network resources — from the office, home, or on the go.

> BYOD does **not** eliminate the need for corporate security policies.

### VPN (Virtual Private Network)
Creates a **secure, encrypted tunnel** through the public internet.

- Allows employees to **remotely access the company network safely** from anywhere.
- Think of it as a private road built on top of a public highway — outsiders cannot see inside.
- **Best choice** when an employee needs the most secure remote access method.

---

## 7. Security Threat — Spyware

| Term | Definition |
|---|---|
| **Spyware** | Malicious software secretly installed on a device to **collect user data** (browsing habits, personal info) without the user's knowledge. |

- Combination of "spy" + "software."
- Key characteristic: operates **secretly** in the background.

---

## Quick Reference Summary

| Concept | One-Line Definition |
|---|---|
| Internet | Global public network of interconnected networks |
| Intranet | Private internal company network |
| Extranet | Controlled network access for external partners |
| ISP | Company that provides internet access |
| WISP | Wireless ISP for areas without cable infrastructure |
| Router | Device that determines the best path for data |
| End Device | User-facing device that originates and receives data |
| Scalability | Ability to grow without degrading existing performance |
| Fault Tolerance | Ability to keep running despite component failures |
| BYOD | Policy allowing personal devices for work use |
| VPN | Encrypted tunnel for secure remote network access |
| Spyware | Malware that secretly collects user data |
| Cellular/Satellite | Internet connections requiring no physical cable to building |
