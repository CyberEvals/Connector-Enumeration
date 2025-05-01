from flask import Flask, render_template, redirect, url_for, abort, request

app = Flask(__name__)

# Example "database" (replace later with real database if you want)
books = {
    1: {
        'id': 1,
        'title': 'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'isbn': '9780743273565',
        'published_date': '1925',
        'available_copies': 3,
        'total_copies': 5
    },
    2: {
        'id': 2,
        'title': '1984',
        'author': 'George Orwell',
        'isbn': '9780451524935',
        'published_date': '1949',
        'available_copies': 2,
        'total_copies': 4
    }
}

@app.route('/')
def index():
    return render_template('index.html', books=books.values())

@app.route('/book/<int:book_id>')
def book_detail(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    return render_template('book_detail.html', book=book)

@app.route('/book/<int:book_id>/borrow', methods=['POST'])
def borrow_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    if book['available_copies'] > 0:
        book['available_copies'] -= 1
    return redirect(url_for('book_detail', book_id=book_id))

@app.route('/book/<int:book_id>/return', methods=['POST'])
def return_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    if book['available_copies'] < book['total_copies']:
        book['available_copies'] += 1
    return redirect(url_for('book_detail', book_id=book_id))

@app.route('/book/<int:book_id>/reserve', methods=['POST'])
def reserve_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    # Reserve logic could go here (e.g., put the user on a waitlist)
    print(f"Reserved book {book['title']}")
    return redirect(url_for('book_detail', book_id=book_id))

@app.route('/book/<int:book_id>/recommend', methods=['GET', 'POST'])
def recommend_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    if request.method == 'POST':
        friend_email = request.form['friend_email']
        print(f"Recommended {book['title']} to {friend_email}")
        return redirect(url_for('book_detail', book_id=book_id))
    return '''
        <h1>Recommend "{}" to a Friend</h1>
        <form method="POST">
            Friend's Email: <input type="email" name="friend_email" required>
            <button type="submit">Send Recommendation</button>
        </form>
    '''.format(book['title'])

if __name__ == '__main__':
    app.run(debug=True)
