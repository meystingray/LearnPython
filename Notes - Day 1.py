# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:33:14 2018

@author: Student
"""

import math

import random

random.seed(val) # val is integer

random.randint(lowerlimir,upperlimit)

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





