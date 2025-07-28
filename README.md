# manage-tsai

A PoC for managing consulting operations, focused on validating timesheets using rule-based checks and delivering contextual notifications via email, SMS, voice, and WhatsApp — with future support for Agentic AI–driven follow-ups.

---

## 🌟 Purpose

This project demonstrates a working Proof of Concept (PoC) for automating timesheet validation and alerting in a consulting business context. It is designed to reduce manual effort and improve compliance by integrating intelligent rule-checking and multi-channel notifications.

---

## ✅ In-Scope Features (PoC Phase)

| Area                 | Details                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------- |
| **Data Input**       | Manual upload via CLI (CSV/XLSX timesheets)                                               |
| **Validation Rules** | - More than 8 hours/day<br>- Weekend or holiday work<br>- Missing weekday entries         |
| **Notifications**    | Email and mock SMS based on user preferences<br>Console output for observability          |
| **Configuration**    | `.env.dev` for credentials and routing<br>Employee directory supports multi-channel prefs |
| **Logging**          | Alerts and violations saved to JSON (SQLite planned)                                      |

---

### 📞 Voice Call Integration (Twilio Voice API)

To enable voice calls from the notifier:

1. Run the voice server locally:

   ```bash
   python notifier/serve_voice.py
   ```

2. Expose it using ngrok:

   ```bash
   ngrok http 5000
   ```

3. Copy the ngrok URL and add it to `.env.dev`:

   ```env
   VOICE_TWIML_URL=https://your-ngrok-url.ngrok-free.app/voice
   ```

4. Voice alerts will now use this endpoint to deliver spoken messages.

⚠️ Note: This endpoint must be reachable by Twilio. You may need to restart ngrok if your machine sleeps or restarts.

---

## 🔒 Not Included in This PoC

* Web-based upload or dashboards (coming next)
* Real-time ingestion (e.g., via API, DB)
* Retry/escalation logic
* Agentic AI reasoning (planned)
* Authentication, authorization, user roles

---

## 🔄 Designed for Growth

This PoC is structured for easy extension:

* Plug-and-play notification channels (email, SMS, voice, WhatsApp)
* Future UI for file uploads, rule inspection, and compliance reporting
* Agentic AI reasoning for choosing the best channel/timing
* Secure config via cloud secret managers

---

## 🧠 Architecture Direction

* **RENO (Realtime Event Notification Orchestrator)**: A future module that will handle adaptive, rule- and context-aware delivery strategies.
* **Agentic Follow-up**: Notification behavior will eventually adapt based on past user response history and alert severity.

---

## 🚀 Run Locally

```bash
# Setup
pip install -r requirements.txt

# Add your .env.dev with email credentials
cp .env.sample .env.dev

# Run the PoC
python main.py data/sample_timesheet.csv
```

---

### 📝 TODOs and Known Limitations

This PoC is intentionally scoped and omits production-grade robustness. Key areas for future improvement:

* [ ] ✅ Standardized notifier gateway (`notify.py`) with clean voice integration
* [ ] 🟢 Add WhatsApp integration via Twilio sandbox
* [ ] 🌐 Add minimal Web UI for uploading timesheets and showing violations
* [ ] ⟳ Retry logic for failed alerts (SMS, Voice)
* [ ] 📜 Logging framework for violations and alert delivery (JSON or SQLite)
* [ ] ❌ SMS alerts currently blocked by Twilio campaign (code is in place)
* [ ] ⚠️ Flask voice endpoint is ephemeral — consider Dockerized or cloud-hosted version
* [ ] 🔋 Improve debugging visibility in console (print SMS/Voice errors before raising)
* [ ] 📄 Unit tests for alerting logic
* [ ] 📤 Admin dashboard or audit log for tracking alert delivery
