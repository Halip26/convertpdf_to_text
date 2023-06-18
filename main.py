import PyPDF2
import os


if(os.path.isdir("temp") == False):
    os.mkdir("temp")

txtpath = ""
pdfpath = ""


# Berikan jalur untuk pdf kamu di sini
pdfpath = input(
    "Enter the name of your pdf file - please use backslash when typing in directory path: ")
# Sediakan jalur untuk file teks keluaran
txtpath = input(
    "Enter the name of your txt file - please use backslash when typing in directory path: ")

# Ini adalah contoh direktori dasar di mana semua file teks kamu akan disimpan jika kamu tidak memberikan jalur tertentu
BASEDIR = os.path.realpath("temp")
print(BASEDIR)


if(len(txtpath) == 0):
    txtpath = os.path.join(BASEDIR, os.path.basename(
        os.path.normpath(pdfpath)).replace(".pdf", "")+".txt")
pdfobj = open(pdfpath, 'rb')

pdfread = PyPDF2.PdfFileReader(pdfobj)

x = pdfread.numPages

for i in range(x):
    pageObj = pdfread.getPage(i)
    with open(txtpath, 'a+') as f:
        f.write((pageObj.extractText()))
    # Ini hanya memberikan gambaran umum tentang apa yang ditambahkan ke output kamu, kamu dapat menghapusnya jika mau
    print(pageObj.extractText())

pdfobj.close()
