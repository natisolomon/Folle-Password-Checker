# main.py

from flask import Flask, render_template, request
import re

app = Flask(__name__)

# Load common passwords from file
with open("common.txt", "r") as f:
    common_passwords = set(f.read().splitlines())

def check_password_strength(password):
    # Check length
    if len(password) < 8:
        return "Weak"
    
    # Check for common passwords
    if password in common_passwords:
        return "Weak"

    # Add more checks here (e.g., uppercase, lowercase, digits, symbols)
    
    # If none of the above conditions are met, consider it strong
    return "Strong"

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        password = request.form["password"]
        strength = check_password_strength(password)
        return render_template("result.html", strength=strength)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
