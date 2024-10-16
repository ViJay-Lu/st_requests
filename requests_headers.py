import requests

url = "https://movie.douban.com/j/search_subjects"
query_params = {
    "type":"movie",
    "tag":"热门",
    "page_limit":10,
    "page_start":0
}

headers = {
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}
#不加headers参数， 请求报错418
rsp = requests.get(url, params=query_params,headers=headers)
print(rsp.status_code)
print(rsp.json())