import os
import PyPDF2

def merge_pdfs(folder_path, output_path):
    # Get list of PDF files in the folder
    pdf_files = [f for f in os.listdir(folder_path) if f.endswith('.pdf')]

    # Create a PdfWriter object
    pdf_writer = PyPDF2.PdfWriter()

    # Merge each PDF file into the PdfWriter object
    for pdf_file in pdf_files:
        with open(os.path.join(folder_path, pdf_file), 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

    # Write the merged PDF to the output file
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

if __name__ == "__main__":
    folder_path = 'balkan-football/'  # Change this to the path of your folder
    output_path = 'football-in-balkans.pdf'  # Change this to the desired output file path
    merge_pdfs(folder_path, output_path)
