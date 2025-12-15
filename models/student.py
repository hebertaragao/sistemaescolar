from database.connection import get_connection

class Student:
    def __init__(self, name, birthdate, grade):
        self.name = name
        self.birthdate = birthdate
        self.grade = grade

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO students (name, birtdate, grade) VALUES(self.name, self.birthdate, self.grade)")
        conn.commit()
        conn.close()

        @staticmethod
        def all():
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            students = cursor.fetchall()
            conn.close()
            return students
        
        