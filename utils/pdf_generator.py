from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from database.connection import get_connection
from config.settings import SCHOOL_NAME

def gerar_boletim(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    # Buscar dados do aluno
    cursor.execute("SELECT name, grade FROM students WHERE id=?", (student_id,))
    aluno = cursor.fetchone()
    if not aluno:
        conn.close()
        return None

    nome_aluno, serie = aluno

    # Buscar notas
    cursor.execute("""
        SELECT subjects.name, grades.grade
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE grades.student_id=?
    """, (student_id,))
    notas = cursor.fetchall()

    # Buscar faltas
    cursor.execute("SELECT date, status FROM attendance WHERE student_id=?", (student_id,))
    faltas = cursor.fetchall()

    conn.close()

    # Criar PDF
    filename = f"{nome_aluno.replace(' ', '_')}_boletim.pdf"
    doc = SimpleDocTemplate(filename, pagesize=A4)
    elements = []
    styles = getSampleStyleSheet()

    # Cabeçalho com logo e nome da escola
    try:
        logo = Image("assets/logo.png", width=60, height=60)
        header_table = Table([[logo, Paragraph(f"<b>{SCHOOL_NAME}</b>", styles["Title"])]], colWidths=[70, 400])
        elements.append(header_table)
    except:
        elements.append(Paragraph(f"<b>{SCHOOL_NAME}</b>", styles["Title"]))
    elements.append(Spacer(1, 20))

    # Dados do aluno
    elements.append(Paragraph(f"Aluno: <b>{nome_aluno}</b>", styles["Normal"]))
    elements.append(Paragraph(f"Série: <b>{serie}</b>", styles["Normal"]))
    elements.append(Spacer(1, 20))

    # Tabela de notas
    data_notas = [["Disciplina", "Nota", "Status"]]
    media_total = 0
    qtd_notas = 0
    for disciplina, nota in notas:
        status = "Aprovado" if nota >= 7 else "Reprovado"
        data_notas.append([disciplina, f"{nota:.1f}", status])
        media_total += nota
        qtd_notas += 1

    if qtd_notas > 0:
        media_final = media_total / qtd_notas
        resultado_final = "Aprovado" if media_final >= 7 else "Reprovado"
        data_notas.append(["Média Final", f"{media_final:.1f}", resultado_final])

    tabela_notas = Table(data_notas, colWidths=[200, 100, 150])
    tabela_notas.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightblue),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 12),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
    ]))
    elements.append(Paragraph("<b>Notas</b>", styles["Heading2"]))
    elements.append(tabela_notas)
    elements.append(Spacer(1, 20))

    # Tabela de faltas
    data_faltas = [["Data", "Status"]] + [[data, status] for data, status in faltas]
    tabela_faltas = Table(data_faltas, colWidths=[200, 150])
    tabela_faltas.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("TEXTCOLOR", (0,0), (-1,0), colors.black),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("BOTTOMPADDING", (0,0), (-1,0), 12),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
    ]))
    elements.append(Paragraph("<b>Presenças/Faltas</b>", styles["Heading2"]))
    elements.append(tabela_faltas)

    # Gerar PDF
    doc.build(elements)
    return filename