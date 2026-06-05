from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib import colors
import os
import string

OUTPUT_DIR = "build"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "english_handwriting_practice_book.pdf")

PAGE_WIDTH, PAGE_HEIGHT = letter

LETTERS = {
    "A": "Apple",
    "B": "Ball",
    "C": "Cat",
    "D": "Dog",
    "E": "Elephant",
    "F": "Fish",
    "G": "Goat",
    "H": "Horse",
    "I": "Ice Cream",
    "J": "Jug",
    "K": "Kite",
    "L": "Lion",
    "M": "Monkey",
    "N": "Nest",
    "O": "Orange",
    "P": "Parrot",
    "Q": "Queen",
    "R": "Rabbit",
    "S": "Sun",
    "T": "Tiger",
    "U": "Umbrella",
    "V": "Van",
    "W": "Watch",
    "X": "X-ray",
    "Y": "Yak",
    "Z": "Zebra",
}


def draw_page_border(c):
    c.setStrokeColor(colors.black)
    c.setLineWidth(1.2)
    c.rect(0.35 * inch, 0.35 * inch, PAGE_WIDTH - 0.7 * inch, PAGE_HEIGHT - 0.7 * inch)


def draw_handwriting_row(c, y, left=0.65 * inch, right=7.85 * inch):
    top = y
    mid = y - 0.20 * inch
    base = y - 0.42 * inch
    bottom = y - 0.62 * inch

    c.setStrokeColor(colors.lightgrey)
    c.setLineWidth(1)

    c.line(left, top, right, top)
    c.line(left, base, right, base)
    c.line(left, bottom, right, bottom)

    c.setDash(3, 3)
    c.line(left, mid, right, mid)
    c.setDash()

    c.setStrokeColor(colors.black)


def draw_trace_text(c, text, y, size=42):
    draw_handwriting_row(c, y)

    c.setFont("Helvetica-Bold", size)
    c.setFillColor(colors.lightgrey)
    c.drawString(0.8 * inch, y - 0.50 * inch, text)
    c.setFillColor(colors.black)


def draw_blank_row(c, y):
    draw_handwriting_row(c, y)


def draw_picture_box(c, letter, word):
    x = 0.65 * inch
    y = PAGE_HEIGHT - 2.0 * inch
    w = 1.35 * inch
    h = 1.15 * inch

    c.setStrokeColor(colors.black)
    c.setLineWidth(1)
    c.roundRect(x, y, w, h, 8)

    c.setFont("Helvetica-Bold", 34)
    c.drawCentredString(x + w / 2, y + 0.55 * inch, letter)

    c.setFont("Helvetica", 9)
    c.drawCentredString(x + w / 2, y + 0.18 * inch, word)


def cover_page(c):
    draw_page_border(c)

    c.setFont("Helvetica-Bold", 30)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 2.0 * inch, "English Handwriting")
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 2.55 * inch, "Practice Book")

    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 3.35 * inch, "Capital and Small Letters")

    c.setFont("Helvetica", 15)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 4.2 * inch, "A to Z Alphabet Practice")
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 4.65 * inch, "Trace and Write")

    c.setFont("Helvetica-Bold", 50)
    c.setFillColor(colors.lightgrey)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 5.7 * inch, "A a  B b  C c")
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 6.5 * inch, "X x  Y y  Z z")
    c.setFillColor(colors.black)

    c.showPage()


def instruction_page(c):
    draw_page_border(c)

    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 1.0 * inch, "How to Use This Book")

    c.setFont("Helvetica", 15)
    y = PAGE_HEIGHT - 1.8 * inch

    instructions = [
        "1. Trace the grey letters carefully.",
        "2. Write the letters on the blank lines.",
        "3. Practice both capital and small letters.",
        "4. Say the word aloud while writing.",
        "5. Use pencil first for neat handwriting.",
    ]

    for line in instructions:
        c.drawString(0.8 * inch, y, line)
        y -= 0.45 * inch

    y -= 0.3 * inch
    draw_trace_text(c, "A A A A A", y, 40)
    y -= 0.85 * inch
    draw_trace_text(c, "a a a a a", y, 40)
    y -= 0.85 * inch
    draw_blank_row(c, y)

    c.showPage()


def alphabet_chart_page(c):
    draw_page_border(c)

    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 0.8 * inch, "Full Alphabet Chart")

    c.setFont("Helvetica-Bold", 22)
    y = PAGE_HEIGHT - 1.5 * inch
    x_start = 0.8 * inch
    gap_x = 1.25 * inch

    letters = list(string.ascii_uppercase)

    for i, letter in enumerate(letters):
        row = i // 5
        col = i % 5

        x = x_start + col * gap_x
        y_pos = y - row * 0.75 * inch

        c.setFillColor(colors.lightgrey)
        c.drawString(x, y_pos, f"{letter} {letter.lower()}")
        c.setFillColor(colors.black)

    c.showPage()


def letter_practice_page(c, letter):
    small = letter.lower()
    word = LETTERS[letter]

    draw_page_border(c)

    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 0.65 * inch, f"Letter {letter} {small}")

    draw_picture_box(c, letter, word)

    c.setFont("Helvetica-Bold", 18)
    c.drawString(2.3 * inch, PAGE_HEIGHT - 1.25 * inch, f"{letter} is for {word}")

    c.setFont("Helvetica-Bold", 60)
    c.setFillColor(colors.lightgrey)
    c.drawString(2.3 * inch, PAGE_HEIGHT - 2.0 * inch, f"{letter} {small}")
    c.setFillColor(colors.black)

    y = PAGE_HEIGHT - 2.6 * inch

    draw_trace_text(c, f"{letter} {letter} {letter} {letter} {letter}", y, 42)
    y -= 0.82 * inch

    draw_trace_text(c, f"{small} {small} {small} {small} {small}", y, 42)
    y -= 0.82 * inch

    draw_trace_text(c, f"{letter}{small} {letter}{small} {letter}{small} {letter}{small}", y, 42)
    y -= 0.82 * inch

    draw_blank_row(c, y)
    y -= 0.82 * inch

    draw_blank_row(c, y)
    y -= 0.82 * inch

    draw_trace_text(c, f"{word}   {word}", y, 32)
    y -= 0.82 * inch

    draw_blank_row(c, y)

    c.showPage()


def extra_practice_pages(c):
    # Capital alphabet practice page
    draw_page_border(c)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 0.65 * inch, "Capital Letters Practice")

    y = PAGE_HEIGHT - 1.4 * inch
    capital_rows = [
        "A B C D E F",
        "G H I J K L",
        "M N O P Q R",
        "S T U V W X",
        "Y Z",
    ]

    for row in capital_rows:
        draw_trace_text(c, row, y, 38)
        y -= 0.82 * inch
        draw_blank_row(c, y)
        y -= 0.82 * inch

    c.showPage()

    # Small alphabet practice page
    draw_page_border(c)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 0.65 * inch, "Small Letters Practice")

    y = PAGE_HEIGHT - 1.4 * inch
    small_rows = [
        "a b c d e f",
        "g h i j k l",
        "m n o p q r",
        "s t u v w x",
        "y z",
    ]

    for row in small_rows:
        draw_trace_text(c, row, y, 38)
        y -= 0.82 * inch
        draw_blank_row(c, y)
        y -= 0.82 * inch

    c.showPage()

    # Mixed alphabet practice page
    draw_page_border(c)
    c.setFont("Helvetica-Bold", 22)
    c.drawCentredString(PAGE_WIDTH / 2, PAGE_HEIGHT - 0.65 * inch, "Capital and Small Letters Practice")

    y = PAGE_HEIGHT - 1.4 * inch
    mixed_rows = [
        "Aa Bb Cc Dd",
        "Ee Ff Gg Hh",
        "Ii Jj Kk Ll",
        "Mm Nn Oo Pp",
        "Qq Rr Ss Tt",
        "Uu Vv Ww Xx",
        "Yy Zz",
    ]

    for row in mixed_rows:
        draw_trace_text(c, row, y, 34)
        y -= 0.75 * inch
        draw_blank_row(c, y)
        y -= 0.75 * inch

    c.showPage()


def create_pdf():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    c = canvas.Canvas(OUTPUT_FILE, pagesize=letter)

    cover_page(c)
    instruction_page(c)
    alphabet_chart_page(c)

    for letter in string.ascii_uppercase:
        letter_practice_page(c, letter)

    extra_practice_pages(c)

    c.save()
    print(f"PDF created: {OUTPUT_FILE}")


if __name__ == "__main__":
    create_pdf()
