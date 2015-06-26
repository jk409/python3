__author__ = 'Administrator'
import rpyc
from rpyc import Service
from rpyc.utils.server import ThreadedServer
import os
class Test(Service):
    def exposed_cmd(self,cmd):
        #return os.system(cmd)
        return os.popen(cmd)

sr = ThreadedServer(Test, port=1999, auto_register=False)
sr.start()
