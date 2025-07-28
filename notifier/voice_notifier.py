# notifier/voice_notifier.py

import os
from twilio.rest import Client
from urllib.parse import urlencode
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "../.env.dev"))

class VoiceNotifier:
    def __init__(self):
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_number = os.getenv("TWILIO_FROM_NUMBER")
        self.base_url = os.getenv("VOICE_TWIML_URL")

        if not all([self.account_sid, self.auth_token, self.from_number, self.base_url]):
            raise ValueError("Missing required environment variables for VoiceNotifier")

        self.client = Client(self.account_sid, self.auth_token)

    def send(self, violation, to_number):
        message = violation.get("message", "Timesheet issue detected. Please review.")
        twiml_url = f"{self.base_url}/voice?{urlencode({'message': message})}"
        
        call = self.client.calls.create(
            to=to_number,
            from_=self.from_number,
            url=twiml_url
        )
        print(f"📞 Voice call initiated. Call SID: {call.sid}")


def send_voice(violation, to_number):
    VoiceNotifier().send(violation, to_number)
