# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 22:17:27 2014

@author: rdevera
"""

# Chapter 1: Exercise 4
# Make a program where you set a length given in meters and then compute and write 
# out the corresponding length measure in inches, in feed, in yards, and in miles. 
# Use that one inch is 2.54 cm, one foot is 12 inches, one yard in 3 feet, and one 
# British mile is 1760 yards.

# Choose a length in meters
m = input("Choose a length in meters; m = ")

# 1 meter is 100 cm

m_to_cm = m*100
print m_to_cm

# 1 inch is 2.54 cm

cm_to_inch = m_to_cm/2.54
print cm_to_inch

# 1 ft is 12 inches

inch_to_feet = cm_to_inch/12
print inch_to_feet

# 1 yd is 3 feet

feet_to_yd = inch_to_feet/3
print feet_to_yd

# 1760 yd is 1 british mile

yd_to_mile = feet_to_yd/1760
print yd_to_mile