#!/usr/bin/env python
#coding:utf-8

import tornado.httpserver
import tornado.ioloop
import tornado.web
import os.path

from tornado.options import define, options
define('port', default='8000', help='run in given port', type=int)



class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r'/index/([^/]+)', IndexHandler),
			(r'/c', CarouselHandler)
		]
		settings = dict(
			blog_title=u"Tornado CMS",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            # # ui_modules={"Entry": EntryModule},
            # xsrf_cookies=True,
            # cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            # login_url="/auth/login",
            # autoescape=None,
            # debug=True,
		)
		tornado.web.Application.__init__(self, handlers, **settings)

		"""数据库"""
		self.db = None



class BaseHandler(tornado.web.RequestHandler):
	"""基类

	封装数据库操作
	"""
	@property
	def db(self):
		return self.application.db



class IndexHandler(BaseHandler):
	"""主页"""

	def get(self, arg):
		self.render('index.html', title=arg)
		# self.write('geek world!')



class CarouselHandler(BaseHandler):
	""""""
	
	def get(self):
		self.render("carousel.html", title=u"Test")




class loginHandler(BaseHandler):
	"""登录"""

	def get(self):
		pass
					


		
def main():
	tornado.options.parse_command_line()
	http_server = tornado.httpserver.HTTPServer(Application())
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
	


if __name__ == '__main__':
	print 'Running Web Server ......'
	main()
