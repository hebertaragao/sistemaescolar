from database.connection import get_connection

class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO teachers (name, subject) VALUES (?, ?)", (self.name, self.subject))
        conn.commit()
        conn.close()

    @staticmethod
    def all():
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM teachers")
        teachers = cursor.fetchall()
        conn.close()
        return teachers

    