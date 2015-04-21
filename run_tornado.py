import tornado.ioloop
import tornado.web

from tornado_app.urls import urlpatterns


def main():
    application = tornado.web.Application(urlpatterns)
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()