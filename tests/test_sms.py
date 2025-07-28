# test_sms.py

from notifier.sms_notifier import send_sms

# Replace with your own verified phone number (in E.164 format)
TO_NUMBER = "+14252609692"

send_sms(TO_NUMBER, "Hello from Twilio. Reply STOP to unsubscribe.", dry_run=False)

