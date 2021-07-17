from random import randint
from abc import ABC, abstractmethod


class Bank(ABC):
    def __init__(self):
        self.balance = 0

    @abstractmethod
    def charge(self, amount): pass

    @abstractmethod
    def deposit(self, amount): pass

    @abstractmethod
    def getBalance(self): pass


class Checking(Bank):
    def charge(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return '${}.00'.format(self.balance)


# Entry point for the app
if __name__ == '__main__':
    # instance of the class
    checking = Checking()

    # sets the protected variable
    checking.deposit(randint(100, 1000))
    # gets the protected variable
    print('\nYour starting balance is:\n\t{}\n'.format(checking.getBalance()))

    spend = randint(10, 90)
    print('\nYou spent:\n\t${}.00\n'.format(spend))
    # increments the protected variable
    checking.charge(spend)
    # gets the protected variable
    print('\nYour balance is:\n\t{}\n'.format(checking.getBalance()))
