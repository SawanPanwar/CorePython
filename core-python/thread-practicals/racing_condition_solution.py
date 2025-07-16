from time import sleep
from threading import *
import threading


class Account:

    def __init__(self):
        self.lock = threading.Lock()
        self.balance = 0

    def set_balance(self, balance):
        sleep(1)
        self.balance = balance

    def get_balance(self):
        sleep(1)
        return self.balance

    def diposite(self, amount):
        self.lock.acquire()
        bal = self.get_balance()
        self.set_balance(bal + amount)
        self.lock.release()


class Racing(Thread):

    def __init__(self, account: Account, name):
        super().__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.diposite(100)
            print(self.name, self.account.get_balance())


def main_task():
    acc = Account()
    # create thread instances
    t1 = Racing(acc, "abc")
    t2 = Racing(acc, "xyz")

    # Start threads
    t1.start()
    t2.start()


# Run main task
main_task()