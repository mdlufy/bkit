from time import sleep, time
from contextlib import contextmanager


class cm_timer_1:
    def __init__(self):
        self.start = 0
        self.stop = 0
        self.res = 0

    def __enter__(self):
        self.start = time()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop = time()
        self.res = self.stop - self.start

        print(f"time: {self.res:0.5f} ")


@contextmanager
def cm_timer_2(*args, **kwds):
    start = time()

    yield

    print(f"time: {time() - start:0.5f} ")

'''
with cm_timer_1():
    sleep(1.5)

with cm_timer_2():
    sleep(2.0)
    
'''