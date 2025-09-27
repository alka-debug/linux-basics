from flask import Flask
import socket
from datetime import datetime

app= Flask(__name__)

@app.route("/")
def home():
    return "<h1>HY MOM</h1>"


@app.route("/status")
def status():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>HY MOM</h1><h2>Server: {hostname} | IP: {ip} | Time: {now}</h2>"
if __name__ == "__main__":
   app.run(host="0.0.0.0", port=5000)
