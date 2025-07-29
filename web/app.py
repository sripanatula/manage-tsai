import logging

# ✅ Configure logging early and globally
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

from flask import Flask
from web.voice_routes import voice_blueprint
from web.sms_routes import sms_blueprint

app = Flask(__name__)
app.register_blueprint(voice_blueprint)  # Register voice routes
app.register_blueprint(sms_blueprint)    # Register SMS routes  # Register SMS routes


if __name__ == "__main__":
    app.run(port=5000)
