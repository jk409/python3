__author__ = 'Administrator'
import sys,os
dir_cfg="./"
#file=sys.argv[1]
#hostname=sys.argv[2]
#app=sys.argv[3]
#ip=sys.argv[4]
#port=sys.argv[5]

def test(file,hostname,app,ip,port):
    filepath=dir_cfg+file
    if os.path.exists(filepath):
        try:
            wf=open(filepath,'a')
            wf.write(data_02%(hostname,app,port))
            wf.flush()
            wf.close()
            print(ip,hostname,app,port,'Ok!')
        except:
            print('Write file fail!')
            wf.close()
    else:
        try:
            wf=open(filepath,'w')
            wf.write(data_01%(hostname,hostname,ip,hostname,app,port))
            wf.flush()
            wf.close()
            print(ip,hostname,app,port,'Ok!')
        except:
            print('Write file fail!')
            wf.close()

data_01='''
define host{
        use                     generic-host
        host_name               %s
        alias                   %s
        address                 %s
        }

define service {
        use                             generic-service
        host_name                       %s
        service_description             %s
        check_command                   check_tcp!%s
}
'''
data_02='''
define service {
        use                             generic-service
        host_name                       %s
        service_description             %s
        check_command                   check_tcp!%s
}
'''
#print("%-40s %-10s"%('7899999999999999999999','hhh'))

if __name__ == "__main__":
    test('kkk.cfg','kkk','HTTP','114.114.114.114','80')