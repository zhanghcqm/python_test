#-*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup

def get_html(urllist):
    # 获取网页请求
    res = requests.get(urllist)
    # 将网页转化为soup对象标准xml输出
    soup = BeautifulSoup(res.text, 'html.parser')
    # 找到所有img标签，并且class=BDE_Image的项
    src = soup.find_all("img",class_="BDE_Image")
    return src

def write_img(url):
    for link in url:
        # 获取image的url
        picurl = link.get('src')
        # 获取image二进制流数据
        picres = requests.get(picurl).content
        # 创建图片
        file = open(r"H:\images\%s.jpg" % picurl[-9:-4],"wb")
        file.write(picres)
    file.close()

url = get_html("https://tieba.baidu.com/p/5254036393")
write_img(url)