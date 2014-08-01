# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 23:38:10 2014

@author: rdevera
"""

# Chapter 1: Exercise 7

# Suppose sombody has written a simple one-line program for computing sin(1)

# x=1; print 'sin(%g)=%g' % (x,sin(x))

# What is the error? This will print the error 

"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sin' is not defined  
""" 

# How do we fix this error? This is saying that the function sin is not defined
# which is also telling us that we do not have sin imported from the math 
# module. To fix this error the user needs to import sin from math like so:

from math import sin

x = 1; print 'sin(%g)=%g' % (x,sin(x))