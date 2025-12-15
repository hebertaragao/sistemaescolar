from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

def gerar_boletim(aluno, notas):
    c = canvas.Canvas(f"{aluno}_boletim.pdf", pagesize=A4)
    c.drawString(100, 800, f"Boletim Escolar - {aluno}")
    y = 750
    for disciplina, nota in notas.items():
        c.drawString(100, y, f"{disciplina}: {nota}")
        y -= 30
    c.save()
