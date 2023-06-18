# create code that can be convert pdf file to txt
import os
import warnings
from pdfreader import SimplePDFViewer

# Membuat direktori jika belum ada
if not os.path.exists("hasil"):
    os.makedirs("hasil")

# Membuka file PDF dengan mode baca biner
with open("./pdf_file/contoh.pdf", "rb") as pdf_file:

    # Membuat objek SimplePDFViewer
    pdf_viewer = SimplePDFViewer(pdf_file)

    # Filtering warning data binary
    warnings.filterwarnings("ignore", category=Warning)

    # Melakukan iterasi tiap halaman pada dokumen PDF
    for idx, canvas in enumerate(pdf_viewer):

        # Mendapatkan teks dari halaman saat ini
        page_text = "".join(canvas.strings)

        # Menentukan nama file hasil
        output_name = f"hasil/example-page{idx}.txt"

        # Menulis teks hasil ekstraksi ke dalam file teks
        with open(output_name, "w") as txt_file:
            txt_file.write(page_text)
