import threading
import time


def first_thread(name):
    for i in range(1, 11):
        time.sleep(3)
        print(name, i)


def second_thread(name):
    for i in range(1, 11):
        time.sleep(1)
        print(name, i)


t1 = threading.Thread(target=first_thread, args=('daemon',), daemon='True')
t2 = threading.Thread(target=second_thread, args=('abc',))

t1.start()
time.sleep(2)
t2.start()
