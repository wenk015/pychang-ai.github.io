import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: " + os.getcwd())

titanic = pd.read_csv("titanic_data.csv")
# 顯示前5筆
print(titanic.head())
titanic.head().to_html("ch13-5a-01.html")
print("---------------------------")
# 顯示統計摘要資訊
print(titanic.describe())
titanic.describe().to_html("ch13-5a-02.html")
print("---------------------------")
# 顯示資料集資訊
print(titanic.info())
