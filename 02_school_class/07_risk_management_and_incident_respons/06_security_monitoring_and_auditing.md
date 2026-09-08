# Security Monitoring and Auditing (VU23219/VU23221 — Session 8)

## 1. Cyber Risk Management Process (9 steps)

1. **Identify Asset**
2. **Identify Threats**
3. **Identify Vulnerabilities**
4. **Risk Assessment** — Qualitative: (a) Likelihood, (b) Impact, (c) Risk Level → plotted on a Risk Matrix
5. **Risk Treatment** — (a) Accept, (b) Eliminate/Avoid, (c) Minimise/Mitigate, (d) Transfer
6. **Implement Security Control** — (a) Physical, (b) Administrative, (c) Technical
7. **Evaluate Control** — assess Residual Risk
8. **Document**
9. **Incident Response** — Planning → Identify → Containment → Eradication → Recovery

**Core formula:** `Risk = f(Threat, Vulnerability)` — visualised as a Venn diagram where the overlap of Threat ∩ Vulnerability = Risk.

---

## 2. SIEM (Security Information and Event Management)

**SIEM = SIM + SEM**
- **SEM** (Security Event Management) — real-time event monitoring and correlation
- **SIM** (Security Information Management) — log collection, storage, and reporting

**Concept:** SIEM acts as a *funnel* — it collects activity from many different sources in real time, organises everything into a simplified format, and presents it through a centralised management console.

### 4 core SIEM functions
1. **Data Collection** — agents deployed on monitored systems (servers, endpoints, network devices) forward logs to the SIEM.
2. **Normalization** — raw logs come in different formats from different device types (e.g. Check Point firewall, Cisco router, Snort IDS all logging the same event differently). SIEM converts these into a common structured format (Date / Time / Event_Name / Src_IP / Src_Port / Dst_IP / Dst_Port / Device_Type), enabling correlation across sources.
3. **Correlation & Analysis** — links normalized events together to detect meaningful patterns (e.g. identifying an attack from multiple related log entries).
4. **Event Management & Reporting** — dashboards with multiple visualisations; events are prioritised, assigned to teams, tracked through resolution, and reported on.

### Wazuh in the TSOC environment
- Open-source SIEM; agents installed on lab machines collect logs and forward them to the **Wazuh manager**, which analyses the data.
- Continuously monitors endpoints, servers, and network activity.
- Automatically generates alerts on abnormal activity (e.g. multiple failed login attempts, malware activity).
- Alerts include: rule level (severity), rule description, agent name, timestamp, event type.
- **Rule level scale:** 0–15 → 15+ is "severe", ~0–6 is "low". Example seen in class: rule level 10 = high severity, immediate investigation required.
- Example alert dashboard data reviewed: `data.event_type: Credential dumping attempt`, severity: high, source IP, username, process name — all queryable/filterable in the Wazuh alerts dashboard.
- **ELK Stack** (Elasticsearch, Logstash, Kibana) visualises and analyses this data via dashboards so SOC analysts can quickly spot unusual activity.

### Other common security monitoring tools
| Tool | Description |
|---|---|
| **Wazuh** (open-source) | Host-based intrusion detection, log analysis, file integrity monitoring, threat detection |
| **Splunk** | Powerful security analytics platform for collecting/searching/analysing large volumes of machine data |
| **Datadog** | Cloud-based infrastructure monitoring, security analytics, performance monitoring |
| **SolarWinds** | Network monitoring — tracks network performance and security events |

---

## 3. Monitoring vs Logging vs Auditing

Though often used together, these three serve distinct purposes in cybersecurity operations:

| Aspect | Monitoring | Logging | Auditing |
|---|---|---|---|
| **Definition** | Continuous observation of systems, networks, and security events to detect suspicious behaviour or threats in real time | Recording of system activities and events within an organisation's IT environment | Review and analysis of logs and security activities to ensure compliance and evaluate control effectiveness |
| **Purpose** | Detect and respond to security threats as they occur | Provide a historical record of system and user activities | Verify that security policies, procedures, and controls are working correctly |
| **Focus** | Real-time detection and alerting | Data collection and storage of events | Periodic review and compliance assessment |
| **Examples** | Detecting multiple failed login attempts, unusual network traffic, malware activity | Login attempts, file access events, system configuration changes | Reviewing access logs, checking policy compliance, investigating past incidents |
| **Timeframe** | Continuous / real-time | Continuous event recording | Periodic or scheduled review |

**In short:** Logging records → Monitoring watches in real time → Auditing reviews it all afterward to evaluate whether controls are actually working.

- TSOC example — Monitoring: **Wazuh** alerts
- TSOC example — Auditing: **ELK dashboards** + **Cydarm** (incident management platform used to document and analyse incidents)

---

## 4. Review and Monitor Security Controls (Section 8.2)

Once controls are implemented and a system is authorised to operate, organisations must ensure controls remain effective over time via **continuous monitoring**.

Referenced standards:
- **NIST SP 800-37 (Risk Management Framework), Step 6: Monitor Security Controls** — maintaining security of authorised systems by continuously observing the system/environment for changes, threats, or vulnerabilities that introduce new risk.
- **NIST SP 800-137 — Information Security Continuous Monitoring (ISCM)** — organisations should implement ongoing monitoring processes to assess control effectiveness, detect emerging threats, and support risk-based decision making.

*(Deeper coverage of this section flagged by the trainer for a later term.)*

---

## 5. Practical relevance to Assessment Task 2 (Group Project — NovaStyle, Brute Force scenario)

- The "detecting multiple failed login attempts" example directly maps to our group's **Brute Force Login Attack** scenario — this is the kind of Wazuh alert the Blue Team would use for detection in Part C.
- Monitoring/Logging/Auditing distinctions are directly relevant to Part A Section 10 (Review and Monitoring Plan).
- SIEM tool selection (Wazuh) already featured in Part A's Vendor Product Evaluation — today's class reinforced *why* Wazuh fits (real-time alerting on credential/brute-force related risks #1, #2, #3, #7).

---

*Notes compiled from live class captions (Tuesday afternoon session, VU23219/VU23221, Trainer: Mani Nallasamy) — some caption fragments were reconstructed from context where transcription was garbled.*
