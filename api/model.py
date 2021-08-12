from flask_sqlalchemy import SQLAlchemy
from config import create_app
 
db = SQLAlchemy(create_app())
 
 
# model class to create table structure in db
class Matrett(db.Model):
    __tablename__ = 'matrett'
 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String())
    author = db.Column(db.String(), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=0)
 
    def __init__(self, title, genre, author, quantity):
        self.title = title
        self.genre = genre
        self.author = author
        self.quantity = quantity
 
    def __repr__(self):
        return f'{self.id}'