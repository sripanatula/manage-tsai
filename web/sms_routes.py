# web/sms_routes.py
from flask import Blueprint, request, Response
from logger import log_info, log_error, log_debug

sms_blueprint = Blueprint("sms", __name__)

@sms_blueprint.route('/sms-status', methods=['POST'])
def handle_sms_status_callback():
    """
    Handles incoming Twilio SMS status callbacks.
    This endpoint is hit by Twilio to update the status of a sent SMS.
    """
    try:
        payload = request.form.to_dict()
        message_sid = payload.get('MessageSid')
        message_status = payload.get('MessageStatus')

        # Log the status update. In a real application, you might update a database.
        log_info("SMS Status Update", {
            "message_sid": message_sid,
            "status": message_status,
            "payload": payload
        })

        # Acknowledge receipt to Twilio with a 204 No Content
        return Response(status=204)

    except Exception as e:
        log_error("Error in Twilio SMS status callback", {
            "error": str(e),
            "payload": request.form.to_dict()
        })
        # Even on error, it's best to return a 2xx response to Twilio
        return Response(status=500)