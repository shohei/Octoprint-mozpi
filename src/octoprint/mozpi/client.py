#-*-coding: utf-8-*-
import websocket
import threading
import time
from multiprocessing import Process

DEBUG=False
# DEBUG=True

class Mozpi():
    def __init__(self,ws_url):
        self.ws_url = ws_url 

    def on_message(self,ws,message):
        print message
    
    def on_error(self,ws,error):
        print error
    
    def on_close(self,ws):
        print "ws closed"
        self.ws.close()
    
    def on_open(self,ws):
        print "ws connected"

    def start(self):
        if DEBUG == True:
            websocket.enableTrace(True) 
        self.ws = websocket.WebSocketApp(self.ws_url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        self.ws.on_open=self.on_open
        # self.ws.run_forever()
        # thread.start_new_thread(self.ws.run_forever(),())
        # t = threading.Thread(target=self.ws.run_forever)
        # t.start()
        p = Process(target=self.ws.run_forever)
        p.start()

if __name__=="__main__":
    # m = Mozpi("ws://echo.websocket.org")
    m = Mozpi("ws://localhost:8080")
    t = threading.Thread(target=m.start())
    t.start()
    print "Your program goes here"

