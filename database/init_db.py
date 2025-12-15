from database.connection import get_connection
from utils.password import hash_password

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    # Usuários
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT,
        role TEXT
    )
    """)

    # Alunos
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        birthdate TEXT,
        grade TEXT
    )
    """)

    # Professores
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        subject TEXT
    )
    """)

    # Disciplinas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    # Notas
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        subject_id INTEGER,
        grade REAL,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(subject_id) REFERENCES subjects(id)
    )
    """)

    # Presenças
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        date TEXT,
        status TEXT,
        FOREIGN KEY(student_id) REFERENCES students(id)
    )
    """)

    # -------------------------------
    # Dados iniciais
    # -------------------------------

    # Usuários (senha com hash)
    users = [
        ("admin", hash_password("1234"), "admin"),
        ("professor1", hash_password("1234"), "teacher"),
        ("aluno1", hash_password("1234"), "student"),
    ]
    cursor.executemany("INSERT OR IGNORE INTO users (username, password, role) VALUES (?, ?, ?)", users)

    # Alunos
    students = [
        ("João Silva", "2008-05-12", "8º Ano"),
        ("Maria Souza", "2007-09-20", "9º Ano"),
    ]
    cursor.executemany("INSERT OR IGNORE INTO students (name, birthdate, grade) VALUES (?, ?, ?)", students)

    # Professores
    teachers = [
        ("Carlos Pereira", "Matemática"),
        ("Ana Lima", "Português"),
    ]
    cursor.executemany("INSERT OR IGNORE INTO teachers (name, subject) VALUES (?, ?)", teachers)

    # Disciplinas
    subjects = [
        ("Matemática",),
        ("Português",),
        ("História",),
        ("Ciências",),
    ]
    cursor.executemany("INSERT OR IGNORE INTO subjects (name) VALUES (?)", subjects)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Banco inicializado com dados de exemplo!")

        # Notas iniciais
    grades = [
        (1, 1, 8.5),  # João Silva - Matemática
        (1, 2, 7.0),  # João Silva - Português
        (2, 1, 9.0),  # Maria Souza - Matemática
        (2, 3, 6.5),  # Maria Souza - História
    ]
    cursor.executemany("INSERT OR IGNORE INTO grades (student_id, subject_id, grade) VALUES (?, ?, ?)", grades)

    # Faltas iniciais
    attendance = [
        (1, "2025-03-01", "Presente"),
        (1, "2025-03-02", "Falta"),
        (2, "2025-03-01", "Presente"),
        (2, "2025-03-02", "Presente"),
    ]
    cursor.executemany("INSERT OR IGNORE INTO attendance (student_id, date, status) VALUES (?, ?, ?)", attendance)