#-*-coding: utf-8-*-
import websocket
import thread
import time

DEBUG=False
# DEBUG=True

class Mozpi():
    def __init__(self,ws_url):
        self.ws_url = ws_url 
        if self.ws_url =="":
            self.ws_url = "ws://echo.websocket.org"

    def on_message(self,ws,message):
        print message
    
    def on_error(self,ws,error):
        print error
    
    def on_close(self,ws):
        print "ws closed"
        self.ws.close()
    
    def on_open(self,ws):
        print "ws connected"
        thread.start_new_thread(self.run,())

    def run(self,*args):
        # for i in range(5):
        #     self.ws.send(u"hello")
        #     time.sleep(1)
        while True:
            pass

    def start(self):
        if DEBUG == True:
            websocket.enableTrace(True) 
        self.ws = websocket.WebSocketApp(self.ws_url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        self.ws.on_open=self.on_open
        self.ws.run_forever()

if __name__=="__main__":
    # m = Mozpi("ws://echo.websocket.org")
    m = Mozpi("ws://localhost:8080")
    m.start()

