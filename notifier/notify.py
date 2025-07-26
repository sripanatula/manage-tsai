# notifier/notify.py

from config.employee_directory import get_profile
from notifier.email_notifier import send_email
from notifier.print_notifier import notify as print_notify
# from notifier.sms_notifier import send_sms  # to be added next

def notify(violation):
    employee_id = violation["employee_id"]
    profile = get_profile(employee_id)

    if not profile:
        print(f"⚠️ No profile found for {employee_id}")
        return

    prefs = profile.get("notification_prefs", [])

    # Always print for observability
    print_notify(violation)

    # Naive priority handler (first available channel)
    for channel in prefs:
        if channel == "email":
            send_email(violation, profile["email"])
            break
        elif channel == "sms":
            print(f"ℹ️ SMS notification would be sent to {profile['phone']}")
            break
        else:
            print(f"⚠️ Unknown channel: {channel}")
