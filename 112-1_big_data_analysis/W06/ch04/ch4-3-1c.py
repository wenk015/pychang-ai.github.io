from bs4 import BeautifulSoup
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 使用HTML5的data-屬性搜尋<div>標籤
tag_div = soup.find(attrs={"data-custom": "important"})
print(tag_div.text)


