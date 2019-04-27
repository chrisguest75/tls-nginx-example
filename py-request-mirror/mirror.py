#!/usr/bin/env python3
from flask import Flask, request, abort, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST', 'PUT', 'DELETE'])
def mirror():

    headers = {}
    for header in request.headers.environ.keys():
        if not (header.startswith("werkzeug") or header.startswith('wsgi')):
            headers[header] = request.headers.environ[header]

    response_json = {
        'request_json': request.json, 
        'request_headers': headers 
    }

    return jsonify(response_json), 200

if __name__ == "__main__":
    server_port = os.environ.get('PORT')
    if server_port is None:
        logger.error(f"PORT environment variable not set")
        exit(1)

    app.run(port=server_port, host='0.0.0.0')
