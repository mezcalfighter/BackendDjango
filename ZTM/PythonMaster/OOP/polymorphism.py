# Polymorphism - Many forms 
class User:
    def sign_in(self):
        print("Logged in")

    def attack(self):
        print("Do nothing")

class Wizard(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power

    # This method will override the existing attack method from parent, however it also can be called
    def attack(self):
        User.attack(self)
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows, arrows left: {self.num_arrows}")

wizard1 = Wizard("Merlin",50)
archer1 = Archer("Robin",30)