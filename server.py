import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Career Cruise Control Backend is live!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render assigns a port
    app.run(host="0.0.0.0", port=port, debug=True)
