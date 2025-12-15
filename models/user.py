from database.connection import get_connection

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    @staticmethod
    def authenticate(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
        user = cursor.fetchone()
        conn.close()
        return user
