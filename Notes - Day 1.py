# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:33:14 2018

@author: Student
"""

import sys
sys.path.append("C:\\Users\\Student\\Documents\\GitHub\\LearnPython")

import math

import random

random.seed(val) # val is integer

random.randint(lowerlimir,upperlimit)






# STRINGS ####################################################

import re # import regular expressions module

"\n" # newline

# using backslash to escape quote inside the string
'in today\'s class'
"the person said \"hello\""

# indexing inside strings
co = "ONLC"
co[-1] = "C"  # last character is always -1 going backwards
co[0] = "O"


# strings are immutable
# asdf"[2] = "f" doesn't work
# can multiply strings to duplicate
"asdf"*4 = 'asdfasdfasdfasdf'

# Split strings
company = "Online Consulting"
company.split()[1]
Out[122]: 'Consulting'

# get last: use negative 1
company = "Online Consulting Incorporated"
company.split()[-1]
f = company.split()
f[len(f)-1]

# function vs. method - terms are used interchangeably
print(x) # <-- function
string.upper() # <-- method

[[fill]align][sign][width][,][.precdision][type]



# ITERABLES #################################################
mylist = []
# Can contain other lists

mylist.append(1) # Can call mylist.append
mylist.insert(1,1) #mylist.insert(what,where)
del mylist[2]
mylist.pop(0) # deletes an element of the list and returns that value
mylist.index(2) # returns that element
mylist.reverse() # reverse the order
mylist2.sort() # but requires all elements of list to be the same time

random.choice(mylist) # chooses a random value within a sequence
random.shuffle(mylist) # shuffle list

pass # keyword to let python know to pass through a function


{, , , ,} # set
{: } #dictionary
(, , , ,)  # tuple
# Tuple
myt = "123","234234",234234,23,4234
# to force a single element to a tuple, use a comma
myt = 1,  # is a tuple
myt = 1 # is an integer

# Ranges: a sequence of numbers, useful for loops
r1 = range(11)
list(r1)  # convert to list
list(range(1,11))
list(range(1,102,10))  # range(start,stop,stride i.e. step by)
