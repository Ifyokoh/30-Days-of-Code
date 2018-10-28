#Task 
#Given the meal price (base cost of a meal), tip percent (the percentage of the
#meal price being added as tip), and tax percent (the percentage of the meal
#price being added as tax) for a meal, find and print the meal's total cost.

#Solution

import math
import os
import random
import re
import sys

def solve(meal_cost, tip_percent, tax_percent):

    if __name__ == '__main__':
        meal_cost = float(input())

        tip_percent = int(input())
        tip_percent = meal_cost * (tip_percent / 100)

        tax_percent = int(input())
        tax_percent = meal_cost * (tax_percent / 100)

        totalCost = meal_cost + tip_percent + tax_percent
        print(round(totalCost))

solve(12.00, 20, 8)
