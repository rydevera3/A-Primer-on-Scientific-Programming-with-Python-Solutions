# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 14:04:55 2014

@author: rdevera
"""

# Chapter 1: Exercise 11
# Compute the air resistance on a football
# The drag force, due to air resistance, on an object can be expressed as
# F_d = 1/2*C_D*rho*A*V^2
# where rho is the density of the air, V is the velocity of the object, A
# is the cross-sectional area (normal to velocity direction) and C_D is
# the drag coefficient , which depends heavily on the shape of the object and the 
# roughness of the surface.
# The gravity force on an object with mass m is F_g = m*g, where 
# g = 9.81 m/s^2
# We can use the formula for F_d and F_g to study the importance of air 
# resistance versus gravity when kicking a football. The density of air is 
# rho = 1.2 kg/m^3. We have A = pi*a^2 for any ball with radius a. For a football
# a = 11 cm. The mass of a football is 0.43 kg. C_D can be taken as 0.2.
# Make a program that computes the drag force and the gravity force on a football.
# Write out the forces with one decimal in units of Newton (N = kg m/s^2)
# Also print the ratio of the drag force and the gravity force. Define
# C_D, rho, A, V, m, g, F_d and F_g as variables, and put a comment with the 
# corresponding unit. Use the program to calculate the forces on the ball
# for a hard kick, V=120 km/h and for a soft kick V=10 km/h.

from math import pi

g = 9.81 # m/s^2
rho = 1.2 # kg/M^3

# a = 11 cm needs to be converted to meters there are 100 centimeters in a meter
a = 11/100.0 # m
m = 0.43 # kg
C_D = 0.2
A = pi*a**2

# V for the kick has to be expressed in m/s
# for every 1 km there are 1000 m and for every hour there are 3600 seconds

V1 = 120*1000/3600.0
V2 = 10*1000/3600.0

F_d = 1.0/2.0*C_D*rho*A*V1**2
F_g = m*g
ratio = F_d/F_g
print 'The drag force for the hard kick is %g N' % F_d
print 'The force of gravity on the football is %g N' % F_g
print 'The ratio of drag force to gravity force is %g N' % ratio

F_d = 1.0/2.0*C_D*rho*A*V2**2
F_g = m*g
ratio = F_d/F_g

print 'The drag force for the hard kick is %g N' % F_d
print 'The force of gravity on the football is %g N' % F_g
print 'The ratio of drag force to gravity force is %g N' % ratio