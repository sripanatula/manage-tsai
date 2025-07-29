from flask import Flask
from web.voice_routes import voice_blueprint

app = Flask(__name__)
app.register_blueprint(voice_blueprint)

if __name__ == "__main__":
    app.run(port=5000)
