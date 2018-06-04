import requests

url = "http://127.0.0.1:5000/login"

payload = {"userneme":"admin","password":"123456"}
headers = {
    # 'Content-Type': "application/json"
    }

response = requests.request("POST", url, json=payload, headers=headers)
hdata = response.json()
code = hdata["code"]
print(code)
if code == 200:
    print("测试通过")
else:
    print("测试失败")