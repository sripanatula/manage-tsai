# notifier/sms_notifier.py
from logger import log_debug, log_info, log_error
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.dev")

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TWILIO_CALLBACK_BASE_URL = os.getenv("TWILIO_CALLBACK_BASE_URL")
SMS_ENABLED = os.getenv("SMS_ENABLED", "false").lower() == "true"

# Initialize Twilio client
client = None
if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    except Exception as e:
        print(f"❌ Failed to initialize Twilio client: {e}")
        client = None

def send_sms(violation, to_number):
    """
    Sends an SMS via Twilio for the given violation to the specified number.
    """
    if not client:
        log_error("Twilio client not initialized. Check configuration.", {})
        return

    log_debug("Preparing SMS", {
        "employee_id": violation.get("employee_id"),
        "date": violation.get("date"),
        "to": to_number
    })
    
    message_text = (
        f"Timesheet Alert:\n"
        f"Employee ID: {violation['employee_id']}\n"
        f"Date: {violation['date']}\n"
        f"Violation: {violation['violation']}"
    )

    if not SMS_ENABLED:
        log_info("Dry-run: SMS not sent (SMS_ENABLED=false)", {
            "to": to_number,
            "message": message_text
        })
        return

    try:
        message = client.messages.create(
            to=to_number,
            from_=TWILIO_FROM_NUMBER,
            body=message_text,
            status_callback=f"{TWILIO_CALLBACK_BASE_URL}/sms-status"
        )

        log_info("SMS sent", {
            "employee_id": violation.get("employee_id"),
            "date": violation.get("date"),
            "violation": violation.get("violation"),
            "to": to_number,
            "sid": message.sid
        })

        # Optionally log delivery status if available immediately
        if message.status:
            log_debug("SMS status", {
                "sid": message.sid,
                "status": message.status
            })

    except Exception as e:
        log_error("Failed to send SMS", {
            "employee_id": violation.get("employee_id"),
            "date": violation.get("date"),
            "to": to_number,
            "error": str(e)
        })
