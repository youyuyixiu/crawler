# 爬取图片/视频并保存到本地

import requests
import os
url = 'https://pic4.zhimg.com/50/v2-66928fa0219e841427e7a3cbec45a74a_hd.jpg'
# url = 'https://qncdn.miaopai.com/stream/tUmAepT9quDIZ4RTYQaR0dfI8VHcKls97OHL9Q___16_0_1528008596.mp4?ssig=fdd867dedf5ffd81d3111f486809e93a&time_stamp=1528109666993'
root = 'E://crawler//'
# path = root + url.split('/')[-1]
path = root + '齐达内.jpg'
# path = root + '小米NFC宣传片.mp4'
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path,'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print("图片已经存在")
except:
    print('爬取失败')