from bs4 import BeautifulSoup
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")      
    
# 使用多條件來搜尋HTML標籤
tag_div = soup.find("div", class_="question")
print(tag_div.prettify())
tag_p = soup.find("p", class_="question")
print(tag_p.prettify())

