# notifier/email_notifier.py

import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env.dev")

SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
 # App Password, not your Gmail login
# notifier/email_notifier.py

def send_email(violation, recipient_email):
    """
    Sends an email about the violation to the specified recipient.
    """
    if not SENDER_EMAIL or not SENDER_PASSWORD:
        print("❌ Missing email credentials in environment. Check .env.dev.")
        return

    subject = "Timesheet Alert"
    body = (
        f"Employee ID: {violation['employee_id']}\n"
        f"Date: {violation['date']}\n"
        f"Violation: {violation['violation']}"
    )

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = recipient_email

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
        print(f"📧 Email sent to {recipient_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
