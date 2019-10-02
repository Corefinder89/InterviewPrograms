# Creating a thread without using a class
from threading import *

def display():
    print("Hello world")

for i in range(5):
    t = Thread(target=display)
    #Start the thread
    t.start()
