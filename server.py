from flask import Flask, request
app = Flask(__name__)

@app.route('/track', methods=['POST'])
def track():
    data = request.json
    print(f"Reçu: {data}")
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
