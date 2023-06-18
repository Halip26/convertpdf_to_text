# create code that can be convert pdf file to txt
import os
import sys
import warnings
from pdfreader import SimplePDFViewer

# cek apakah direktori sudah ada
if len(sys.argv) < 2:
    print("Usage: python main.py <pdf_file>")
    sys.exit(1)

# get pdf filename from command line argument
pdf_file_name = sys.argv[1]

# Membuat direktori jika belum ada
if not os.path.exists("hasil"):
    os.makedirs("hasil")

# Membuka file PDF dengan mode baca biner
with open(pdf_file_name, "rb") as pdf_file:

    # create SimplePDFViewer object
    pdf_viewer = SimplePDFViewer(pdf_file)

    # Filtering warning data binary
    warnings.filterwarnings("ignore", category=Warning)

    # Melakukan iterasi tiap halaman pada dokumen PDF
    for idx, canvas in enumerate(pdf_viewer):

        # Mendapatkan teks dari halaman saat ini
        page_text = "".join(canvas.strings)

        # Menentukan nama file hasil
        output_name = f"hasil/{os.path.splitext(os.path.basename(pdf_file_name))[0]}-page{idx}.txt"

        # Menulis teks hasil ekstraksi ke dalam file teks
        with open(output_name, "w") as txt_file:
            txt_file.write(page_text)
