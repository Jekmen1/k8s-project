from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello_flask():
    hostname = socket.gethostname()
    return f"Hello Flask, hostname:{hostname}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)