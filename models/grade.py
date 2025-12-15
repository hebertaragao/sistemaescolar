from database.connection import get_connection

class Grade:
    def __init__(self, student_id, subject_id, grade):
        self.student_id = student_id
        self.subject_id = subject_id
        self.grade = grade

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)",
                       (self.student_id, self.subject_id, self.grade))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_student(student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT subjects.name, grades.grade
            FROM grades
            JOIN subjects ON grades.subject_id = subjects.id
            WHERE grades.student_id=?
        """, (student_id,))
        grades = cursor.fetchall()
        conn.close()
        return grades