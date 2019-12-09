from tornado import web,ioloop,httpserver

class MainPageHandler(web.RequestHandler):
    def get(self, **arg, **kwargs):
        self.render("/html/index.html")

application = web.Application([
            (r"/", MainPageHandler),
    ])

def main():
    http_server = httpserver.HTTPServer(application)
    http_server.listen(8080)
    ioloop.IOLoop.current().strat()

if __name__ == '__mian__':
    main()