# notifier/notify.py

from config.employee_directory import get_profile
from notifier.email_notifier import send_email
from notifier.sms_notifier import send_sms
from notifier.voice_notifier import send_voice
from notifier.print_notifier import notify as print_notify

NOTIFIER_REGISTRY = {
    "email": send_email,
    "sms": send_sms,
    "voice": send_voice
}

def notify(violation):
    employee_id = violation["employee_id"]
    profile = get_profile(employee_id)

    if not profile:
        print(f"⚠️ No profile found for {employee_id}")
        return

    prefs = profile.get("notification_prefs", [])

    # Always print for observability
    print_notify(violation)

    for channel in prefs:
        handler = NOTIFIER_REGISTRY.get(channel)
        if handler:
            try:
                contact = profile.get("email") if channel == "email" else profile.get("phone")
                handler(violation, contact)
                break
            except Exception as e:
                print(f"❌ {channel.upper()} notification failed: {e}")
        else:
            print(f"⚠️ Unknown channel '{channel}' for {employee_id}")
