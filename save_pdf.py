from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

def save_to_pdf(summary, font_choice, font_size, font_color, filename):
    font_name = "Helvetica"

    if font_choice == "OpenDyslexic":
        font_path = os.path.join(os.path.dirname(__file__), "open-dyslexic.ttf")
        try:
            pdfmetrics.registerFont(TTFont("OpenDyslexic", font_path))
            font_name = "OpenDyslexic"
        except Exception as e:
            print(f"Not able to load OpenDyslexic. Using default. Error: {e}")
            font_name = "Helvetica"

    elif font_choice == "Tiresias":
        font_path = os.path.join(os.path.dirname(__file__), "Tiresias_Infofont.ttf")
        try:
            pdfmetrics.registerFont(TTFont("Tiresias", font_path))
            font_name = "Tiresias"
        except Exception as e:
            print(f"Not able load Tiresias font. Using default. Error: {e}")
            font_name = "Helvetica"

    elif font_choice == "Tahoma":
        font_path = os.path.join(os.path.dirname(__file__), "Tahoma.ttf")
        try:
            pdfmetrics.registerFont(TTFont("Tahoma", font_path))
            font_name = "Tahoma"
        except Exception as e:
            print(f"Not able load Tiresias font. Using default. Error: {e}")
            font_name = "Helvetica"
   
    elif font_choice == "Verdana":
        font_path = os.path.join(os.path.dirname(__file__), "Verdana.ttf")
        try:
            pdfmetrics.registerFont(TTFont("Verdana", font_path))
            font_name = "Verdana"
        except Exception as e:
            print(f"Not able load Tiresias font. Using default. Error: {e}")
            font_name = "Helvetica"
   
    elif font_choice == "Garamond":
        font_path = os.path.join(os.path.dirname(__file__), "Garamond.ttf")
        try:
            pdfmetrics.registerFont(TTFont("Garamond", font_path))
            font_name = "Garamond"
        except Exception as e:
            print(f"Not able load Tiresias font. Using default. Error: {e}")
            font_name = "Helvetica"

    c = canvas.Canvas(filename, pagesize=LETTER)
    c.setFont(font_name, font_size)
    c.setFillColor(font_color)

    x, y = 72, 720
    line_spacing_multiplier = 1.5
    paragraph_spacing_multiplier = 2.0

    line_height = int(font_size * line_spacing_multiplier)
    paragraph_spacing = int(font_size * paragraph_spacing_multiplier)
    max_width = 460

    for paragraph in summary.split('\n'):
        words = paragraph.split()
        line = ""
        for word in words:
            test_line = f"{line} {word}".strip()
            if c.stringWidth(test_line, font_name, font_size) <= max_width:
                line = test_line
            else:
                c.drawString(x, y, line)
                y -= line_height
                line = word
        if line:
            c.drawString(x, y, line)
            y -= line_height
        y -= (paragraph_spacing - line_height)

    c.save()
    print(f"\n PDF saved as: {filename} using font: {font_name}")
