# The Concept: Overriding replaces a parent's method. super() calls the parent's method so you can add more logic to it.


class Animal:
    def speak(self):
        return "some sound"
    
class Dog(Animal):
    def speak(self):
        return "woof"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"
    
cats = Cat()

print(cats.speak())