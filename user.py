from abc import ABC
from random import randint

class System (ABC):
    
    name = "Islamic Bank Limited"
    def __init__(self,name,email,address,phone):
        self.name = name
        self.email = email
        self.address = address
        self.phone = phone

class User (System):
    def __init__(self, name, email, address, phone):
        self.balance = 00.00
        self.min_withdraw = 100
        self.max_withdraw = 1000000
        super().__init__(name, email, address, phone)
        
    def view_balance (self):
        print (f'Your Total Amount is : {self.balance} tk')

    def deposit(self,amount):
        if amount < 0:
            print (f'You have no amount in Your account !')
        else :
            self.balance += amount
            print (f'{amount} taka Deposited Successfully ')

    def withdraw(self,amount):
        if amount < self.min_withdraw:
            print(f'You can not Withdraw Money below : {self.min_withdraw} tk')
        elif amount > self.max_withdraw:
            print(f'You can not withdraw More than {self.max_withdraw} tk')
        else:
            self.balance -= amount 
            print (f'Here  is Your money {amount} tk\nYour Balance after withdraw Money {self.balance} tk')

class Account(System):
    def __init__(self, name, email, address, phone,account_types,gender,account_number):
        self.account_types = account_types
        self.gender = gender
        self.account_number = account_number
        super().__init__(name, email, address, phone,)

class Admin(System):
    account_numbers = 100000
    def __init__(self, name, email, address, phone):
        super().__init__(name, email, address, phone)
        
    def creat_account (self,bank,account):
        bank.create_account(account)

    def delete_account(self,bank,account_name):
        bank.delete_account(account_name)

    def view_account(self,bank):
        bank.view_account()
        
