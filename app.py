from flask import Flask, request, jsonify

app = Flask(__name__)
robot_memory = {}

@app.route('/')
def home():
    return "Kamzy Bot is online!"

@app.route('/speak', methods=['POST'])
def speak():
    data = request.json
    message = data.get('message', '')
    return jsonify({"reply": f"Kamzy says: {message}"})

@app.route('/remember', methods=['POST'])
def remember():
    data = request.json
    key = data.get('key', '')
    value = data.get('value', '')
    robot_memory[key] = value
    return jsonify({"status": "saved"})

@app.route('/recall', methods=['GET'])
def recall():
    key = request.args.get('key', '')
    value = robot_memory.get(key, 'not found')
    return jsonify({"value": value})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
