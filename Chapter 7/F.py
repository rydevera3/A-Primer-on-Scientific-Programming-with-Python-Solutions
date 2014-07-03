# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 17:34:18 2014

@author: rdevera
"""

# Chapter 7: Problem 1

# Make a class F that implements the function
# f(x;a,w) = exp(-a*x)sin(wx)
# A value(x) method computes the values of f, while a and w are class
# attributes.


import math as math

class F:
    
    def __init__(self,a,w):
        self.a=a
        self.w=w
        
    def value(self,x):
        return math.exp(-self.a*x)*math.sin(self.w*x)
        
    