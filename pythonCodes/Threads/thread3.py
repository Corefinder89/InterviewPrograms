# Creating a thread using the implemented class as a sub class of the Thread class
from threading import Thread

class MyThread(Thread):
    def __init__(self, str):
        Thread.__init__(self)
        self.str = str

    def run(self):
        print(self.str)

t1 = MyThread('Balthazar')
t1.start()
t1.join()
