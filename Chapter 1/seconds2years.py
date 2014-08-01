# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 22:06:20 2014

@author: rdevera
"""

# Chapter 1: Exercise 3
# Can a newborn baby in Norway expect to live for one billion (10^9)
# seconds?

# There are 60 seconds in a minute 60 minutes in an hour 24 hours in a day
# and 365 days in a year
# This is assuming that a newborn baby will live a natural life free of diseases, 
# any possible accidents, and any environmental factors that might affect a 
# persons health

sec = 60
minutes = 60
hours  = 24
day = 365

total_seconds = sec*minutes*hours*day

# number of seconds given
num_secs = 10**9 # ** is how we compute a power in python

years_on_earth = num_secs/total_seconds
print years_on_earth

# assuming a person can live up to 80 years average
if years_on_earth < 80:
    print "The newborn can live for one billion seconds"
else:
    print "The newborn will not live for one billion seconds"
    
    