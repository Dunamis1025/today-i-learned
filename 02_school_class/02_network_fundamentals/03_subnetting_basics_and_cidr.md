# 🌐 Subnetting Basics and CIDR

## 1. What is an IP address?

An IPv4 address is divided into two parts:

- **Network portion** → identifies the network
- **Host portion** → identifies a device inside that network

Example:
- `192.168.1.10/24`

In this example:
- `192.168.1` = network portion
- `10` = host portion

---

## 2. Prefix Length

The number after the slash is called the **prefix length**.

Examples:
- `/8` → first 8 bits are network bits
- `/16` → first 16 bits are network bits
- `/24` → first 24 bits are network bits

This tells us how much of the address belongs to the network and how much belongs to the host.

---

## 3. Classful Addressing

Traditional IPv4 classes:

| Class | First Octet Range | Default Prefix |
|------|-------------------|----------------|
| A | 1–126 | /8 |
| B | 128–191 | /16 |
| C | 192–223 | /24 |

Examples:
- `43.109.23.12/8` → Class A
- `129.221.23.13/16` → Class B
- `209.211.3.22/24` → Class C

---

## 4. Subnet Mask

A subnet mask shows which part is network and which part is host.

- **1** = network bit
- **0** = host bit

Examples:

| CIDR | Subnet Mask |
|------|-------------|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |
| /27 | 255.255.255.224 |
| /28 | 255.255.255.240 |
| /29 | 255.255.255.248 |
| /30 | 255.255.255.252 |
| /31 | 255.255.255.254 |
| /32 | 255.255.255.255 |

---

## 5. Network Address and Broadcast Address

### Network Address
The **network address** is found by turning all **host bits to 0**.

### Broadcast Address
The **broadcast address** is found by turning all **host bits to 1**.

### Usable Host Range
- **First usable address** = network address + 1
- **Last usable address** = broadcast address - 1

---

## 6. Maximum Number of Hosts

Formula:

`2^n - 2`

Where:
- `n` = number of host bits
- `-2` = subtract network address and broadcast address

Examples:
- `/24` → 8 host bits → `2^8 - 2 = 254`
- `/16` → 16 host bits → `2^16 - 2 = 65,534`
- `/8` → 24 host bits → `2^24 - 2 = 16,777,214`

---

## 7. Example Questions

### PC1: 43.109.23.12 /8
- Class: A
- Network Address: `43.0.0.0`
- Broadcast Address: `43.255.255.255`
- Host bits: 24
- Usable Hosts: `2^24 - 2 = 16,777,214`
- First Usable: `43.0.0.1`
- Last Usable: `43.255.255.254`

### PC2: 129.221.23.13 /16
- Class: B
- Network Address: `129.221.0.0`
- Broadcast Address: `129.221.255.255`
- Host bits: 16
- Usable Hosts: `2^16 - 2 = 65,534`
- First Usable: `129.221.0.1`
- Last Usable: `129.221.255.254`

### PC3: 209.211.3.22 /24
- Class: C
- Network Address: `209.211.3.0`
- Broadcast Address: `209.211.3.255`
- Host bits: 8
- Usable Hosts: `2^8 - 2 = 254`
- First Usable: `209.211.3.1`
- Last Usable: `209.211.3.254`

### PC4: 2.71.209.233 /8
- Class: A
- Network Address: `2.0.0.0`
- Broadcast Address: `2.255.255.255`
- Host bits: 24
- Usable Hosts: `2^24 - 2 = 16,777,214`
- First Usable: `2.0.0.1`
- Last Usable: `2.255.255.254`

### PC5: 155.200.201.141 /16
- Class: B
- Network Address: `155.200.0.0`
- Broadcast Address: `155.200.255.255`
- Host bits: 16
- Usable Hosts: `2^16 - 2 = 65,534`
- First Usable: `155.200.0.1`
- Last Usable: `155.200.255.254`

---

## 8. What is Subnetting?

Subnetting means dividing one large network into smaller networks.

To do subnetting:
- borrow bits from the host portion
- add them to the network portion
- create smaller subnets

This is why subnetting is often explained as:

**“stealing bits from the host portion.”**

---

## 9. CIDR and Block Size

Common CIDR patterns:

| CIDR | Mask | Block Size |
|------|------|------------|
| /25 | 255.255.255.128 | 128 |
| /26 | 255.255.255.192 | 64 |
| /27 | 255.255.255.224 | 32 |
| /28 | 255.255.255.240 | 16 |
| /29 | 255.255.255.248 | 8 |
| /30 | 255.255.255.252 | 4 |
| /31 | 255.255.255.254 | 2 |

### Quick pattern
Subnet numbers increase by the **block size**.

For example:
- `/26` → block size = 64
- subnets = `0, 64, 128, 192`

---

## 10. /31 Special Case

Normally:

- `/31` → 1 host bit
- `2^1 - 2 = 0 usable hosts`

But in a **point-to-point link** between two routers, `/31` can still be used because broadcast is not needed in the same way.

---

## 11. Worked Example: Divide 192.168.1.0/24 into 4 subnets

### Requirement
- Network: `192.168.1.0/24`
- Need: **4 subnets**
- Each subnet must support **45 hosts**

### Step 1: Check host requirement
- `2^5 = 32` → not enough
- `2^6 = 64` → enough

So:
- host bits = 6
- new prefix = `32 - 6 = /26`

### Step 2: New subnet mask
- `/26` = `255.255.255.192`

### Step 3: Block size
- `256 - 192 = 64`

So the subnet ranges are:
- `0`
- `64`
- `128`
- `192`

### Final Answer

#### First Subnet
- Network Address: `192.168.1.0`
- Maximum Hosts: `62`
- Broadcast Address: `192.168.1.63`
- First Usable Address: `192.168.1.1`
- Last Usable Address: `192.168.1.62`

#### Second Subnet
- Network Address: `192.168.1.64`
- Maximum Hosts: `62`
- Broadcast Address: `192.168.1.127`
- First Usable Address: `192.168.1.65`
- Last Usable Address: `192.168.1.126`

#### Third Subnet
- Network Address: `192.168.1.128`
- Maximum Hosts: `62`
- Broadcast Address: `192.168.1.191`
- First Usable Address: `192.168.1.129`
- Last Usable Address: `192.168.1.190`

#### Fourth Subnet
- Network Address: `192.168.1.192`
- Maximum Hosts: `62`
- Broadcast Address: `192.168.1.255`
- First Usable Address: `192.168.1.193`
- Last Usable Address: `192.168.1.254`

---

## 12. Core Problem-Solving Process

When solving subnetting problems:

1. Identify the prefix
2. Find the number of host bits
3. Calculate usable hosts with `2^n - 2`
4. Turn host bits to 0 for the network address
5. Turn host bits to 1 for the broadcast address
6. Use block size to find the next subnet
7. Find first and last usable addresses

---

# 🇰🇷 한국어 요약

## 1. IP 주소 구조
IPv4 주소는 두 부분으로 나뉜다.

- **네트워크 부분** → 어떤 네트워크인지 식별
- **호스트 부분** → 그 네트워크 안의 장치 번호

예:
- `192.168.1.10/24`
- `192.168.1` = 네트워크
- `10` = 호스트

---

## 2. Prefix Length
슬래시 뒤 숫자는 **프리픽스 길이**이다.

- `/8` → 앞 8비트가 네트워크
- `/16` → 앞 16비트가 네트워크
- `/24` → 앞 24비트가 네트워크

---

## 3. 기본 클래스
전통적인 클래스 구분:

- Class A → 1~126 → /8
- Class B → 128~191 → /16
- Class C → 192~223 → /24

---

## 4. 서브넷 마스크
서브넷 마스크는 네트워크와 호스트를 구분한다.

- 1 = 네트워크
- 0 = 호스트

예:
- /24 = 255.255.255.0
- /25 = 255.255.255.128
- /26 = 255.255.255.192

---

## 5. 네트워크 주소와 브로드캐스트 주소
- **Network Address** = host 비트를 전부 0으로
- **Broadcast Address** = host 비트를 전부 1로
- **First Usable** = network + 1
- **Last Usable** = broadcast - 1

---

## 6. 사용 가능한 호스트 수
공식:

`2^n - 2`

- n = host 비트 수
- -2 = network 주소와 broadcast 주소 제외

예:
- /24 → 254개
- /16 → 65,534개
- /8 → 16,777,214개

---

## 7. 서브네팅
서브네팅은 하나의 큰 네트워크를 여러 개의 작은 네트워크로 나누는 것이다.

방법:
- host 부분에서 비트를 빌려와
- network 부분에 추가한다

즉, **host bit를 borrowed bits로 바꾸는 과정**이다.

---

## 8. CIDR와 블록 사이즈
자주 나오는 패턴:

- /25 → 128
- /26 → 64
- /27 → 32
- /28 → 16
- /29 → 8
- /30 → 4

블록 사이즈만 알면 subnet 증가값을 빠르게 찾을 수 있다.

---

## 9. /31 특수 케이스
원래 /31은 usable host가 0개지만,
라우터와 라우터를 연결하는 point-to-point 링크에서는 예외적으로 사용할 수 있다.

---

## 10. 실전 예제
`192.168.1.0/24`를 4개의 subnet으로 나누고, 각 subnet은 45 hosts를 지원해야 한다.

풀이:
- 45 hosts 필요
- 2^5 = 32 → 부족
- 2^6 = 64 → 가능
- host bits = 6
- 새 prefix = /26
- subnet mask = 255.255.255.192
- block size = 64

결과:
- 192.168.1.0/26
- 192.168.1.64/26
- 192.168.1.128/26
- 192.168.1.192/26

각 subnet은 usable host 62개를 가진다.

---

## 11. 문제 푸는 순서
1. prefix 확인
2. host bits 계산
3. usable hosts 계산
4. network address 찾기
5. broadcast address 찾기
6. block size로 다음 subnet 찾기
7. first / last usable address 찾기
