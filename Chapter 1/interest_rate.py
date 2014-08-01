# -*- coding: utf-8 -*-
"""
Created on Thu Jul 31 23:15:05 2014

@author: rdevera
"""

# Chapter 1: Exercise 6
# let p be a bank's interest rate in percent per year. An initial amount A has then grown
# to A(1+p/100)^n after n years. Make a program for computing how much money 1000
# euros have grown to after 3 years with 5% interest rate.

# Initial amount A

A = input("Initial amount of euros A: A = ")
A = float(A)

# Percentage rate

P = input("Enter an integer percentage rate: P = ")
P = float(P)

# Number of years

n = input("Enter number of years: n = ")
n = float(n)

print A*(1+P/100)**n