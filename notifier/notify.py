# notifier/notify.py

from config.employee_directory import get_profile
from notifier.email_notifier import send_email
from notifier.sms_notifier import send_sms
from notifier.voice_notifier import send_voice
from notifier.print_notifier import notify as print_notify
from logger import log_info, log_error, log_debug

NOTIFIER_REGISTRY = {
    "email": send_email,
    "sms": send_sms,
    "voice": send_voice
}

def notify(violation):
    employee_id = violation["employee_id"]
    profile = get_profile(employee_id)

    if not profile:
        log_error("No profile found for employee", {"employee_id": employee_id})
        return

    prefs = profile.get("notification_prefs", [])

    log_debug("Processing notification", {
        "employee_id": employee_id,
        "preferences": prefs,
        "violation": violation
    })

    # Always print for observability
    print_notify(violation)

    for channel in prefs:
        handler = NOTIFIER_REGISTRY.get(channel)
        if handler:
            try:
                contact = profile.get("email") if channel == "email" else profile.get("phone")
                log_info("Sending notification", {
                    "employee_id": employee_id,
                    "channel": channel,
                    "contact": contact
                })
                handler(violation, contact)
                break
            except Exception as e:
                log_error("Notification failed", {
                    "employee_id": employee_id,
                    "channel": channel,
                    "error": str(e)
                })
        else:
            log_error("Unknown notification channel", {
                "employee_id": employee_id,
                "channel": channel
            })
