#coding=utf-8
__author__ = 'Administrator'
import sys
#sys.path.append('./')
#import tornado.autoreload
#import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options
import tornado.template
import tornado.httpclient
import tornado.gen

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)


class myapp(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/admin", AdminHandler),
            (r"/test", testHandler),
        ]
        settings = {
            "cookie_secret": "b2Jc2sWbQLKos6GkHn/VB9oXwQQ8S0R0kRvJ5/xJ89E=",
            'template_path':'templates',
            'static_path' :'static',
            'debug':'False'
        }
        tornado.web.Application.__init__(self, handlers, **settings)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        text = self.get_argument("message", "来宾")
        self.write("{'GET':'%s'}"%text)
        print("{'GET':'%s'}"%text)

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('B-JUI/index.html')

    def post(self):
        name = self.get_argument("name",'guest')
        passwd = self.get_argument("passwd",'None')
        #self.render('index.html')
        self.write('%s:%s'%(name,passwd))

class testHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('test.html')





if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(myapp())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
