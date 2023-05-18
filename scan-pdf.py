import PyPDF2

pdf_path = 'document.pdf' # укажите путь к PDF-файлу здесь

# Открываем PDF-файл и считываем первые две страницы (или меньше, если страниц меньше двух)
with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    num_pages = min(pdf_reader.getNumPages(), 2)
    for i in range(num_pages):
        page = pdf_reader.getPage(i)
        print(page.extractText())

