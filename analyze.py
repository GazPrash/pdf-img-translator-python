import sys
import pandas as pd
import langdetect as ldet
import matplotlib.pyplot as plt


class Analyze:
    def __init__(self, content: str, chartjs:bool = False) -> None:
        self.content = content
        self.plt = plt
        self.chartjs = chartjs

        self.lang_code_db = pd.read_csv("utils/language_codes.csv")

    def detect_language(self):
        lang_code = ldet.detect(self.content)
        return (
            self.lang_code_db[self.lang_code_db["alpha2"] == lang_code]["English"]
            .to_string()
            .split()[1]
        )

    def statistics(self):
        content_dict = {
            x: self.content.count(x) for x in self.content.split(" ") if x != ""
        }
        content_se = pd.Series(content_dict)
        content_se = content_se.sort_values(ascending=False).head(10)

        if self.chartjs:
            return content_se

        else:
            self.plt.figure(figsize=(15, 5))
            self.plt.plot(content_se.index, content_se, linewidth="2")
            plt.show()
