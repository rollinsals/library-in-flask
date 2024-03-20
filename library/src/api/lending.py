
from ..models import ReadersBooks, LibraryBooks, db
from flask import Blueprint, jsonify, abort, request

bp = Blueprint('lending', __name__, url_prefix='/lending')

# check a book out of a library
@bp.route('', methods=['POST'])
def checkout():
    for req in ["reader", "library_id", "book_id"]:
        if req not in request.json:
            abort(400)

    
    li_book = LibraryBooks.query.get_or_404((request.json["library_id"],request.json["book_id"]))
    if li_book.available_copies > 0:
        new_check_out = ReadersBooks(
            reader_id = request.json['reader'],
            book_id = request.json['book_id'],
            library_id = request.json['library_id']
        )
        db.session.add(new_check_out)
        li_book.available_copies -= 1
        db.session.commit()
    else:
        return jsonify({
            "status": "Book not available to be checked out."
        })

    return jsonify({
        "status": "book checked out",
        "book": new_check_out.book.title,
        "reader": new_check_out.reader.profile.username,
        "checked_out": new_check_out.checked_out_date,
        "due_date": new_check_out.due_date,

    })


# return book to the original library checked out of
@bp.route('', methods=['DELETE'])
def checkin():
    for req in ["reader", "book_id"]:
        if req not in request.json:
            abort(400)

    checked_book = ReadersBooks.query.get_or_404((request.json['reader'], request.json['book_id']))
    lib_book = LibraryBooks.query.get_or_404((checked_book.library_id, request.json['book_id']))

    try:
        db.session.delete(checked_book)
        lib_book.available_copies += 1
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
    