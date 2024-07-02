#OOP
class PlayerCharacter:
    membership = True # Class Object Attribute - it is static
    def __init__(self,name="Anonymous",age=0):
        if(self.membership):
            self.name = name #attribute
            self.age = age # attribute
        if(self.age < 18):
            print(f"{self.name} You are not old enough") 

    def run(self):
        print(f"Player: {self.name} is running")

    def message(self, message="No message to:"):
        print(f"{message} {self.name}")
         
    @classmethod # Method on the class but no need to instanciate it
    def adding_things(cls,num1,num2):
        return num1 + num2
    
    @staticmethod # Same as classmethod but you do not have access to the instance
    def adding_things2(cls,num1,num2):
        return num1 + num2

player1 = PlayerCharacter("MezcalFighter",27)
player1.run()
player1.message("Hello!")

player2 = PlayerCharacter()
player2.run()
player2.message()

print(player1.adding_things(2,3))
print(PlayerCharacter.adding_things(2,3))