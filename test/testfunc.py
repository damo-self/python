#!/usr/bin/python3.4
import math

def myfunc(a,b,c):
    dat=math.sqrt(abs(b*b-4*a*c))
    return (0-b+dat)/2*a,(0-b-dat)/2*a
print(myfunc(2,3,1))