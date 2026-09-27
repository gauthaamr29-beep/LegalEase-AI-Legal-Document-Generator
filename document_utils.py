from io import BytesIO
from docx import Document
from docx.shared import Pt
from fpdf import FPDF

def sanitize_text(text):
    for old, new in {"“": '"', "”": '"', "‘": "'", "’": "'", "–": "-", "—": "-"}.items():
        text = text.replace(old, new)
    return text

def format_docx(text, doc_type):
    doc = Document()
    title = doc.add_paragraph()
    run = title.add_run(doc_type.upper())
    run.bold = True
    run.font.size = Pt(16)

    for line in sanitize_text(text).splitlines():
        p = doc.add_paragraph(line)
        for run in p.runs:
            run.font.name = "Times New Roman"
            run.font.size = Pt(11)

    output = BytesIO()
    doc.save(output)
    output.seek(0)
    return output

class LegalPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 8, "LegalEase", align="C")
        self.ln(8)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", size=8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

def format_pdf(text, doc_type):
    pdf = LegalPDF()
    pdf.set_auto_page_break(auto=True, margin=18)
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, sanitize_text(doc_type), ln=True, align="C")
    pdf.ln(5)
    pdf.set_font("Helvetica", size=11)
    for paragraph in sanitize_text(text).splitlines():
        if paragraph.strip():
            pdf.multi_cell(0, 7, paragraph)
            pdf.ln(2)
    return BytesIO(bytes(pdf.output(dest="S")))
