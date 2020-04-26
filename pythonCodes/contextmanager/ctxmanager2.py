from contextlib import contextmanager

@contextmanager
def managed_filename(name):
    try:
        f = open(name, 'w')
        yield f
    finally:
        f.close()

with managed_filename('hello.txt') as f:
    f.write("Hello World")
    f.write("Bye Bye")
