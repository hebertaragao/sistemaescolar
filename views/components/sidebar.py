import flet as ft

def sidebar(page: ft.Page, on_nav):
    return ft.Container(
        content=ft.Column(
            [
                ft.Text("Menu", size=18, weight="bold"),
                ft.ElevatedButton("Administração", on_click=lambda e: on_nav("admin")),
                ft.ElevatedButton("Professor", on_click=lambda e: on_nav("teacher")),
                ft.ElevatedButton("Aluno", on_click=lambda e: on_nav("student")),
                ft.ElevatedButton("Sair", on_click=lambda e: on_nav("logout")),
            ],
            spacing=10,
        ),
        width=200,
        bgcolor=ft.colors.BLUE_50,
        padding=10,
    )
