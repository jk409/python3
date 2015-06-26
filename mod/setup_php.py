__author__ = 'Administrator'
import os
def show():
    print('''
    python版本3.x
    <----------------------------------------------------------->
        0.开启所以服务                  00.关闭所以服务
        1.开启【Nginx】服务             10.关闭【Nginx】服务
        2.开启【Php_fastcgi】服务       20.关闭【Fast_cgi】服务
        3.开启【Mysql】服务             30.关闭【Mysql】服务
    <------------------------------------------------------------>
''')
def main():
    wnmp_path = os.getcwd()
    show()
    chioce=input('your chioce:')

    if chioce == '1':
        nginx_path=wnmp_path+'\\nginx\\nginx.exe'
        os.system(nginx_path)
        print(nginx_path,'all')




if __name__ == "__main__":
    main()