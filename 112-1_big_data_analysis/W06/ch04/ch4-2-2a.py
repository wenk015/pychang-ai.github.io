from bs4 import BeautifulSoup

import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")

tags = soup("img")
tag = tags[0]
print("圖片網址: ", tag.get("src", None))
print("alt屬性: ", tag["alt"])
print("屬性: ", tag.attrs)


