import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: " + os.getcwd())

df = pd.read_csv("test.csv")
# 建立布林遮罩
df2 = pd.isnull(df);
print(df2)
df2.to_html("ch13-3-1d.html")