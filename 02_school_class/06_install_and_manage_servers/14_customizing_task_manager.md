# Lab 14: Customizing the Task Manager — Study Notes

## Overview

This lab covers the fundamentals of monitoring and customizing the **Windows 10 Task Manager**.  
Task Manager is a built-in system utility that allows administrators and users to monitor system performance, manage running processes, and diagnose resource issues in real time.

---

## Lab Environment

| Virtual Machine       | IP Address    | Account       | Password  |
|-----------------------|---------------|---------------|-----------|
| Windows 10 PC1        | 192.168.1.203 | student       | Train1ng$ |
| Windows 10 PC2        | 192.168.1.202 | student       | Train1ng$ |
| Windows Server 2012 R2| 192.168.1.200 | Administrator | Train1ng$ |

**Network:** 192.168.1.0/24

---

## How to Open Task Manager

- **Right-click** the Start Menu → Select **Task Manager**
- Alternatively: `Ctrl + Shift + Esc`

> If a black screen with date/time appears on login, click anywhere to bring up the login prompt.

---

## 1. Services Tab

The **Services** tab displays all Windows services and their current state.

### Key Columns
| Column      | Description                                      |
|-------------|--------------------------------------------------|
| Name        | Service name                                     |
| PID         | Process ID (only assigned to Running services)   |
| Description | Brief description of the service                 |
| Status      | Current state of the service                     |
| Group       | Service group it belongs to                      |

### Status Values
- **Running** — The service is currently active and consuming system resources
- **Stopped** — The service is inactive; no PID is assigned

### Key Finding (Q1 & Q2)
- Only **Running** services are assigned a **PID**
- **Stopped** services have no PID
- Example running services with PIDs observed in this lab:
  - `WSearch` — PID 2584
  - `wmiApSrv` — PID 3488
  - `Spooler` — PID 1040
  - `QEMU-GA` — PID 1516

---

## 2. Performance Tab

The **Performance** tab provides real-time graphs and statistics for system resources.

### CPU
- Displays a live **% Utilization** graph
- Shows: Utilization, Speed, Processes, Threads, Handles, Up time

#### Lab Results (Q3)
| Metric    | Value  |
|-----------|--------|
| Processes | 39     |
| Threads   | 668    |
| Handles   | 16,287 |
| Speed     | 2.29 GHz |
| Utilization | 1%  |

---

### Memory
- Displays memory usage over time
- Shows: In use, Available, Committed, Cached, Paged pool, Non-paged pool

#### Lab Results (Q4)
| Metric              | Value   |
|---------------------|---------|
| Physical memory in use | 556 MB |
| Total installed memory | 2.0 GB |
| Memory utilization  | 30%     |

---

### Disk 0 (C: X:)
- Displays **Active time** and **Disk transfer rate** graphs
- Shows: Capacity, Formatted size, Read/Write speed

#### Lab Results (Q5)
| Metric             | Value   |
|--------------------|---------|
| Total capacity     | 50.0 GB |
| Formatted          | 47.3 GB |
| Active time        | 0%      |
| Average response   | 0 ms    |

---

### Ethernet
- Displays network **Throughput** graph
- Shows: IPv4 address, IPv6 address, Adapter name, Connection type

#### Lab Results (Q6)
| Metric       | Value                          |
|--------------|--------------------------------|
| IPv4 Address | 192.168.0.203                  |
| IPv6 Address | fe80::8962:5c6e:3e30:9b23%3   |
| Send/Receive | 0 Kbps (idle)                  |

---

## 3. App History Tab

The **App History** tab shows cumulative resource usage per app since a specific date, for the current user account.

### Key Columns
- **CPU time** — Total CPU time consumed by the app
- **Network** — Total network data used
- **Metered network** — Data used on metered connections
- **Tile updates** — Resources used by live tile updates

### How to Sort
- Click any column header to sort by that metric
- Click again to reverse sort order

#### Lab Results (Q7)
| App     | CPU Time |
|---------|----------|
| Cortana | 0:00:01  |
| Others  | 0:00:00  |

> **Cortana** had the highest CPU time usage among all listed apps.

---

## 4. Processes Tab

The **Processes** tab shows all currently running apps and background processes with real-time resource metrics.

### Key Columns
| Column  | Description                          |
|---------|--------------------------------------|
| Name    | Process/app name                     |
| Status  | Running state                        |
| CPU     | Current CPU usage %                  |
| Memory  | Current RAM usage (MB or %)          |
| Disk    | Current disk I/O                     |
| Network | Current network usage                |

### Sorting by Memory
- Click the **Memory** column header to sort by RAM usage (highest first)

#### Lab Results — Before Opening Edge (Q8)
| Process  | Memory  |
|----------|---------|
| Cortana  | 28.6 MB |
| Service Host: Local System | 21.4 MB |
| Desktop Window Manager | 13.9 MB |

- **Overall memory utilization:** 29%

---

## 5. Viewing Application Impact on Memory

### Steps
1. Launch **Microsoft Edge** from the taskbar
2. Switch back to Task Manager
3. Observe the change in memory utilization

#### Lab Results (Q9)
- Memory usage increased from **29% → 33%** after opening Edge

### Switching Memory Display to Percentages
- Right-click on the **Microsoft Edge** process
- Select: `Resource Values > Memory > Percents`

#### Lab Results (Q10)
| Process        | Memory % |
|----------------|----------|
| Cortana        | 4.6%     |
| Microsoft Edge | 1.7%     |

---

## Key Takeaways

- **Task Manager** is essential for real-time system monitoring and troubleshooting
- **Services tab**: Only *Running* services have PIDs assigned
- **Performance tab**: Provides granular breakdown of CPU, RAM, Disk, and Network usage
- **App History tab**: Tracks cumulative resource usage per app over time
- **Processes tab**: Allows sorting by resource type to quickly identify resource-heavy processes
- Opening a new application (e.g., Edge) **directly increases memory utilization**, which is observable in real time through Task Manager
- Switching the memory view to **Percentages** gives a clearer relative picture of per-process memory consumption

---

*Windows 10 Administration Lab Series — Lab 14*  
*NDG / CSSIA | Holmesglen Institute*
