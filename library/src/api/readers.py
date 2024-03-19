"""
User Profile Management

Rollin Salsbery
"""

from flask import Blueprint, jsonify, abort, request
from ..models import Reader, Profile, db



bp = Blueprint('readers', __name__, url_prefix='/user')

@bp.route('', methods=['GET'])
def index():
    readers = Reader.query.all()
    result = []
    for r in readers:
        result.append(r.serialize())
    return jsonify(result)

@bp.route('<int:id>', methods=['GET'])
def show(id: int):
    reader = Reader.query.get_or_404(id, "User not found")
    acct = Profile.query.get(reader.library_card)
    return jsonify(acct.serialize())

@bp.route('/<int:id>/reviews', methods=['GET'])
def show_reviews(id: int):
    reader = Reader.query.get_or_404(id, "Account not found")
    result = []
    for r in reader.reviews:
        result.append(r.serialize())
    return jsonify(result)

@bp.route('/<int:id>/loans', methods=['GET'])
def show_loans(id: int):
    reader = Reader.query.get_or_404(id, "Account not found")
    result = []
    for b in reader.books_checked_out:
        result.append(b.serialize())
    return jsonify(result)


@bp.route("", methods=['POST'])
def create_user():
    if 'username' not in request.json or 'password' not in request.json:
        abort(400)

    new_user = Profile(
        username= request.json['username'],
        password= request.json['password']
    )
    new_reader = Reader(
        profile= new_user
    )

    db.session.add(new_user)
    db.session.add(new_reader)
    db.session.commit()
    return jsonify(new_reader.serialize())

@bp.route("<int:id>", methods=['PUT', 'PATCH'])
def update_user():
    if 'username' not in request.json and 'password' not in request.json:
        abort(400)

    user = Reader.query.get_or_404(id), "User not found"
    if 'username' in request.json:
        user.profile.username = request.json['username']

    if 'password' in request.json:
        user.profile.password = request.json['password']

    try:
        db.session.commit()
        return jsonify(True, user.profile.serialize())
    except:
        return jsonify(False)

@bp.route("/<int:id>", methods=['DELETE'])
def delete_user():
    reader = Reader.query.get_or_404(id, 'User not found')
    profile = reader.profile

    try:
        db.session.delete(reader)
        db.session.delete(profile)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)