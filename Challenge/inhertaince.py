#TODO

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    
    def get_bonus(self):
        return self.salary * 0.1
    
class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def get_bonus(self):
        return self.salary * 0.15

class Intern(Employee):
    def __init__(self, name, salary, university):
        super().__init__(name, salary)
        self.university = university

    def get_bonus(self):
        return self.salary * 0.05
    

Managers = Manager("Alice",100000, 10)
interns = Intern("bob", 20000,"xyz university")

print(F"{Managers.name},{Managers.get_bonus()}")
