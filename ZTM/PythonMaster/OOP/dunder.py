# Dunder Methods
class Toy():
    def __init__(self,color,age):
        self.color = color
        self.age = age

    # You can also define what you do with the dunder methods
    # Avoid modifying dunder methods - only when you want to behave some certain way
    def __str__(self):
        return f"{self.color}"
    
    def __len__(self):
        return 5
    
    def __del__(self):
        print("deleted!")

    def __call__(self):
        print("yess??")

action_figure = Toy("red",0)
print(str(action_figure))
print(action_figure.__str__()) # Both are the same and included in all objects
print(action_figure.__len__())
print(action_figure.__call__())