# Networking Devices — Study Notes

A summary of core networking hardware: what each device does, how it works, and how it compares to the others.

---

## 1. Network Interface Card (NIC)

The NIC provides the physical connection between a computer and a network.

- **Function:** Acts as the bridge that lets a computer communicate with other devices over a network.
- **Types:**
  - *Ethernet NIC* — wired connections
  - *Wireless NIC* — connects to 802.11 wireless networks
- **Form Factor:** Most modern computers have NICs built into the motherboard, though they can also be added via expansion slots or USB.
- **Key Operations:**
  - **Addressing** — uses a unique **MAC address** to identify itself on the network
  - **Data Transmission** — converts data into bits and sends it out onto the network
- Most current NICs support **gigabit Ethernet speeds (1000 Mbps)**, including wireless capability, often built directly into the motherboard.

---

## 2. Repeater

In early networking, repeaters, hubs, and bridges were used to expand and connect networks.

- **Purpose:** Regenerates weak signals.
- **Role:** Signals weaken over long distances; a repeater detects this and restores the signal to its original strength.
- **Alias:** Also called an **"extender"** because it extends the distance a signal can travel.
- **Modern Usage:** Mainly used today to regenerate signals in **fiber-optic cables**.
- **Note:** Nearly all modern networking devices that send/receive data have built-in signal regeneration.

---

## 3. Hub

A legacy device used to connect multiple computers into a single network.

- **Operation:** Receives data on one port and **broadcasts it to all other ports** — every connected device receives the data, regardless of the intended recipient.
- **Drawback:** All devices share one bandwidth path, so heavy traffic slows the whole network.
- **Status:** Legacy technology, rarely used today.

---

## 4. Bridge

Introduced to divide large networks into smaller **segments**.

- **Operation:** Keeps a record of which devices are in which segment, and forwards data only to the relevant segment instead of broadcasting everywhere.
- **Benefit:** Filters unnecessary traffic, improving overall network efficiency.
  - *Example:* A print job within Segment 1 doesn't flood into Segment 2, keeping traffic organized and fast.

---

## 5. Switch

The modern replacement for hubs and bridges — efficient and cost-effective.

- **Core Function — Microsegmentation:** Sends data only to the specific device it's intended for (not a broadcast like a hub), giving every device dedicated bandwidth.
- **How It Works:**
  - Every device has a unique **MAC address**.
  - The switch learns which device is on which port and records this in a **switching table**.
  - Incoming traffic is checked against this table and forwarded only to the correct port.
- **Managed vs. Unmanaged:**
  | Type | Description | Use Case |
  |---|---|---|
  | **Managed Switch** | Configurable settings, security (e.g., port security), VLAN support | Large enterprise networks |
  | **Unmanaged Switch** | Plug-and-play, no configuration needed | Home / small office networks |

---

## 6. Wireless Access Point (AP)

Provides network connectivity to wireless devices (laptops, tablets, etc.).

- **Operation:** Uses radio waves to communicate with wireless NICs in devices.
- **Coverage:** Limited range — large spaces need multiple APs.
- **AP vs. Wireless Router:** A basic AP only provides connectivity; a wireless router adds extra features on top of that.

---

## 7. Router

Connects **different networks** together — acts as a gateway to the outside world (e.g., the internet).

- **Router vs. Switch/AP:** Switches and APs handle traffic *within* a single network using **MAC addresses**; routers connect *separate networks* using **IP addresses**.
- **Gateway Function:** In larger networks, a router connects switches (which host LANs) to external networks.
- **Integrated/Multipurpose Routers:** Home/small-office routers typically combine a router, switch, wireless AP, and modem into a single device for convenience.

---

## 8. Quick Reference Table

| Device | Core Function |
|---|---|
| **Bridge** | Legacy device used to divide a LAN into segments |
| **Hub** | Legacy device that increased the number of devices connectable to a LAN |
| **Switch** | Microsegments a LAN; forwards data based on **MAC address** |
| **Repeater** | Regenerates weak network signals |
| **Router** | Connects networks; forwards data based on **IP address** |
| **Wireless AP** | Uses radio waves to extend network reach wirelessly |
| **NIC** | Connects end devices directly to the network |

---

## 9. Network Security Devices

### Firewall
A security barrier between a trusted internal network and an untrusted external network (e.g., the internet).

- **Function:** Monitors/controls incoming and outgoing traffic based on predefined security rules — often **Access Control Lists (ACLs)** — to permit or deny traffic.
- **Performance:** Doesn't use the protected computer's own resources, so it has no impact on processing speed.
- **Integration:** Home/small-office integrated routers typically bundle switch + router + firewall functions. OS-level firewalls (e.g., Windows Defender) can add an additional layer.

### Intrusion Detection System (IDS)
- **Mode:** Passive monitoring.
- **Function:** Observes traffic and compares it against known malicious signatures (attack patterns); **alerts** administrators when a threat is detected — does not block it.

### Intrusion Prevention System (IPS)
- **Mode:** Active, **inline** — all inbound/outbound traffic must pass through it.
- **Function:** Inspects data *before* it reaches its destination. Safe traffic passes through; malicious traffic is **blocked immediately**.
- **Key Difference from IDS:** IDS detects and alerts; IPS detects and **actively prevents**.
- **Caution:** Because it inspects all traffic in real time, a poorly configured IPS can slow down network performance.

---

## 10. Key Takeaways

1. **Evolution of LAN connectivity:** Hub (broadcast all) → Bridge (segment-aware) → Switch (MAC-based microsegmentation) is the historical progression toward efficiency.
2. **Switches operate within a LAN** using MAC addresses; **routers connect separate networks** using IP addresses — this is the fundamental Layer 2 vs. Layer 3 distinction.
3. **Repeaters/extenders** solve signal degradation over distance, now mostly relevant to fiber-optic signal regeneration.
4. **Security layers stack:** Firewall (rule-based gatekeeping) + IDS (passive detection/alerting) + IPS (active inline blocking) together form a layered defense strategy.
5. **Integrated/consumer devices** (home routers) bundle router + switch + AP + firewall + modem into one box for simplicity — but enterprise environments use these as separate, dedicated, and more configurable devices.
