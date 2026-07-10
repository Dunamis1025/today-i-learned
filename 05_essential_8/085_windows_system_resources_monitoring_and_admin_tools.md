# Windows System Resources & Administrative Tools — Study Notes

## Lab: Monitor and Manage System Resources

### Part 1 — Event Viewer & Windows Defender

**Goal:** Observe how Windows logs a service status change.

**Process:**
- Confirm Windows Defender (Real-time protection) is ON in Windows Security.
- Check the status of the *Windows Defender Antivirus Network Inspection Service* in the Services console.
- Turn Real-time protection OFF, refresh the Services console, and note the status change.
- Open Event Viewer → Windows Logs → Application → search "defender" to find the related log entries and check the Source and Severity level.
- Turn Real-time protection back ON and confirm the corresponding log entry appears.

**Key concept:** Every service state change (start/stop) generates a log entry in Event Viewer, which records the source, severity (Information/Warning/Error), and timestamp. This is the primary tool for auditing what happened on a system and when.

---

### Part 2 — Impact of Stopping Services

**Goal:** See how stopping a service breaks dependent functionality.

**Process:**
- Open Notepad → File → Print → note an available printer (e.g., a virtual printer like "Microsoft Print to PDF" or a real one shown by Windows).
- In Computer Management → Services, stop **Print Spooler**, then try printing again.
  - **Result:** The printer dropdown fails to load (infinite loading, no printers listed) because Print Spooler manages all print job handling and printer communication.
  - **Fix:** Restart the Print Spooler service — printing works normally again.
- Try stopping **DHCP Client** (handles automatic IP address / DNS registration).
  - Windows warns that other dependent services will also stop ("Stop Other Services" dialog).
  - Choosing **No** cancels the stop, keeping DHCP Client running.

**Key concept:** Windows services often have dependencies. Stopping a core service (like Print Spooler or DHCP Client) can silently break unrelated-looking features (printing, network/IP configuration). This is why service management requires caution — one change can cascade into multiple failures, especially for networking-critical services.

---

### Part 3 — Monitoring System Resources (Performance Monitor)

**Goal:** Log real-time memory usage to a file using a Data Collector Set.

**Process:**
1. In Computer Management → System Tools → Performance → Data Collector Sets → User Defined, create a new set named **"Memory Logs"** (manual/advanced mode).
2. Add the performance counter **Memory → Available MBytes**.
3. Set the sample interval to **4 seconds**.
4. Save output to `C:\PerfLogs`.
5. Set the log format to **Comma Separated (CSV)**.
6. Start the collector, open/close a browser to change memory usage, then stop the collector.
7. Open the resulting `DataCollector01.csv` file (via Notepad or Excel).
   - The **rightmost column** shows the actual measured value (Available MBytes) at each timestamp.
8. Clean up: delete the Data Collector Set and the log folder in `C:\PerfLogs`.

**Key concept:** Performance Monitor / Data Collector Sets let you track system metrics (CPU, memory, disk, etc.) over time and export them as CSV for analysis — useful for diagnosing performance issues or capacity planning.

---

## Matching Exercise: Choosing the Right Administrative Tool

| Tool | When to use it |
|---|---|
| **Print Management** | Troubleshooting an unavailable office printer |
| **Component Services** | Checking how a new COM component is configured |
| **Administrative Tools** | Accessing multiple system management utilities from one place |
| **Windows Memory Diagnostics** | Testing for faulty RAM after installing new memory and the PC becomes unstable |
| **Event Viewer** | Investigating which app/service is causing frequent system freezes/crashes |

---

## Core Windows System Tools

### System Information (`msinfo32`)
Shows a full overview of hardware, software, and driver details. Useful for diagnosing problems by checking installed components and software versions.

### System Configuration (`msconfig`)
Used to troubleshoot startup issues. Lets you selectively enable/disable startup services and programs to identify what's preventing Windows from booting normally.

### The Registry
A large hierarchical database storing configuration settings for Windows and installed programs — updated automatically whenever settings change (e.g., changing wallpaper, installing software). Main root keys:

- **HKEY_LOCAL_MACHINE** — machine-wide hardware and security settings
- **HKEY_CURRENT_USER** — settings for the currently logged-in user
- **HKEY_CLASSES_ROOT** — file type associations and program links
- **HKEY_USERS** — settings for all users on the machine
- **HKEY_CURRENT_CONFIG** — current hardware profile/configuration state

### Registry Editor (`regedit`)
The tool used to directly view and edit Registry values. Extremely sensitive — incorrect changes can break hardware, software, or the entire OS, so it must be used with great care.

---

## Big-Picture Takeaways
- Windows services are interdependent; stopping one can silently disable unrelated features (printing, networking).
- Event Viewer is the central place to audit service/state changes and diagnose recurring issues.
- Performance Monitor / Data Collector Sets provide quantitative, time-stamped resource usage data (CPU, memory, etc.) for deeper diagnostics.
- `msinfo32`, `msconfig`, and `regedit` are core low-level diagnostic/configuration tools — regedit in particular should be used cautiously since it directly modifies core OS settings.
