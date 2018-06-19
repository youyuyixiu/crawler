# 爬取京东商品页--小米mix2

import requests
url = 'https://item.jd.com/5159286.html'
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers = kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[0:2000])
except:
    print('爬取失败')
