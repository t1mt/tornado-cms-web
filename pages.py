#!/usr/bin/env python


import tornado.httpserver
import tornado.ioloop
import tornado.web


from tornado.options import define, options
define('port', default='8000', help='run in given port', type=int)


class Application(tornado.web.Application):
	def __init__(self):
		handlers = [
			(r'/index', indexHandler)
		]
		settings = dict(
			blog_title=u"Tornado CMS",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={"Entry": EntryModule},
            xsrf_cookies=True,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/auth/login",
            autoescape=None,
		)
		tornado.web.Application.__init__(self, handlers, **settings)



def main():
	pass


if __name__ == '__main__':
	main()
