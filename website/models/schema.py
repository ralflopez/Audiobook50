user_schema = """
    CREATE TABLE users (
        id INTEGER, 
        username TEXT NOT NULL, 
        hash TEXT NOT NULL, 
        PRIMARY KEY(id));
    CREATE UNIQUE INDEX username ON users (username);
    """