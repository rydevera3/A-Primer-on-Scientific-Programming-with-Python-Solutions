# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 11:08:36 2014

@author: rdevera
"""

# Chpater 7: Problem 3

# Add an attribute transactions to the Account class from Chapter 7.2.1.
# The new attribute counts the number of transactions done in the deposit and
# withdrawl methods. The total number of transactions should be printed in the 
# dump method. Write a simple test program to demonstate the transaction gets the 
# right value after some calls to deposit and withdrawl.

class Account:
    def __init__(self,name,account_number,initial_amount):
        self.name=name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 0
        
    def deposit(self,amount):
        self.balance += amount
        self.transactions += 1
        
    def withdrawl(self,amount):
        self.balance -= amount
        self.transactions += 1
        
    def dump(self):
        s = '%s, %s, balance: %s' % (self.name,self.no,self.balance)
        print s
        print 'Your total amount of transactions is ' + str(self.transactions)
        
def main():
    
    account1 = Account("Ryan de Vera","19371554951",2000)
    account1.deposit(10000)
    account1.withdrawl(10)
    account1.dump()
    
    account2 = Account("John Olsen","1948723482",15)
    account2.withdrawl(20)
    account2.dump()
    
if __name__=="__main__":
    main()
        
    