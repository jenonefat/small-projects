import PyPDF2
import os


def merge_pdf():
    # grabbing current working directory
    cwd = os.getcwd()
    # creating a PDF merger object
    merger = PyPDF2.PdfMerger()
    # iterate through all files in directory
    for file in os.listdir(cwd):
        if file.endswith(".pdf"):
            # append each PDF file to merger object
            merger.append(file)
            # naming output file for merged PDFs
            merger.write("combined.pdf")
            print(file)


if __name__ == "__main__":
    merge_pdf()