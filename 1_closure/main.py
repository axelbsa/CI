# -*- coding: utf-8 -*- 
#
# In programming languages, a closure (also lexical closure or function closure) 
# is a function or reference to a function together with a referencing environment—a table 
# storing a reference to each of the non-local variables 
# (also called free variables or upvalues) of that function
#
# -- Wikipedia
#
# We can show this using nested functions in python 
##

def outside_func(x):
    multiplier = 2
    def inside_func(y):
        return multiplier*y
    
    print inside_func(x)

outside_func(5)


