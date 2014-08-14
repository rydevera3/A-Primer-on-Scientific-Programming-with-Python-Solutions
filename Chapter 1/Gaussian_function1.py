# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 13:54:35 2014

@author: rdevera
"""

# Chapter 1: Exercise 10
# Evaluate a gaussian function
# The bell shaped gaussian function 
# f(x) = 1/(sqrt(2*pi)*s)*exp(-0.5*(x-m/s)^2)
# is one of the most widely used functions in science and technology. The 
# parameters m and s are real numbers, where s must be greater than zero.
# Make a program for evaluating this function when m=0, s=2 and x=1.
# Verify the program's result by comparing with hand calculations on a calculator.

from math import pi, exp, sqrt

m = 0
s = 2
x = 1

f = 1.0/(sqrt(2*pi)*s)*exp(-0.5*(x-m/s)**2)
print 'The value of the Gaussian function is %g' % f

# The calculated value for f is 
# f = 0.1209854 so the results are correct.

