import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: " + os.getcwd())

df = pd.read_csv("test.csv")
print(df)
print("---------------------------")
df.info()
 