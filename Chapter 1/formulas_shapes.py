# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 13:21:32 2014

@author: rdevera
"""

# Chpater 1: Exercise 8
# Type in program text. 
# Type the following program in your editor and execute it. If your program does not
# work, check that you have copied the code correctly:

from math import pi

h=5.0 # height
b=2.0 # base
r=1.5 # radius

area_parallelogram = h*b
print 'The area of the parallelogra is %.3f' % area_parallelogram

area_square = b**2
print 'The area of the square is %g' % area_square

area_circle = pi*r**2
print 'The area of the circle is %.3f' % area_circle

volume_cone = 1.0/3*pi**2*h
print 'The volume of the cone is %.3f' % volume_cone 