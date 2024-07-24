import re
from pdfminer.high_level import extract_text,extract_pages
import pdfplumber

with pdfplumber.open('lib/1018.pdf') as pdf:
    pages = pdf.pages
    for page in pages:
        print(page.extract_text())