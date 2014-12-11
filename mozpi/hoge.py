from client import Mozpi
import threading

m = Mozpi("ws://localhost:8080")
t= threading.Thread(target=m.start())
t.start()
# m.start()
print "started"
