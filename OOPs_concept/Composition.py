# One class "has a" list of other objects. This is how your Library managed Book objects.

class Engine:
    def __init__(self,power):
        self.power = power

    def start(self):
        return f"engine with {self.power}hp started"
    
class Car:
    def __init__(self,engine):
        self.engine = engine

    def start(self):
        return self.engine.start()
    

engine = Engine(200)
car = Car(engine)

print(car.start())



        