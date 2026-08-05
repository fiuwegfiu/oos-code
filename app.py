from flask import Flask, jsonify, request
import random
import string
import os

app = Flask(__name__)


# =====================
# SECURITY
# =====================

API_KEY = os.environ.get("API_KEY")


def verify_api_key():
    auth = request.headers.get("Authorization")

    if auth != API_KEY:
        return False

    return True


# =====================
# GENERATORS
# =====================

def numbers(amount):
    return ''.join(random.choice(string.digits) for _ in range(amount))


def letters(amount):
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(amount))


def lletters(amount):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(amount))

# =====================
# HOME
# =====================

@app.route("/")
def home():
    return "OOS API Online"


# =====================
# JOIN CODE
# =====================

@app.route("/generate/join")
def join():

    if not verify_api_key():
        return jsonify({"error": "Unauthorized"}), 401

    code = f"{numbers(3)}{lletters(2)}{numbers(3)}{letters(1)}"

    return jsonify({
        "code": code
    })


# Report ID
@app.route("/generate/reportid")
def agent():
    code = f"R-{numbers(2)}{lletters(1)}{numbers(1)}{letters(2)}"

    return jsonify({
        "code": code
    })
