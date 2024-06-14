import json
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

TEMP_DATA = []
HUM_DATA = []

@app.route("/")
def root_route():
    return "Hello world!"

@app.route("/temp")
def get_temp():
    return jsonify(TEMP_DATA)

@app.route("/hum")
def get_hum():
    return jsonify(HUM_DATA)

@app.route("/submit-temp", methods=["POST"])
def post_temp():
    pesan = request.data.decode("utf8")
    data_entry = {
        "value": float(pesan),
        "timestamp": datetime.now().isoformat()
    }
    TEMP_DATA.append(data_entry)
    print(data_entry)
    return f"Received temperature {pesan} at {data_entry['timestamp']}"

@app.route("/submit-hum", methods=["POST"])
def post_hum():
    pesan = request.data.decode("utf8")
    data_entry = {
        "value": float(pesan),
        "timestamp": datetime.now().isoformat()
    }
    HUM_DATA.append(data_entry)
    print(data_entry)
    return f"Received humidity {pesan} at {data_entry['timestamp']}"

@app.route("/submit", methods=["POST"])
def post_data():
    pesan = request.data.decode("utf8")
    pesan = json.loads(pesan)
    temp_entry = {
        "value": float(pesan["temp"]),
        "timestamp": datetime.now().isoformat()
    }
    hum_entry = {
        "value": float(pesan["hum"]),
        "timestamp": datetime.now().isoformat()
    }
    TEMP_DATA.append(temp_entry)
    HUM_DATA.append(hum_entry)
    print(pesan)
    return f"Received data {pesan} with temp timestamp {temp_entry['timestamp']} and hum timestamp {hum_entry['timestamp']}"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
