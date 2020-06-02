#coding:utf-8
import requests
globalsession = requests.session()#自动管理 cookies
from requests.sessions import RequestsCookieJar
postdata={
    "product.sku":"huk023",
    "product.refSku":"",
    "product.id":"",
    "product.available":"true",
    "_product.available":"on",
    "_product.preOrder":"on",
    "dateAvailable":"2018-08-10",
    "product.manufacturer.id":"1",
    "product.type.id":"1",
    "descriptions[0].name":"Tshirt023",
    "descriptions[0].seUrl":"tshirt023",
    "descriptions[0].productHighlight":"",
    "descriptions[0].description":"",
    "descriptions[0].metatagTitle":"",
    "descriptions[0].metatagDescription":"",
    "descriptions[0].language.id":"1",
    "descriptions[0].language.code":"en",
    "descriptions[0].id":"",
    "descriptions[0].metatagKeywords":"",
    "descriptions[0].productExternalDl":"",
    "productPrice":"200.00",
    "availability.productQuantity":"6000",
    "availability.productQuantityOrderMin":"1",
    "availability.productQuantityOrderMax":"2",
    "_product.productShipeable":"on",
    "availability.region":"*",
    "availability.id":"",
    "product.productVirtual":"false",
    "product.productWeight":"",
    "product.productHeight":"",
    "product.productLength":"",
    "product.sortOrder":"0",
    "productImage.productImage":"",
    "product.taxClass.id":"1",

}
url = "http://192.168.20.151:8080/admin/products/save.html"
files={
    "image":("02.png",open("02.png","rb"),"image/png")
    #参数名,    文件名称      文件内容              文件类型
}
logindata={
    "username":"admin",
    "password":"password"
}
loginurl = "http://192.168.20.151:8080/login";
def login(url,postdata):
    globalsession.post(url=url,data=postdata)
    pass
def loginwithcookies():
    cookievalue=None
    rsp =requests.post(loginurl,logindata)
    cookiesjar = RequestsCookieJar()
    #requests.post(loginurl,logindata,cookies=cookiesjar)
    #cookiesjar.set("JSESSIONID",cookievalue)
    return cookiesjar
    pass
def uploadgood(url,data,files,cookiejar):
    rsp =requests.post(url,data=data,files=files,cookies=cookiejar)
    return rsp.content
    pass
if __name__ == '__main__':
   # login(loginurl,logindata)
   # print uploadgood(url=url,data=postdata,files=files)
   cookiejar = loginwithcookies()
   uploadgood(url=url, data=postdata, files=files,cookiejar=cookiejar)