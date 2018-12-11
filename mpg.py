# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:53:22 2018

@author: Student
"""

def mpg(miles,gallons):
    return(miles/gallons)
    
def main():
    miles = int(input("Enter miles: "))
    gallons = int(input("Enter gallons: "))
    print("Calculated MPG: ",round(mpg(miles,gallons),2))
    

    
main()