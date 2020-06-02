#！/usr/bin/python3.7
# -*- coding: utf-8 -*-

import requests,bs4

# 获取html文档
def get_html(url):
    response = requests.get(url)
    #response.encoding = 'utf-8'
    return response.text

# 获取笑话内容
def get_joke(html):
    #将response转换成bs4.BeautifulSoup类型
    soup = bs4.BeautifulSoup(html, "html.parser")
    #通过BeautifulSoup使用CSS选择器语法选择指定的标签

    for i in range(9):
        joke_content = soup.select('.recmd-content')[i].get_text()
        #打开要存储的本地文件
        file_name = open(r"F:\py\爬虫1.txt", "a")
        # 将内容写入文件
        file_name.write('第{}条：'.format(i+1))
        file_name.write(joke_content)
        file_name.write('\n')
        # 关闭文件
        file_name.close()

if __name__ == '__main__':
    url_joke = "https://www.qiushibaike.com"
    html = get_html(url_joke)
    get_joke(html)


