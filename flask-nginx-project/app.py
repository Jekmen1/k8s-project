from flask import Flask
import socket
import requests

app = Flask(__name__)

@app.route("/")
def hello_flask():
    hostname = socket.gethostname()
    return f"Hello Flask, hostname:{hostname}"

@app.route("/nginx")
def nginx_flask():
    data = requests.get("http://nginx")

    return f"{data.text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)