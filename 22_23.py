import requests
r = requests.get('https://www.python123.io/ws/demo.html')
demo = r.text
# print(demo)

# 从bs4库中引入BeautifulSoup类型
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, 'html.parser')
# 为每个标签加换行符
# print(soup.prettify())

# 返回title标签
# print(soup.title)
# 返回第一个a标签
# print(soup.a)

# print(soup.a.name)
# print(soup.a.parent.name)
# print(soup.a.parent.parent.name)
# print(soup.a.parent.parent.parent.name)

tag = soup.a
# print(tag.attrs)
# print(tag.attrs['class'])
# print(tag.attrs['href'])
# print(tag.attrs['id'])
# print(type(tag.attrs))
# print(type(tag))

# print(soup.a.string)
# print(soup.p)
# print(soup.p.string)
# print(type(soup.p.string))

newSoup = BeautifulSoup('<b><!--This is a comment--></b><p>This is not comment</p>','html.parser')
# print(newSoup.p.string)
# print(newSoup.b.string)
# print(type(newSoup.p.string))
# print(type(newSoup.b.string))


