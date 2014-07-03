# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 18:59:40 2014

@author: rdevera
"""

# Chapter 7: Problem 6

# The constructor in class Line in Exercise 7.5 takes two points as arguments.
# NOw we want to have more flexibility i the way we specify a straight line:
# we can give two points, a point and a slope, or a slope and the line's
# interception with the y-axis.

class Line2:
    
    def __init__(self,p1,p2):
        if isinstance(p1,(tuple,list)) and isinstance(p2,(tuple,list)):
            # p1 and p2 is a point
            self.x0 = p1[0]
            self.y0 = p1[1]
            self.x1 = p2[0]
            self.y1 = p2[1]
            self.method = 1
            
        elif isinstance(p1,(tuple,list)) and (p2,(float,int)):
            # p1 is a point and p2 is a slope
            self.a = p2
            self.b = p1[1]-p2*p1[0]
            self.method = 2
            
        else:
            # p1 is a slope and p2 is the lines intercept
            self.m = p1
            self.b = p2
            self.method = 3
            
    def value(self,x):
        if (self.method==1):
            m = float(self.y1-self.y0)/float(self.x1-self.x0)
            b = self.y1-m*self.x1
            return m*x+b
        elif(self.method==2):
            return self.a*x+self.b
        else:
            return self.m*x+self.b
        
            
def main():
    
    l1 = Line2((0,-1),(2,4))
    print l1.value(0.5)
    print "\n"
    
    l2 = Line2((0,-1),5.0/2.0)
    print l2.value(0.5)
    print "\n"
    
    l3 = Line2(5.0/2.0,3)
    print l3.value(0.5)

    
if __name__=="__main__":
    main()