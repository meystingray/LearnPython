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

[,,,,] # list
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

# Joining lists of strings with 
r5 = "rock paper scissors"
"*".join(r5)
Out[19]: 'rock*paper*scissors'

# Dictionary
# Use curly braces {}
 myd = {"name":"kris","city":"Dallas","team":"bears"}
 myd['fave number'] = 10
 myd['city']
 myd.values()
 myd.keys()
 myd['cars'] = [1,2,3,4,5]
 myd['cars'][1]
 myd.get('country','default value if key does not exist')
 # 'default value if key does not exist'
# can be nested dictionary
 
 
 # *args and **kwargs
 *args: arbitrary number of args to function
 
 
 #################################### Flow Control
 False objects: None, 0, 0.0, [], ""
 bool(None) == False
 bool(0) == False
 bool(0.0) == False
 bool([]) == False
 # no switch in python
 
 all() and any() - check if any are true
 
 while (expression is True):
     # code to repeat
     if (expression is true):
        # code 
        
for i in range(10):
    print(i)
else: # can have an else to announce completion of looping
    print("loop is done")

# magic command to remove all numbers in IPython
%reset

 # List Comprehension
# want to filter, subset or transorm one list to another list
list1 = [3,4,1,6,9]
list2 = []
for x in list1:
    list2.append(x**2)
list2 = [x**2 for x in list1]

list3 = []
for x in list1:
    if x % 2 == 1:
        list3.append(x)
list3 = [x for x in list1 if x%2 == 1]
 
 
 [word for word in words if word[0].lower().startswith("r")]
 [word for word in words if word[0].upper() == "R"]
 
 
 
 
 # File Processing
 file = open("C:\python\py_intro\file-processing\Demos\my_files\a b c.txt",'r') # 'r' means read, which is default
 open(,'r') # read
 open(,'w') # write, creates a file if it doesn't exist
 file = open("somefile.txt",'a') # append, appends to the existing file, creates if it doesn't exist
 file.write("here is some text for this file")  # write's 31 characters
 file.close() # save what we've done
 file = open("somefile.txt")
 fileContent = file.read()
 with open("anotherfile.txt",'w') as file:  # don't have to do a separate close
     file.write("here is another file")
     
 with open("anotherfile.txt",'a') as file:  # don't have to do a separate close
     file.write("\n here is more text")
 
 with open("anotherfile.txt",'r') as file:
     filelines = file.readlines()
 
filelines = []
with open("anotherfile.txt",'r') as file:
    for line in file:
        line = line.replace("\n","") # remove newline character
        filelines.append(line)
  
 words = ['Woodstock', 'Gary', 'Tucker', 'Gopher', 'Spike', 'Ed',
         'Faline', 'Willy', 'Rex', 'Rhino', 'Roo', 'Littlefoot',
         'Bagheera', 'Remy', 'Pongo', 'Kaa', 'Rudolph', 'Banzai',
         'Courage', 'Nemo', 'Nala', 'Alvin', 'Sebastian', 'Iago']  
    
# write a file
with open('wordlist.txt','w') as file:
    for word in words:
        file.write(word + "\n")
    
with open('wordlist.txt','r') as file:
    mylist = file.readlines()
    
    
# os module
# already available in python
import os
os.getcwd() # get current working directory
os.listdir() # print all the files in the directory
os.path
    
# for csv's, different module
import csv
csv.writer
csv.reader


# Chapter 11: Exception Handling
# Very good handling of different classes of errors
try:
    with open('afilename.txt') as f:
        file.read()
    
except FileNotFoundError:
    print('file not found')
    
except NameError:
    print('bad code')
    
except:
    print('i have no idea')

# To figure out what Exception you're getting    
try:
    1/0
except Exception as e:
    print(type(e)) #prints object type
    print(e) #prints value of str(e)
else:
    # only do this if I did not have an error
    print("here")
finally:
    # do this no matter what
    print("and finally...")
    
    
    
    
    
    
# Chapter 13: Date and Time 

import time
import datetime
Jan 1, 1970 "the epoch" == the beginning of time
# use timeit module for specifically testing performance
epoch = time.gmtime(0)
# Time string
time.mktime(time.localtime())
time.time()
datetime.date(1776, 7, 4)
datetime.date.today()














 