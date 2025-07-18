from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenue sur mon site Railway !"

# On écoute sur le port donné par Railway
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Railway donne $PORT
    app.run(host="0.0.0.0", port=port)
