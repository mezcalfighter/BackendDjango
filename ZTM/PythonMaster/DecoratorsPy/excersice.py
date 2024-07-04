# Calculate a function time using decorators
import time as t

def time_cal(func):
    def do_something(*args, **kwargs):
        start = t.time()
        func(*args, **kwargs)
        print(t.time() - start)
    return do_something

@time_cal
def say_hello(message):
    for _ in range(0,1000):
        continue
    print(message)

say_hello("Hello, I am using decorators")