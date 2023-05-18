import PyPDF2
import fitz
import pytesseract
from PIL import Image
from io import BytesIO

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

pdf_path = 'document.pdf'
doc = fitz.open(pdf_path)

# Открываем PDF-файл и считываем первые две страницы (или меньше, если страниц меньше двух)
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = min(pdf_reader.getNumPages(), 2)
    for i in range(num_pages):
        page = pdf_reader.getPage(i)
        print(page.extractText())

image_xrefs = {}

all_text = ""

for i in range(min(2, len(doc))):
    page = doc[i]
    all_text += page.get_text()

    for image in page.get_images():
        image_xrefs.setdefault(image[0])

for index, xref in enumerate(image_xrefs):
    img = doc.extract_image(xref)
    text = pytesseract.image_to_string(Image.open(BytesIO(img["image"])), lang="rus")

    print(text)
