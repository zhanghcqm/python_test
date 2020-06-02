import urllib.request
def grab(url):
    # 打开传入的网址
    resp = urllib.request.urlopen(url)
    # 读取网页源码内容
    data = resp .read()
    # 打开要存储的文件
    file_name = open(r"F:\py\源代码.txt", "wb")
    # 将代码写入文件
    file_name.write(data)
    # 关闭文件
    file_name.close()
    print("下载源码完成")

if __name__ == '__main__':
    # 按照格式输入网址
    web_addr = input("请输入网址：")
    print(web_addr)
    try:
        grab(web_addr)
    except:
        print("网址输入有误")
