# DDoS (Distributed Denial of Service)

## What is DDoS?

DDoS stands for **Distributed Denial of Service**.

It is a cyber attack that tries to make a website, server, or network unavailable to normal users by sending a very large amount of traffic, requests, or data at the same time.

- **Denial of Service (DoS)** means blocking normal service.
- **Distributed** means the attack comes from many devices, not just one.

In simple words, a DDoS attack is like **too many fake customers rushing into a shop at once**, so real customers cannot enter or get service.

---

## Difference Between DoS and DDoS

### DoS
A **DoS attack** usually comes from **one device** or one source.

### DDoS
A **DDoS attack** comes from **many devices at the same time**.

Because many devices are involved, DDoS attacks are:

- harder to stop
- harder to trace
- more powerful than a normal DoS attack

---

## How a DDoS Attack Works

A DDoS attack usually works in the following way:

1. The attacker infects many devices with malware.
2. These infected devices become part of a **botnet**.
3. The attacker sends commands to the botnet.
4. All infected devices send traffic or requests to the target at the same time.
5. The target becomes slow, overloaded, or completely unavailable.

---

## What is a Botnet?

A **botnet** is a group of infected computers or devices that are controlled by an attacker.

These devices may include:

- computers
- phones
- servers
- IoT devices such as cameras or routers

The owner of the infected device often does not know that their device is being used in an attack.

---

## Main Goal of a DDoS Attack

The main goal of a DDoS attack is to **disrupt normal service**.

Attackers may do this to:

- take down a website
- cause financial loss
- damage a company’s reputation
- distract security teams while another attack happens
- demand ransom money
- make a political or social statement

---

## Common Types of DDoS Attacks

DDoS attacks can happen in different ways.  
Some attacks focus on traffic volume, while others focus on exhausting system resources.

### 1. Volumetric Attack
This type of attack sends a huge amount of traffic to use up the target’s bandwidth.

Example:
- UDP flood

The main goal is to fill the network connection with useless traffic.

---

### 2. Protocol Attack
This type of attack abuses network protocols and tries to exhaust server or firewall resources.

Examples:
- SYN flood
- Ping of Death
- Smurf attack

The main goal is to overwhelm networking equipment or connection tables.

---

### 3. Application Layer Attack
This type of attack targets the application itself, such as a website or web server.

Examples:
- HTTP flood
- repeated login requests
- repeated search requests

These attacks may use less traffic, but they are still dangerous because they target functions that require more processing power.

---

## Common DDoS Examples

### UDP Flood
The attacker sends a large number of UDP packets to random ports on the target.
The target tries to process each packet and becomes overloaded.

### SYN Flood
The attacker sends many TCP connection requests but does not complete the connection process.
This leaves many half-open connections and uses up server resources.

### HTTP Flood
The attacker sends many HTTP requests to a website.
The web server becomes too busy responding to fake requests and cannot serve real users.

### DNS Amplification
The attacker sends small DNS requests with a spoofed source IP address.
The DNS server sends much larger responses to the victim.
This makes the attack stronger through **amplification**.

---

## What is Amplification?

**Amplification** means making the attack traffic much bigger than the original request.

For example:

- attacker sends a small request
- the server sends back a much larger response
- the victim receives a huge amount of traffic

This helps attackers create powerful DDoS attacks with less effort.

---

## What is Spoofing in DDoS?

**Spoofing** means faking the source IP address.

In some DDoS attacks, the attacker changes the source IP so that:
- the response goes to the victim
- the attacker hides their real identity

Spoofing is often used in reflection and amplification attacks.

---

## Reflection Attack

A **reflection attack** happens when the attacker sends requests to a third-party server, but uses the victim’s IP address as the source.

As a result:
- the third-party server replies to the victim
- the victim receives large amounts of unexpected traffic

Common services used in reflection attacks include:
- DNS
- NTP
- SSDP

---

## Signs of a DDoS Attack

A system may be under DDoS attack if:

- the website becomes very slow
- users cannot access the service
- the server crashes or stops responding
- network traffic suddenly increases
- there are too many requests from many IP addresses
- unusual traffic patterns appear

---

## Impact of DDoS Attacks

DDoS attacks can cause serious problems such as:

- service downtime
- business interruption
- loss of customer trust
- financial damage
- extra recovery cost
- reduced productivity
- possible distraction from other cyber attacks

For example, if an online shopping site goes down during busy hours, the company may lose many sales.

---

## Why DDoS is Dangerous

DDoS is dangerous because it does not always need to hack into the system directly.
Instead, it attacks the availability of the service.

This relates to the **CIA Triad**:

- **Confidentiality** = keeping data secret
- **Integrity** = keeping data accurate
- **Availability** = keeping systems and services accessible

DDoS mainly attacks **Availability**.

---

## How to Reduce DDoS Risk

Some common protection methods include:

- using firewalls and intrusion prevention systems
- rate limiting
- load balancing
- content delivery networks (CDN)
- DDoS protection services
- traffic filtering
- blackhole routing in severe cases
- monitoring traffic patterns
- keeping systems updated

Organizations should also prepare an incident response plan in case a DDoS attack happens.

---

## Simple Real-Life Analogy

Imagine a restaurant with 20 seats.

If 500 fake customers suddenly enter or block the entrance:
- real customers cannot come in
- staff become overwhelmed
- service stops working properly

That is similar to a DDoS attack.

The problem is not always that the restaurant is broken.  
The problem is that it is overloaded by too many fake requests.

---

## Key Terms

### DDoS
Distributed Denial of Service

### DoS
Denial of Service

### Botnet
A group of infected devices controlled by an attacker

### Spoofing
Faking the source IP address

### Amplification
Making the response much bigger than the request

### Reflection
Sending requests to another server so the reply goes to the victim

### Availability
Making sure services are accessible when needed

---

## Short Summary

DDoS is a cyber attack that uses many devices to overload a target such as a website, server, or network.  
Its main purpose is to stop normal service and make the target unavailable to real users.  
Common forms include UDP flood, SYN flood, HTTP flood, and amplification attacks.  
DDoS mainly affects **availability**, which is one of the three parts of the CIA Triad.

---

## One-Line Memory Tip

**DDoS = many devices sending too much traffic to make a service unavailable.**
