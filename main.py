from text_parser import Parser
from translator import Translator

pdf_path = "dotslash.pdf"

p1 = Parser(doc_file_path= pdf_path, encryption= False, password= None)
content = p1.pdf_extract()

print(content)

# t1 = Translator(content)
# print(t1.translate_to('Ukrainian'))
