"""
Library Branch API

Rollin Salsbery
"""

from flask import Blueprint, jsonify, abort, request
from ..models import Library, db

bp = Blueprint('libraries', __name__, url_prefix='/branches')

# show all
@bp.route('', methods=['GET'])
def index():
    branches = Library.query.all()
    result = []
    for b in branches:
        result.append(b.serialize())
    return jsonify(result)

# show
@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    branch = Library.query.get_or_404(id, "Branch not found")
    return jsonify(branch.serialize())

# show the books associated with this library
# not sure how to access the copies columns in the intermediate table
@bp.route('/<int:id>/book_inventory', methods=['GET'])
def list_books(id: int):
    branch = Library.query.get_or_404(id, "Branch not found")
    result = []
    for b in branch.book_inventory:
        result.append(b.serialize_book())
    return jsonify(result)


@bp.route('', methods=['CREATE'])
def create_branch():
    if 'branch_name' not in request.json or 'location' not in request.json:
        abort(400)

    l = Library(
        branch_name=request.json['branch_name'],
        location=request.json['location']
    )
    db.session.add(l)
    db.session.commit()
    return jsonify(l.serialize())