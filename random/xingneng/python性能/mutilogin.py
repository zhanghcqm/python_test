#coding=utf-8
import threading
import requests
import time
class LoginThread(threading.Thread):
    def __init__(self,userName,time):
        threading.Thread.__init__(self)
        self.logondata={
                        "userName" : "835306816@qq.com",
                            "password" : "123456",
                            "storeCode" : "DEFAULT"
        }
        self.logondata["userName"]=userName+"@qq.com"
        self.url = "http://192.168.20.151:8080/shop/customer/logon.html";

        pass
    def run(self):
        begin = time.time()
        end=time.time()
        while int(end-begin)<= 60 :
            print('thread'+threading.Thread.getName(self) +"is running")
            rsp = requests.post(self.url, self.logondata)
            rsp = rsp.json()
            assert rsp["response"]["status"] == 0, "respone is wrong"
            end =time.time()



def createThread(num,userlist,time):
    '''

    :param num: thread number
    :time time
    :return:
    '''
    threadlist=[]

    for i in range(num):
        single = LoginThread(userName=userlist[i],time=time)
        threadlist.append(single)
    for trd in threadlist:
        trd.start()
if __name__ == '__main__':
    userlist = ['123456730', '123456731', '123456732', '123456733', '123456734', '123456735', '123456736', '123456737',
                '123456738', '123456739', '123456740', '123456741', '123456742', '123456743', '123456744', '123456745',
                '123456746', '123456747', '123456748', '123456749']
    createThread(len(userlist),userlist,60)
    pass