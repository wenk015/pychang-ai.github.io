from bs4 import BeautifulSoup
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋兄弟標籤
tag_div = soup.find(id="q1")
print(tag_div.p.a.text)
print("-----------")
tag_div = soup.select("#q1 ~ .survey")
for item in tag_div:            
    print(item.p.a.text)  
print("-----------")
tag_div = soup.select("#q1 + .survey")
for item in tag_div:            
    print(item.p.a.text)   


