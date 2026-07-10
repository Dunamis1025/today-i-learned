# Windows Networking & CLI — Study Notes

## 1. Group Policy CLI

- **`gpupdate`** — Forces an immediate refresh of Group Policy settings.
  - `gpupdate /force` — reapplies all policies even if unchanged.
- **`gpresult`** — Displays the Resultant Set of Policy (RSoP) currently applied to a user/computer.
  - `gpresult /R` — summary view in the terminal.
  - `gpresult /H report.html` — exports a report to HTML.
  - ⚠️ Note: `/H` is not available on **Windows Home edition** (Group Policy management tools are limited/removed on Home).

## 2. User & Network Resource Management (`net` command)

- **`net user`**
  - `net user` — lists all local accounts.
  - `net user <username>` — shows account details (active status, password expiration, group membership).
  - `net user <username> <password> /add` — creates a new account (requires admin privileges).
  - `net user <username> /delete` — removes an account.
- **`net use`**
  - `net use` — lists current network drive connections.
  - `net use * "\\computername\sharename" /user:username password` — maps a network share to the next available drive letter.
  - `net use Y: /delete` — disconnects a mapped drive.

## 3. Domain vs. Workgroup vs. Homegroup

| Type | Description |
|---|---|
| **Domain** | Centralized management via a domain controller; used in businesses. One login works across any machine on the network. |
| **Workgroup** | Peer-to-peer setup for small networks/home use; each computer manages its own accounts and permissions independently. |
| **Homegroup** | Simplified home file/printer sharing (Windows 7/8, early Win10) using a single shared password. Removed starting Windows 10 v1803. Could not be created on domain-joined machines. |

## 4. Network File Sharing & Drive Mapping

- **Mapped drive**: assigns a letter (A–Z) to a remote share so it behaves like a local drive.
- **Permission levels** for shared resources:
  - **Read** — view/open files and run programs; no editing.
  - **Change** — Read + add/edit/delete files and subfolders.
  - **Full Control** — Change + Read + modify permissions and take ownership (NTFS only).
- Actual effective access = the **more restrictive** of NTFS (Security tab) permissions and Share (Sharing tab) permissions — a key troubleshooting concept.

## 5. Sharing a Folder (GUI Workflow)

1. Right-click folder → **Give access to** (quick/basic sharing) or **Properties → Sharing tab → Advanced Sharing** (full control).
2. **Security tab**: add users/groups (e.g., "Everyone") and set NTFS permissions (Read/Modify/Full Control).
3. **Advanced Sharing → Permissions**: set share-level permissions (Read/Change/Full Control).
4. For sharing to work network-wide without credentials, disable **Password Protected Sharing** in *Network and Sharing Center → Advanced sharing settings*.
5. Access a remote share via `\\ComputerName\ShareName` in File Explorer or the Run box.

## 6. Administrative Shares

- Hidden shares ending in `$` (e.g., `C$`), auto-created by Windows for system administration.
- Not visible when browsing the network; accessible only by local Administrators group members.
- Users can create their own hidden share by appending `$` to a custom share name.

## 7. Printer Sharing

- **Local printer sharing**: a printer physically attached to one PC (USB/direct) is shared out via the printer's Properties → Sharing tab; that PC acts as the print server.
- **Network printer mapping**: a printer with built-in Ethernet/Wi-Fi connects directly to the network and is added via the "Add Printer" wizard — no host PC required.

## 8. Configuring a Wired NIC

- IP configuration methods:
  - **Static (manual)** — IP address, subnet mask, default gateway entered manually.
  - **Dynamic** — obtained automatically via DHCP (IPv4) or SLAAC (IPv6).
- **APIPA**: if DHCP fails, Windows self-assigns an address in the `169.254.x.y` range.
- **Alternate Configuration**: a backup static IPv4 config used when DHCP is unavailable — useful for laptops moving between networks.
- IPv6 settings (address, prefix length, gateway) are configured similarly via the NIC's IPv6 properties.
- Best practice: disable the onboard NIC in BIOS when installing a new physical NIC.

## 9. Network Profiles

- **Public**: PC is hidden from other devices; file/printer sharing disabled. Use on untrusted networks.
- **Private**: PC is discoverable; file/printer sharing enabled. Use on trusted/home networks only.

## 10. Verifying Connectivity — GUI & CLI

**GUI**: Network Connections → adapter **Status** window shows IP, gateway, MAC address; **Diagnose** button auto-troubleshoots.

**CLI tools**:
- `ipconfig` — basic IP address, subnet mask, default gateway.
- `ipconfig /all` — full config including DHCP server, DNS server, MAC address.
- `ipconfig /release` / `ipconfig /renew` — release/request a DHCP-assigned IP.
- `ipconfig /displaydns` — shows cached DNS lookups.
- `ipconfig /flushdns` — clears the DNS cache.
- `ping <target>` — tests Layer 3 (network) reachability using ICMP echo request/reply; works with an IP or a hostname (triggers a DNS lookup first).
- `tracert <target>` — traces the hop-by-hop path to a destination; useful for locating where connectivity breaks.
- `nslookup <target>` — queries DNS to resolve a hostname ↔ IP address.
- `netstat -b -n` — lists active connections/ports and the process (`-b`) responsible for each, skipping DNS resolution (`-n`) for speed. Requires an elevated (admin) command prompt.

---
*Compiled from Cisco IT Essentials (ITE) lab materials and course videos.*
