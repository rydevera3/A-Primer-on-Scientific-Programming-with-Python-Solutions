# -*- coding: utf-8 -*-
"""
Created on Tue Jul  8 08:56:22 2014

@author: rdevera
"""

# Chapter 7: Problem 9

# Restructure the code in the Lagrange function from Exercise 5.13 in a class.
# The constructor should take the points as argument, and a call method should 
# evaluate the pl(x) polynomial at an arbitrary point x. Include the graph function
# as a method in the class. Write the verify function and call it as described
# in Exercise 5.13. Use the class to repeat the investigations that show how the 
# interpolating polynomial may oscillate as the number of interpolation points
# increases.

import numpy as np
import matplotlib.pyplot as plt

class Lagrange:
    
    def __init__(self,points):
        self.xc=points[:,0]
        self.yc=points[:,1]
        
    def __call__(self,x):
        n=self.xc.shape[0]
        Lk = np.zeros([n,1])
        for k in range(n):
            L = 1
            for j in range(n):
                if(k!=j):
                    temp = L*float(x-self.xc[j])/float(self.xc[k]-self.xc[j])
                    L = temp
            Lk[k]=L        
        
        return np.dot(np.transpose(Lk),self.yc)
        
    def graph(self):
        xa = np.sort(self.xc)
        idx = np.argsort(self.xc)
        ya = self.yc[idx] 
        plt.plot(xa,ya)
        
    def verify(self,points):
        n,m = points.shape
        if(n>m):
            return abs(points[:,0]-points[:,1])
        else:
            return abs(points[0,:]-points[1,:])
        
        
def main():
    
    # Set up object for test
    # points array should have x values in first column and y values in second
    # column
    p = np.array([[1,1],[2,4],[-2,4],[3,9],[0,0]]) # Create an n by 2 array
    p1 = Lagrange(p)
    print p1(4)
    p1.graph()
    
    x = np.linspace(0,np.pi,5)
    y = np.sin(x)
    p2 = np.transpose(np.array([x,y]))
    
    p_s = Lagrange(p2)
    pl = np.zeros([len(x),1])
    check_points = np.zeros([len(x),2])
    
    for k in range(len(x)):
        pl[k] = p_s(x[k])
    check_points = np.array([pl,y])
    
    print p_s.verify(check_points)
    
    x_mid = 1.045
    y_mid_actual = np.sin(x_mid)
    y_mid_lagrange = p_s(x_mid)
    print y_mid_actual, y_mid_lagrange
    print abs(y_mid_actual-y_mid_lagrange)
    
    
if __name__=="__main__":
    main()
                    
        