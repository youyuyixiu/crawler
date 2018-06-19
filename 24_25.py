# 标签遍历
from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.python123.io/ws/demo.html')
demo = r.text
# print(demo)

# 下行遍历  contents children descendants
soup = BeautifulSoup(demo,'html.parser')
# print(soup.head)
# print(soup.head.contents)
# print(soup.body.contents)
# print(len(soup.body.contents))
# print(soup.body.contents[1])
# for child in soup.body.children:
#     print(child)

# 上行遍历  parent  parents
# print(soup.title.parent)
# print(soup.html.parent)
# for parent in soup.a.parents:
#     if parent is None:
#         print(parent)
#     else:
#         print(parent.name)

# 平行遍历  必须发生在同一个父节点下  next_sibling  previous_sibling  next_siblings  previous_siblings
# print(soup.a.next_sibling)
# print(soup.a.next_sibling.next_sibling)
# print(soup.a.previous_sibling)
# print(soup.a.previous_sibling.previous_sibling)
# print(soup.a.previous_sibling.parent)

# newSoup = BeautifulSoup('<p>肖树一</p>','html.parser')
# print(newSoup.p.string)
# print(newSoup.p.prettify())
