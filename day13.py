# DAY 13 LIST COMPREHENSION
language = 'Python'
lst = [i for i in language]
print(lst)

print ('---------------------------------------------')

#print a list of odd number in the range of 10
odd_range_list = [i for i in range(1,10,2)]
print('The list of odd numbers within the range: ',odd_range_list)

print ('---------------------------------------------')

# Make a list of tuples with format (i, i*i)
numbers = [(i, i * i) for i in range(11)]
print('The list of tupple within that range: ',numbers)

print ('---------------------------------------------')

# List comprehension can be combined with if expression
# Generate the list of even numbers within a given range
def even_range(range_num):
    even =[i for i in range(range_num) if i % 2==0]
    print('The list of even number within the range of {} is {}'.format(range_num,even ))
even_range(20)

print ('---------------------------------------------')

# Filter numbers: let's filter out positive even numbers from the list below
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
positive_even_filter = [i for i in numbers if i % 2 == 0 and i >= 0]
print('The filter list of positive even number list: ', positive_even_filter)

print ('---------------------------------------------')

# Flattening a three dimensional array
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened_list =[flattened for i in list_of_lists for flattened in i]
print(flattened_list)

print ('---------------------------------------------------')

# LAMBDA FUNCTION (Lambda function is a small anonymous function without a name.)
# It can take any number of arguments, but can only have one expression. Lambda function is similar to anonymous functions in JavaScript.
# We need it when we want to write an anonymous function inside another function.

area_of_rectangle = lambda l,b: l * b
print('The area of the rectangle with lenght l and breadth b: ',area_of_rectangle(4,5))

print ('---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
# Lambda function in another function
def power(x):
    return lambda n : x ** n
cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets function(x)(n)
print(cube)          # 8
two_power_of_five = power(2)(5) 
print(two_power_of_five)  # 32


print ('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print('EXERCISE DAY 13')
# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered_number = [i for i in numbers if i <= 0]
print('Filtered list with negative and zero:', filtered_number)

print ('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list_2 = [k for i in list_of_lists for j in i for k in j]
print('The flattened list: ', flattened_list_2)

print ('-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

# Using list comprehension create the following list of tuples:
tuple_list = [(i, 0, 1, i**1, i**2, i**3, i**4 ) for i in range(11)]
print('The tuple list is ', tuple_list)

print ('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

#Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_flat_list =[[k.upper(), k.upper()[:3]] for i in countries for j in i for k in j]
print('The new flattened list of countries: ', new_flat_list)

# Change the following list to a list of dictionaries:
countries=[[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
new_flat_dict = [{'country': k.upper()} for i in countries for j in i for k in j]
print('The new flat dict: ', new_flat_dict)

print ('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concat_list =[j[0] + ' ' + j[1] for i in names for j in i ]
print(concat_list)

print ('----------------------------------------------------------------------------------------------------------------------------------------------------------------')

# Write a lambda function which can solve a slope or y-intercept of linear functions.
slope = lambda x,y,intercept: (y - intercept)/ x
intercept = lambda x,y,slope: y-(slope*x)
print('The slope of the linear function is ',slope(2,8,4))
print('The intercept of the linear function is ',intercept(2,8,2))