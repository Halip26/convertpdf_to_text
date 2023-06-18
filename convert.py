import PyPDF2

pdf_path = 'C:\Users\HALIP 26\Documents\python-scripts\convertpdf_to_text\pdf_file\contoh.pdf'
txt_path = '\hasil\hasil.txt'

with open(pdf_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)
    with open(txt_path, 'w') as txt_file:
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            txt_file.write(page.extractText())
