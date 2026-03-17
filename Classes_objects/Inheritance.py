# The Concept: A child class takes everything from the parent class so you don't have to rewrite code.

class Animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"
    
class Dog(Animal):
    def speak(self):
        return f"{self.name} bales: Woof!"
    
dog =Dog("Buddy")
print(dog.speak())