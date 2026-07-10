# Windows OS Installation & Management — Study Summary

## 1. Windows 10 Installation

**Requirements:** blank hard drive, Windows 10 installer (USB/DVD)

**Steps:**
1. Boot from installation media
2. Click *Next* → *Install now*
3. Enter product key, accept license terms
4. Choose **Custom: Install Windows only (advanced)** and select the unallocated drive space
5. Windows copies files and restarts multiple times automatically
6. Set region and keyboard layout
7. Choose **Set up for personal use**
8. Create a **local (offline) account** instead of a Microsoft account — set username, password, and security questions
9. Configure Cortana and privacy settings
10. Installation finishes → desktop loads

---

## 2. Finalizing Installation

**Account types:**
- **Administrator** – full control (install/remove programs, change all settings)
- **Standard User** – limited control (can't install software or change system-wide settings)

**Adding a user account:** Settings → Accounts → Family & other users → Add someone else to this PC → *I don't have this person's sign-in information* → *Add a user without a Microsoft account*

**Post-install checks:**
- **Windows Update** — scans and installs security patches/software
- **Device Manager** — checks hardware status
  - ⚠️ Yellow triangle = device problem
  - Gray circle w/ down arrow = device disabled
  - Driver tab options: view driver details, update driver, roll back driver, uninstall device

---

## 3. Disk Cloning & Mass Deployment

- **Sysprep (System Preparation Tool):** wipes machine-specific info (hardware IDs, etc.) from a "master" image before cloning it to other computers, preventing conflicts.
- **Deployment methods for large organizations:**
  - **Network installation** – deploy OS to many machines over the network
  - **Image-based installation** – clone a pre-configured master image to other PCs
  - **Recovery/custom options** – recovery partitions, advanced startup, repair installs

**PXE (Preboot Execution Environment):** lets a computer with no OS installed boot and install Windows over the network via its network card, without physical media.

**Unattended installation:** uses an **answer file** (XML, created with **Windows System Image Manager / ADK**) containing all setup answers (language, accounts, software) so installation runs automatically from a shared folder or USB with no user input.

---

## 4. System Restore & Recovery

**System Restore**
- Rolls back *system files only* to an earlier restore point (does **not** touch personal files)
- Access: Control Panel → System and Security → Security and Maintenance → Recovery → Open System Restore
- Restore points are created automatically (e.g., updates) or manually

**Recovery options** (Settings → Update & Security → Recovery)
- **Recovery Partition** – hidden factory-image area on the drive; restores factory state; may include vendor software; inaccessible if the drive itself fails
- **Reset this PC**
  - *Keep my files* – removes apps/settings, keeps personal data, reinstalls Windows
  - *Remove everything* – wipes everything back to default

---

## 5. OS Upgrade Considerations (Windows 10 → 11)

**Before upgrading:**
- Check **product lifecycle / end-of-support date**
- Verify **hardware meets Windows 11 minimum requirements** (can check via Windows Update)
- Review **deprecated features** that may affect your workflow
- Check **app/driver compatibility** — use *Compatibility mode* (right-click exe → Properties → Compatibility tab) if needed
- Check **partition style**: drives over 2TB need **GPT** instead of **MBR** (requires UEFI)
  - Check via Disk Management or PowerShell (`diskpart` → `list disk`)
- **Back up files and settings** (external drive, File History, or cloud)

**Upgrade methods:**
- **In-place upgrade** – upgrades over the existing OS, keeps files/settings/apps; back up first
- **Clean install** – erases the drive and installs fresh; requires bootable media and a product key

**After upgrading:**
- Update drivers via Device Manager
- Run Windows Update
- Create a new **system restore point** or **system image** for safety

---

## 6. Boot Methods & BIOS/UEFI

**Boot devices/media types:**
- Bootable USB/DVD (created with Media Creation Tool)
- **PXE / network boot** – boots via NIC, pulls OS from a server; used for mass deployment in large organizations; needs PXE-capable NIC + DHCP/TFTP server infrastructure
- Internet-based boot – downloads install image directly online
- Hard drive partition boot – used for dual-boot setups

**BIOS vs UEFI**
- **BIOS** – legacy firmware on the motherboard chip; controls booting, keyboard, basic hardware setup
- **UEFI** – modern replacement; faster boot, better security, supports large drives

**Accessing firmware settings:**
- **Boot key method** – press Esc/Delete/F2/F12 (varies by manufacturer) right after power-on
- **Windows Settings method** – Settings → Update & Security → Recovery → Advanced startup → Restart now → Use a device

Boot order can be changed inside BIOS/UEFI to prioritize USB/DVD over the internal drive.

---

## 7. Windows Boot Sequence & Startup/Troubleshooting Modes

**Boot sequence:** Power on → **POST** (hardware check) → BIOS checks boot device order → reads **MBR (Master Boot Record)** on the boot device → loads Windows Boot Manager → OS starts.

**Windows 7 – Advanced Boot Options (press F8):**
- **Safe Mode** – loads only essential drivers/services (for troubleshooting)
- **Safe Mode with Networking** – Safe Mode + network access
- **Safe Mode with Command Prompt** – command-line only, no desktop
- **Last Known Good Configuration** – reverts to the last successful boot settings

**Windows 8/10 – Startup Settings:**
- F8 is disabled by default for faster boot
- Access via: hold **Shift** while clicking Restart → Troubleshoot → Advanced options → Startup Settings
- Offers similar options to Windows 7 (Safe Mode variants, disable driver signature enforcement, etc.)

**Key terms:**
| Term | Meaning |
|---|---|
| MBR | First sector read at boot; points to the Volume Boot Record / Boot Manager |
| F8 | Opens Advanced Boot Options (Windows 7) |
| Safe Mode | Minimal diagnostic startup mode |
| BIOS | Firmware that reads CMOS settings and initializes hardware |
| Last Known Good Configuration | Restores last successful boot settings |
| Boot device priority | Order in which storage devices are checked at startup |
