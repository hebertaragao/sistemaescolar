from database.connection import get_connection

def lancar_nota(student_id, subject_id, grade):
    conn.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO grades (student_id, subject_id, grade) VALUES (%s, %s, %s)", (student_id, subject_id, grade))
    conn.commit()
    conn.close()
    return "Nota lançada com sucesso!"

def lancar_falta(student_id, date, status="Falta"):
    conn.get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (student_id, date, status) VALUES (%s, %s, %s)", (student_id, date, status))
    conn.commit()
    conn.close()
    return "Falta lançada com sucesso!"
