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
        self.render('default.html')

    def post(self):
        content = self.get_argument("content",'guest')
        getHtml = self.get_argument("schtmlnr",'None')
        #self.render('index.html')
        self.write('%s:%s'%(content,getHtml))






if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(myapp())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
