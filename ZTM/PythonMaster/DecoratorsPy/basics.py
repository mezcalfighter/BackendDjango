# Decorators - functions to act like variables (they super charge our function)
# @classmethod @staticmethods - are decorators

# Decorators wraps another function
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print("*********")
        func(*args, **kwargs)
        print("*********")
    return wrap_func

@my_decorator
def hello(greeting,emoji=":)"):
    print(greeting, emoji)

@my_decorator
def bye(see_ya):
    print(see_ya)

hello("Helloooooooo")
bye("See ya later!")

# It's running like this
# a = my_decorator(hello)
# a()