from database.connection import get_connection

class Subject:
    def __init__(self, name):
        self.name = name

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO subjects (name) VALUES (?)", (self.name,))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM subjects")
        subjects = cursor.fetchall()
        conn.close()
        return subjects