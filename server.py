from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with Flask

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Career Cruise Control API"}), 200

@app.route("/register", methods=["POST"])
def register_user():
    data = request.json
    if not data.get("email"):
        return jsonify({"error": "Email is required"}), 400

    return jsonify({"message": f"User {data['email']} registered successfully!"}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)

