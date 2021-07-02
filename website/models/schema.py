user_schema = """
    CREATE TABLE users (
        id INTEGER, 
        username TEXT NOT NULL, 
        hash TEXT NOT NULL, 
        PRIMARY KEY(id)
    );
    CREATE UNIQUE INDEX username ON users (username);
"""

author_schema = """
    CREATE TABLE authors (
        id INTEGER,
        name TEXT,
        PRIMARY KEY(id)
    );
"""

book_schema = """
    CREATE TABLE books (
        id TEXT UNIQUE NOT NULL,
        title TEXT,
        author_id INTEGER,
        contributor_id INTEGER,
        PRIMARY KEY(id),
        FOREIGN KEY (author_id) REFERENCES authors(id),
        FOREIGN KEY (contributor_id) REFERENCES users(id)
    );
"""

saves_scema = """
    CREATE TABLE saves (
        id INTEGER,
        user_id INTEGER,
        book_id INTEGER,
        PRIMARY KEY(id),
        FOREIGN KEY(user_id) REFERENCES users(id),
        FOREIGN KEY(book_id) REFERENCES books(id),
        UNIQUE(user_id, book_id)
    );
"""
