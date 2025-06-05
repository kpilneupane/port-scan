from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan():
    data = request.json
    target = data.get('target')
    start_port = int(data.get('start_port', 1))
    end_port = int(data.get('end_port', 1024))

    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except Exception:
            continue

    return jsonify({'target': target, 'open_ports': open_ports})
