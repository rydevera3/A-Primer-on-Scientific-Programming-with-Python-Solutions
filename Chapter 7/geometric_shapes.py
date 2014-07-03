# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 18:20:27 2014

@author: rdevera
"""

# Chapter 7: Problem 4

# The purpose of this exercise is to create classes like class Circle from 
# Chapter 7.2.3 for representing other geometric figures: a rectangle with width
# W, height H and lower left corner (x0,y0); and a general triangle specified by
# its three verticies (x0,y0),(x1,y1) and (x2,y2). Provide three methods:
# __init__, area and circumference.


import math

class Rectangle:
    
    def __init__(self,W,H,x0,y0):
        self.W=W
        self.H=H
        self.x0=x0
        self.y0=y0
        
    def area(self):
        return self.W*self.H
        
    def circumference(self):
        return 2*(self.W+self.H)
        
class Triangle:
    
    def __init__(self,v1,v2,v3):
        self.x0 = v1[0]
        self.y0 = v1[1]
        self.x1 = v2[0]
        self.y1 = v2[1]
        self.x2 = v3[0]
        self.y2 = v3[1]
        
    def area(self):
        return abs((self.x0*(self.y1-self.y2)+self.x1*(self.y2-self.y0)+self.x2*(self.y0-self.y1))/2.0)
        
    def circumference(self):
        d1 = math.sqrt((self.x1-self.x0)**2+(self.y1-self.y0)**2)
        d2 = math.sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2)
        d3 = math.sqrt((self.x2-self.x0)**2+(self.y2-self.y0)**2)
        return d1+d2+d3
        
def main():
    
    R = Rectangle(5,3,1,3)
    print R.area()
    print R.circumference()
    print "\n"
    
    T = Triangle((0,0),(2,0),(2,2))
    print T.area()
    print T.circumference()
    
    
if __name__=="__main__":
    main()
        