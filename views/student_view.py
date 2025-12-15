import flet as ft
from controllers.student_controller import visualizar_boletim, visualizar_faltas

def student_view(page: ft.Page):
    student_id = ft.TextField(label="ID do Aluno")
    boletim_output = ft.Column()
    faltas_output = ft.Column()

    def mostrar_boletim(e):
        boletim = visualizar_boletim(student_id.value)
        boletim_output.controls.clear()
        for disciplina, nota in boletim:
            boletim_output.controls.append(ft.Text(f"{disciplina}: {nota}"))
        page.update()

    def mostrar_faltas(e):
        faltas = visualizar_faltas(student_id.value)
        faltas_output.controls.clear()
        for data, status in faltas:
            faltas_output.controls.append(ft.Text(f"{data}: {status}"))
        page.update()

    page.add(
        ft.Column([
            ft.Text("Portal do Aluno", size=20, weight="bold"),
            student_id,
            ft.Row([
                ft.ElevatedButton("Ver Boletim", on_click=mostrar_boletim),
                ft.ElevatedButton("Ver Faltas", on_click=mostrar_faltas)
            ]),
            boletim_output,
            faltas_output
        ])
    )
