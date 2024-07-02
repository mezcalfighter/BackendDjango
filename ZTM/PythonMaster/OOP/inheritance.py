# Inheritance
# Users
#   - Wizards
#   - Archer
class User:
    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self,name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    def __init__(self,name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows, arrows left: {self.num_arrows}")

wizard1 = Wizard("Merlin",50)
archer1 = Archer("Robin",100)
wizard1.sign_in()
archer1.sign_in()

wizard1.attack()
archer1.attack()

# Check if instance of
print(isinstance(wizard1,Wizard)) # It will check if wizard1 is an instance of Wizard - True
print(isinstance(wizard1,User)) # It will check if wizard1 is an instance of User - True (User is parent to Wizard)