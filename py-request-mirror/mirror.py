#!/usr/bin/env python3
from flask import Flask, request, abort, jsonify
import os
import write_request
db_writer = write_request.write_request("mysql+mysqlconnector://root:example@127.0.0.1:3306/requests_tracking")
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

    db_writer.write(response_json)

    return jsonify(response_json), 200

if __name__ == "__main__":
    server_port = os.environ.get('PORT')
    if server_port is None:
        print(f"PORT environment variable not set")
        exit(1)

    app.run(port=server_port, host='0.0.0.0')
