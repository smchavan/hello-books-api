from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#import os
#from dotenv import load_dotenv 
db = SQLAlchemy()
migrate = Migrate()
#load_dotenv()
def create_app(test_config=None):
    app = Flask(__name__)
    from .routes import hello_world_bp,books_bp

    app.register_blueprint(hello_world_bp)
    app.register_blueprint(books_bp)
    app.config["SQLARCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgress:postgres@localhost:5432/hello_books_development"
    db.init_app(app)
    migrate.init_app(app,db)

    return app