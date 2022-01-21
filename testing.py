#           Project Tree
#       Driver ----->  Main program that process the input info via API or Command Line.
#       Langauge Detection ---> using langdect
#       Translation -----> using Google Translate Library
#       Text Extraction from Image, PDF ------> using OpenCV
#       Extra Utility Stuff -----------> TODO
#
#
#
#
#
#
#
#
#

# import googletrans
# import langdetect as ldet
# from googletrans import Translator

# import PyPDF2 as pydf
# import pdfplumber as plum


# with plum.open("dotslash.pdf") as pdf:
#     page1 = pdf.pages[1]
#     p1info = page1.extract_text()

from deep_translator import GoogleTranslator

stuff = "Si vous parlez anglais sur ce serveur, plus de personnes seront en mesure de vous aider. Merci."
tslate = GoogleTranslator(source= 'auto', target='en').translate(text= stuff)
print(tslate)

# output : If you speak English on this server, more people will be able to help you. Thank you.



# streamp = "dotslash.pdf"
# file = open("docc.pdf", "rb")


# read = pydf.PdfFileReader(stream= file)
# out = read.getPage(0)


# print(read.)

# print(read.getNumPages())
# print()
# readpage = pydf.PdfFileReader(stream= out)

# print(out.extractText())


# response = ldet.detect("hombre")

# translator = Translator()
# perf = translator.translate("Hi There")

# print(perf.text)



