# create code that can be convert pdf file to txt
import PyPDF2
import os


# Create directory if it doesn't exist
if not os.path.exists("hasil"):
    os.makedirs("hasil")

# Open the PDF file in read-binary mode
with open("sample.pdf", 'rb') as pdf_file:

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the total number of pages in the PDF document
    num_pages = pdf_reader.getNumPages()

    # Loop through each page in the document
    for page_num in range(num_pages):

        # Get the current page object
        page_obj = pdf_reader.getPage(page_num)

        # Extract the text from the current page
        page_text = page_obj.extractText()

        # Define file name
        output_name = f"hasil/example-page{page_num}.txt"

        # Write extracted text to txt file
        with open(output_name, 'w') as txt_file:
            txt_file.write(page_text)
