from flask import Flask, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Active CORS pour accepter les requêtes cross-origin

@app.route('/track', methods=['POST'])
def track():
    data = request.get_json()
    ip = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {ip} > {data}\n"
    print(log_line)  # Affiche dans la console
    with open("log_visiteurs.txt", "a") as f:
        f.write(log_line)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

