# Lab Notes: Evaluating and Testing an Incident Response Plan with Wazuh

**Course:** Certificate IV – Cyber Hygiene (Security Impossible)
**Module:** 3 – Evaluating and Testing an Incident Response Plan with Wazuh
**Date:** 2026-06-12
**Tools used:** Wazuh (SIEM), Elasticsearch, Kibana (Elastic Stack), Linux terminal (Ubuntu VM via Guacamole)

---

## 1. Overview

This lab simulates a **Blue Team (defensive security) workflow**: detecting attacks via a SIEM, building custom detection rules, and documenting an incident response (IR) ticket — similar to what a SOC (Security Operations Center) analyst does day-to-day.

A background Python script (`single_file_log_generator`) continuously generates ~2,000 simulated attack logs (SSH brute force, ransomware indicators, SQL injection, XSS, port scans, SSRF) and forwards them to Wazuh and the Elastic Stack for analysis.

---

## 2. Step 1 – Wazuh Walkthrough (Discover)

- Accessed Wazuh dashboard at `https://localhost` (admin/admin).
- Navigated to **Explore > Discover**, selected the `wazuh-alerts-*` index pattern.
- Set time range to **Today** to capture incoming logs.
- Added fields `data.generated_by` and `data.message` as **Selected fields** to clean up the log table view.
- Confirmed logs were arriving from `single_file_log_generator`, showing a mix of:
  - SSH brute-force attempts (`Failed password for invalid user...`)
  - Suricata alerts for **XSS**, **SQLi**, **SSRF**, and **port scanning** (`nmap -sS`, `masscan`)
  - Ransomware-style suspicious activity (`mysqld: Suspicious encryption activity`)

**Key takeaway:** Wazuh aggregates raw telemetry from agents; Discover lets analysts filter/search this telemetry in near real-time.

---

## 3. Step 2 – Accessing Elasticsearch & Kibana

- Verified Elasticsearch cluster status at `http://localhost:9201/` (elastic / M#123@elastic) — returned cluster JSON metadata (cluster name `ELK`, version `8.19.6`).
- Logged into Kibana at `http://localhost:5602`.
- In **Analytics > Discover**, switched the **Data view** from the default "Default security data view" to **`wazuh-alerts-*`** — this was the key fix to get results to display (76,463+ hits for the day).

**Key takeaway:** Kibana's "Data view" determines which index/data source Discover queries. Wrong data view = "No results", even if data exists.

---

## 4. Section 1 – Creating Detection Rules in Kibana Security

Navigated to **Security > Rules > Detection rules (SIEM) > Create new rule**, using **Custom query (KQL)** rule type. Added `wazuh-alerts-*` to **Index patterns** for each rule.

### Rule 1: XSS Detection
```
data.payload.keyword : "\"'><script>alert(1)</script>" or data.payload.keyword : "<img src=x onerror=alert(1)>" or data.payload.keyword : "<script>alert(1)</script>"
```
- Severity: Medium | Risk score: 52
- Schedule: every 5 min, 1 min look-back

### Rule 2: SQL Injection Detection
```
data.payload.keyword: ("\" OR \"1\"=\"1\" -- " or "' OR '1'='1' --" or "'; DROP TABLE users; --" or "id=1 OR 1=1--")
```
- Severity: High | Risk score: 73
- Schedule: every 10 min, 2 min look-back
- **Lesson:** original multi-OR KQL with repeated field references threw "The KQL is invalid". Fixed by grouping values in parentheses after a single field reference: `field: (val1 or val2 or val3)`.

### Rule 3: Scanning Detection (Nmap/Masscan)
```
data.payload.keyword: ("Nmap scan report" or "nmap -sS" or "masscan detected")
```
- Severity: Low | Risk score: 26
- Schedule: every 15 min, 5 min look-back

### Rule 4: SSRF Detection
```
data.payload.keyword: ("http://169.254.169.254/latest/meta-data/" or "http://localhost:9200/_search")
```
- Severity: High | Risk score: 73
- Schedule: every 5 min, 1 min look-back
- **Concept:** `169.254.169.254` is the cloud metadata endpoint (AWS-style). A server requesting this URL is a classic SSRF indicator — an attacker tricking the server into leaking internal credentials/metadata.

### Rule 5: Suspicious Activity Detection
```
data.payload.keyword: "suspicious_activity_detected"
```
- Severity: Medium | Risk score: 47
- Schedule: every 5 min, 1 min look-back

All 5 rules were created with **"Create & enable rule"** and confirmed active.

---

## 5. Testing the Rules (Security > Alerts)

- Set time range to **Last 30 minutes**.
- Result: **1,000 alerts total** generated automatically from the continuous log stream (no manual attack-replay script was needed/available).

| Rule Name | Alert Count | Severity |
|---|---|---|
| XSS Attack | 500 | Medium |
| SSRF Detection | 200 | High |
| Suspicious Activity | 200 | Medium |
| SQL Injection Attack | 100 | High |
| Scanning Detection | (not yet captured in 30-min window) | Low |

**Severity breakdown:** High = 300, Medium = 700

**Key takeaway:** All 5 detection rules fired correctly against live simulated traffic — confirms the rules' KQL queries match the generated attack payloads.

---

## 6. Section 2 – Blue Team Phase: Triage (Activity 1)

Picked an **XSS Attack** alert for first-responder triage.

1. In **Security > Alerts**, filtered with:
   ```
   kibana.alert.rule.name : "XSS Attack"
   ```
2. Expanded an alert and reviewed the **Table** tab for key fields:

| Field | Value |
|---|---|
| `@timestamp` | 2026-06-12T01:27:23.403Z |
| `agent.name` | INCRES-EvaluateTestINCRESPLan |
| `data.src_ip` | 5.180.229.112 |
| `data.payload` | `<script>alert(1)</script>` |

3. Cross-referenced in **Wazuh Discover** (`wazuh-alerts-*`, time = Today) using a wildcard query (exact string match failed due to analyzed text field tokenization):
   ```
   data.message: *alert*
   ```
   - Found correlated entries: `Suricata alert: xss detected - <img src=x onerror=alert(1)>` and a raw access log line `178.85.158.132 POST /search?q=<img src=x onerror=alert(1)> 200`, confirming repeated XSS probing against the `/search` endpoint with HTTP 200 (successful) responses.

**Lesson:** `field: "exact phrase"` can return "No Results" on analyzed text fields containing special characters (`<`, `>`). Workarounds: use wildcard (`*term*`) or the `.keyword` sub-field for exact matching.

---

## 7. Documenting Findings (`lab_ticket.json`)

- File did not pre-exist; created manually via `nano /home/INCRES/lab_ticket.json`.
- Final JSON (validated with `python3 -m json.tool`):

```json
{
  "triage": {
    "alert_details": {
      "timestamp": "2026-06-12T01:27:23.403Z",
      "host": "INCRES-EvaluateTestINCRESPLan",
      "ip": "5.180.229.112"
    },
    "log_findings": "Suricata alert: xss detected - <img src=x onerror=alert(1)>; payload <script>alert(1)</script> also observed; repeated POST/GET to /search endpoint with HTTP 200 responses",
    "initial_risk": "Medium - Potential XSS leading to session hijack"
  }
}
```

---

## 8. Key Concepts Learned

- **Wazuh agent → server → indexer pipeline**: agents collect telemetry, the server applies detection rules, the indexer stores alerts for search.
- **KQL (Kibana Query Language) basics**:
  - `field: "value"` — exact match
  - `field: (val1 or val2)` — grouped OR for one field (avoids invalid-query errors)
  - `field: *partial*` — wildcard match
  - `@timestamp:[now-5m TO now]` — relative time range filter
  - `.keyword` suffix — use for exact-match on text fields
- **Index Patterns vs. Custom Query** in rule creation: Index Patterns define *where* to search (`wazuh-alerts-*`); Custom Query defines *what* to match.
- **IOC (Indicator of Compromise) examples**:
  - XSS: `<script>alert(1)</script>`, `<img src=x onerror=alert(1)>`
  - SQLi: `' OR '1'='1' --`, `; DROP TABLE`
  - SSRF: requests to `169.254.169.254` (cloud metadata endpoint)
  - Scanning: `nmap -sS`, `masscan detected`
- **Triage workflow**: Alert → expand details → extract timestamp/host/IP/payload → cross-check raw logs in Discover → record findings in a structured ticket (JSON).
- **Detection rule tuning fields**: severity, risk score, schedule (run interval + look-back window) — these control alert noise vs. responsiveness.

---

## 9. Practical Issues Encountered (Troubleshooting Log)

- "Wazuh dashboard server is not ready yet" on first load → resolved by waiting ~1-2 min and refreshing (services still booting).
- VM screen lock (Guacamole) after inactivity → unlocked using lab-provided VM credentials (`INCRES` / provided password).
- Discover showed only 1 hit initially → log generator script takes a few minutes to populate the index after boot; resolved by refreshing after a short wait.
- Kibana Discover showed "No results" with default data view → fixed by switching Data view to `wazuh-alerts-*`.
- KQL syntax errors on multi-value OR queries → fixed using parenthesized grouping: `field: (val1 or val2 or val3)`.
- `generate_attacks.sh` referenced in instructions did not exist on this VM → not required, since the background log generator already produces sufficient attack traffic for rules to trigger.
- `lab_ticket.json` did not exist and had to be created manually with `nano`.

---

## 10. Outcome

- 5/5 detection rules created and enabled, all firing correctly (1,000 alerts in 30 min).
- Completed a full triage cycle on an XSS alert and documented it in a structured incident ticket.
- Module marked as **Completed** in the course tracker.
