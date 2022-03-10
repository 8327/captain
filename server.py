from os import path
from flask import Flask
from flask import jsonify
from flask import render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from litequeue import SQLQueue

http_port = 10443
db_file = "/tmp/captain.queue"
users = {
        "role_001": generate_password_hash("1234"),
        "role_002": generate_password_hash("1234")
}

app = Flask(__name__)
auth = HTTPBasicAuth()
queue = SQLQueue(db_file, check_same_thread=False)

@auth.verify_password
def verify_password(username, password):
    if username in users:
        if check_password_hash(users.get(username), password):
            return username

# no auth for /
@app.route('/')
def main():
    return render_template("index.html")

@app.route('/api/<path:filename>')
@auth.login_required
def api(filename):
    queue.put(filename)
    resp = jsonify(success=True)
    return resp

if __name__ == '__main__':
    if path.exists('ssl'):
        app.run(debug=False, host="0.0.0.0", ssl_context=('ssl/cert.pem', 'ssl/key.pem'), port=http_port)
    else:
        app.run(debug=False, host="0.0.0.0", ssl_context='adhoc', port=http_port)

