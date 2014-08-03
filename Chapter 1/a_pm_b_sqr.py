# -*- coding: utf-8 -*-
"""
Created on Sun Aug  3 13:42:52 2014

@author: rdevera
"""

# Chapter 1: Exercise 9
# Type in programs and debug them
# Type these short programs in your editor and execute them. When they do not
# work, identify and correct the erroneous statements. 

#c) Verify these equations:

# (a+b)^2 = a^2+2ab+b^2
# (a-b)^2 = a^2-2ab+b^2

"""
a = 3,3 b=5,3

a2 = a**2
b2 = b**2

eq1_sum = a2+2ab+b2
eq2_sum = a2-2ab+b2

eq1_pow = (a+b)**2
eq2_pow = (a-b)**2

print 'First equation: %g=%g', % (eq1_sum, eq1_pow)
print 'Second equation: %g=%g', % (eq2_sum, eq2_pow)

1. Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Spyder.app/Contents/Resources/lib/python2.7/spyderlib/widgets/externalshell/sitecustomize.py", line 540, in runfile
    execfile(filename, namespace)
  File "/Users/rdevera/A Primer on Scientific Programming with Python Solutions/Chapter 1/a_pm_b_sqr.py", line 18
    a = 3,3 b=5,3
            ^
SyntaxError: invalid syntax

2. Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Spyder.app/Contents/Resources/lib/python2.7/spyderlib/widgets/externalshell/sitecustomize.py", line 540, in runfile
    execfile(filename, namespace)
  File "/Users/rdevera/A Primer on Scientific Programming with Python Solutions/Chapter 1/a_pm_b_sqr.py", line 33
    a = 3.3 b=5.3
            ^
SyntaxError: invalid syntax

3. Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Spyder.app/Contents/Resources/lib/python2.7/spyderlib/widgets/externalshell/sitecustomize.py", line 540, in runfile
    execfile(filename, namespace)
  File "/Users/rdevera/A Primer on Scientific Programming with Python Solutions/Chapter 1/a_pm_b_sqr.py", line 47
    eq1_sum = a2+2ab+b2
                   ^
SyntaxError: invalid syntax

4. Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Applications/Spyder.app/Contents/Resources/lib/python2.7/spyderlib/widgets/externalshell/sitecustomize.py", line 540, in runfile
    execfile(filename, namespace)
  File "/Users/rdevera/A Primer on Scientific Programming with Python Solutions/Chapter 1/a_pm_b_sqr.py", line 64
    print 'First equation: %g=%g', % (eq1_sum, eq1_pow)
                                   ^
SyntaxError: invalid syntax

"""

# The above code has many errors. The first one is the , in 3,3 and 5,3. These
# values should be 3.3 and 5.3. The second is the spaceing between a and b
# to fix this just define a and b on separate lines. The third error is in 2ab
# there needs to be a multiplicatin operator 2*a*b. The fourth error is in the
# print statement. There should be no , after %g'.

a = 3.3 
b = 5.3
a2 = a**2
b2 = b**2

eq1_sum = a2+2*a*b+b2
eq2_sum = a2-2*a*b+b2

eq1_pow = (a+b)**2
eq2_pow = (a-b)**2

print 'First equation: %g=%g' % (eq1_sum, eq1_pow)
print 'Second equation: %g=%g' % (eq2_sum, eq2_pow)


