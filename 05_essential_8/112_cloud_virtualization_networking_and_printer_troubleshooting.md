# IT Essentials / Networking & Hardware Study Notes

A concise reference summary covering displays, cloud, virtualization, networking, hardware, mobile devices, printers, and troubleshooting concepts.

---

## 1. Input/Output Devices

**Q: What characteristic best describes a touch screen?**
**A: An input device that recognizes touch and pressure as instructions.**
A touch screen is an input device because you give commands by touching the display. Unlike a standard monitor (output only), a touch screen both displays information and captures user interaction.

---

## 2. Displays

**Q: New LCD monitor looks pixelated. Solution?**
**A: Set the screen to native resolution.**
LCDs have a fixed physical pixel count (native resolution). If output settings don't match it, the image looks blurry/distorted. Matching the native resolution restores sharpness. (Same principle applies to a pixelated shared laptop display in a conference room, and to laptop internal displays.)

**Q: Where is the integrated Wi-Fi antenna typically located in a laptop?**
**A: Above the screen (inside the display bezel).**
Placing antennas at the top of the display gives a clearer signal path, away from metal components and the user's hands near the keyboard, improving Wi-Fi reception.

---

## 3. Cloud Computing

**Q: A company sets up a new switch supplied by its cloud provider. Which cloud model?**
**A: IaaS (Infrastructure as a Service).**
IaaS rents out virtualized hardware infrastructure — servers, network devices, storage — over the internet. Companies avoid buying/maintaining physical equipment and instead scale infrastructure remotely.

**Q: What does it mean for a cloud service to be "metered"?**
**A: The company is charged based on the amount of service used.**
Like a utility bill (electricity/water), metered cloud billing charges based on actual consumption (data stored, bandwidth, server time) rather than a flat fee — a pay-as-you-go model.

---

## 4. Power over Ethernet (PoE)

**Q: Which two devices commonly use PoE?**
**A: Wireless access points, IP phones.**
PoE delivers both data and electrical power over a single Ethernet cable. This is ideal for devices mounted in hard-to-wire locations (ceilings, walls, desks), eliminating the need for separate power outlets.

---

## 5. Virtualization

**Q: Security measure for a VM running Windows 10?**
**A: Each virtual machine should have antivirus software installed.**
A VM behaves like a real standalone computer with its own OS, so it's equally vulnerable to malware. An unprotected VM can become a gateway to attack the host machine or network — treat it with the same security rigor as physical hardware.

**Q: Two functions of hypervisors?**
**A: Manage virtual machines; allocate physical system resources to virtual machines.**
A hypervisor lets multiple VMs run on one physical computer. It (1) manages each VM's lifecycle independently and (2) distributes CPU, memory, and storage among the VMs — essentially acting as both manager and resource allocator.

---

## 6. Wireless & Mobile Connectivity

**Q: Wireless technology used by a TV remote control?**
**A: IR (Infrared).**
IR sends invisible light signals and requires line-of-sight (no pairing needed) — the standard for TV remotes, unlike Bluetooth/Wi-Fi.

**Q: Traveler's laptop (Wi-Fi/Ethernet only) needs internet via a 3G/4G smartphone. Solution?**
**A: Enable tethering and create a hotspot.**
Tethering shares the phone's mobile data connection. Creating a hotspot turns the phone into a mini Wi-Fi router so the laptop can connect wirelessly.

**Q: Non-overlapping Wi-Fi channels for multiple APs on 802.11g (2.4GHz)?**
**A: Channels 1, 6, and 11.**
In the 2.4GHz band, only channels 1, 6, and 11 don't overlap in frequency. Using this combination across multiple access points prevents interference and connection drops — the industry-standard practice for warehouse/large-facility Wi-Fi.

**Q: Best low-cost technology for a frequent traveler to always stay connected to the corporate network?**
**A: Cellular (4G LTE/5G).**
Cellular uses widely available mobile infrastructure for connectivity anywhere. Satellite is expensive, microwave is for fixed point-to-point links, and ISDN is outdated wired tech — none suit mobile travelers.

---

## 7. Networking Devices & Concepts

**Q: Device that prevents flooding out of every port (except broadcast/unknown-destination traffic)?**
**A: Switch.**
Unlike a hub (which blasts data to every port), a switch learns MAC addresses of connected devices and forwards data only to the intended port, improving efficiency.

**Q: Router feature needed so devices with dynamically assigned private IPs can access the internet?**
**A: NAT (Network Address Translation).**
Private IPs can't route directly on the public internet. NAT translates internal private IPs to a single public IP, letting multiple devices share one internet connection.

**Q: Device that keeps servers, providing the same service, evenly utilized?**
**A: Load balancer.**
A load balancer distributes incoming requests evenly across multiple servers, preventing any one server from being overwhelmed and keeping the system stable and responsive.

**Q: Protocol that automates IP address assignment, and its port number?**
**A: DHCP, port 67.**
DHCP automatically assigns IP addresses to devices joining a network. The DHCP server listens for client requests on port 67 — this is why devices get internet access instantly upon connecting to Wi-Fi without manual configuration.

**Q: Device that converts digital signals to analog and vice versa?**
**A: Modem** (short for "modulator-demodulator").
Computers use digital signals; many telecom networks (e.g., phone lines) use analog. The modem translates between the two so data can travel over such lines.

**Q: What are plenum-rated cables used for?**
**A: Cables installed inside the floors and ceilings of buildings (plenum spaces used for air circulation/HVAC).**
Because these spaces circulate air throughout a building, a fire there could spread toxic smoke quickly. Plenum-rated cables use fire-resistant materials that resist ignition and emit minimal smoke, making them code-compliant for these areas.

---

## 8. Hardware / Cooling / Server Management

**Q: What transfers heat away from the processor first?**
**A: Thermal compound.**
Thermal compound fills microscopic gaps between the CPU surface and heatsink, being the first material to receive and transfer heat away from the CPU before it moves to the cooling system.

**Q: Correct order to install a heat sink/fan assembly on a CPU?**
**A:**
1. Apply thermal compound to the CPU.
2. Align the heat sink/fan retainers with the motherboard holes.
3. Place the fan and heat sink assembly onto the CPU socket.
4. Tighten the retainers to secure the assembly.
5. Connect the fan's power cable to the motherboard's "CPU FAN" connector.

This order matters because the CPU must already be seated in its socket before the heatsink can be mounted and secured, and cooling can only start once the assembly is powered.

**Q: Device to manage multiple servers with one keyboard, mouse, and monitor?**
**A: KVM switch** (Keyboard, Video, Mouse).
A KVM switch lets an administrator control multiple servers/computers from a single set of peripherals, switching between them via button or shortcut — saves space and simplifies server room management.

---

## 9. Mobile Devices

**Q: Two field-replaceable mobile device components?**
**A: SIM card, battery.**
"Field replaceable" means a user/technician can swap the part without special tools or complex disassembly. SIM cards and batteries qualify; touch screens, accelerometers, and internal SSDs typically do not (they require advanced disassembly/soldering).

**Q: Two advantages of flash memory storage (SSD-equivalent) in mobile devices?**
**A: Power efficiency, lightweight components.**
Flash memory has no moving parts (unlike HDDs), so it uses less power (longer battery life) and is much lighter/more compact — improving portability. Note: it's usually soldered onto the board, so it's not user-upgradeable.

---

## 10. Printers

**Q: Advantage of a printer connected to a hardware print server vs. a computer-shared printer?**
**A: A hardware print server is always available to all users.**
A computer-shared printer requires that computer to stay powered on. A dedicated hardware print server runs independently and is always on, so the printer stays accessible regardless of any single workstation's status.

**Q: First thing a technician should check when no print jobs are coming out on a shared network printer?**
**A: The print queue.**
The print queue holds pending jobs in order. A stuck or failed job can block everything behind it. Checking the queue for errors or stalled jobs is the first troubleshooting step.

**Q: Laser printer prints shadow images/text ("ghosting"). What part to replace?**
**A: The drum.**
Ghosting happens when the imaging drum fails to fully clear residual toner from its previous rotation, causing prior content to bleed into new prints. Replacing the drum resolves it.

**Q: Which printer does Windows choose first when multiple printers are configured?**
**A: The printer set as the default printer.**
Windows automatically routes print jobs to whichever device is marked "Default Printer" unless the user manually selects another one.

---

## 11. Troubleshooting Methodology

**Q: Technician asks a customer a series of questions about a network connection problem — which troubleshooting step?**
**A: Identify the problem.**
This is the first stage of structured troubleshooting: gathering details (when it started, error messages, recent changes) to clearly define the issue before forming theories or attempting fixes.

**Q: Customer's printer problem is beyond the technician's knowledge — what should the technician do?**
**A: Gather as much information as possible and escalate the problem.**
Rather than guessing (which risks making things worse), the correct professional approach is to document everything found so far and escalate to a higher-tier support team/technician.

---

## Quick Reference Table

| Topic | Answer |
|---|---|
| Touch screen characteristic | Input device (recognizes touch/pressure) |
| Pixelated new monitor fix | Set to native resolution |
| Cloud model for rented switch | IaaS |
| Metered cloud service | Billed by usage |
| PoE common devices | Wireless APs, IP phones |
| VM security | Install antivirus on every VM |
| Hypervisor functions | Manage VMs; allocate physical resources |
| TV remote wireless tech | IR |
| Pixelated laptop display fix | Set to native resolution |
| NAT purpose | Translate private IPs to public IP |
| Device preventing port flooding | Switch |
| Non-overlapping 2.4GHz channels | 1, 6, 11 |
| Heat transfer from CPU (first) | Thermal compound |
| Laptop connect via phone data | Tethering / hotspot |
| Multi-server control device | KVM switch |
| Print server advantage | Always available to all users |
| No print jobs — check first | Print queue |
| Beyond technician's knowledge | Escalate the problem |
| Digital↔analog conversion device | Modem |
| Field-replaceable mobile parts | SIM card, battery |
| Load balancing device | Load balancer |
| DHCP port | 67 |
| Plenum cable use | Inside floors/ceilings (air-handling spaces) |
| Flash memory advantages | Power efficiency, light weight |
| Default printer behavior | Windows prints to default printer |
| Digital signal problem: shadow/ghost print | Replace drum |
| Best mobile tech for frequent traveler | Cellular (4G/5G) |
| Troubleshooting step: asking questions | Identify the problem |
| Heat sink install order | Compound → align → place → tighten → connect power |
| Wi-Fi antenna location (laptop) | Above the screen |
