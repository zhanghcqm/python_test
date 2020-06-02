# coding:utf-8
import threading
import  random
class Player(threading.Thread):
    '''
    thread class
    '''
    def __init__(self,mode):
        threading.Thread.__init__(self,name="thread1")
        self.mode = mode
    def downloadqq(self):
        for i in range(30*10000):
            print("i am downloading qq")
    def playmp3(self):
        for i in range(30*10000):
            print("i am downloading mp3")
    def playmp4(self):
        for i in range(30*10000):
            print("i am downloading mp4")
    def run(self):
        if 0 ==self.mode:
            self.downloadqq()
        elif 1 == self.mode:
            self.playmp3()
        elif 2 == self.mode:
            self.playmp4()


if __name__ == '__main__':
    threads =[]
    threadnum =50
    for i in  range(threadnum):
        mode = random.randint(0,3)
        thread = Player(mode)
        threads.append(thread)
        pass
    for i in range(threadnum):
        threads[i].start()
    pass
