import requests
from urllib3 import request

#eg1:
#rsp = requests.get("https://api.github.com/events")
rsp = requests.request("GET", "https://api.github.com/events")
print(rsp.status_code)
print(rsp.text)
print(rsp.url)
print(rsp.headers)
print(rsp.cookies)
print(rsp.json())

#eg2:
param = {
    "shouji":"13963241566",
    "appkey":"0c818521d38759el"
}
#rsp_param = requests.get("http://sellshop.5istudy.online/sell/shouji/query", params=param)
rsp_param = requests.request("GET","http://sellshop.5istudy.online/sell/shouji/query",
                       params=param)
print(rsp_param.status_code)
print(rsp_param.text)
