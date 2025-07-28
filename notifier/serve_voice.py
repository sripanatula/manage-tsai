# notifier/serve_voice.py

"""
Minimal Flask server that serves Twilio-compatible TwiML
for outbound voice call messages.

Example:
    https://<your-ngrok-url>/voice?message=Your%20text%20here
"""

import os
from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/voice", methods=["GET", "POST"])
def voice():
    # Use GET param or default message
    message = request.args.get("message", "Hello. This is a default Kailash notification.")
    
    # Sanitize basic content
    if not isinstance(message, str) or len(message.strip()) < 3:
        message = "Message not provided or invalid."

    twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say voice="alice">{message}</Say>
</Response>"""
    return Response(twiml, mimetype='text/xml')


if __name__ == "__main__":
    port = int(os.getenv("VOICE_PORT", 5000))
    debug = bool(os.getenv("VOICE_DEBUG", "1") == "1")
    print(f"🔊 Voice TwiML server running on http://localhost:{port}/voice")
    app.run(debug=debug, port=port)
