import os

from flask import Flask
from flask import jsonify
from flask import render_template
from litequeue import SQLQueue

http_port = 18000
db_file = "/tmp/captain.queue"

app = Flask(__name__)
queue = SQLQueue(db_file, check_same_thread=False)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/api/<path:filename>')
def api(filename):
    queue.put(filename)
    resp = jsonify(success=True)
    return resp

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=http_port)

