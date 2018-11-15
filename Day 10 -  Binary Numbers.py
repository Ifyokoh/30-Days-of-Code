# Task 
# Given a base-10 integer, n, convert it to binary (base-2). Then find and
# print the base-10 integer denoting the maximum number of consecutive 1's
# in n's binary representation.




#Solution
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    
    n = int(input())

    count = 0
    while n:
        n &= n << 1
        count += 1

    print(count)
    
    

    #Another method
    n = int(input().strip())
    t = "{0:b}".format(n)
    print(max(map(len,t.split("0"))))
