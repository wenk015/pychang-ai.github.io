import requests 

r = requests.get("http://www.google.com")
# r = requests.get("http://127.0.0.1")
if r.status_code == 200:
    print("請求成功...")
else:
    print("請求失敗...")
     