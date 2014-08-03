# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 13:35:48 2014

@author: rdevera
"""

# Chapter 1: Exercise 9
# Type in programs and debug them
# Type these short programs in your editor and execute them. When they do not
# work, identify and correct the erroneous statements. 

#b) Work witht he expressions for movement with constant acceleration:
"""
v0 = 3 m/s
t = 1 s
a = 2 m/s**2
s = v0*t+1/2 a*t**2
print s
"""

"""
1. Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Spyder.app/Contents/Resources/lib/python2.7/spyderlib/widgets/externalshell/sitecustomize.py", line 540, in runfile
    execfile(filename, namespace)
  File "/Users/rdevera/A Primer on Scientific Programming with Python Solutions/Chapter 1/acceleration.py", line 15
    v0 = 3 m/s
           ^
SyntaxError: invalid syntax

2. Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Spyder.app/Contents/Resources/lib/python2.7/spyderlib/widgets/externalshell/sitecustomize.py", line 540, in runfile
    execfile(filename, namespace)
  File "/Users/rdevera/A Primer on Scientific Programming with Python Solutions/Chapter 1/acceleration.py", line 41
    s = v0*t+1/2 a*t**2
                 ^
SyntaxError: invalid syntax

"""

# In this code we need to comment out the m/s, s and m/s**2. We also need to 
# put a multiplication operator between 1/2 and a we also need to make sure 
# we are not doing integer division with the 1/2

v0 = 3 # m/s - meters per second units
t = 1 # s - seconds
a = 2 # m/s**2 - measure for acceleration is meters per second squared
s = v0*t+1.0/2.0*a*t**2
print s


