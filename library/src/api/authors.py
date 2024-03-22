"""
API For Author model
"""

from flask import Blueprint, jsonify, abort, request
from ..models import Author, db

bp = Blueprint('author', __name__, url_prefix='/author')

@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    a = Author.query.get_or_404(id, 'Author not fount')
    return jsonify(a.serialize())

@bp.route('/<int:id>/books', methods=['GET'])
def list_books(id: int):
    a = Author.query.get_or_404(id, 'Author not found')
    result = []
    for b in a.books_written:
        result.append(b.serialize())
    return jsonify(result)

@bp.route('', methods=['POST'])
def create():
    if 'name' not in request.json:
        abort(400)


    if 'bio' not in request.json:
        bio = ''
    else:
        bio = request.json['bio']

    new_author = Author(
        name= request.json['name'],
        bio= bio
    )
    try:
        db.session.add(new_author)
        db.session.commit()
        return jsonify(True, 'New author created')
    except:
        return jsonify(False)
