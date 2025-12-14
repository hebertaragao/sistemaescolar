from database.connection import get_connection

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    #Usuarios

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                   username TEXT UNIQUE,
                   password TEXT,
                   role TEXT);
    """)

    # Alunos

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students ( id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   name TEXT,
                   birthdate TEXT,
                   grade TEXT);
    """)

    # Professores

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS teachers ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT,
                     subject TEXT);
     """)
    
    # Disciplinas

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subjects ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                   )
    """)

    # Notas

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS grades ( id INTEGER PRIMARY KEY AUTOINCREMENT,   
                     student_id INTEGER,
                     subject_id INTEGER,
                     grade REAL,
                     FOREIGN KEY(student_id) REFERENCES students(id),
                     FOREIGN KEY(subject_id) REFERENCES subjects(id));
     """)
    
    # Presenças

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                   student_id INTEGER,
                   date TEXT,
                     status TEXT,
                        FOREIGN KEY(student_id) REFERENCES students(id));
        """)
    
    conn.commit()
    conn.close()
    