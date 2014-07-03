# -*- coding: utf-8 -*-
"""
Created on Thu Jul  3 18:45:13 2014

@author: rdevera
"""

# Chapter 7: Problem 5

# Make a class Line whose constructor takes two points p1 and p2
# (2-tuples or 2-lists) as input. The line goes through these two points.
# A value(x) method computes a value on the line at point x.

class Line:
    
    def __init__(self,p1,p2):
        self.x0 = p1[0]
        self.y0 = p1[1]
        self.x1 = p2[0]
        self.y1 = p2[1]
        
    def value(self,x):
        # Slope of a line is Rise/Run
        m = float((self.y1-self.y0))/float((self.x1-self.x0))
        
        # Find y intercept
        b = self.y1-m*self.x1
        return (m*x+b)
    
# Simple Example
    
def main():
    
    line = Line((0,-1),(2,4))
    print line.value(0.5), line.value(0), line.value(1)
    
if __name__=="__main__":
    main()