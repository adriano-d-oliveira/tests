import json
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

def pdf_to_json(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    data = {}
    for page in PDFPage.get_pages(pdf_file):
        interpreter.process_page(page)
        data['text'] = retstr.getvalue()
    return json.dumps(data)

# Usage:

# pdf_file = open('test.pdf', 'rb')
# json_data = pdf_to_json(