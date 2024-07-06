import PyPDF2

with open("dummy.pdf","rb") as file: #read  binary mode
    reader = PyPDF2.PdfFileReader(file)
    print(reader.numPages)

    # Rotate page
    page=reader.getPage(0)
    page.rotateClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open("tilt.pdf","wb") as new_file:
        writer.write(new_file)