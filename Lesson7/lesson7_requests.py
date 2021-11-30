import requests


header = {
    "UserAgent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0"
}

params = {
    "text": "python",
    "lr": "213"
}

res = requests.get("https://yandex.ru", headers=header, params=params)
print(res)
print(res.status_code)
print(res.headers)
print(res.content)
print(res.text)
print(res.json())
