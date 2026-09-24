# 📘 Cisco Networking Academy – CCNA Study Notes (Day 1)

## 📌 1. Cisco IOS Configuration Files

### 🔹 Running Configuration
- Stored in RAM
- Active configuration
- Applied immediately when commands are entered
- Lost when the device is restarted

### 🔹 Startup Configuration
- Stored in NVRAM
- Loaded when the device boots
- Must manually save using:
  copy running-config startup-config

---

## 📌 2. Cisco IOS Modes

### 🔹 User EXEC Mode
- Prompt: Router>
- Limited access
- Can view some information only
- Cannot make configuration changes

### 🔹 Privileged EXEC Mode
- Prompt: Router#
- Accessed using:
  enable
- Full command access

### 🔹 Global Configuration Mode
- Prompt: Router(config)#
- Entered using:
  configure terminal
- Used to configure the device

---

## 📌 3. Password Types

### 🔹 enable secret
- Protects Privileged EXEC mode
- Encrypted password
- Required when entering enable

### 🔹 Console Password
- Protects physical access (console line)

### 🔹 VTY Password
- Protects remote access (Telnet / SSH)

---

## 📌 4. Cisco Device Memory Types

- RAM → Running config (volatile, lost on reboot)
- NVRAM → Startup config (saved permanently)
- Flash → IOS image storage
- ROM → Boot instructions

👉 Key Point:
Only RAM loses data when the device restarts

---

## 📌 5. VLAN (Virtual LAN)

### 🔹 Definition
A method to logically separate networks on the same physical switch

### 🔹 Benefits
- Security
- Traffic control
- Network organization

### 🔹 Default VLAN
- VLAN 1

### 🔹 SVI (Switched Virtual Interface)
- Virtual interface for VLAN
- Used for management (IP address)

---

## 📌 6. CLI Help Features

### 🔹 Context-Sensitive Help
- Use ?
- Shows available commands and options

### 🔹 Example
show ?
show ip ?

---

## 📌 7. DHCP (Dynamic Host Configuration Protocol)

### 🔹 Function
Automatically assigns:
- IP address
- Subnet mask
- Default gateway
- DNS server

👉 No need for manual IP configuration

---

## 📌 8. Shell in Operating System

### 🔹 Function
Interface between user and kernel

👉 Flow:
User → Shell → Kernel → Hardware

---

## 📌 9. Hostname Rules (Cisco)

- No spaces
- Must start with a letter
- Less than 64 characters
- Case-insensitive (upper/lower both allowed)

---

## 📌 10. Important Cisco Commands

### 🔹 Load saved config into running config
copy startup-config running-config

### 🔹 Save running config
copy running-config startup-config

---

## 📌 11. Subnet Basics

### 🔹 Example
IP: 10.1.100.50  
Mask: 255.255.0.0 (/16)

👉 Network = 10.1.0.0

### 🔹 Rule
/16 → first 2 octets = network  
Remaining = host

---

## 📌 12. Key Exam Concepts

- Running config = RAM (immediate, volatile)
- Startup config = NVRAM (saved)
- VLAN 1 = default VLAN
- DHCP = automatic IP assignment
- ? = help command
- Shell = user ↔ kernel interface

---

# 🚀 Summary

This session covered:
- Cisco IOS fundamentals
- Device memory structure
- CLI modes and commands
- VLAN, DHCP, and subnet basics

👉 These are core CCNA fundamentals and must be fully understood
