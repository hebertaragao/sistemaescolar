from models.student import Student
from models.teacher import Teacher
from models.subject import Subject

def cadastrar_aluno(nome, nascimento, serie):
    aluno = Student(nome, nascimento, serie)
    aluno.save()
    return "Aluno cadastrado com sucesso!"

def cadastrar_professor(nome, disciplina):
    professor = Teacher(nome, disciplina)
    professor.save()
    return "Professor cadastrado com sucesso!"

def cadastrar_disciplina(nome):
    disciplina = Subject(nome)
    disciplina.save()
    return "Disciplina cadastrada com sucesso!"
