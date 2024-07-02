class User:
    def __init__(self,email):
        self.email = email

    def sign_in(self):
        print("Logged in")

class Wizard(User):
    def __init__(self,name, power, email):
        #This is adding the required email from the parent object
        User.__init__(self, email)
        self.name = name
        self.power = power

    def attack(self):
        print(f"attacking with power of {self.power}")

class Archer(User):
    # Super will call the object parent and add the attributes from there
    def __init__(self,name, num_arrows,email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f"attacking with arrows, arrows left: {self.num_arrows}")

wizard1 = Wizard("Merlin",50,"merlin@gmail.com")
archer1 = Archer("Robin",300,"robin@gmail.com")

print(wizard1.email)
print(archer1.email)