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
              _is_deleted boolean DEFAULT 0,
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
    TABLENAME = "Todo"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def get_by_id(self, _id):
        query = f"SELECT id, Title, Description, DueDate, _is_done " \
                f"from {self.TABLENAME} WHERE _is_deleted != {1} AND id={_id}"
        print(query)
        result = self.conn.execute(query).fetchall() #fetchall returns list of tuples
        print(result)
        db_result = dict()
        for elt in result:
            db_result["id"] = elt[0]
            db_result["Title"] = elt[1]
            db_result["Description"] = elt[2]
            db_result["DueDate"] = elt[3]
            db_result["_is_done"] = elt[4]
        return db_result

    def create(self, params):
        query = f'insert into {self.TABLENAME} ' \
                f'(Title, Description, DueDate, UserId) ' \
                f'values ("{params.get("Title")}","{params.get("Description")}",' \
                f'"{params.get("DueDate")}","{params.get("UserId")}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)

class User:
    TABLENAME = "User"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, name, email):
        query = f'insert into {self.TABLENAME} ' \
                f'(Name, Email) ' \
                f'values ({name},{email})'
        result = self.conn.execute(query)
        return result
