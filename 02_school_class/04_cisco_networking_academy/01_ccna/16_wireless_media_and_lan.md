# Wireless Media and Wireless LAN

## 4.6.1 Properties of Wireless Media

Wireless media carry electromagnetic signals using radio or microwave frequencies. It is the **third way** to connect to the physical layer of a network.

### Limitations of Wireless

| Limitation | Description |
|------------|-------------|
| **Coverage area** | Construction materials and local terrain can limit effective coverage |
| **Interference** | Susceptible to interference from cordless phones, fluorescent lights, microwave ovens, etc. |
| **Security** | No physical access required to intercept transmissions; network security is a major concern |
| **Shared medium** | WLANs operate in half-duplex; only one device can send or receive at a time; more users = less bandwidth per user |

> **Note:** Although wireless is growing in popularity, copper and fiber remain the most common physical layer media for routers and switches.

---

## 4.6.3 Wireless LAN

A WLAN requires the following devices:

- **Wireless Access Point (AP):** Concentrates wireless signals and connects to existing copper-based infrastructure (e.g., Ethernet). Home routers integrate router + switch + AP into one device.
- **Wireless NIC adapters:** Provide wireless communication capability to network hosts.

### Key Points
- When purchasing wireless devices, ensure **compatibility and interoperability**
- **Interoperability:** The ability of devices from different manufacturers to work together seamlessly
- Network administrators must apply stringent security policies to protect WLANs from unauthorized access

---

## Packet Tracer Lab - Connect a Wired and Wireless LAN

### Addressing Table

| Device | Interface | IP Address | Connects To |
|--------|-----------|------------|-------------|
| Cloud | Eth6 | N/A | F0/0 |
| Cloud | Coax7 | N/A | Port0 |
| Cable Modem | Port0 | N/A | Coax7 |
| Cable Modem | Port1 | N/A | Internet |
| Router0 | Console | N/A | RS232 |
| Router0 | F0/0 | 192.168.2.1/24 | Eth6 |
| Router0 | F0/1 | 10.0.0.1/24 | F0 |
| Router0 | Ser0/0/0 | 172.31.0.1/24 | Ser0/0 |
| Router1 | Ser0/0 | 172.31.0.2/24 | Ser0/0/0 |
| Router1 | F1/0 | 172.16.0.1/24 | F0/1 |
| WirelessRouter | Internet | 192.168.2.2/24 | Port 1 |
| WirelessRouter | Eth1 | 192.168.1.1 | F0 |
| Family PC | F0 | 192.168.1.102 | Eth1 |
| Switch | F0/1 | 172.16.0.2 | F1/0 |
| Netacad.pka | F0 | 10.0.0.254 | F0/1 |
| Configuration Terminal | RS232 | N/A | Console |

---

### Cable Connection Summary

| # | From (Device & Port) | Cable Type | To (Device & Port) |
|---|----------------------|------------|---------------------|
| 1 | Cloud Eth6 | Copper Straight-Through | Router0 F0/0 |
| 2 | Cloud Coax7 | Coaxial | Cable Modem Port0 |
| 3 | Router0 Ser0/0/0 | Serial DCE | Router1 Ser0/0 |
| 4 | Router0 F0/1 | Copper Cross-Over | Netacad.pka F0 |
| 5 | Router0 Console | Console | Configuration Terminal RS232 |
| 6 | Router1 F1/0 | **Fiber** ⚠️ | Switch F0/1 |
| 7 | Cable Modem Port1 | Copper Straight-Through | WirelessRouter Internet |
| 8 | WirelessRouter Eth1 | Copper Straight-Through | Family PC F0 |

### Cable Selection Guide

| Cable | When to Use |
|-------|-------------|
| Copper Straight-Through | Different device types (router↔switch, PC↔switch) |
| Copper Cross-Over | Same device types (router↔router, PC↔PC) |
| Serial DCE | WAN connection between routers (clock signal provider) |
| Serial DTE | WAN connection between routers (clock signal receiver) |
| Console | Router/switch management (no network access, config only) |
| Fiber | Fiber-optic ports only |

---

### Verification Results (Part 4)

#### Family PC → netacad.pka Ping Test ✅
```
C:\>ping netacad.pka
Pinging 10.0.0.254 with 32 bytes of data:
Reply from 10.0.0.254: bytes=32 time=3ms TTL=126
Reply from 10.0.0.254: bytes=32 time=18ms TTL=126
Reply from 10.0.0.254: bytes=32 time=1ms TTL=126
Reply from 10.0.0.254: bytes=32 time=9ms TTL=126
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss)
```

#### Web Browser Test ✅
- URL: `http://netacad.pka` → Page loaded successfully ("My favorite page!")

#### Home PC → Switch Ping Test ✅
```
C:\>ping 172.16.0.2
(First 2 packets timed out due to ARP processing, then succeeded)
Packets: Sent = 4, Received = 2, Lost = 2 (50% loss)
```

#### Router0 Interface Status ✅
```
Router0>show ip interface brief
Interface         IP-Address    OK? Method Status            Protocol
FastEthernet0/0   192.168.2.1   YES manual up                up
FastEthernet0/1   10.0.0.1      YES manual up                up
Serial0/0/0       172.31.0.1    YES manual up                up
Serial0/0/1       unassigned    YES unset  administratively down  down
Vlan1             unassigned    YES unset  administratively down  down
```

---

### Troubleshooting Log

#### Issue 1: Serial Connection Between Router0 and Router1
- **Symptom:** Serial0/0 port not visible on Router1; only Serial0/1 available
- **Cause:** The .pka file configured Router1's serial port as Serial0/1
- **Fix:** Used Serial DCE cable on Serial0/1 → connection successful ✅

#### Issue 2: Router1 to Switch Connection Failure
- **Symptom:** Both Copper Straight-Through and Copper Cross-Over cables returned connection errors
- **Root Cause:** Router1's FastEthernet1/0 port icon showed two circles, indicating a **fiber-optic port**, not a standard RJ-45 copper port
- **Attempted fixes:**
  - ❌ Copper Straight-Through → Connection Error
  - ❌ Copper Cross-Over → Connection Error
  - ❌ Replacing module via Physical tab → Blocked (Interface Locked by author's design)
- **Final fix:** Used **Fiber cable** on Switch's GigabitEthernet port → connection successful ✅

#### Lesson Learned
> Always check the **port icon** before selecting a cable:
> - Standard square icon → Copper (RJ-45)
> - Two-circle icon → Fiber-optic
>
> In locked .pka files, module replacement may not be possible. Match the cable type to the existing port hardware.

---

## Key Terms

| Term | Definition |
|------|------------|
| **Interoperability** | Ability of devices from different manufacturers to work together without issues |
| **Overkill** | Using something far more powerful than necessary (e.g., WiMAX for simple IoT devices) |
| **Half-duplex** | Communication mode where only one party can send or receive at a time |
| **DCE** | Data Communications Equipment; provides clock signal in a serial WAN link |
| **DTE** | Data Terminal Equipment; receives clock signal in a serial WAN link |
| **AP (Access Point)** | Device that concentrates wireless signals and connects to a wired network |
| **SFP** | Small Form-factor Pluggable; slot that accepts fiber-optic modules on GigabitEthernet ports |
| **show ip interface brief** | CLI command to display status of all router interfaces at a glance |

---

## Quiz Review

**Q3. Which wireless standard is best suited for industrial and IoT environments?**

✅ **Answer: Zigbee**

| Option | Why it's wrong |
|--------|---------------|
| Bluetooth | Short-range only; not suitable for large-scale IoT |
| **Zigbee** ✅ | Low power, supports large device networks, ideal for IoT |
| WiMAX | Designed for long-range broadband; overkill for IoT |
| Wi-Fi | High power consumption; inefficient for many IoT devices |
