# Task 
# Given an integer, n, print its first 10 multiples. Each multiple n x i(where 1 <= i <= 10)
# should be printed on a new line in the form: n x i = result.



#import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    i = 0
    for i in range(0, 10):
        i = i + 1
        value = n * i
        print(str(n) + ' x ' + str(i) + ' = ' + str(value))
