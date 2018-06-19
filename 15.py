# 爬取京东商品页--小米mix2s

import requests
try:
    r = requests.get("https://item.jd.com/6735790.html")
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text)
except:
    print("爬取失败")


