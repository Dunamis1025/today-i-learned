# IT Fundamentals — Study Notes

A quick-reference summary of hardware, networking, and virtualization concepts.

## Displays & Input

- **Touch screen**: Best described as an *input device* that recognizes touch and pressure as instructions — not just an output display.
- **Native resolution**: When an LCD/LED monitor looks blurry or pixelated, set the display to its native resolution (the resolution matching its actual physical pixel grid). Mismatched resolution forces the image to stretch/shrink, causing blur.

## Cloud Computing

- **IaaS (Infrastructure as a Service)**: If a company is configuring physical/virtual infrastructure (e.g., a switch) supplied by a cloud provider, that's IaaS — the provider rents out raw infrastructure, and the customer manages the configuration.

## Networking

- **PoE (Power over Ethernet)**: Delivers both data and power over a single Ethernet cable. Commonly used for **wireless access points** and **IP phones**, especially in locations without easy access to power outlets.
- **NAT (Network Address Translation)**: Required to let devices with private IP addresses (assigned dynamically via DHCP) access the public internet. NAT translates private IPs into a single public IP on the router.
- **Switch vs. Hub**: A switch learns MAC addresses per port and forwards data only to the intended destination, avoiding the inefficiency of a hub (which floods data to every port).
- **Tethering/Hotspot**: When a laptop only has Wi-Fi/Ethernet but no cellular connection, enabling a smartphone's hotspot lets the laptop connect to the internet via the phone's 3G/4G data.
- **Print queue**: When all print jobs fail on a shared network printer, the *first* thing to check is the print queue — a stuck or errored job at the front can block everything behind it. IP address, user permissions, and hardware (fuser) issues are lower-priority checks because they usually show other symptoms first (e.g., other users unaffected, physical error messages, noise).

## Hardware

- **Thermal compound**: Fills microscopic gaps between the CPU surface and heatsink, acting as the first medium that conducts heat away from the processor.
- **KVM switch** (Keyboard, Video, Mouse): Lets an admin control multiple servers with a single keyboard/mouse/monitor set, switching between them via a button or hotkey.
- **Hardware print server**: Unlike a printer shared through a specific computer (which must stay powered on), a dedicated hardware print server is always available on the network regardless of any single computer's power state.

## Virtualization

- **Virtual machine (VM) security**: A VM is a fully independent, self-contained ("standalone") environment running its own OS — it needs antivirus software installed just like a physical machine.
- **Hypervisor functions**: (1) Allocates physical resources (CPU, RAM, storage) to virtual machines, and (2) manages the VM lifecycle (create, start, stop, etc.).

## Wireless Tech

- **IR (Infrared)**: The wireless technology most traditional TV remote controls use — requires line-of-sight (pointing the remote at the TV).
