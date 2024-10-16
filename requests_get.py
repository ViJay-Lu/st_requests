import requests

#eg1:
req = requests.get("https://api.github.com/events")

print(req.status_code)
print(req.text)
print(req.url)
print(req.headers)
print(req.cookies)
print(req.json())

#eg2:
param = {
    "shouji":"13963241566",
    "appkey":"0c818521d38759el"
}
req = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=param)
print(req.status_code)
print(req.text)
