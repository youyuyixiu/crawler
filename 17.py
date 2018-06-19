# 爬虫模拟百度搜索

import requests
url = 'http://www.baidu.com/s'
# url = 'http://www.google.com/search'
# url = 'http://www.so.com/s'
try:
    kv = {'wd': 'python'}
    # kv = {'q': 'python'}
    # kv = {'q': 'python'}
    r = requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(len(r.text))
except:
    print('爬取失败')