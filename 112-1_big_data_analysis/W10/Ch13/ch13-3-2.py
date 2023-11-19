import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: " + os.getcwd())

df = pd.read_csv("test2.csv")
print(df)
df.to_html("ch13-3-2.html")
