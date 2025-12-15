import flet as ft
from controllers.teacher_controller import lancar_nota, lancar_falta

def teacher_view(page: ft.Page):
    student_id = ft.TextField(label="ID do Aluno")
    subject_id = ft.TextField(label="ID da Disciplina")
    grade = ft.TextField(label="Nota")
    msg = ft.Text("")

    def salvar_nota(e):
        msg.value = lancar_nota(student_id.value, subject_id.value, grade.value)
        page.update()

    page.add(
        ft.Column([
            ft.Text("Painel do Professor", size=20, weight="bold"),
            student_id,
            subject_id,
            grade,
            ft.ElevatedButton("Lançar Nota", on_click=salvar_nota),
            msg
        ])
    )
