## Kailash – An AI-Driven Timesheet Management

### 🌟 Purpose

To demonstrate a working Proof of Concept (PoC) for a system that:

1. Reviews and analyzes timesheets (CSV/Excel)
2. Identifies anomalies using sample rules
3. Reaches out to the user to correct issues using methods including Email and SMS

This PoC is intentionally scoped to **manual triggers**, **hardcoded rules**, and **a single alert channel**. However, it lays the groundwork for an enterprise-scale, prompt, and self-learning solution intended to serve the needs of large, multi-national organizations.

---

### 🔧 In-Scope Features

| Area              | Details                                                                                     |
| ----------------- | ------------------------------------------------------------------------------------------- |
| **Data Input**    | Manual upload via CLI (local CSV/XLS file)                                                  |
| **Rules Applied** | - More than 8 hours/day  <br>- Weekend or holiday entry  <br>- Missing entries for workdays |
| **Alerting**      | One channel to start: SMS (via Twilio or mock)  <br>Templated message format                |
| **Logging**       | Local log of alerts and violations (JSON or SQLite)                                         |

---

### 🔒 Not Included in This PoC

* Web UI or dashboards
* Real-time or scheduled ingestion
* Alert retries or escalation logic
* Agentic/AI follow-up or resolution handling
* Authentication, authorization, user roles

---

### 🛠️ Designed for Future Growth

This PoC **does not implement** AI/agentic capabilities, but it is structured to allow for:

* Plug-and-play alert channels
* Rule expansion
* Message personalization
* Intelligent follow-up

These can be layered on post-PoC as part of the broader **Realtime Event Notification Platform**.

