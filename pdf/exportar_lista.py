from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from pathlib import Path


def exportar_lista_pdf(publicadores, titulo="Lista de Publicadores"):
    pasta = Path("dados/exports")
    pasta.mkdir(parents=True, exist_ok=True)

    arquivo = pasta / "lista_publicadores.pdf"

    c = canvas.Canvas(str(arquivo), pagesize=A4)
    y = 800

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, titulo)
    y -= 30

    c.setFont("Helvetica", 11)

    for nome in publicadores:
        if y < 50:
            c.showPage()
            y = 800
        c.drawString(50, y, nome)
        y -= 20

    c.save()
    return arquivo
