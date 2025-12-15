import flet as ft
from controllers.auth_controller import login
from views.admin_view import admin_view
from views.teacher_view import teacher_view
from views.student_view import student_view

def login_view(page: ft.Page):
    username = ft.TextField(label="Usuário")
    password = ft.TextField(label="Senha", password=True, can_reveal_password=True)
    message = ft.Text("")

    def handle_login(e):
        result = login(username.value, password.value)
        if result["status"] == "success":
            page.controls.clear()
            if result["role"] == "admin":
                admin_view(page)
            elif result["role"] == "teacher":
                teacher_view(page)
            else:
                student_view(page)
            page.update()
        else:
            message.value = result["message"]
            page.update()

    page.add(
        ft.Column([
            ft.Text("Login - Sistema Escolar", size=20, weight="bold"),
            username,
            password,
            ft.ElevatedButton("Entrar", on_click=handle_login),
            message
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )
