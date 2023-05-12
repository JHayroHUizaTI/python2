class Account:
    """Simple account class with balance"""
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        if amount >0:
            self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
    def show_balance(self):
        print(f"{self.name} your Balance is {self.balance}")

if __name__ == '__main__':
    name = input("what is your name? ")
    yolo= Account(name,0)
    yolo.show_balance()
    yolo.deposit(1200)
    yolo.withdraw(500)
    yolo.show_balance()

