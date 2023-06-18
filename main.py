# create code that can be convert pdf file to txt
import os
from pdfreader import SimplePDFViewer

# Create directory if it doesn't exist
if not os.path.exists("hasil"):
    os.makedirs("hasil")

# Open the PDF file in read-binary mode
with open("sample.pdf", 'rb') as pdf_file:

    # Create a PDF viewer object
    pdf_viewer = SimplePDFViewer(pdf_file)

    # Iterate through each page in the PDF document
    for idx, canvas in enumerate(pdf_viewer):

        # Get the text from the current page
        page_text = "".join(canvas.strings)

        # Define file name
        output_name = f"hasil/example-page{idx}.txt"

        # Write extracted text to txt file
        with open(output_name, 'w') as txt_file:
            txt_file.write(page_text)
