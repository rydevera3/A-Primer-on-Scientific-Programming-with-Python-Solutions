# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 17:45:07 2014

@author: rdevera
"""

# Chapter 7: Problem 2

# Make a class Simple with one attribute i, one method double, which replaces
# the value of i by i+i, and a constructor that initializes the attribute.

class Simple:
    
    def __init__(self,i=1):
        self.i=i
        
    def double(self):
        return 2*self.i


def main():
    
    s1 = Simple(4)
    for i in range(4):
        s1.double()
    print s1.i
    
    
if __name__=="__main__":
    main()