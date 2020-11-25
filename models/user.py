import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users' # table name for db
    id = db.Column(db.Integer, primary_key = True)
    
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username): ##replace self with class since self is not used
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users WHERE username=?"
        result = cursor.execute(query, (username,))
        row = result.fetchone() # fetch first row
        if row:
            #user = cls(row[0], row[1], row[2]) # each column
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):  ##replace self with class since self is not used
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * from users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()  # fetch first row
        if row:
            # user = cls(row[0], row[1], row[2]) # each column
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user