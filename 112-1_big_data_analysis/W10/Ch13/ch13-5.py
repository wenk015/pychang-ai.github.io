import pandas as pd
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: " + os.getcwd())

titanic = pd.read_csv("titanic_data.csv")
# 顯示資料集的形狀
print(titanic.shape)
