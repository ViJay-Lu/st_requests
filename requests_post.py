import requests

req = requests.post("https://jsonplaceholder.typicode.com/posts")

print(req.status_code)
print(req.json())