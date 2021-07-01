import sqlite3

class SQL:
    def __init__(self, uri):
        self.uri = uri
    
    def execute(self, query_string, *args):
        self.connection = sqlite3.connect(self.uri)
        self.connection.row_factory = self.dict_factory
        self.cursor = self.connection.cursor()

        self.cursor.execute(query_string, args if len(args) else None)
        rows = self.cursor.fetchall()

        self.connection.commit()
        self.connection.close()

        return rows
        

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d