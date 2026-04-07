'''from fpdf import FPDF

def save_notes_as_pdf(notes, file_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in notes.split("\n"):
        line = line.encode("latin-1", "replace").decode("latin-1")
        pdf.multi_cell(0, 10, line)

    pdf.output(file_path)
    return file_path '''

from fpdf import FPDF

def save_notes_as_pdf(notes, file_path):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=12)

    lines = notes.split("\n")

    for line in lines:

        # TITLE formatting
        if line.startswith("TITLE"):
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, line, ln=True)
            pdf.ln(5)

        # HEADINGS
        elif line.strip().isdigit() or line.isupper():
            pdf.set_font("Arial", "B", 14)
            pdf.cell(0, 10, line, ln=True)
            pdf.ln(3)

        # BULLETS
        elif line.startswith("-"):
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 8, line)
            pdf.ln(2)

        else:
            pdf.set_font("Arial", size=12)
            pdf.multi_cell(0, 8, line)
            pdf.ln(2)

    pdf.output(file_path)
    return file_path