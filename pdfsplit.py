import PyPDF2
import os
from PyPDF2 import PdfFileWriter, PdfFileReader

inputname = ""
while (not os.path.isfile(inputname)):
    inputname = raw_input("Enter path to file: ")
    bool = os.path.isfile(str(inputname))
    if (not os.path.isfile(inputname)):
        print("Invalid file path (make sure it ends in .pdf)")

inputpdf = PdfFileReader(file(inputname, "rb"))

inputname = str(inputname).replace(".pdf", "")

for i in xrange(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    outputStream = file(inputname + "-%s.pdf" % i, "wb")
    output.write(outputStream)
    outputStream.close();

print("Success!")