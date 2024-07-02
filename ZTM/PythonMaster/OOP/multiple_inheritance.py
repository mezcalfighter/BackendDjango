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
    def __init__(self,name, num_arrows,):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f"attacking with arrows, arrows left: {self.num_arrows}")

    def run(self):
        print("Ran really fast")

class HybridBorg(Wizard,Archer):
    def __init__(self, name, power, num_arrows):
        Wizard.__init__(self,name,power)
        Archer.__init__(self,name,num_arrows)

hybridborg = HybridBorg("Borgie", 50, 100)
print(hybridborg.attack())
print(hybridborg.check_arrows())

wizard1 = Wizard("Merlin",50)
archer1 = Archer("Robin",300)