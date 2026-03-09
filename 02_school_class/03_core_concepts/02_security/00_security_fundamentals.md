# Security Fundamentals

## Introduction

Security fundamentals are the basic concepts that help us understand how cyber attacks happen, how systems are protected, and how security teams respond to threats.

When studying cyber security, it is important to understand not only attack tools, but also protocols, services, vulnerabilities, and monitoring methods. Many topics in cyber security are connected in one flow:

Network scanning -> Service detection -> Vulnerability discovery -> Exploitation -> Monitoring and analysis

This document explains the core concepts in a simple and beginner-friendly way.

---

## 1. What is a vulnerability?

A vulnerability is a weakness in a system, application, service, or configuration that can be abused by an attacker.

Examples:
- An old web server version with a known bug
- A weak password
- An open service that should not be exposed
- Software that has not been patched

A vulnerability does not always mean the system is already hacked, but it means there is a risk that an attacker can use it.

---

## 2. What is CVE?

CVE stands for **Common Vulnerabilities and Exposures**.

A CVE is a public identifier used to name a known security vulnerability. It gives security researchers and organisations a common reference.

Format:
- CVE-Year-Number

Example:
- CVE-2021-44228

This helps everyone talk about the same vulnerability clearly.

---

## 3. What is Log4j and Log4Shell?

Log4j is a Java logging library. It helps applications record events such as:
- user login
- system errors
- requests
- warnings

A major vulnerability was found in Log4j in 2021:

- **CVE-2021-44228**
- Also known as **Log4Shell**

This vulnerability allowed remote code execution in some cases. It became very famous because Log4j was used in many systems around the world.

---

## 4. What is a protocol?

A protocol is a set of rules that devices use to communicate over a network.

Examples:
- HTTP for websites
- HTTPS for secure websites
- SSH for secure remote login
- SMB for file sharing
- ICMP for network checking

Protocols are important because many cyber attacks target services that use these protocols.

---

## 5. What is SSH?

SSH stands for **Secure Shell**.

SSH is a protocol used to securely connect to another computer over a network. It is commonly used by administrators to manage Linux servers and network devices remotely.

Example:
- Logging into a remote server
- Running commands on another machine
- Managing files securely

SSH is encrypted, which makes it much safer than older remote login methods.

---

## 6. What is Telnet, and how is it different from SSH?

Telnet is an older remote access protocol.

It was used to connect to another device through a command line, but it does **not encrypt** traffic. This means usernames and passwords could be exposed if someone captured the traffic.

SSH replaced Telnet in most environments because SSH encrypts communication.

Difference:
- Telnet = remote access without encryption
- SSH = remote access with encryption

---

## 7. What is OpenSSH?

SSH is the protocol.

OpenSSH is a software implementation of SSH. It is one of the most common SSH tools used on Linux and Unix-like systems.

If you scan a machine and see something like:
- OpenSSH 7.4

it means the target system is running the OpenSSH software.

---

## 8. What is Apache?

Apache, also called **Apache HTTP Server**, is a web server.

A web server is software that delivers web pages to users when they visit a website in a browser.

If a server runs Apache, it may host:
- websites
- web applications
- online portals

Apache is one of the most common web servers in the world.

---

## 9. What is SMB?

SMB stands for **Server Message Block**.

It is a protocol mainly used for:
- file sharing
- printer sharing
- accessing shared folders over a network

SMB is very common in Windows environments.

Example:
- shared company folder
- network drive
- printer access in an office

---

## 10. What does "SMB vulnerability" mean?

An SMB vulnerability means there is a security weakness in the SMB service or in the way SMB is implemented.

If a system exposes SMB and has a flaw, an attacker may be able to:
- access files
- move through the network
- execute malicious code
- take control of the system

This is why SMB security is very important.

---

## 11. What is Nmap?

Nmap stands for **Network Mapper**.

Nmap is a network scanning tool used to discover:
- live hosts
- open ports
- running services
- service versions
- sometimes the operating system

Security professionals use Nmap for:
- network discovery
- security assessment
- penetration testing
- troubleshooting

Attackers may also use Nmap for reconnaissance.

Example command:
```bash
nmap 192.168.1.10

12. What does -sV mean in Nmap?

Example:

nmap -sV 192.168.1.10

The option -sV means service version detection.

It tells Nmap to try to identify which services are running and which versions they are using.

Example result:

OpenSSH 7.4

Apache 2.4.41

This is useful because some versions may have known vulnerabilities.

13. What is an exploit?

An exploit is a piece of code, technique, or method used to take advantage of a vulnerability.

If a system has a weakness, an exploit is what an attacker uses to abuse that weakness.

In simple words:

vulnerability = weakness

exploit = attack method

14. What is exploitation?

Exploitation is the stage where the attacker actively uses a vulnerability to attack a target.

This can include:

gaining access

running malicious code

stealing information

crashing a system

Typical attack flow:

Reconnaissance

Scanning

Vulnerability discovery

Exploitation

15. What is penetration testing?

Penetration testing, often called pentesting, is an authorised security test where a security professional attempts to attack a system in order to find weaknesses.

The purpose is defensive:

find vulnerabilities

assess security controls

improve protection

A penetration tester acts like an attacker, but with permission.

16. What is Metasploit?

Metasploit is a penetration testing and exploitation framework.

It contains many modules that help security professionals:

test vulnerabilities

run exploits

verify weaknesses

study attack behaviour in lab environments

It is widely used in cyber security training and authorised testing.

A module path may look like this:

exploit/windows/smb/ms17_010

This means:

exploit = attack module

windows = target operating system

smb = target service/protocol

ms17_010 = related vulnerability

17. What is MS17-010?

MS17-010 is a Microsoft security bulletin identifier for a serious SMB-related vulnerability in Windows.

It became very famous because it was connected to major cyber attacks.

This vulnerability affected SMB and allowed attackers to exploit unpatched Windows systems.

18. What is EternalBlue?

EternalBlue is a well-known exploit that targeted the SMB vulnerability related to MS17-010.

It became widely known because it was used in large-scale cyber attacks such as WannaCry.

Why it matters:

It spread quickly

It affected many organisations

It showed how dangerous unpatched systems can be

19. What is NSA?

NSA stands for National Security Agency.

It is a United States government agency related to intelligence and security.

In cyber security discussions, the NSA is often mentioned because some cyber tools and exploits were reportedly linked to it before being leaked publicly.

20. What is ICMP?

ICMP stands for Internet Control Message Protocol.

It is used for network communication related to status and diagnostics.

It is commonly used to check whether a device is reachable.

21. What is ping?

Ping is a network command that uses ICMP to test connectivity between devices.

Example:

ping 8.8.8.8

This sends ICMP echo requests to the target.

If replies come back, it means:

the target is reachable

the network path is working

8.8.8.8 is a well-known Google DNS server, so many people use it for quick network testing.

22. What is Wireshark?

Wireshark is a packet analysis tool.

It captures and displays network traffic so users can inspect packets and understand what is happening on the network.

Wireshark can show:

DNS traffic

HTTP traffic

HTTPS traffic

TCP connections

ICMP ping packets

It is useful for:

troubleshooting

protocol analysis

incident investigation

learning network behaviour

23. What is SOC?

SOC stands for Security Operations Center.

A SOC is a team or environment responsible for monitoring and responding to cyber security threats.

Typical SOC activities include:

monitoring alerts

reviewing logs

investigating suspicious traffic

responding to incidents

analysing threats

In a lab environment, a SOC lab is a training space where students learn how security monitoring works.

24. What is SOC analysis?

SOC analysis means examining logs, alerts, events, and network behaviour to identify suspicious or malicious activity.

This may include:

checking firewall logs

reviewing alerts in a SIEM

identifying unusual connections

analysing attack patterns

SOC analysis is part of cyber defence.

25. Red Team and Blue Team

In cyber security exercises:

Red Team simulates attackers

Blue Team defends systems

Sometimes Purple Team helps improve cooperation between both sides

Red Team activities:

scanning

exploiting

attacking

Blue Team activities:

monitoring

detecting

responding

26. Basic cyber attack flow

A simple cyber attack flow often looks like this:

Reconnaissance
Gather information about the target

Scanning
Use tools like Nmap to identify ports and services

Service and version detection
Find software and versions

Vulnerability discovery
Search for known weaknesses, such as CVEs

Exploitation
Use an exploit or framework like Metasploit

Post-exploitation
Maintain access or move further inside the environment

Detection and monitoring
Blue Team or SOC detects suspicious behaviour

Packet and log analysis
Wireshark and SOC tools help investigate activity

Conclusion

Security fundamentals connect many different topics together. Protocols, services, vulnerabilities, scanning tools, exploitation frameworks, and monitoring systems all play a role in cyber security.

Understanding these basic concepts helps build a strong foundation for:

network security

penetration testing

SOC analysis

cyber security careers

The more these concepts are studied together, the easier it becomes to understand real-world attack and defence scenarios.
