# Chapter 7 Study Notes – Laptops, Mobile Devices & Email Protocols

---

## 1. Email Protocols

### SMTP (Simple Mail Transfer Protocol)
- Used to **send** email — from client to server, and between servers
- Text-based; uses **ASCII encoding only**
- Requires **MIME** to handle attachments
- Port: **TCP 25**

### POP3 (Post Office Protocol v3)
- Used to **download** email from server to local device
- Typically **deletes** the original from the server after download
- Best for single-device access
- Port: **TCP 110**

### IMAP (Internet Message Access Protocol)
- **Synchronizes** email folders between server and client
- Email stays on the server — accessible from multiple devices
- Faster than POP3 but requires more disk space and CPU
- Common in large networks (e.g., universities)
- Latest version: **IMAP4** | Port: **TCP 143**

### MIME (Multipurpose Internet Mail Extensions)
- Extends SMTP to support **non-text content**: images, documents, etc.
- Works in conjunction with SMTP

### SSL (Secure Sockets Layer)
- **Encrypts** email data in transit
- Supported by most email clients and servers

### Microsoft Exchange & MAPI
- Enterprise email server with integrated calendar and contact management
- Uses **MAPI (Messaging Application Programming Interface)** for rich client-server communication

---

## 2. Email Account Setup Requirements
| Field | Description |
|---|---|
| Email Address | Unique address (e.g., user@example.net) |
| Display Name | Name shown to recipients |
| Email Protocol | POP3 or IMAP for incoming mail |
| Incoming/Outgoing Server | Provided by ISP or network admin |
| Account Credentials | Username + strong password |

---

## 3. Bluetooth Pairing

### Process (Android & iOS)
1. Put device into **discoverable mode**
2. Find the connection **PIN** in device docs
3. Go to **Settings → Bluetooth** and turn it on
4. Select the discovered device
5. Enter the PIN

> Pairing stores authentication info so you only need to do this once per device pair.

---

## 4. Data Synchronization

### Android
- Syncs via **Google account** (contacts, calendar, email) over the internet
- Go to: Settings → Accounts & backup → Manage accounts → Sync account
- Supports **auto-sync** (can be disabled to save battery)

### iOS
- **Backup**: Copies all data (messages, app settings, photos) to a computer or iCloud
- **Sync**: Keeps content (music, apps, videos) consistent between device and iTunes
- **Wi-Fi Sync**: After initial USB setup, can sync wirelessly on same network

### Cloud Sync
- Services like **Microsoft OneDrive** enable platform-independent sync across devices

---

## 5. Preventive Maintenance

### Why It Matters
Mobile devices are exposed to: dust, liquid spills, drops, extreme temperatures, and moisture — all of which can cause serious internal damage.

### Laptop Cleaning Guide
| Component | Method |
|---|---|
| Exterior Case | Soft lint-free cloth + mild solution |
| Cooling Vents / Fan | Compressed air or anti-static vacuum; tweezers for debris |
| Display | Lint-free cloth + screen-specific cleaner |
| Keyboard | Slightly damp lint-free cloth |
| Touchpad | Approved cleaner on cloth — never wet cloth directly |

**Before cleaning:** Power off, unplug, remove battery if possible.  
**Never use:** Ammonia-based or alcohol-based cleaners.

### Mobile Device Maintenance (3 Key Tasks)
1. **Cleaning** — Use soft microfiber cloth + touchscreen-safe cleaner; never ammonia/alcohol
2. **Data Backup** — Regularly back up contacts, photos, apps, settings to cloud
3. **Software Updates** — Update OS and apps promptly for new features, performance, and security fixes

---

## 6. Troubleshooting Process (6 Steps)

| Step | Action |
|---|---|
| 1 | **Identify the problem** – Gather symptoms from the user |
| 2 | **Establish a theory of probable cause** – Form an educated guess |
| 3 | **Test the theory** – Confirm or rule out the cause |
| 4 | **Plan & implement the solution** – Fix the issue |
| 5 | **Verify functionality & prevent recurrence** – Test everything works |
| 6 | **Document findings** – Record the problem, steps taken, parts used, time spent |

### Question Types for Step 1
- **Open-ended**: "What problems are you experiencing?" → Gets detailed descriptions
- **Closed-ended**: "Is the device still under warranty?" → Gets yes/no facts

---

## 7. Common Problems & Solutions

### Laptop
| Issue | Likely Cause | Fix |
|---|---|---|
| Won't power on | Dead battery / bad adapter | Try different AC adapter |
| Screen issues | Cable or driver problem | Check display cable, update drivers |
| Keyboard malfunction | Driver or Num Lock issue | Toggle Num Lock, check drivers |
| No network | Config issue | Reset network settings |
| No external display | Output not toggled | Press **Fn + display key** |

### Mobile Devices
| Issue | Likely Cause | Fix |
|---|---|---|
| Won't power on | Dead battery / dirty port | Clean port, try different charger |
| Slow charging | Debris in port / bad cable | Clean port, replace cable/adapter |
| Frozen/unresponsive | App crash / overload | Force restart, remove problematic apps |
| Overheating | Too many apps running | Close all apps, let device cool |
| No Wi-Fi / Bluetooth | Config error | Reset network settings, restart |
| Locked out | Forgotten PIN | Use account recovery |

---

## 8. Hardware Quick Reference

| Component | Key Fact |
|---|---|
| **CPU** | Uses **throttling** to reduce heat and power consumption |
| **Laptop Motherboard** | Form factor **varies by manufacturer** (not standardized like ATX) |
| **SODIMM** | Used in laptops due to **small form factor**; removed by pressing clips outward |
| **LCD Display** | Uses CCFL (contains mercury) or LED backlighting |
| **Card Reader** | Reads **SD cards** (not optical media) |
| **CRU** | Customer Replaceable Unit — parts users can replace themselves (battery, RAM, HDD) |

---

## 9. Power Management (ACPI States)

| State | Description |
|---|---|
| **S0** | Fully on and operational |
| **S1** | CPU & RAM powered; unused devices off (light sleep) |
| **S3** | Sleep — only RAM powered |
| **S4** | Hibernate — contents saved to disk, fully powered off |

---

## 10. Connectivity & Location

### Wireless Standards
- **Bluetooth** — Short-range; used for headphones, keyboards, mice
- **Wi-Fi** — Preferred for data at hotels; low cost vs. cellular roaming
- **GPS** — Uses satellite signals for precise location (latitude/longitude)
- **Cellular + Wi-Fi** used together for location services (geocaching, geotagging, device tracking)

---

## 11. Chapter Summary
- Laptops run full OS (Windows/macOS/Linux) with desktop-compatible ports
- Mobile devices run specialized OSes and are highly portable but more vulnerable
- All portable devices need **preventive maintenance** due to harsh exposure
- Use the **6-step troubleshooting process** for systematic problem resolution
- Key email protocols: **SMTP** (send) | **POP3** (download + delete) | **IMAP** (sync)
- **Bluetooth pairing**, **data sync**, and **backup** are essential mobile skills
