import requests
#eg1:
rsp = requests.post("https://jsonplaceholder.typicode.com/posts")

print(rsp.status_code)
print(rsp.json())

#eg2:by params
param = {
    "shouji":"13963241566",
    "appkey":"0c818521d38759el"
}
rsp_param = requests.post("http://sellshop.5istudy.online/sell/shouji/query",
                          params=param)
print(rsp_param.status_code)
print(rsp_param.text)

#eg3:by json
json_data = {
    "title":"foo",
    "body":"bar",
    "uerid":1
}

rsp_json = requests.post("https://jsonplaceholder.typicode.com/posts",
                         json=json_data)

print(rsp_json.status_code)
print(rsp_json.json())

#eg4:by data
data = {
    "title":"foo"
}
rsp_data = requests.request("POST","https://dict.youdao.com/keyword/key",
                            data=data)
#req_data = requests.post("https://dict.youdao.com/keyword/key",data=data)
print(rsp_data.status_code)
print(rsp_data.text)