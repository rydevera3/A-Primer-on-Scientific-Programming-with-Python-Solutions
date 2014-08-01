# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 22:40:55 2014

@author: rdevera
"""

# Chapter 1: Exercise 5
# The density of a substance is defined as rhp = m/V, where m is the mass
# of a volume V. Compute and print out the mass of one liter of each of the following
# substances whose densities in g/cm^3 are found in the file src/files/densities.dat:
# iron, air, gasoline, ice, the human body, silver, and platinum 

# this files can be found at www.simula.no/intro-programming
# click the link zipfile for the 2nd edition

# we want to find the mass of one liter of each substance
# m = V*rho, also 1 liter is 1000 cubic centimeteres


# From the data we can see that 
iron = 7.8
air = 0.0012
gasoline = 0.67
ice = 0.9
the_human_body = 1.03
silver = 10.5
platinum = 21.4

# NOTE: There are ways to import data automatically but since this is an introductory
# chapter is addressed in subsequent chapters we will just assign variable names to the 
# densities.

# Compute the masses

m_iron = iron*1000
m_air = air*1000
m_gasoline = gasoline*1000
m_ice = ice*1000
m_hb = the_human_body*1000
m_silver = silver*1000
m_platinum = platinum*1000

print m_iron, m_air, m_gasoline, m_ice, m_hb, m_silver, m_platinum


