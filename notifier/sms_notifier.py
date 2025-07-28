# notifier/sms_notifier.py

import os
from dotenv import load_dotenv
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

load_dotenv(dotenv_path=".env.dev")

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_FROM_NUMBER = os.getenv("TWILIO_FROM_NUMBER")
TWILIO_MESSAGING_SERVICE_SID = os.getenv("TWILIO_MESSAGING_SERVICE_SID")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to_number: str, message: str, dry_run: bool = False):
    print("DEBUG:", os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
    if dry_run:
        
        print(f"[DRY RUN] SMS to {to_number}: {message}")
        return

    try:
        message = client.messages.create(
            body=message,
            # from_=TWILIO_FROM_NUMBER,
            messaging_service_sid=os.getenv("TWILIO_MESSAGING_SERVICE_SID"),
            to=to_number
        )
        msg_status = client.messages(message.sid).fetch()
        print(f"✅ Sent SMS to {to_number} (SID: {message.sid})")
    
        if msg_status.status in ['undelivered', 'failed']:
            print(f"⚠️  Delivery failed: {msg_status.error_code} - {msg_status.error_message}")
        else:
            print(f"✅ SMS delivered to {to_number} (SID: {message.sid}, Status: {msg_status.status})")

    except Exception as e:
        print(f"❌ Failed to send SMS to {to_number}: {e}")
    except TwilioRestException as e:
        print(f"❌ Twilio Error {e.code}: {e.msg}")