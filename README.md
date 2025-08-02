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
| **Notifications**    | Email, SMS, and Voice based on user preferences<br>Feature flag control for SMS/Voice channels<br>Comprehensive logging for all notification attempts |
| **Configuration**    | `.env.dev` for credentials and routing<br>Employee directory supports multi-channel prefs<br>Feature flags: `SMS_ENABLED`, `VOICE_ENABLED` |
| **Logging**          | Comprehensive JSON logging throughout pipeline<br>Audit trail from parsing to notification delivery |
                                       |
---

---

### 📞 Twilio Webhook Server

The application includes a central Flask web server to handle all incoming webhooks from Twilio for voice call TwiML generation and SMS/WhatsApp status updates.

To run the server:

1. Start the local voice callback server:

    ```bash
    source .venv/bin/activate
    python web/app.py
    ```

2. Ensure `TWILIO_CALLBACK_BASE_URL` in your `.env.dev` file points to your public ngrok URL (e.g., `https://abc.ngrok-free.app`). The application will append the appropriate paths (`/voice`, `/sms-status`, etc.) to this base URL.

⚠️ Note: This endpoint must be reachable by Twilio. You may need to restart ngrok if your machine sleeps or restarts.

---

### 🚦 Feature Flags

The application supports feature flags to control notification channels:

- **SMS_ENABLED**: Set to `true` in `.env.dev` to enable SMS notifications via Twilio
- **VOICE_ENABLED**: Set to `true` in `.env.dev` to enable voice call notifications via Twilio

When disabled, these channels will log dry-run messages instead of making actual calls.

---

### 📱 WhatsApp Notifications (Twilio Sandbox)

WhatsApp notifications are sent to employees with `"whatsapp"` in their `notification_prefs`. This requires setting up the Twilio Sandbox.

**One-Time Sandbox Setup:**

1.  Go to your Twilio Console and navigate to **Messaging > Try it out > Send a WhatsApp message**.
2.  Follow the instructions to connect your device to the sandbox. This typically involves sending a specific code (e.g., `join-certain-words`) from your WhatsApp to the Twilio sandbox number provided on that page.
3.  The phone number you use to join the sandbox must be the one listed for the employee in `config/employee_directory.py`.

Once the sandbox is active, the application can send template messages to your WhatsApp number.

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

### Prerequisites
- Python 3.8+
- ngrok (for Twilio webhooks)
- Twilio account (for SMS/Voice)

### Setup Steps

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure environment:**
   ```bash
   # Copy sample environment file
   cp .env.sample .env.dev
   
   # Edit .env.dev with your credentials:
   # - Twilio credentials (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER)
   # - Email credentials (SENDER_EMAIL, SENDER_PASSWORD)
   # - Feature flags (SMS_ENABLED=true/false, VOICE_ENABLED=true/false)
   ```

3. **Start the webhook server:**
   ```bash
   # Terminal 1: Start Flask webapp
   python web/app.py
   ```

4. **Start ngrok for Twilio webhooks:**
   ```bash
   # Terminal 2: Start ngrok tunnel
   ngrok http 5000
   ```

5. **Update callback URL:**
   ```bash
   # Copy the ngrok URL (e.g., https://abc123.ngrok-free.app)
   # Update TWILIO_CALLBACK_BASE_URL in .env.dev with this URL
   ```

6. **Run the timesheet processor:**
   ```bash
   # Terminal 3: Process timesheet
   python main.py data/sample_timesheet.csv
   ```

### Important Notes
- The webapp must be running for SMS/Voice notifications to work
- ngrok URL must be accessible by Twilio (public HTTPS)
- Restart ngrok if your machine sleeps or restarts
- Feature flags control whether actual calls/SMS are sent vs dry-run logging

---

### 📝 TODOs and Known Limitations

This PoC is intentionally scoped and omits production-grade robustness. Key areas for future improvement:

* [✅] ✅ Standardized notifier gateway (`notify.py`) with clean voice integration
* [✅] 🟢 Add WhatsApp integration via Twilio sandbox
* [✅] 📜 Comprehensive logging framework with JSON structured logs
* [✅] 🚦 Feature flags for SMS and Voice notification control
* [ ] 🌐 Add minimal Web UI for uploading timesheets and showing violations
* [ ] ⟳ Retry logic for failed alerts (SMS, Voice)
* [ ] ❌ SMS alerts currently blocked by Twilio campaign (code is in place)
* [ ] ⚠️ Flask voice endpoint is ephemeral — consider Dockerized or cloud-hosted version
* [ ] 📄 Unit tests for alerting logic
* [ ] 📤 Admin dashboard or audit log for tracking alert delivery
