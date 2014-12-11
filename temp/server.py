import tornado.iolooop
import tornado.web
import tornado.websocket
import tornado.template


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("hello")

class WSHandeler(tornado.websocket.WebSocketHandler):
    def open(self):
        print "open"
        self.write_message("opened")

    def on_message(self,message):
        self.write_message(message)

    def on_close(self):
        print "close"

def main():
    application = tornado.web.Application([
        (r'/ws',WSHandler),
        (r'/',MainHandler)
   ])
    application.listen(8000)
    tornado.ioloop.IOLoop.instnce().start()

if __name__=="__main__":
    main()
