# -*- coding: utf-8 -*-
"""
Created on Sun Jul  6 11:23:38 2014

@author: rdevera
"""

# Chapter 7: Problem 8

# Make a class for linear springs.
# To elongate a spring a distance x, one needs to pull the spring with a force
# kx. The parameter k is known as the spring constant. The corresponding potential
# energy in the spring is 1/2kx^2. Make a class for springs. Let the constructor
# store k as a class attribute, and impltement the methods force(x) and energy(x)
# for evaluating the force and potential energy respectively. 

# Define class linear spring with two classes inside. We now have a class linear
# spring with two callable methods Force and Energy.

class linearSpring:
    pass

    class Force:
    
    # Force on a linear spring is given by k*x
    
        def __init__(self,k=1):
            self.k = k
        def __call__(self,x):
            return self.k*x
        
    class Energy:
    
        def __init__(self,k=1):
            self.k = k
        def __call__(self,x):
            return 0.5*self.k*(x**2)
    
        

        
def table(f, a, b, n, heading=''):
    """ Write out f(x) for x in [a,b] with steps h=(b-a)/n """
    print heading
    h = (b-a)/float(n)
    for i in range(n+1):
        x = a+i*h
        print 'function value = %10.4f at x=%g' % (f(x),x)
        
def main():
    k = 2.5
    a = 1
    b = 2
    n = 5
    
    springForce = linearSpring.Force(k)   
    table(springForce,a,b,n)
    
    springEnergy = linearSpring.Energy(k)
    table(springEnergy,a,b,n)
    
if __name__=="__main__":
    main()