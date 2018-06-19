import requests
r = requests.get("http://httpbin.org/get")
# print(r.text)

r = requests.head("http://httpbin.org/head")
# print(r.headers)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
# print(r.text)

r = requests.post("http://httpbin.org/post", data='ABC')
# print(r.text)

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.put("http://httpbin.org/put", data=payload)
print(r.text)


