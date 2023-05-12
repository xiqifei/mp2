import subprocess
from flask import Flask, request
import socket

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def handle_request():
    if request.method == "POST":
        # Create a separate process to run stress_cpu.py
        subprocess.Popen(["python3", "stress_cpu.py"])

    elif request.method == "GET":
        # Return the private IP address of the EC2 instance
        ip_address = socket.gethostbyname(socket.gethostname())
        return ip_address

    return "Request processed"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
