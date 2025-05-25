# save html file on local for futur analysis (usefull when bug on html)
from pathlib import Path

def save_html_file_for_futur_analysis(file_name, response):
    Path("../outpout/").mkdir(parents=True, exist_ok=True)
    with open("../outpout/"+file_name+".html", "w", encoding="utf-8") as f:
        f.write(response.text)