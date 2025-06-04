class calculator:
    def add(self,a,b):
        return a+b
calc=calculator()
result=calc.add(5,3)
print("result",result)

class car:
    def __init__(self):
        self.accelerator=False
        self.brake=False
        self.clutch=False
    def start(self):
        self.clutch=True
        self.accelerator=True
        self.brake=True
        print("car started")
car1=car()
car1.start()

class account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("total balance=",self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs", amount, "was credited")
        print("total balance=", self.get_balance())
    def get_balance(self):
        return self.balance

acc1=account(100000,3)
acc1.debit(1000)
acc1.credit(200)



