import threading

# Current thread running in the system
print("Currently running thread in the system: ",threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("The current thread is the main thread")
else:
    print("The current thread is not the main thread")
