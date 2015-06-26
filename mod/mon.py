# coding: UTF-8
import os,inspect,socket,time
num = 0
class kkk:
    def __init__(self):
        self.data={}

    def getAmber(self):
        global num
        num+=1
        return num

    def getDate(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

    def getProcess(self):
        return os.popen('ps -ef |wc -l').readlines()[0].split()[0]

    def getDisk(self):
        return os.popen("df -h |grep '/$'").readlines()[0].split()

    def getMem(self):
        return os.popen('free -m').readlines()[1].split()[1:4]

    def getSwap(self):
        return os.popen('free -m').readlines()[3].split()[1:]

    def getLoad(self):
        return os.popen('uptime').readlines()[0].split()[-3:]

    def getHost(self):
        return socket.gethostname()

    def getUser(self):
        return os.popen('uptime').readlines()[0].split()[3]

    def getRuntime(self):
        return os.popen('uptime').readlines()[0].split()[2]

    def getSystem(self):
        return os.popen('cat /etc/redhat-release').readlines()[0].split('\n')[0]

    def getKerner(self):
        return os.popen('uname -r').readlines()[0].split('\n')[0]


    def run(self):
        for fun in inspect.getmembers(self,predicate=inspect.ismethod):
            if fun[0][:3] == 'get':
                #print fun[1]()
                self.data[fun[0][3:]] = fun[1]()
        return self.data

class windos:
    def __init__(self):
        self.data={}

    def getAmber(self):
        global num
        num+=1
        return num

    def run(self):
        print('123456')

if __name__ == "__main__":
    while 1:
        print (windos().run())
        time.sleep(5)
