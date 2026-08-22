# Networking Study Notes
> CCNA / Networking Fundamentals — Key Concepts Summary

---

## Q16 — Router Boot Mode (NVRAM & Console)

**Scenario:** A router with a valid OS has a config file in NVRAM. The config has an `enable secret` password but **no console password**.

**Question:** Which mode is displayed when the router boots?

**Answer:** `User EXEC Mode`

### Key Concepts

| Term | What It Is | Analogy |
|------|-----------|---------|
| **NVRAM** (Non-Volatile RAM) | Stores the router's startup config; data persists after power-off | Hard drive / USB — files survive shutdown |
| **Console Port** | Physical management port for direct local access to the router | A technician's direct service port on a machine |
| **User EXEC Mode** | The default, restricted mode shown at startup — read-only "viewer" access | A museum with no key — you can look, not touch |

### Logic
- No console password → router doesn't prompt for credentials on console access
- Router lands directly in **User EXEC Mode** (`Router>`)
- To reach **Privileged EXEC Mode** (`Router#`), the `enable secret` password is still required

---

## Q17 — The `ping` Command (ICMP)

**Question:** Which command tests connectivity between two devices using echo request and echo reply messages?

**Answer:** `ping`

### Key Concepts

| Term | Description |
|------|-------------|
| **ping** | CLI command that sends ICMP Echo Requests and waits for Echo Replies |
| **ICMP** | The underlying protocol (set of rules) that defines how echo messages work |
| **Echo Request** | "Are you there?" — sent by the source device |
| **Echo Reply** | "Yes, I'm here!" — response from the destination device |

### Analogy
> Ringing a doorbell to see if someone is home. `ping` is the action; ICMP is the rule that defines how the doorbell works.

---

## Q — Reliable Network Architecture (Security, Fault Tolerance, Scalability)

**Question:** Match each network architecture requirement to its description.

### Matching Answers

| Architecture | Description | Analogy |
|---|---|---|
| **Security** | Protect the network from unauthorized access | Security guard at a building entrance |
| **Fault Tolerance** | Provide redundant links and devices | Backup generators / emergency exits |
| **Scalability** | Expand the network without degrading service for existing users | Adding floors to a building without slowing the elevators |

---

## Q — IPv6 Hierarchical Addressing & Maximum Subnets per Sub-site

**Scenario:** A company uses IPv6 with a hierarchical subnet structure:
`site` → `sub-site` → `subnet` (each section = 1 hex digit)

**Question:** What is the maximum number of subnets per sub-site?

**Answer:** `16`

### Key Concepts

| Term | Description | Analogy |
|------|-------------|---------|
| **Subnet** | A smaller, logical division of a larger network | A building unit (apt. number) within a complex |
| **Sub-site** | A sub-division within a site (e.g., a campus within a city) | A district within a city |
| **Nibble** | 4 bits grouped together; one hexadecimal digit = 1 nibble | One "slot" in an address label |
| **Hexadecimal** | Base-16 number system (0–9, A–F) | 16 possible values per digit slot |

### The Math
- One hex digit (nibble) = 4 bits = **16 possible values** (0, 1, 2 … 9, A, B, C, D, E, F)
- The subnet field uses **one hex digit** → **16 unique subnets** per sub-site

### Hierarchy Summary

```
Site        →  City
Sub-site    →  District
Subnet      →  Neighborhood block
Nibble      →  The single digit used to label each block
```

---

## Q — Verifying IPv6 Routing is Enabled

**Scenario:** Only employees on IPv6 interfaces can't reach remote networks. Analyst needs to verify IPv6 routing is enabled.

**Answer:** `show ipv6 route`

### Why This Command?

| Command | What It Does | Best For This Task? |
|---------|-------------|---------------------|
| `show ipv6 route` | Displays the IPv6 routing table; errors out if IPv6 routing is off | ✅ **Yes — most direct verification** |
| `show running-config` | Shows entire config as text; `ipv6 unicast-routing` buried inside | ❌ Inefficient |
| `show ipv6 interface` | Shows IPv6 address status per interface | ❌ Doesn't confirm global routing |
| `copy startup-config running-config` | Loads saved config into memory | ❌ Not a verification command |

### Key Concept
- IPv6 routing requires `ipv6 unicast-routing` to be enabled in global config mode
- If disabled, `show ipv6 route` returns an error or empty table → confirms the issue

---

## Q — UDP Characteristics

**Question:** What is a characteristic of UDP?

**Answer:** UDP is a **connectionless, fire-and-forget** protocol — it sends data without verifying the receiver is ready.

### UDP vs TCP (Quick Comparison)

| Feature | UDP | TCP |
|---------|-----|-----|
| Connection setup | ❌ None (connectionless) | ✅ 3-way handshake |
| Delivery guarantee | ❌ No | ✅ Yes |
| Order guarantee | ❌ No | ✅ Yes |
| Error checking / reassembly | ❌ Minimal | ✅ Full |
| Speed | ✅ Very fast | Slower (overhead) |
| Use cases | Streaming, gaming, VoIP | File transfer, web, email |

### Analogy
> UDP is like mailing a letter — you drop it in the box without knowing if the recipient is home, if it arrives in order, or if it arrives at all. Fast, but no guarantees.

### Common Wrong Answers (and why they're wrong)

| Wrong Statement | Why It's Wrong |
|----------------|----------------|
| "UDP datagrams take the same path and arrive in order" | UDP has no path consistency or ordering guarantee |
| "Apps using UDP are always unreliable" | UDP is a *transport choice*, not a quality judgment — streaming apps work great with it |
| "UDP reassembles received datagrams in the correct order" | UDP does not reassemble — that's TCP's job |
| "UDP only sends data when the destination is ready" | That describes TCP (connection-oriented); UDP sends regardless |

---

## Quick Reference Glossary

| Term | Definition |
|------|-----------|
| **NVRAM** | Non-Volatile RAM; stores router startup config, survives power loss |
| **Console** | Physical port for direct local management of a router/switch |
| **User EXEC Mode** | Router prompt `>` ; read-only, limited commands |
| **Privileged EXEC Mode** | Router prompt `#` ; full access, requires enable password |
| **ping** | Command using ICMP echo request/reply to test connectivity |
| **ICMP** | Internet Control Message Protocol; handles diagnostic messages |
| **Security** | Protecting network from unauthorized access |
| **Fault Tolerance** | System continues operating despite failures via redundancy |
| **Scalability** | Ability to grow without degrading existing performance |
| **IPv6** | 128-bit addressing scheme; successor to IPv4 |
| **Subnet** | Logical subdivision of a network |
| **Nibble** | 4-bit group = 1 hexadecimal digit; 16 possible values |
| **UDP** | User Datagram Protocol; fast, connectionless, no delivery guarantee |
| **TCP** | Transmission Control Protocol; reliable, ordered, connection-based |
| **ipv6 unicast-routing** | Cisco IOS command to enable IPv6 packet forwarding |
| **show ipv6 route** | Displays IPv6 routing table; verifies routing is active |
