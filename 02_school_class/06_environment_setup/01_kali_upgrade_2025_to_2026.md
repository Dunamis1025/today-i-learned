# Kali Linux Upgrade: 2025.4 → 2026.1

> **Environment:** VMware Workstation on Windows 11
> **Goal:** Upgrade Kali Linux from version 2025.4 to 2026.1
> **Result:** ✅ Successfully upgraded

---

## Step 1: Check Current Version

```bash
cat /etc/os-release
```

Output confirmed version was **2025.4**:

```
VERSION_ID="2025.4"
VERSION="2025.4"
VERSION_CODENAME=kali-rolling
```

Also checked kernel version:

```bash
uname -r
```

Output: `6.16.8+kali-amd64`

---

## Step 2: Attempt Upgrade (First Attempt — Failed)

```bash
sudo apt update && sudo apt full-upgrade -y
```

### Error 1: Repository does not have a Release file

```
Err:2 http://http.kali.org/kali kali-rolling Release
Cannot initiate the connection to http.kali.org:80 (2607:5300:203:3fe6::).
— connect (101: Network is unreachable)
Error: The repository 'http://http.kali.org/kali kali-rolling Release'
does not have a Release file.
```

**Two problems identified:**
1. `sources.list` was using `http://` instead of `https://`
2. Network was unreachable (VM could not connect to the internet)

---

## Step 3: Fix sources.list (http → https)

Checked current sources.list:

```bash
cat /etc/apt/sources.list
```

Output showed `http://` — needed to change to `https://`

Attempted to edit manually with nano:

```bash
sudo nano /etc/apt/sources.list
```

> **Issue:** Changes were not saved properly (forgot to confirm with Ctrl+X → Y → Enter)

Used `sed` command instead to force the replacement:

```bash
sudo sed -i 's|http://http.kali.org|https://http.kali.org|g' /etc/apt/sources.list
```

Verified the change:

```bash
cat /etc/apt/sources.list
```

Output confirmed `https://` was now set:

```
deb https://http.kali.org/kali kali-rolling main contrib non-free non-free-firmware
```

---

## Step 4: Diagnose Network Issue

Even after fixing sources.list, the update still failed with **Network is unreachable**.

Tested connectivity:

```bash
ping 8.8.8.8
```

Output:

```
From 192.168.10.20 icmp_seq=1 Destination Host Unreachable
ping: sendmsg: No route to host
100% packet loss
```

**Confirmed:** VM had no internet access.

---

## Step 5: Investigate Network Configuration

Checked IP address assignment:

```bash
ip addr show
```

Key findings:
- `eth0` had two IPs assigned:
  - `192.168.10.20/24` (static, incorrect subnet)
  - `192.168.29.128/24` (dynamic, correct VMware NAT subnet)

Checked routing table:

```bash
ip route show
```

Output:

```
default via 192.168.10.1 dev eth0 proto static metric 100
192.168.10.0/24 dev eth0 ...
192.168.29.0/24 dev eth0 ...
```

**Root cause identified:**
The default gateway was set to `192.168.10.1`, but the correct VMware NAT gateway was on the `192.168.29.x` subnet.

---

## Step 6: Find Correct Gateway IP

Opened VMware Virtual Network Editor on Windows:

`Edit → Virtual Network Editor → VMnet8 (NAT) → NAT Settings`

Found:
- **Subnet IP:** `192.168.29.0`
- **Gateway IP:** `192.168.29.2` ← this was the correct gateway

---

## Step 7: Fix Default Gateway

Removed the incorrect default route and added the correct one:

```bash
sudo ip route del default
sudo ip route add default via 192.168.29.2
```

Tested connectivity again:

```bash
ping 8.8.8.8
```

Output:

```
64 bytes from 8.8.8.8: icmp_seq=1 ttl=128 time=5.60 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=128 time=5.30 ms
13 packets transmitted, 13 received, 0% packet loss
```

**Network restored successfully.**

---

## Step 8: Run Upgrade

```bash
sudo apt update && sudo apt full-upgrade -y
```

During the upgrade, a prompt appeared asking to restart services for the GNU libc library upgrade — selected **OK** and pressed Enter to continue.

After completion:

```bash
sudo reboot
```

---

## Step 9: Verify Upgrade

After reboot:

```bash
cat /etc/os-release
```

Output confirmed successful upgrade:

```
PRETTY_NAME="Kali GNU/Linux Rolling"
VERSION_ID="2026.1"
VERSION="2026.1"
VERSION_CODENAME=kali-rolling
```

---

## Summary: What Went Wrong and Why

| Problem | Cause | Fix |
|---------|-------|-----|
| `sources.list` used `http://` | Default config uses insecure HTTP | Changed to `https://` using `sed` |
| nano edits not saved | Forgot Ctrl+X → Y → Enter | Used `sed -i` command instead |
| Network unreachable | Default gateway pointed to wrong subnet (`192.168.10.1`) | Changed gateway to `192.168.29.2` (VMware NAT gateway) |
| Wrong gateway assigned | VM had two IPs on different subnets; static route took priority | Deleted old default route, added correct one manually |

---

## Key Commands Reference

```bash
# Check Kali version
cat /etc/os-release

# Check kernel version
uname -r

# Fix sources.list (http to https)
sudo sed -i 's|http://http.kali.org|https://http.kali.org|g' /etc/apt/sources.list

# Check IP addresses
ip addr show

# Check routing table
ip route show

# Fix default gateway
sudo ip route del default
sudo ip route add default via <correct_gateway_ip>

# Test connectivity
ping 8.8.8.8

# Run upgrade
sudo apt update && sudo apt full-upgrade -y
```

---

## Notes

- VMware NAT gateway IP can be found at:
  `VMware Workstation → Edit → Virtual Network Editor → VMnet8 → NAT Settings → Gateway IP`
- The gateway is typically `<subnet>.2` (e.g. if subnet is `192.168.29.0`, gateway is `192.168.29.2`)
- The `ip route` fix above is **temporary** and resets on reboot.
  To make it permanent, configure it in `/etc/network/interfaces` or use NetworkManager.
- Kali Linux uses a **rolling release** model — upgrading with `full-upgrade` always brings you to the latest version
