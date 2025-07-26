# ✅ TODOS for manage_tsai

This document tracks progress and plans for the `manage_tsai` project — a PoC system for validating timesheets and eventually automating follow-ups using notification orchestration and Agentic AI.

---

## ✅ Phase 1: PoC (Completed)

- [x] CSV/XLSX file parsing
- [x] Rule engine (hours > 8, weekend work, missing weekday entry)
- [x] Centralized `notify()` dispatcher
- [x] Print + Email notifiers
- [x] Config extracted to `.env.dev` (SMTP, email)
- [x] Global employee directory with channel preferences
- [x] Mock SMS routing + console display
- [x] `.gitignore` for sensitive data

---

## 🚧 Phase 2: Near-Term (In Progress or Planned)

- [ ] Web UI for:
  - [ ] Uploading timesheets
  - [ ] Viewing validation results
  - [ ] Viewing sent notifications
  - [ ] Inspecting rule definitions
- [ ] Twilio SMS integration (real delivery to test numbers)
- [ ] Voice call notifications (Twilio)
- [ ] Modular notification plugins (email, sms, voice)
- [ ] SQLite logging of notifications + violations
- [ ] Unit + functional test coverage (`pytest`)
- [ ] Config refactor: support YAML/JSON config beyond `.env`
- [ ] CLI improvements (flags, file upload path, summaries)

---

## 🧠 Phase 3: Future Vision (enterprise or production ready)

- [ ] Agentic AI–based follow-up behavior
  - [ ] Learn from past response history
  - [ ] Decide best channel dynamically
  - [ ] Adjust retry/escalation behavior
- [ ] Move credentials to secure secrets manager (e.g., AWS Secrets Manager)
- [ ] Pluggable rule engine
- [ ] Dashboard for compliance visibility
- [ ] Timesheet ingestion from APIs or databases

---

## 📌 Notes

- `manage_tsai` = Manage Timesheets with AI
- `RENO` (Realtime Event Notification Orchestrator) will be a separate, pluggable module that handles channel decisions.
