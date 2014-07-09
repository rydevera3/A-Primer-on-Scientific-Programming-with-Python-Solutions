# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 20:39:21 2014

@author: rdevera
"""

# Chapter 7: Problem 7

# Condider a quadratic function f(x;a,b,c)=ax^2+bx+c. Make a class Quadratic
# for representing f, where a,b and c are attributes, and the methods are 
# 1. value for computing a value of f at a point x
# 2. table for writing out a table x and f values for n x values in the 
# interval [L,R]
# 3.roots for computing the two roots

import numpy as np
import pandas as pd

class Quadratic:
    
    def __init__(self,a=1,b=1,c=1):
        self.a = a
        self.b = b
        self.c = c
        
    def value(self,x):
        return self.a*(x**2)+self.b*x+self.c
        
    def table(self,interval,n):
        
        x = np.transpose(np.linspace(interval[0],interval[1],n))
        f = np.zeros([n,1])
        q = Quadratic(self.a,self.b,self.c)
        for k in range(n):
            f[k] =q.value(x[k])
            
        df =  pd.DataFrame(np.transpose(np.array([x,f])))
        df.columns = ['x','f']
        return df
        
def main():
    
    q = Quadratic(2,1,5)
    print q.value(2)
    print q.table([1,3],5)
    
    
if __name__=="__main__":
    main()
            
        