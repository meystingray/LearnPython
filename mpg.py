# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 14:53:22 2018

@author: Student
"""
import sys
def mpg(miles,gallons):
    return(miles/gallons)
    
def main(args = []):
    #print(args)
    if len(args) == 1:
        miles = int(input("Enter miles: "))
        gallons = int(input("Enter gallons: "))
    else:
        miles = int(args[1])            
        gallons = int(args[2])
        
    print("Calculated MPG: ",round(mpg(miles,gallons),2))
            
if __name__ == '__main__':
    main(sys.argv)