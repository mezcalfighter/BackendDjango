# Scope - What variables do I have access to?

# Global variable
total = 0

def count():
    global total # You need to first say you will use total globally
    total += 1
    return total

count()
count()
print(count())

# NonLocal variable - grabs the variable from global value so it does not duplicate by creating a local 
def outer():
    x="local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:",x)
    inner()
    print("outer:",x)

outer()