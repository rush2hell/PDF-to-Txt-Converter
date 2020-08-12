from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
import io

pdf_path = "Path for PDF File"

pdf = open(pdf_path, 'rb')
temp_memory = io.StringIO()

lp = LAParams()
res_man = PDFResourceManager()
convert_text = TextConverter(res_man, temp_memory, laparams=lp)
interpreter = PDFPageInterpreter(res_man, convert_text)


for i in PDFPage.get_pages(pdf):
    interpreter.process_page(i)
    text = temp_memory.getvalue()

file = open("Path of Text file",'wb')
file.write(text.encode('utf-8'))
