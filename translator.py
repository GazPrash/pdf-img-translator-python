import sys
from deep_translator import GoogleTranslator
import pandas as pd


class Translator:
    def __init__(self, content) -> None:
        self.content = content
        self.size = len(content)
        if self.size > 500:
            self.exceeds_limit = True
        else:
            self.exceeds_limit = False

        self.lang_code_db = pd.read_csv("utils/language_codes.csv")

    def translate_to(self, language) -> str:
        tslated_text = ""
        lang_code = (
            self.lang_code_db[self.lang_code_db["English"] == language]["alpha2"]
            .to_string()
            .split()[1]
        )

        if self.exceeds_limit:
            # 22,342  ----> 22342 =  500(44) +  R
            # (THAT R HAS TO BE LESS THAN 500 BY DIV ALGO)
            mainlooplen = self.size // 500
            remlooplen = self.size % 500

            for i in range(mainlooplen):
                # print(tslated_text)
                tslated_text += GoogleTranslator(
                    source="auto", target=lang_code
                ).translate(text=self.content[i * 500 : (i + 1) * 500])

            tslated_text += GoogleTranslator(source="auto", target=lang_code).translate(
                text=self.content[:-(remlooplen)]
            )

        else:
            tslated_text = GoogleTranslator(source="auto", target=lang_code).translate(
                text=self.content
            )

        return tslated_text
