# Creating a thread without using a class, send arguments as tuple

from threading import *

def display(string):
    print(string)

for i in range(5):
    t = Thread(target=display, args=('Hello World',))
    t.start()
