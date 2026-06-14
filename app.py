from flask import Flask, jsonify, request
from flask_cors import CORS
import base64
import hashlib
import time
import random
import string
import os

app = Flask(__name__)
CORS(app)

POD_NAME = os.environ.get("HOSTNAME", "payment-service-local")

def mock_encrypt(message):
    reversed_msg = message[::-1]
    encoded = base64.b64encode(reversed_msg.encode()).decode()
    return encoded[:20] + "..." if len(encoded) > 20 else encoded

def generate_message_id():
    return "MSG-" + ''.join(random.choices(string.digits, k=4))

def generate_key_id():
    return "KEY-" + hashlib.md5(str(time.time()).encode()).hexdigest()[:8].upper()

@app.route("/")
def index():
    return jsonify({"service": "payment-service", "version": "1.0.0", "status": "healthy", "pod": POD_NAME})

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "pod": POD_NAME})

@app.route("/api/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "Message is required"}), 400

    if len(message) > 200:
        return jsonify({"error": "Message too long (max 200 chars)"}), 400

    start = time.time()
    encrypted = mock_encrypt(message)
    duration_ms = round((time.time() - start) * 1000 + random.uniform(5, 15), 2)

    return jsonify({
        "success": True,
        "original_length": len(message),
        "encrypted": encrypted,
        "message_id": generate_message_id(),
        "key_id": generate_key_id(),
        "algorithm": "AES-256-CBC (mock)",
        "processed_by": POD_NAME,
        "namespace": "dev",
        "processing_time_ms": duration_ms,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime())
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
