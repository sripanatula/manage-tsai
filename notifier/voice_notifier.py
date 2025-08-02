# notifier/voice_notifier.py

from logger import log_debug, log_info, log_error
from twilio.rest import Client
from dotenv import load_dotenv
import os
from urllib.parse import urlencode

load_dotenv(dotenv_path=".env.dev")

# Twilio configuration
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TWILIO_CALLBACK_BASE_URL = os.getenv("TWILIO_CALLBACK_BASE_URL")
VOICE_ENABLED = os.getenv("VOICE_ENABLED", "false").lower() == "true"

# Initialize Twilio client
client = None
if TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN:
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    except Exception as e:
        print(f"❌ Failed to initialize Twilio client: {e}")
        client = None

def send_voice(violation, to_number):
    """
    Initiates a Twilio voice call with a violation message.
    """
    if not client:
        log_error("Twilio client not initialized. Check configuration.", {})
        return

    log_debug("Preparing voice call", {
        "employee_id": violation.get("employee_id"),
        "date": violation.get("date"),
        "to": to_number
    })

    message_text = f"Timesheet issue detected on {violation['date']}: {violation['violation']}."

    if not VOICE_ENABLED:
        log_info("Dry-run: Voice call not initiated (VOICE_ENABLED=false)", {
            "to": to_number,
            "message": message_text
        })
        return
    query_params = urlencode({"message": message_text})
    callback_url = f"{TWILIO_CALLBACK_BASE_URL}/voice?{query_params}"

    try:
        call = client.calls.create(
            twiml=None,
            url=callback_url,
            to=to_number,
            from_=TWILIO_FROM_NUMBER
        )

        log_info("Voice call initiated", {
            "employee_id": violation.get("employee_id"),
            "date": violation.get("date"),
            "violation": violation.get("violation"),
            "to": to_number,
            "sid": call.sid,
            "status": call.status
        })

    except Exception as e:
        log_error("Failed to initiate voice call", {
            "employee_id": violation.get("employee_id"),
            "date": violation.get("date"),
            "to": to_number,
            "error": str(e)
        })
