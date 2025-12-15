import flet as ft
from views.components.header import header
from views.components.sidebar import sidebar
from controllers.admin_controller import cadastrar_aluno

def admin_view(page: ft.Page):
    nome_aluno = ft.TextField(label="Nome do Aluno")
    nascimento = ft.TextField(label="Data de Nascimento")
    serie = ft.TextField(label="Série")
    msg = ft.Text("")

    def salvar_aluno(e):
        msg.value = cadastrar_aluno(nome_aluno.value, nascimento.value, serie.value)
        page.update()

    def navegar(destino):
        page.controls.clear()
        if destino == "teacher":
            from views.teacher_view import teacher_view
            teacher_view(page)
        elif destino == "student":
            from views.student_view import student_view
            student_view(page)
        elif destino == "logout":
            from views.login_view import login_view
            login_view(page)
        else:
            admin_view(page)
        page.update()

    page.add(
        ft.Row([
            sidebar(page, navegar),
            ft.Column([
                header(page),
                ft.Text("Painel Administrativo", size=20, weight="bold"),
                nome_aluno,
                nascimento,
                serie,
                ft.ElevatedButton("Cadastrar Aluno", on_click=salvar_aluno),
                msg
            ], expand=True)
        ])
    )
