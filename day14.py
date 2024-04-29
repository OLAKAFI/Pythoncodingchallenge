# HIGHER ORDER FUNCTIONS
# Function as a Parameter
def sum_numbers(nums):  # normal function
    return sum(nums)    # a sad function abusing the built-in sum function :<

def higher_order_function(f, lst):  # function as a parameter
    summation = f(lst)
    return summation
result = higher_order_function(sum_numbers, [1, 2, 3, 4, 5])
print(result)       # 15


# # Function as a Return Value
def square(x):          # a square function
    return x ** 2

def cube(x):            # a cube function
    return x ** 3

def absolute(x):        # an absolute value function
    if x >= 0:
        return x
    else:
        return -(x)

def higher_order_function(type): # a higher order function returning a function
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute

result = higher_order_function('square')
print(result(3))       # 9
result = higher_order_function('cube')
print(result(3))       # 27
result = higher_order_function('absolute')
print(result(-3))      # 3

print('----------------------------------------------------------------------------------------------------')

# Built-in Higher Order Functions
# Python - Map Function

lists = [1, 2, 3, 4, 5] # iterable
def square(x):
    return x ** 2
lists_squared = map(square, lists)      #map(function, iteratable lists)
print(list(lists_squared))    # [1, 4, 9, 16, 25]
# Lets apply it with a lambda function
lists_squared = map(lambda x : x ** 2, lists)
print(list(lists_squared))    # [1, 4, 9, 16, 25]

print('----------------------------------------------------------------------------------------------------')

numbers_int = [1, 2, 3, 4, 5]  # iterable
numbers_str = map(str, numbers_int)
print(list(numbers_str))    # [1, 2, 3, 4, 5]

print('----------------------------------------------------------------------------------------------------')

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']  # iterable
changed_names = map (lambda name: name.upper(), names)
print(list(changed_names))

print('----------------------------------------------------------------------------------------------------')


# Python - Filter Function
# Lets filter only even nubers
numbers = [1, 2, 3, 4, 5]  # iterable
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False

# even_numbers = filter(is_even, numbers)
even_numbers = filter(lambda num: True if num % 2 == 0 else False, numbers)
print(list(even_numbers))       # [2, 4]


print('----------------------------------------------------------------------------------------------------')

names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
long_names = filter(lambda name: True if len(name) >= 7 else False, names)
print(list(long_names))

print('----------------------------------------------------------------------------------------------------')
from functools import reduce
numbers_str = ['1', '2', '3', '4', '5']
total = reduce(lambda x,y: int(x) + int(y), numbers_str)
max_number =reduce(lambda a,b: a if int(a)>int(b) else b, numbers_str)
print('The maximum number in the list is', max_number)
print('Total of the list is: ', total)


print('----------------------------------------------------------------------------------------------------')
print('EXERCISE DAY 14')
print('----------------------------------------------------------------------------------------------------')
# Use for loop to print each country in the countries list.
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for country in countries:
    print(country)
for name in names:
    print(name)
for numb in numbers:
    print(numb)

# list_countries = [country for country in countries]
# list_names = [name for name in names]
# list_numbers = [num for num in numbers]
# print('The list of countries:', list_countries)
# print('The list of names:', list(list_names))
# print('The list of numbers:', list(list_numbers))

# Use map to create a new list by changing each country to uppercase in the countries list
uppercase_country =map(lambda country: country.upper(), countries)
uppercase_names =map(lambda name: name.upper(), names)
print('The uppercase of the countries list: ', list(uppercase_country))
print('The uppercase of the names list: ', list(uppercase_names))

# Use map to create a new list by changing each number to its square in the numbers list
square_number = map(lambda num: num**2, numbers)
print('The square of the numbers in the list: ', list(square_number))

print('----------------------------------------------------------------------------------------------------')

# Use filter to filter out countries containing 'land'.
filter_land = filter(lambda x: True if 'land' in str(x) else False, countries)
print('The list of country that contains the word land: ', list(filter_land))

# Use filter to filter out countries having exactly six characters.
countries_with_6char = filter(lambda x: True if len(x) ==6 else False, countries)
print('The countries with 6 characters: ', list(countries_with_6char))

# Use filter to filter out countries containing six letters and more in the country list.
countries_with_6up = filter(lambda x: True if len(x) >=6 else False, countries)
print('The countries with 6 or more characters: ', list(countries_with_6up))

# Use filter to filter out countries starting with an 'E'
countries_start_E = filter(lambda x: True if str(x[0]) == 'E'else False, countries)
print('Countries that starts with E: ', list(countries_start_E))

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback))