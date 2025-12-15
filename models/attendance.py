from database.connection import get_connection

class Attendance:
    def __init__(self, student_id, date, status):
        self.student_id = student_id
        self.date = date
        self.status = status

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (?, ?, ?)",
                       (self.student_id, self.date, self.status))
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_student(student_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT date, status FROM attendance WHERE student_id=?", (student_id,))
        attendance = cursor.fetchall()
        conn.close()
        return attendance