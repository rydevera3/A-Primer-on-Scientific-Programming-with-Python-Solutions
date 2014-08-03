# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 13:27:12 2014

@author: rdevera
"""

# Chapter 1: Exercise 9
# Type in programs and debug them
# Type these short programs in your editor and execute them. When they do not
# work, identify and correct the erroneous statements. 

#a) Does sin^2(x)+cos^2(x)=1?

"""
from math import sin, cos
x = pi/4
1_VAL = sin^2(x)+cos^2(x)
print 1_VAL
"""

# prints the error
"""
1. Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Spyder.app/Contents/Resources/lib/python2.7/spyderlib/widgets/externalshell/sitecustomize.py", line 540, in runfile
    execfile(filename, namespace)
  File "/Users/rdevera/A Primer on Scientific Programming with Python Solutions/Chapter 1/sin2_plus_cos2.py", line 17
    1_VAL = sin^2(x)+cos^2(x)
        ^
SyntaxError: invalid syntax 

2. Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Spyder.app/Contents/Resources/lib/python2.7/spyderlib/widgets/externalshell/sitecustomize.py", line 540, in runfile
    execfile(filename, namespace)
  File "/Users/rdevera/A Primer on Scientific Programming with Python Solutions/Chapter 1/sin2_plus_cos2.py", line 39, in <module>
    VAL_1 = sin(x)^2+cos(x)^2
TypeError: unsupported operand type(s) for ^: 'float' and 'float'
"""

# To fix the code we do the following change 1_VAL since a variable name cannot
# start with a number. We also need to import pi form the math module. Finally
# we also need to change sin^(x), cos^(x)

from math import sin, cos, pi
x = pi/4
VAL_1 = sin(x)**2+cos(x)**2
print VAL_1
