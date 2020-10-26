import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db')
        self.create_user_table()
        self.create_to_do_table()

    def create_to_do_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS "Todo" (
              id INTEGER PRIMARY KEY,
              Title TEXT,
              Description TEXT,
              _is_done boolean,
              _is_deleted boolean,
              CreatedOn Date DEFAULT CURRENT_DATE,
              DueDate Date,
              UserId INTEGER FOREIGNKEY REFERENCES User(_id)
            );
        """
        self.conn.execute(query)

    def create_user_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS "User" (
              _id INTEGER PRIMARY KEY,
              Name TEXT,
              Email TEXT
            );
        """
        self.conn.execute(query)

class ToDoModel:
    TABLENAME = "TODO"

    def __int__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description, TABLENAME):
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description) ' \
                f'values ("{text}","{description}")'

        result = self.conn.execute(query)
        return result

class User:
    TABLENAME = "User"

    def create(self, name, email):
        query = f'insert into {self.TABLENAME} ' \
                f'(Name, Email) ' \
                f'values ({name},{email})'
        result = self.conn.execute(query)
        return result