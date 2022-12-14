from flask import Blueprint, jsonify, abort, make_response
class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description

books = [
    Book(1, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(2, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
] 
books_bp = Blueprint("books", __name__, url_prefix="/books")
@books_bp.route("", methods=["GET"])
def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message":f"book {book_id} invalid"}, 400))

    for book in books:
        if book.id == book_id:
            return book

    abort(make_response({"message":f"book {book_id} not found"}, 404))
def handle_books():
    books_response = []
    for book in books:
        books_response.append({
        "id": book.id,
        "title": book.title,
        "description": book.description
    })
    return jsonify(books_response)
@books_bp.route("/<book_id>", methods=["GET"])
def handle_book(book_id):
    book = validate_book(book_id)

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description,
    }
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




hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body,200
@hello_world_bp.route("/hello/JSON",methods = ["GET"])
def say_hello_jason():
    return {
        "name": "cheezeItMan",
        "mesage": "Need more Cheez!",
        "hobbies": ["Snacks","Coding","Gardening"]
    } , 200
@hello_world_bp.route("/broken-endpoint-withbroken-server-code",methods = ["GET"])
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello",
        "hobbies": ["Fishing","Swimming","Watching","Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body,404




