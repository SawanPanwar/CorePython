import threading
from threading import *
def hello(name):
    for i in range(1, 15):
        print("Hello", i, name)
    return


t1 = threading.Thread(target=hello, args= ("ram",))
t2 = threading.Thread(target=hello, args= ("shyam",))

t1.start()
t2.start()
