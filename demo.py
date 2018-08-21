import requests

url = "http://127.0.0.1:5000/login"
payload = {"username":"admin","password":"123456"}
headers = {
    'Content-Type': "application/json"
    }
response = requests.request("POST", url, json=payload, headers=headers)
print(response.json())