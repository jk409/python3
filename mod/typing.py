__author__ = 'Administrator'
import sys,time,socket
#E-mail:jk409@qq.com
#example: test.py   ip   80
ip   = sys.argv[1]
port = sys.argv[2]
timeout = 0.5
while 1:
    #time.sleep(0.8)
    try:
        time.sleep(1)
        sc=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        port = int(port)
        sc.settimeout(timeout)
        sc.connect((ip,port))
        print (ip,':',port,':OK')
    except socket.timeout:
        print(ip,':',port,':Fail')

    #except KeyboardInterrupt:
    #    break
    except:
        break
