import flet as ft
from controllers.student_controller import visualizar_boletim, visualizar_faltas
from utils.pdf_generator import gerar_boletim

def student_view(page: ft.Page):
    student_id = ft.TextField(label="ID do Aluno")
    boletim_output = ft.Column()
    faltas_output = ft.Column()
    msg = ft.Text("")
    download_button = ft.ElevatedButton("Download PDF", disabled=True)
    progress_bar = ft.ProgressBar(width=300, visible=False)

    def mostrar_boletim(e):
        boletim = visualizar_boletim(student_id.value)
        boletim_output.controls.clear()
        for disciplina, nota in boletim:
            status = "Aprovado" if nota >= 7 else "Reprovado"
            boletim_output.controls.append(ft.Text(f"{disciplina}: {nota} - {status}"))
        page.update()

    def mostrar_faltas(e):
        faltas = visualizar_faltas(student_id.value)
        faltas_output.controls.clear()
        for data, status in faltas:
            faltas_output.controls.append(ft.Text(f"{data}: {status}"))
        page.update()

    def gerar_pdf(e):
        # Mostrar barra de progresso
        progress_bar.visible = True
        progress_bar.value = None  # animação indeterminada
        msg.value = "Gerando boletim..."
        page.update()

        # Simular processamento
        filename = gerar_boletim(student_id.value)

        # Ocultar barra de progresso
        progress_bar.visible = False

        if filename:
            msg.value = "Boletim gerado com sucesso!"
            # Ativa botão de download estilizado
            download_button.disabled = False
            download_button.icon = ft.icons.DOWNLOAD
            download_button.text = "Baixar Boletim PDF"
            download_button.bgcolor = ft.colors.BLUE
            download_button.color = ft.colors.WHITE
            download_button.on_click = lambda ev: page.launch_url(filename)

            # SnackBar de confirmação
            page.snack_bar = ft.SnackBar(
                ft.Text("📄 Boletim pronto para download!"),
                bgcolor=ft.colors.GREEN,
                open=True
            )
        else:
            msg.value = "Aluno não encontrado."
            page.snack_bar = ft.SnackBar(
                ft.Text("⚠️ Erro: aluno não encontrado."),
                bgcolor=ft.colors.RED,
                open=True
            )
        page.update()

    page.add(
        ft.Column([
            ft.Text("Portal do Aluno", size=20, weight="bold"),
            student_id,
            ft.Row([
                ft.ElevatedButton("Ver Boletim", on_click=mostrar_boletim),
                ft.ElevatedButton("Ver Faltas", on_click=mostrar_faltas),
                ft.ElevatedButton("Gerar PDF", on_click=gerar_pdf),
            ]),
            progress_bar,
            boletim_output,
            faltas_output,
            msg,
            download_button
        ])
    )