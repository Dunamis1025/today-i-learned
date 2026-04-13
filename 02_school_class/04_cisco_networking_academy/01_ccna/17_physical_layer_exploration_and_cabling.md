# Physical Layer Exploration and Device Connectivity

## 1. Objective
The goal of this lab was to understand how data packets physically travel across vast distances and to master the physical assembly of network devices, including module installation and appropriate cabling.

---

## 2. Part A: Physical Mode Exploration (Traceroute)
In this section, I traced the physical path of IP packets from Monterey, California, to Honolulu, Hawaii.

### Key Concepts
* **Hop-by-Hop Journey:** Each router along the path represents a "hop." Using the `tracert` command, I identified how packets move from a private home network through an ISP's Point of Presence (POP).
* **Latency and Distance:** I observed a significant jump in Round Trip Time (RTT) from ~23ms to ~85ms when the packets crossed the Pacific Ocean via submarine cables.
* **IXP (Internet Exchange Point):** Identified where different ISPs (e.g., Comcast and Internet2) interconnect to exchange traffic.

### Path Breakdown
1. **Local Loop:** Home PC -> Home Router -> ISP POP (Comcast).
2. **Backbone:** San Jose IXP -> Los Angeles IXP.
3. **Submarine Cable:** SEA-US cable crossing the Pacific Ocean.
4. **Destination:** University of Hawaii Network.

---

## 3. Part B: Connecting the Physical Layer
This part focused on the hardware aspect of networking—customizing devices to meet connectivity requirements.

### Hardware Customization (Modules)
Since standard routers and switches often have limited ports, I performed the following hardware upgrades:
* **Router Expansion:** Installed the **HWIC-4ESW** switching module in the Cisco 1941 router to provide additional FastEthernet ports for end devices (PC1, PC2, PC3).
* **Switch Expansion:** Installed the **PT-SWITCH-NM-1FGE** (Gigabit Fiber) module in Switch2 to enable high-speed optical connectivity.
* **Important Rule:** Devices must be **powered off** before adding or removing modules (unless they are hot-swappable).

### Cabling Standards
I applied the correct cable types based on the device layers:
* **Copper Straight-Through:** Used for connecting dissimilar devices (e.g., Router to Switch, Switch to PC).
* **Copper Cross-Over:** Used for connecting similar devices (e.g., Switch to Switch).
* **Fiber Optic:** Used for high-speed, long-distance links between Switch3 and Switch2.
* **Serial DCE:** Used for WAN connections between routers (East to West).

---

## 4. Troubleshooting & Verification
During the lab, I encountered and resolved several issues:
* **Interface Status:** Even with correct cabling, interfaces are often `administratively down`. I used the `no shutdown` command in the CLI to activate ports.
* **Port Mismatch:** Ensured Fiber cables were connected to **Gigabit** ports rather than standard Ethernet ports to establish a link.
* **Verification Command:**
  ```bash
  East> show ip interface brief
  Verified that all physical interfaces were Status: up / Protocol: up.
  ```
## 5. Summary
Understanding the physical layer is not just about logical IP addresses; it is about the physical cables, the specific modules, and the actual geographic path the data takes. This lab bridged the gap between abstract networking concepts and real-world hardware implementation.
  
