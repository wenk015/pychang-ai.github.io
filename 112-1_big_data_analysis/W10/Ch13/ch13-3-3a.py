import pandas as pd
from sklearn import preprocessing
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: " + os.getcwd())

df = pd.read_csv("test3.csv")

label_encoder = preprocessing.LabelEncoder()
df["性別"] = label_encoder.fit_transform(df["性別"])
print(df)
df.to_html("ch13-3-3a.html")