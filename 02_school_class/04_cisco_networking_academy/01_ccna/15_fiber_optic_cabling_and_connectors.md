# 12. Fiber-Optic Cabling, Connectors, and Fiber vs Copper

---

## Overview

These notes summarize the core concepts of fiber-optic cabling, including:

- Single-mode fiber (SMF)
- Multimode fiber (MMF)
- Dispersion
- Real-world fiber usage
- Fiber-optic connectors
- Duplex communication in fiber
- Fiber patch cord colors
- Basic fiber safety
- Fiber vs UTP comparison
- Quiz-style review points

Fiber-optic cabling is important in networking because it supports high speed, long distance, and strong resistance to electrical interference.

---

## 1. Single-Mode Fiber (SMF)

### Definition
Single-mode fiber (SMF) is a type of optical fiber with a very small core.

### Characteristics
- Uses **expensive laser technology**
- Sends **a single ray / single stream of light**
- Designed for **long-distance transmission**
- Popular in:
  - Long-haul telephony
  - Cable TV applications
  - Long-distance provider networks

### Distance
- Can span **hundreds of kilometers**
- Suitable for **very long-distance communication**

### Key Idea
Because SMF carries light in a single path, it has less dispersion and lower signal loss over long distances.

### Simple Memory Tip
- **Laser = Single-mode**
- **Long distance = Single-mode**

---

## 2. Multimode Fiber (MMF)

### Definition
Multimode fiber (MMF) is a type of optical fiber with a larger core than SMF.

### Characteristics
- Uses **LED emitters**
- Sends light pulses at **different angles**
- Popular in:
  - LANs
  - Campus networks
  - Shorter-distance enterprise connections

### Bandwidth / Distance
- Can provide bandwidth up to **10 Gbps**
- Supports link lengths up to about **550 meters**
- Often simplified in quiz questions as about **500 meters**

### Key Idea
Because light enters at multiple angles, the signal spreads more over time than in SMF.

### Simple Memory Tip
- **LED = Multimode**
- **Short distance / campus / LAN = Multimode**

---

## 3. Dispersion

### Definition
Dispersion means the **spreading out of a light pulse over time**.

### Why It Matters
If light spreads too much:
- Signal strength becomes weaker
- Signal quality drops
- Maximum transmission distance becomes shorter

### MMF vs SMF
- **MMF has greater dispersion**
- **SMF has less dispersion**

### Result
Because MMF has more dispersion, it can usually travel only up to about **500 meters** before significant signal loss.

### Easy Explanation
Think of it like this:
- If light stays tight and straight, it can travel far
- If light spreads out in many directions, it weakens faster

That is why:
- **SMF = farther**
- **MMF = shorter**

---

## 4. Fiber-Optic Cabling Usage

Fiber-optic cabling is used in four major areas:

### 4.1 Enterprise Networks
Used for:
- Backbone cabling
- Interconnecting infrastructure devices

### 4.2 Fiber-to-the-Home (FTTH)
Used to:
- Deliver always-on broadband internet
- Connect homes and small businesses

### 4.3 Long-Haul Networks
Used by service providers to:
- Connect cities
- Connect countries
- Support long-distance communication infrastructure

### 4.4 Submarine Cable Networks
Used to:
- Provide reliable high-speed, high-capacity communication
- Operate in harsh undersea environments
- Support **transoceanic** distances

### Transoceanic Meaning
**Transoceanic** means:
- Across the ocean
- Passing over or under an ocean
- For example, fiber cables connecting continents through the sea

### Course Focus
In many networking courses, the main focus is using fiber **within the enterprise**.

---

## 5. Fiber-Optic Connectors

### Basic Idea
A fiber-optic connector terminates the end of an optical fiber.

Different connectors exist because equipment may require different:
- Sizes
- Shapes
- Coupling methods

Businesses choose connector types based on their networking equipment.

### SFP Note
Some switches and routers support fiber through an:
- **SFP transceiver**
- SFP = **Small Form-Factor Pluggable**

This allows network devices to use fiber-optic connections through modular ports.

---

## 6. Main Fiber Connector Types

### 6.1 ST Connector
ST connectors were among the earliest connector types used.

#### Features
- Uses a **twist-on / twist-off**
- **Bayonet-style locking mechanism**
- Locks securely in place

#### Memory Tip
- **ST = older style, twist lock**

---

### 6.2 SC Connector
SC connectors are often called:
- **Square connectors**
- **Standard connectors**

#### Features
- Widely used in LAN and WAN environments
- Uses a **push-pull mechanism**
- Supports positive insertion
- Used with both:
  - Multimode fiber
  - Single-mode fiber

#### Memory Tip
- **SC = square / standard / push-pull**

---

### 6.3 LC Simplex Connector
LC simplex is a smaller version of the SC connector.

#### Features
- Smaller size
- Sometimes called:
  - **Little connector**
  - **Local connector**
- Growing in popularity because of its compact size

#### Memory Tip
- **LC = small version of SC**

---

### 6.4 Duplex Multimode LC Connector
A duplex multimode LC connector is similar to an LC simplex connector, but it uses a duplex connector design.

#### Key Idea
- Simplex = one path / one fiber connection
- Duplex = supports paired transmission structure

---

## 7. Duplex Communication in Fiber

### Traditional Limitation
Until recently, light could only travel in **one direction** over a single optical fiber.

### Full Duplex Requirement
To support **full duplex communication**:
- Two fibers were needed
- One fiber for transmitting
- One fiber for receiving

### Patch Cable Structure
Fiber patch cables often:
- Bundle together two optical fibers
- Terminate them with a pair of standard single-fiber connectors

### Duplex Connector
Some connectors can support both:
- Transmit
- Receive

in one duplex connector arrangement.

### BX Standard
BX standards such as **100BASE-BX** allow sending and receiving over a **single fiber** by using:
- Different wavelengths for transmit
- Different wavelengths for receive

### Key Idea
Instead of using two separate fibers, some systems separate traffic by wavelength.

---

## 8. Fiber Patch Cords and Color Codes

Fiber patch cords are used to interconnect infrastructure devices.

### Color Distinction
Patch cord color helps identify the fiber type:

- **Yellow jacket** = Single-mode fiber
- **Orange jacket** = Multimode fiber
- **Aqua jacket** = Multimode fiber

### Memory Tip
- **Yellow = Single-mode**
- **Orange/Aqua = Multimode**

---

## 9. Basic Fiber Safety Note

When fiber cables are not in use:
- They should be protected with a **small plastic cap**

### Why?
This helps protect:
- The connector end
- The fiber surface
- Clean signal transmission quality

---

## 10. Fiber versus Copper

Fiber-optic cabling has many advantages compared with copper cabling.

In enterprise environments, fiber is commonly used for:
- Backbone cabling
- High-traffic point-to-point links
- Interconnection between buildings in multi-building campuses

### Why Fiber Is Good for This
Fiber-optic cables:
- Do **not conduct electricity**
- Have **low signal loss**
- Work well over long distances
- Resist electrical interference

---

## 11. UTP and Fiber-Optic Cabling Comparison

| Implementation Issue | UTP Cabling | Fiber-Optic Cabling |
|---|---|---|
| Bandwidth supported | 10 Mb/s - 10 Gb/s | 10 Mb/s - 100 Gb/s |
| Distance | Relatively short (1 - 100 meters) | Relatively long (1 - 100,000 meters) |
| Immunity to EMI and RFI | Low | High (completely immune) |
| Immunity to electrical hazards | Low | High (completely immune) |
| Media and connector costs | Lowest | Highest |
| Installation skills required | Lowest | Highest |
| Safety precautions | Lowest | Highest |

---

## 12. Key Comparison Summary

### UTP
Advantages:
- Cheaper
- Easier to install
- Lower skill requirement

Disadvantages:
- Shorter distance
- More affected by EMI and RFI
- More affected by electrical hazards
- Lower maximum bandwidth than fiber

### Fiber
Advantages:
- Longer distance
- Higher bandwidth
- Immune to EMI and RFI
- Immune to electrical hazards
- Lower signal loss

Disadvantages:
- Higher cost
- Harder installation
- Requires more skill
- More safety precautions needed

### Simple One-Line Summary
- **UTP = cheaper and easier**
- **Fiber = faster, farther, and safer from interference**

---

## 13. Important Vocabulary

### Telephony
Telephony means:
- Telephone communication
- Technology/system that converts voice into electrical signals and sends it over distance

Example:
- Home phone systems
- Mobile phone systems
- Long-distance voice communication systems

### Dispersion
Dispersion means:
- The spreading out of a light signal over time

### Transoceanic
Transoceanic means:
- Across the ocean
- Ocean-spanning communication

### Backbone Cabling
Backbone cabling means:
- High-capacity central network links that connect major network sections or buildings

---

## 14. Quiz Review Answers

### Question 1
**Which fiber-optic cable type can help data travel approximately 500 meters?**  
**Answer: Multimode**

### Question 2
**Which fiber-optic cable type uses LEDs as a data light source transmitter?**  
**Answer: Multimode**

### Question 3
**Which fiber-optic cable type uses lasers in a single stream as a data light source transmitter?**  
**Answer: Single-mode**

### Question 4
**Which fiber-optic cable type is used to connect long-distance telephony and cable TV applications?**  
**Answer: Single-mode**

### Question 5
**Which fiber-optic cable type can travel approximately 100 km?**  
**Answer: Single-mode**

### Question 6
**Which fiber-optic cable type is used within a campus network?**  
**Answer: Multimode**

---

## 15. Fast Exam Memory Sheet

### Single-Mode Fiber (SMF)
- Small core
- Laser
- Single stream of light
- Less dispersion
- Long distance
- Telephony
- Cable TV
- Long-haul
- Up to hundreds of kilometers
- Yellow patch cord

### Multimode Fiber (MMF)
- Larger core
- LED
- Multiple light angles
- More dispersion
- Shorter distance
- LAN
- Campus
- About 500 to 550 meters
- Orange/Aqua patch cord

### Connectors
- **ST** = twist lock
- **SC** = square / standard / push-pull
- **LC** = small SC
- **Duplex LC** = paired fiber communication

---

## 16. Korean Review Notes (빠른 복습용)

### 싱글모드 광섬유 (SMF)
- 코어가 매우 작다
- 레이저 사용
- 빛이 한 줄기로 간다
- 분산이 적다
- 장거리 전송에 적합하다
- 장거리 전화망, 케이블 TV, 장거리 네트워크에 사용된다
- 수백 km까지 가능하다
- 노란색 패치 코드가 주로 사용된다

### 멀티모드 광섬유 (MMF)
- 코어가 더 크다
- LED 사용
- 빛이 여러 각도로 들어간다
- 분산이 더 크다
- 짧은 거리 전송에 적합하다
- LAN, 캠퍼스, 건물 내부 연결에 사용된다
- 약 500~550m 정도 가능하다
- 주황색 또는 아쿠아색 패치 코드가 사용된다

### 분산 (Dispersion)
- 빛 펄스가 시간이 지나면서 퍼지는 현상
- 분산이 커지면 신호가 약해진다
- MMF가 SMF보다 분산이 더 크다
- 그래서 MMF는 장거리 전송에 불리하다

### 광섬유 사용 분야
- 엔터프라이즈 백본
- FTTH
- 장거리 네트워크
- 해저 케이블 네트워크

### 커넥터
- **ST**: 비틀어 잠그는 방식
- **SC**: 사각형/표준 커넥터, push-pull 방식
- **LC**: SC보다 더 작은 커넥터
- **Duplex LC**: 송수신 쌍 구조 지원

### 광섬유 vs UTP
- 광섬유는 더 빠르고 더 멀리 간다
- EMI/RFI 영향을 받지 않는다
- 전기적 위험에도 강하다
- 하지만 비용이 비싸고 설치가 어렵다

### 시험용 초간단 암기
- **LED = MMF**
- **Laser = SMF**
- **500m = MMF**
- **100km = SMF**
- **Campus = MMF**
- **Long distance = SMF**
- **Yellow = SMF**
- **Orange/Aqua = MMF**

---

## 17. Final Summary

Fiber-optic cabling is a high-performance network medium used for high bandwidth, long distance, and reliable communication. SMF is used for long-distance communication with lasers and low dispersion, while MMF is used for shorter distances with LEDs and a larger core. Fiber connectors such as ST, SC, and LC support different equipment needs. Compared with UTP, fiber provides much better distance, bandwidth, and immunity to interference, but costs more and requires more installation skill.

---
