# One class "has a" list of other objects. This is how your Library managed Book objects.

class Engine:
    def __init__(self,power):
        self.power = power

    def start(self):
        return f"engine with {self.power}np started"
    
    