from logger import log_debug, log_info, log_error
from flask import Flask, request
from web.voice_routes import voice_blueprint
from web.sms_routes import sms_blueprint

app = Flask(__name__)
app.register_blueprint(voice_blueprint)  # Register voice routes
app.register_blueprint(sms_blueprint)    # Register SMS routes  # Register SMS routes



@app.before_request
def log_request():
    log_info("Incoming request received", {
        "method": request.method,
        "path": request.path,
        "args": request.args.to_dict()
    })


if __name__ == "__main__":
    app.run(port=5000)
