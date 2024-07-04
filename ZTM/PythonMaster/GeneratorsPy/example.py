# Fibonacci 
def fib(number):
    a = 0
    b = 1
    for _ in range(number+1):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)