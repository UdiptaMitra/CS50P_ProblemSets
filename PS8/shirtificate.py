"""Suppose that you’d like to implement a CS50 “shirtificate,” a PDF with an image of an I took CS50 t-shirt, shirtificate.png, customized with a user’s own name.
Implement a program that prompts the user for their name and outputs, using fpdf2, a CS50 shirtificate in a file called shirtificate.pdf similar to this one for John Harvard,
The orientation of the PDF should be Portrait.
The format of the PDF should be A4, which is 210mm wide by 297mm tall.
The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
The shirt’s image should be centered horizontally.
The user’s name should be on top of the shirt, in white text.
All other details we leave to you. You’re even welcome to add borders, colors, and lines. Your shirtificate needn’t match John Harvard’s precisely.
And no need to wrap long names across multiple lines.
Before writing any code, do read through fpdf2’s tutorial to learn how to use it. Then skim fpdf2’s API (application programming interface) to see all of its functions
and parameters therefore.
No need to submit any PDFs with your code. But, if you would like, you’re welcome (but not expected) to share a shirtificate with your name on it in any of CS50’s communities!
Note that fpdf2 comes with a class called FPDF, which has quite a few methods, per py-pdf.github.io/fpdf2/fpdf/#fpdf.FPDF. You can install it with:
Note that you can extend FPDF and instantiate your own subclass thereof in order to add a header to every page of a PDF,
per py-pdf.github.io/fpdf2/Tutorial.html#tuto-2-header-footer-page-break-and-image. Or you can add it as text yourself.
Note that you can disable automatic page breaks, which might otherwise cause your PDF to overflow from one page to two, with set_auto_page_break,
per py-pdf.github.io/fpdf2/Margins.html.
Note that a cell’s height can be negative, to move it upward.
You can open shirtificate.pdf, once outputted, by clicking it in VS Code’s file explorer.
"""

from fpdf import FPDF

name = input("Enter name: ")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Helvetica", "B", 40)
pdf.cell(0, 30, "CS50 Shirtificate", align="C")
image_width = 180
x = (pdf.w - image_width) / 2
pdf.image("image.png", x=x, y=60, w=image_width)
pdf.set_font("Helvetica", "B", 24)
pdf.set_text_color(255, 255, 255)
pdf.text(x=60, y=140, text=f"{name} took CS50")
pdf.output("shirtificate.pdf")
