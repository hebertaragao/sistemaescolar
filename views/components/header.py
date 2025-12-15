import flet as ft
from config.settings import SCHOOL_NAME

def header(page: ft.Page):
    return ft.Container(
        content=ft.Row(
            [
                ft.Image(src="assets/logo.png", width=50, height=50),
                ft.Text(SCHOOL_NAME, size=22, weight="bold"),
            ],
            alignment=ft.MainAxisAlignment.START,
        ),
        padding=10,
        bgcolor=ft.colors.BLUE_100,
    )
