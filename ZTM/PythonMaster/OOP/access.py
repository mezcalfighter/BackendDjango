# Private - Public 
# evetyhing is public but there are conventions
class PlayerCharacter:
    def __init__(self,name, age):
        self._name = name
        self._age = age

    def run(self):
        print("Run")

    def speak(self):
        print(f"My name is {self._name}, and I am {self._age} years old")

player1 = PlayerCharacter("Emanuel",27)
player1.name = "!!!"
player1.speak = "Boooo!"

print(player1.speak) # You can still modify it but using _variable its a convention to say something is private