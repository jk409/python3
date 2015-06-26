#coding=utf-8
__author__ = 'Administrator'
import tornado.autoreload
#import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.template
import tornado.httpclient
import tornado.gen
import time,sys
sys.path.append('./mod/')
import sql,tpp
from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)
#实例化sql类
def mysqls():
    return  sql.Mysql('127.0.0.1','root','123456','host')

class myapp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/file",File_Handler),
            (r"/check", Check_Handler),
            (r"/users", Users_Handler),
            (r"/users/add", Usersadd_Handler),
            (r"/users/update", UsersUpdate_Handler),
            (r"/ll", LL_Handler),
            (r"/hostinfo", hostinfo_Handler),
            (r"/delete/(.*)/(.*)", Delete_Handler),
            (r".*", MainHandler),

        ]
        settings = {
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
            'template_path':'templates',
            'static_path' :'static',
            'debug':'False'
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    #@tornado.web.asynchronous
    #@tornado.gen.engine
    def get(self):
        ips=[]
        mysql = mysqls()
        res=mysql.cmd("select *,count(distinct ip) from hostinfo group by ip")
        mysql.close()
        for i in res:
            ips.append(list(i))
        print(ips)
        self.render('index.html',ips=ips)

    def post(self):
        tms=[]
        data=[]
        cpu_data=[]
        ip = self.get_argument('ip')
        mysql = mysqls()
        res=mysql.cmd("select * from hostinfo where ip='%s'"%ip)
        res=list(res)
        for i in res:
            i=list(i)
            #i=eval(list(i))
            ts=time.strftime("%d-%H:%M",time.localtime(i[3]))
            tms.append(ts)
            data.append([ts,i[4:]])
            cpu_data.append(i[4])
        print(data,cpu_data,tms)
        self.render('hostinfo.html',data=data,ips=ip,tms=tms,cpu_data=cpu_data)

class hostinfo_Handler(tornado.web.RequestHandler):
    def get(self):
        tms=[]
        data=[]
        cpu_data=[]
        ip = self.get_argument('ip')
        mysql = mysqls()
        res=mysql.cmd("select * from hostinfo where ip='%s'"%ip)
        res=list(res)
        for i in res:
            i=list(i)
            ts=time.strftime("%d-%H:%M",time.localtime(i[3]))
            tms.append(ts)
            data.append([ts,i[4:]])
            cpu_data.append(i[4])
        print(data)

        self.render('hostinfo.html',data=data,ips=ip,tms=tms,cpu_data=cpu_data)

class File_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('file.html')

class Check_Handler(tornado.web.RequestHandler):
    def get(self):
        res=[]
        self.render('check_index.html',res=res)

    def post(self):
        data=[]
        hostlist=[
            ['127.0.0.1',80],
            ['baidu.com',80],
            ['qq.com',8080]
        ]
        #ip = self.get_argument('ip')
        #port = self.get_argument('port')
        for i in hostlist:
            res=tpp.run(i[0],i[1])
            res=list(res)
            data.append(res)
        print(res,data)
        self.render('check_index.html',res=data)

class Users_Handler(tornado.web.RequestHandler):
    def get(self):
        data=[]
        mysql=mysqls()
        res=mysql.cmd("select id,name,email,phone,qx,zc from users")
        res=list(res)
        for i in res:
            i=list(i)
            data.append(i)
        self.render('users_index.html',data=data)

class Usersadd_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('users_add.html')

    def post(self):
        name = self.get_argument('name')
        passwd = self.get_argument('passwd')
        email = self.get_argument('email')
        phone = self.get_argument('phone')
        qx = self.get_argument('qx')
        mysql=mysqls()
        res=mysql.cmd("select count(name) from users where email='%s' limit 1;"%name)
        res =list(res)
        if res[0][0] != 0:
            self.redirect('/users/add')
        else:
            sqls="insert into  `users` (name,passwd,email,phone,qx) values('%s','%s','%s','%s','%s');"
            mysql.cmd(sqls%(name,passwd,email,phone,qx))
            mysql.commit()
            mysql.close()
            self.redirect('/users')

class UsersUpdate_Handler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name',None)
        if name == None:
            self.redirect('/users')
        mysql=mysqls()
        res=mysql.cmd("select id,name,passwd,email,phone,qx,zc from users where name='%s'"%name)
        res=list(res)
        print(res[0][0],res[0][1])
        self.render('users_update.html',data=res)

    def post(self):
        cmd = self.get_argument('cmd')
        name = self.get_argument('name')
        passwd = self.get_argument('passwd')
        email = self.get_argument('email')
        phone = self.get_argument('phone')
        qx = self.get_argument('qx')
        print(name,passwd,email,phone,qx)
        mysql=mysqls()
        if cmd == 'update':
            sqls="update  `users` set passwd='%s',email='%s',phone='%s',qx='%s' where name='%s';"
            mysql.cmd(sqls%(passwd,email,phone,qx,name))
        if cmd == 'add':
            sqls="insert into  `users` (name,passwd,email,phone,qx) values('%s','%s','%s','%s','%s');"
            mysql.cmd(sqls%(name,passwd,email,phone,qx))
        mysql.commit()
        mysql.close()
        self.redirect('/users')

class UserDelete_Handler(tornado.web.RequestHandler):
    def get(self,id):
        mysql = mysqls()
        mysql.cmd("delete  from hostinfo where ip='%s'"%id)
        mysql.close()
        self.redirect('/user')

class Bind_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('bind.html')

class LL_Handler(tornado.web.RequestHandler):
    def get(self):
        self.render('ll.html')

class Delete_Handler(tornado.web.RequestHandler):
    def get(self,arxg,arxg2):
        #ip = self.get_argument('ip')
        mysql = mysqls()
        if arxg == 'host':
            mysql.cmd("delete  from hostinfo where ip='%s'"%arxg2)
            mysql.commit()
            mysql.close()
            self.redirect('/')
        if arxg == 'users':
            mysql.cmd("delete  from users where name='%s'"%arxg2)
            mysql.commit()
            mysql.close()
            self.redirect('/users')
        pass






if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(myapp())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
