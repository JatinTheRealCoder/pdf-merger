from pypdf import PdfWriter

merger = PdfWriter()
pdfs=[]
n = int(input("how many pdf you want to merge?"))
for i in range(0,n):
    name = input(f"Enter the name of {i+1} pdf:")
    pdfs.append(name)
for pdf in pdfs :
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()