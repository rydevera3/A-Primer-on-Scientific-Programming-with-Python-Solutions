# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 00:12:26 2014

@author: rdevera
"""

# Chapter 7: Problem 10

# Make a class that can only do one thing: pring a writes "Hello, World!" to
# the screen, when a is an instanse of the class.

class HelloWorld:
    
        
    def __str__(self):
        
        return "Hello, World!"
            
def main():
    
    a = HelloWorld()
    
    # Check to see that a is an instance of HelloWorld
    print isinstance(a,HelloWorld)
    
    # HelloWorld has a special method __str__ so that when a in an instance
    # of HelloWorld, print a returns "Hello, World!"
    print a
    

if __name__=="__main__":
    main()