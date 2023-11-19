import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: " + os.getcwd())

df = pd.read_csv("test2.csv")

df1 = df.drop_duplicates()
print(df1)
df1.to_html("ch13-3-2b.html") 
