from flask import Blueprint, request, Response
from twilio.twiml.voice_response import VoiceResponse
from logger import log_info, log_error, log_debug

voice_blueprint = Blueprint("voice", __name__)

@voice_blueprint.route('/voice', methods=['GET', 'POST'])
def handle_voice_callback():
    """
    Generates TwiML for an outbound Twilio Voice call.
    Twilio fetches this URL when a call is initiated.
    """
    try:
        # The message is passed as a query parameter from our notifier
        message = request.args.get("message", "This is a message from the Kailash alert system. Please check your timesheet.")
        log_info("Generating TwiML for voice call", {
            "message": message,
            "request_args": request.args.to_dict()
        })

        response = VoiceResponse()
        response.say(message, voice="alice")
        response.hangup()

        return Response(str(response), mimetype="text/xml")

    except Exception as e:
        log_error("Error in Twilio voice callback", {
            "error": str(e),
            "request_args": request.args.to_dict()
        })
        # Return a valid TwiML response even on error
        response = VoiceResponse()
        response.say("An internal error occurred. Please contact support.", voice="alice")
        return Response(str(response), mimetype="text/xml")
