# Different classes using the same method name but doing different things.

from abc import ABC , abstractmethod

class paymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass

class Credit(paymentMethod):
    def pay(self, amount):
        print(f"{amount}")

class Paypal(paymentMethod):
    def pay (self, amount):
        print(f"{Paypal}")

class Bitcoin(paymentMethod):
    def pay (self,amount):
        print(f"{amount}")

def process_payment(payment_method, amount):
    payment_method.pay(amount)

cc= Credit()

process_payment(cc,100)
