from fpdf import FPDF


class PDF(FPDF):
    def header(self):
        # Rendering logo:
        self.image("/home/anuj/programs/cs50p/p8/shirtificate.png", 0.5, 55)
        # Setting font: helvetica bold 15
        self.set_font("helvetica", "B", 56)
        # Printing title:
        self.cell(0, 30, "CS50 Shirtificate", border=0, align="C")
        # printing name
        self.set_font("helvetica", "B", 32)
        self.cell(-180, 200, f"{name} took CS50", border=0, align="C")
        # Performing a line break:
        self.auto_page_break

name = input("Name: ")

# Instantiation of inherited class
pdf = PDF(format=(210, 297))
pdf.add_page(format=(210, 297))
pdf.output("/home/anuj/programs/cs50p/p8/shirtificate.pdf")
