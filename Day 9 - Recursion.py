#TASK
#Write a factorial function that takes a positive integer, N as a parameter
#and prints the result of N! (N factorial).




#SOLUTION
import math
import os
import random
import re
import sys


def factorial(n):
    if n>1:
        return(n*factorial(n-1))
    else:
        return(1)
print(factorial(int(input())))


#Another method using lambda       
factorial = lambda x : 1 if x<=1 else x*factorial(x-1)
print(factorial(int(input())))
        
