AZURE_KEY = "AZURE_1234567890abcdefghijklmnop"
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyz"
test = "ANUSHKA_ABC123ABZ9"
my_password = "P@ssw0rd1234"
password2="HelloWorld@123"
GITHUB_TOKEN1 = "ghp_1234567890abcdefghijklmnopqrsdfnndfb"

from flask import Flask, request
import sqlite3
import os
import subprocess

app = Flask(__name__)

# ❌ 1. SQL Injection
@app.route("/user")
def get_user():
    user_id = request.args.get("id")
    conn = sqlite3.connect("test.db")
    query = f"SELECT * FROM users WHERE id = {user_id}"  # vulnerable
    result = conn.execute(query)
    return str(result.fetchall())

# ❌ 2. Command Injection
@app.route("/run")
def run_command():
    cmd = request.args.get("cmd")
    return subprocess.check_output(cmd, shell=True)

# ❌ 3. Hardcoded secret
API_KEY = "hardcoded-secret-123"

# ❌ 4. Path traversal
@app.route("/read")
def read_file():
    filename = request.args.get("file")
    with open(filename, "r") as f:
        return f.read()

if __name__ == "__main__":
    app.run(debug=True)
