# For extracting text from pdf and imgs
import sys
import pdfplumber as pdpl
from image_parser import OcrParser


class Parser:
    def __init__(
        self, doc_file_path: str, encryption: bool, password: str = None
    ) -> None:
        self.doc_file_path = doc_file_path
        self.parser = pdpl
        self.encryption = encryption
        self.password = password
        self.res_text = ""

    def parse_auto(self, util: str):
        if "pdf" in self.doc_file_path:
            if self.encryption:
                # write some code for decrypting pdf first | with pass or brute etc...
                pass
            return self.pdf_extract(pw=self.password)

        return self.img_extract()

    def pdf_extract(self, pw: str = None) -> str:
        with self.parser.open(self.doc_file_path, password=pw) as pdf:
            total_pages = len(pdf.pages)
            for i in range(total_pages):
                page_this = pdf.pages[i]
                if page_this.extract_text() is None:
                    print("True")
                self.res_text += page_this.extract_text()#TODO=>New line after every page

        return self.res_text

    def img_extract(self, img_path) -> str:
        # parsing image text using openCV and Tesseract
        ocr = OcrParser(img_path)
        ocr.initialize_tesseract()
        
        return ocr.extract()
