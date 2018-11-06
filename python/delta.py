from numpy import *
from math import *


def deltPositive(delt, a, b):
    roots = [0]*2
    roots[0] = (-b + sqrt(delt)) / (2*a)
    roots[1] = (-b - sqrt(delt)) / (2*a)
    return roots


def deltNull(a, b):
    return -b/(2*a)


def delta(a,b,c):
    delt = pow(b,2) - 4*a*c
    return delt



#MAIN

if __name__ == "__main__" :

    a = -4
    b = 5
    c = 10
    delt = delta(a,b,c)
    
    if (delt > 0)
        print("delta positif, racines : " + deltPositive(
