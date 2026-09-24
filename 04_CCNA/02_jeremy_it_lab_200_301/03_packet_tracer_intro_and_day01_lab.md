# Cisco Packet Tracer Introduction and Day 1 Lab

> **Course:** Jeremy's IT Lab - Free CCNA 200-301 Complete Course
> **Topic:** What labs are, installing and configuring Cisco Packet Tracer, and rebuilding the Day 1 topology
> **Source:** https://youtu.be/a1Im6GYaSno
> **Note:** Lab video that accompanies Day 01 (Network Devices)

---

## 1. What Are Labs and Packet Tracer?

### Lab

- A **lab** is **hands-on practice** with the technology you are studying.
- In the CCNA, that means **configuring Cisco routers and switches** yourself.

### Lab environment options

| Option | Notes |
|--------|-------|
| **Buy real hardware** | Expensive and inconvenient |
| **Cisco Packet Tracer** (Jeremy's choice) | **Free** program that simulates networks on your computer. Fast and easy for building virtual networks |

---

## 2. Downloading and Installing Packet Tracer

- **Where to get it:** the Google Drive link in the video description (the same one that has the flashcards), or `jitl.jp/packet-tracer`.
- **Prerequisite:** a **Cisco account** is required to download. If you do not have one, create it from the bottom of the login page.
- **Supported platforms:** Windows (64-bit and 32-bit), Ubuntu, macOS.
- **Version warning:**
  - Use the **latest version** (8.2 at the time of recording).
  - An older version may **not be able to open lab files** created in a newer version.

---

## 3. Interface and Preferences

### Preferences menu

**Options -> Preferences**

| Tab | What you can change |
|-----|---------------------|
| **Interface** | Show or hide device **model labels** (e.g. 2911 router) |
| **Font** | Font size and color for menus and the **CLI** (e.g. green text on a black background for a "hacker" look) |

### CLI (Command Line Interface)

- The text-based interface where you will **configure routers and switches** in later labs.

---

## 4. Day 1 Lab: Rebuilding the Network Topology

### Using the provided file

- Open the **`day1 lab`** file (from the course files) in Packet Tracer.
- It comes with a **starting setup** (such as the internet router already placed).
- The goal is to **rebuild the topology from the Day 1 video**.

### Devices used

| Type | Model | Where |
|------|-------|-------|
| **Routers** | Cisco **2911** | Internet, New York office, Tokyo office |
| **Switches** | Cisco **2960** | One per office |
| **Firewalls** | Cisco **ASA 5505** | Placed **between the router and the switch** |
| **End devices** | PC x2 | New York |
| | Server x2 | Tokyo |
| | Laptop x1 | The attacker |

### Topology idea

```
 New York office                                  Tokyo office

 [PC1]--\                                         /--[Server1]
 [PC2]----[Switch]--[Firewall]--[Router]==(Internet Router)==[Router]--[Firewall]--[Switch]----[Server2]
                                     |
                                [Attacker laptop]
```

> The diagram is a simplified sketch of the devices listed in the video. Follow the Day 1 video for exact connections.

### Connection shortcut

- Use the **lightning-bolt icon** (**Automatically Choose Connection Type**) to connect devices.
- **Hold `Ctrl` and click the lightning-bolt icon** to keep it selected, so you can connect many cables in a row without re-clicking the icon each time.

---

## 5. Recommended Study Approach

1. **Watch the lecture video, then try to finish the lab yourself** in Packet Tracer first.
2. If you get stuck, it is fine to **watch Jeremy's lab walkthrough video** first.

> **Goal:** reading something 100 times is not as valuable as **actually working with routers and switches**. Hands-on practice builds deeper understanding and prepares you for the exam.

---

## 6. Quick Summary

- **Lab** = hands-on configuration practice with Cisco devices.
- **Packet Tracer** = free simulator; requires a **Cisco account**; use the **latest version**.
- Customize **Options -> Preferences** (model labels, CLI font and colors).
- Day 1 lab devices: **2911 routers, 2960 switches, ASA 5505 firewalls**, plus PCs, servers, and an attacker laptop.
- **Ctrl + lightning-bolt icon** = connect cables repeatedly without re-selecting the tool.
- Try the lab **on your own first**, and use the walkthrough if you get stuck.

---

## 7. My Study Log

- [x] Watched the video
- [ ] Installed Packet Tracer (latest version)
- [ ] Opened the `day1 lab` file
- [ ] Rebuilt the Day 1 topology
- [ ] Watched the lab walkthrough (if needed)

### Notes / Confusing Points

- (add your own notes here)
