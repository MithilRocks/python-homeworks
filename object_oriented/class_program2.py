# WAP to implement a bank account class. Implement withdraw, deposit, check balance method

class My_bank:
    count_account_number = 1

    def __init__(self, name, balance = 0):
        self.name = name
        self.balance = balance
        self.account_number = My_bank.count_account_number

        My_bank.count_account_number += 1
    
    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print("{} amount withdrawn. Balance is: {}".format(amount, self.balance))
        else:
            print("Insufficient balance")

    def deposit(self, deposit):
        self.balance += deposit
        print("{} amount deposited. Balance is: {}".format(deposit, self.balance))