import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: " + os.getcwd())

df = pd.read_csv("test.csv")
# 建立布林遮罩
df1 = pd.isnull(df)
print(df1)
df1.to_html("ch13-3-1d.html")