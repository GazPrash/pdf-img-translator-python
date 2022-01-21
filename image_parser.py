import os
import cv2
import pytesseract
from translator import Translator

class OcrParser:
    def __init__(self, img_path) -> None:
        self.img_path = img_path

    def initialize_tesseract(self):
        tesseract_executable_path = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe" # alternatively --> os.environ
        pytesseract.pytesseract.tesseract_cmd = tesseract_executable_path

    def extract(self, translate_to:str = None) -> str:
        # load image
        img = cv2.imread(self.img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        output_text = pytesseract.image_to_string(img)

        if translate_to:
            tslate = Translator(output_text)
            return tslate.translate_to(translate_to)

        return output_text
