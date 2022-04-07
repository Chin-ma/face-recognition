from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

def invoiceGenerate(personName):
    
    tableData = [
        ["Name", "Fine reason", "Fine amount to be paid"],
        [personName, "No mask in public place", "200"], 
    ]

    docu = SimpleDocTemplate("invoice.pdf", pageSize = A4)
    styles = getSampleStyleSheet()

    doc_style = styles["Heading1"]
    doc_style.alignment = 1

    title = Paragraph("No mask Invoice", doc_style)
    style = TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (4, 4), 1, colors.chocolate),
        ("BACKGROUND", (0, 0), (3, 0), colors.skyblue),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ])

    table = Table(tableData, style=style)
    docu.build([title, table])

invoiceGenerate("personName")