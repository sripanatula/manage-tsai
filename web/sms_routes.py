from flask import Blueprint, request
import logging

sms_blueprint = Blueprint("sms", __name__)

@sms_blueprint.route('/twilio/sms_status', methods=['POST'])
def handle_sms_status_callback():
    """
    Receives delivery status updates from Twilio for SMS messages.
    """
    try:
        sid = request.form.get("MessageSid")
        to = request.form.get("To")
        status = request.form.get("MessageStatus")
        
        logging.info(f"📬 SMS status update: SID={sid}, TO={to}, STATUS={status}")
        return '', 204  # Twilio expects 2xx for success

    except Exception as e:
        logging.error(f"❌ Error processing SMS callback: {e}")
        return '', 500
