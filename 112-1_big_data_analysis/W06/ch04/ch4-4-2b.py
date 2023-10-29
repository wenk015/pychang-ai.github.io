from bs4 import BeautifulSoup
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
with open("Surveys.html", "r", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, "lxml")
#import requests
#r = requests.get("https://fchart.github.io/ML/Surveys.html")
#r.encoding = "utf8"
#soup = BeautifulSoup(r.text, "lxml")  

# 搜尋特定屬性值的標籤
def print_a(tag_a):
    for tag in tag_a:
        print(tag["href"])
    print("-----------")    
tag_a = soup.select("a[href]")
print_a(tag_a)
tag_a = soup.select("a[href='http://example.com/q2']")
print_a(tag_a)
tag_a = soup.select("a[href^='http://example.com']")
print_a(tag_a)
tag_a = soup.select("a[href$='q3']")
print_a(tag_a)
tag_a = soup.select("a[href*='q']")
print_a(tag_a)