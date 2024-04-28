from mymodule import generate_full_name
print(generate_full_name('Asabeneh', 'Yetayeh'))

from mymodule import generate_full_name as fullname
print(fullname('Olatunbosun', 'Kafisanwo'))



# IMPORTING INBUILT MODULES
# OS MODULE
# import os
# os.mkdir('directory_name')      # Creating a directory
# os.chdir('path')                # Changing the current directory
# os.getcwd()                     # Getting current working directory
# os.rmdir()                      # Removing directory

# SYS MODULE
# import sys
# sys.exit()          # to exit sys
# sys.maxsize         # To know the largest integer variable it takes
# sys.path            # To know environment path
# sys.version         # To know the version of python you are using

# STATISTIC MODULE
from statistics import * # importing all the statistics modules
ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(mean(ages))       # ~22.9
print(median(ages))     # 23
print(mode(ages))       # 20
print(stdev(ages))      # ~2.3


print('----------------------------------------------------------------------')

# MATH MODULE
import math
print(dir(math))
print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base

print('----------------------------------------------------------------------')

# RANDOM MODULE
from random import random, randint
print(random())   # it doesn't take any arguments; it returns a value between 0 and 0.9999
print(randint(5, 20)) # it returns a random integer number between [5, 20] inclusive


