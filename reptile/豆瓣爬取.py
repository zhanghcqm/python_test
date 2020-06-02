import requests
from lxml import html
#需要爬数据的网址
url='https://movie.douban.com/'
#session方法，发送get请求获取数据保存到page中
page=requests.session().get(url)
#调用page.text获取网页源码
#使用html的fromstring方法，把html代码显示在TextView
tree=html.fromstring(page.text) 
data=tree.xpath('//li[@class="title"]/a/text()')
print(data)
result='\n'.join(data)
print(result)
