from flask import Flask, request, jsonify, render_template
import time

app = Flask(__name__)
latest_data = {"temperature": 0, "humidity": 0, "timestamp": ""}

@app.route('/')
def dashboard():
    return render_template('dashboard.html', data=latest_data)

@app.route('/data', methods=['POST'])
def receive_data():
    global latest_data
    content = request.json
    latest_data["temperature"] = content["temperature"]
    latest_data["humidity"] = content["humidity"]
    latest_data["timestamp"] = time.strftime("%Y-%m-%d %H:%M:%S")
    print("Received:", latest_data)
    return jsonify({"status": "success"})

@app.route('/live-data', methods=['GET'])
def live_data():
    return jsonify(latest_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
