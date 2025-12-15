from database.connection import get_connection

from database.connection import get_connection

def visualizar_boletim(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT subjects.name, grades.grade
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE grades.student_id=?
    """, (student_id,))
    boletim = cursor.fetchall()
    conn.close()
    return boletim

def visualizar_faltas(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT date, status FROM attendance WHERE student_id=?", (student_id,))
    faltas = cursor.fetchall()
    conn.close()
    return faltas
