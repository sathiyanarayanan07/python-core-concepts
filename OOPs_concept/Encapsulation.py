#  Hiding the "guts" of the object to keep them safe. We use __ (double underscore) to make an attribute private.


#TODO

class password:
    def __init__(self):
        self.__password = None

    def set_password(self,pwd):
        if len(pwd) < 8:
            return False
        
        has_upper = any(char.isupper() for char in pwd)
        has_digit =  any (char.isdigit() for char in pwd)
        
        if not has_upper or  not has_digit:
            return False
        
        self.__password = pwd
        return True
    
    def verify_password(self, pwd):
        return pwd == self.__password
    
p = password()

print(p.set_password("short"))
print(p.set_password("Secure123"))

        
    
        