import json
import requests

def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

url = 'https://www.gitlink.org.cn/api/yi-c/yd/raw/sy.json?ref=master'
data = fetch_data(url)
print(data)
