import flet as ft
from views.login_view import LoginView

def main(page: ft.Page):
    page.title = "Sistema Escolar"
    page.window_width = 1000
    page.window_height = 700
    page.theme_mode = ft.ThemeMode.DARK

    # Inicia na tela de login
    login_view = LoginView(page)
    ft.app(target=main)