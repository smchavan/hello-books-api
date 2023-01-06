from app import db
from app.models.book import Book
from flask import Blueprint, jsonify, make_response, request,abort
from flask import request
books_bp = Blueprint("books", __name__, url_prefix="/books")

@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    new_book = Book.from_dict(request_body)

    db.session.add(new_book)
    db.session.commit()

    return make_response(jsonify(f"Book {new_book.title} successfully created"), 200)

@books_bp.route("", methods=["GET"])
def read_all_books():
    
    title_query = request.args.get("title")
    if title_query:
        books = Book.query.filter_by(title=title_query)
    else:
        books = Book.query.all()

    books_response = []
    for book in books:
        books_response.append(book.to_dict())
    return jsonify(books_response)
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = Book.query.get(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#     }
def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{cls.__name__} {model_id} invalid"}, 400))

    model = cls.query.get(model_id)
    
    if not model:
        abort(make_response({"message":f"{cls.__name__} {model_id} not found"}, 404))
    
    return model

@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    book = validate_model(Book,book_id)
    return book.to_dict()

@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_model(Book,book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully updated"))
@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_model(Book,book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(jsonify(f"Book #{book.id} successfully deleted"))



# from flask import Blueprint, jsonify, abort, make_response
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ] 
#books_bp = Blueprint("books", __name__, url_prefix="/books")
#@books_bp.route("", methods=["GET"])
# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message":f"book {book_id} invalid"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     abort(make_response({"message":f"book {book_id} not found"}, 404))
# def handle_books():
#     books_response = []
#     for book in books:
#         books_response.append({
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#     })
#     return jsonify(books_response)
# @books_bp.route("/<book_id>", methods=["GET"])
# def handle_book(book_id):
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }
'''
    try:
        book_id = int(book_id)
    except:
        return {"message":f"book {book_id} invalid"}, 400
    book_id = int(book_id)
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
    return {"message":f"book {book_id} not found"}, 404
'''




# hello_world_bp = Blueprint("hello_world", __name__)

# @hello_world_bp.route("/hello-world", methods=["GET"])
# def say_hello_world():
#     my_beautiful_response_body = "Hello, World!"
#     return my_beautiful_response_body,200
# @hello_world_bp.route("/hello/JSON",methods = ["GET"])
# def say_hello_jason():
#     return {
#         "name": "cheezeItMan",
#         "mesage": "Need more Cheez!",
#         "hobbies": ["Snacks","Coding","Gardening"]
#     } , 200
# @hello_world_bp.route("/broken-endpoint-withbroken-server-code",methods = ["GET"])
# def broken_endpoint():
#     response_body = {
#         "name": "Ada Lovelace",
#         "message": "Hello",
#         "hobbies": ["Fishing","Swimming","Watching","Reality Shows"]
#     }
#     new_hobby = "Surfing"
#     response_body["hobbies"].append(new_hobby)
#     return response_body,404


