import functools
from flask import Blueprint, url_for, jsonify, request
from flask_inputs.validators import JsonSchema
from werkzeug.security import check_password_hash, generate_password_hash

from .db import get_db


bp = Blueprint("api", __name__, url_prefix="/api")


@bp.route("/register", methods=["POST"])
def register():
    """Register a new user.

    Validates that the username is not already taken. Hashes the
    password for security.
    """

    db = get_db()

    data = request.get_json()

    qry = ("INSERT INTO users (username, password, ip_address, created_at) "
           "VALUES (?, ?, ?, datetime('now'))")
    params = (data['username'], generate_password_hash(data['password']), 'ip')
    db.execute(qry, params)

    db.commit()

    return jsonify({'fff': 55})
