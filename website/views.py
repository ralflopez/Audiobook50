from flask import Blueprint, render_template, session, request
from werkzeug.utils import redirect
from .helpers import login_required, apology
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def index():
    # from .packages.youtube_data_api import getVideoTranscript

    return render_template('index.html')


@views.route('/book')
def book_invalid():
    return redirect('/')


@views.route('/catalogue')
@login_required
def catalogue():
    book_list = db.execute('SELECT books.id, title, name as author, authors.id as author_id FROM books JOIN authors ON authors.id = books.author_id ORDER BY title;')
    print(book_list)
    return render_template('catalogue.html', book_list=book_list, user_id=session.get('user_id'))


@views.route('/book/<v_id>')
@login_required
def book(v_id):
    rows = db.execute('SELECT books.id, title, name as author FROM books JOIN authors ON authors.id = books.author_id WHERE books.id = ?', v_id)
    
    # no book found
    if not len(rows):
        return apology('Book not found')

    book_details = rows[0]
    return render_template('book.html', book_details=book_details)


@views.route('/contribute', methods=['GET', 'POST'])
@login_required
def contribute():
    if request.method == 'POST':
        user_id = session.get('user_id')

        title = request.form.get('title')
        author = request.form.get('author')
        url = request.form.get('yt-url')

        if not title or not author or not url:
            return apology('Please complete info')

        # get id from url
        try:
            start = url.index('?v=') + 3
        except:
            return apology('Invalid URL')

        try:
            end = url.index('&')
        except:
            end = len(url)

        id = url[start: end]
        # get author
        author_id_res = db.execute('SELECT id FROM authors WHERE name LIKE ? LIMIT 1;', f'%{author}%')
        if not len(author_id_res):
            db.execute('INSERT INTO authors (name) VALUES (?);', author)
            author_id_res = db.execute('SELECT id FROM authors WHERE name = ? LIMIT 1;', author)

        author_id = author_id_res[0]['id']

        # push to db
        db.execute('INSERT INTO books (id, title, author_id, contributor_id) VALUES (?, ?, ?, ?);', id, title, author_id, user_id)

        return redirect('/catalogue')

    else:
        return render_template('contribute.html')


@views.route('/login', methods=['GET', 'POST'])
def login():

    if session.get('user_id'):
        return redirect('/')

    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@views.route("/register", methods=["GET", "POST"])
def register():

    if session.get('user_id'):
        return redirect('/')

    """Register user"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirmation = request.form.get('confirmation')

        # error handling
        if not username:
            return apology('Must Enter Username')

        if not password:
            return apology('Must Enter Password')

        if not confirmation:
            return apology('Must Enter Password For Confirmation')

        if password != confirmation:
            return apology('Password Confirmation Doesn\'t Match')

        # check if exist
        user = db.execute('SELECT * FROM users WHERE username = ?', username)
        if len(user) != 0:
            return apology('User already exist. Try logging in instead')

        # insert into db
        db.execute('INSERT INTO users (username, hash) VALUES (?, ?)', username, generate_password_hash(password))

        return redirect('/login')

    # get request
    else:
        return render_template('register.html')


@views.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")