import requests
url = "https://www.baidu.com"
response = requests.get(url)
html = response.text
