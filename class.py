"""
class employee:
    name="Shreya"
    occupation="Accountant"
    def info(self):
        print(f"Employee name is {self.name} and {self.occupation} by profession ")

a=employee()
b=employee()
c=employee()

a.name = "Ruhi"
a.occupation="data analyst"
a.info()
b.name="Raju"
b.occupation="climber"
b.info()
c.name=" Jaggu"
c.occupation="Runner"
c.info()
"""

#decorator
"""def sprinkles(func):
    def wrapper(*args,**kwargs):
        print("You add sprinkles")
        func(*args,**kwargs)
    return wrapper
@sprinkles
def get_me_a_icecream(flavour):
    print(f"I want {flavour} icecreamm")

get_me_a_icecream("vanilla")"""

class Account:
    def __init__(self,bal,acc):
        self.bal=bal
        self.account=acc


#debit method
    def debit(self,amount):
        self.bal-=amount
        print(f"amount {amount} is debited from account")
        print(f"remaining amount is {self.get_bal()}")
    
    #credit method
    def credit(self,amount):
        self.bal+=amount
        print(f"amount {amount} is credited in your account")
        print(f"Your Total balance is {self.get_bal()}")
    
    def get_bal(self):
        return self.bal

acc1=Account(100000,12345)
print("Your bank balance is",acc1.bal)
print("Your account number is",acc1.account)
acc1.debit(1000)
acc1.credit(500)