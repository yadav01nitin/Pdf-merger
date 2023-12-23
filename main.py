import PyPDF2

pdfiles=['1.pdf','2.pdf']
merger = PyPDF2.PdfMerger()

for filename in pdfiles:
    pdfFile=open(filename,'rb')
    pdfReader=PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()

merger.write("NewMergedFile.pdf")







'''
import PyPDF2

mergeFile = PyPDF2.PdfMerger()

mergeFile.append(PyPDF2.PdfReader('1.pdf', 'rb'))

mergeFile.append(PyPDF2.PdfReader('2.pdf', 'rb'))

mergeFile.write("NewMergedFile.pdf")
'''