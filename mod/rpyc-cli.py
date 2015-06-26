# coding: UTF-8
__author__ = 'Administrator'
import rpyc
def run_cmd(ip, port, cmd):
    try:
        conn = rpyc.connect(ip, port)
        res = conn.root.cmd(cmd)
        for line in res:print(line)
        conn.close()
    except:
        conn.close()

if __name__ == "__main__":
    while 1:
        cmd = input('请输入您的指令：')
        if cmd == None or cmd =='':
            continue
        elif cmd == 'quit':
            break
        run_cmd('192.168.0.126', 19999, cmd)