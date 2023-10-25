import os 
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print("current dir: "+os.getcwd())

f = open("demo.txt", "r")
# print(f.read())