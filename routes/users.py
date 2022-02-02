from flask import make_response
from flask import request, jsonify
import sys

sys.path.append("..")
from firebase import Users


def create():
    username = request.args.get("username")
    email = request.args.get("email")
    if Users.where("email", "in", [email]).get():
        for i in Users.where("email", "in", [email]).get():
            if i.exists:
                return "user exists", 231
    else:
        Users.add({u"username": username, u"email": email})
        return "User Created", 200
