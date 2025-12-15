import flet as ft
from controllers.admin_controller import cadastrar_aluno, cadastrar_professor, cadastrar_disciplina

def admin_view(page: ft.Page):
    nome_aluno = ft.TextField(Label = "Nome do Aluno")
    nascimento = ft.TextField("Data de Nascimento")
    serie = ft.TextField(label="Série")
    msg = ft.Text("")

    def salvar_aluno(e):
        msg.value = cadastrar_aluno(nome_aluno.value, nascimento.value, serie.value)
        page.update()

    page.add(
        ft.Column([
            ft.Text("Painel Administrativo", size=20, weight="bold"),
            nome_aluno,
            nascimento,
            serie,
            ft.ElevatedButton("Cadastrar Aluno", on_click=salvar_aluno),
            msg
        ])
    )