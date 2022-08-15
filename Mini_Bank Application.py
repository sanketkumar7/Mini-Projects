import math
from time import sleep
class Customer:
    '''This class is devlop by the Sanketkumar'''
    bankname='Sanketkumar'
    def __init__(self,name,balance=0.0):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount;
        print(f"The amount {amount} has been deposited successfully")
        pass
    def withdraw(self,amount):
        if amount<self.balance:
            print("Withdrawing Cash :",amount)
            self.balance=self.balance-amount
            print("Please collect your Cash...")
            sleep(2)
            print(f"Withdraw Successful. Available balance is {self.balance}")
        else:
            print("Insufficient Balance")
            print("Available Balance:",self.balance)
print(f'Welcome the the {Customer.bankname} Bank')
name=input("Enter your Name")
c=Customer(name)
while True:
    print('d-Deposit | w- Withdraw | E- Exit')
    option=input('Please select option d/w/E : ')
    flag=0
    if option.lower()=='d':
        while flag==0:
            amount=float(input('Please enter amount to deposit. :'))
            if amount>=1:
                c.deposit(amount)
                flag=1
            else:
                print("Please enter the valid amount")
    elif option.lower()=='w':
        while flag==0:
            amount=float(input('Please enter amount to withdraw. :'))
            if amount>=1:
                c.withdraw(amount)
                flag=1
            else:
                print("Please enter the valid amount")
    elif option.lower()=='e':
        print("Thank you for Banking.")
        break
    else:
        print("Please enter the valid option.")