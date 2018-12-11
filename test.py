# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:16:23 2018

@author: Student
"""


greeting = "hi"

def main2():
    global greeting
    greeting = "hi2"
    name = input("What is your first name: ")
    say_holla(name)
    q(name)

def say_holla(name = "class"):
    print("holla",name)
    
def q(name):
    print(name)

if __name__ == "__main__":
    print(__name__)
    main()
    
    
for name in dir():
    if not name.startswith('_'):
        del globals()[name]