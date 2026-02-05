from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f'{self.book_name}\nTitle: {self.book_name}\nAuthor: {self.author}\nPublisher: {self.publisher}'
    
@app.route('/')
def index():
    return 'Hello! Welcome to my book database.'

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_data = {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}
        output.append(book_data)

    return{"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = Book.query.get_or_404(id)
    return {'name': book.book_name, 'author': book.author, 'publisher': book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(book_name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

@app.route('/books/<id>', methods=['DELETE'])
def delete_book(id):
    book = Book.query.get(id)
    if book is None:
        return {'error': 'not found'}
    db.session.delete(book)
    db.session.commit()
    return {'message': "Deleted"}

@app.route('/books/<id>', methods=['PUT'])
def update_book(id):
    # Have to grab the existing record
    book = Book.query.get_or_404(id)
    data = request.get_json()

    # This updates attributes directly on the 'book' object. * book = Book.query.get_or_404(id)
    if 'name' in data:
        book.book_name = data['name']
    if 'author' in data:
        book.author = data['author']
    if 'publisher' in data:
        book.publisher = data['publisher']
    
    # Save changes
    db.session.commit()
    return {'message': 'Updated Successfully'}, 200

    
if __name__ == "__main__":
    """Automates the creation of the database for the first time. 
       Also, gives me a reference of the code needed to initialize the database.
       Will not work with 'flask run'"""
    
    with app.app_context():
        db.create_all()
        print('Database initialized.')