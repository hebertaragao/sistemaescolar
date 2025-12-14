from database.connection import get_connection

class User:
    def __init__(Self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    @staticmethod
    def authenticate(username, password):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        cursor.close()
        return user