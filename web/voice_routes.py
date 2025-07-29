from flask import Blueprint, request, Response
import logging

voice_blueprint = Blueprint("voice", __name__)

@voice_blueprint.route('/twilio/voice', methods=['POST'])
def handle_twilio_voice_callback():
    """
    Handles incoming Twilio Voice webhook for timesheet alerts.
    """
    try:
        payload = request.form.to_dict()
        logging.info(f"📞 Twilio Voice callback received: {payload}")

        # You likely have logic to determine the message content
        # For now, just send a generic response
        response_xml = """
        <Response>
            <Say voice="alice">This is a message from the Kailash alert system. Please check your timesheet.</Say>
        </Response>
        """
        return Response(response_xml, mimetype="text/xml")

    except Exception as e:
        logging.error(f"❌ Error in Twilio voice callback: {e}")
        return Response("<Response><Say>Internal Error</Say></Response>", mimetype="text/xml")
