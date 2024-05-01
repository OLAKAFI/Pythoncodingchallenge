# DAY 17
# Exception Handling

# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - year_born
#     print('You are {name}. And your age is {age}.')
# except TypeError:
#     print('Type error occur')
# except ValueError:
#     print('Value error occur')
# except ZeroDivisionError:
#     print('zero division error occur')
# else:
#     print('I usually run with the try block') #if no exception or error execute this
# finally:
#     print('I alway run.')   # Always run regardless of error/exceptions


# # SHORT HAND FOR EXCEPTION
# try:
#     name = input('Enter your name:')
#     year_born = input('Year you born:')
#     age = 2019 - year_born
#     print('You are {name}. And your age is {age}.')
# except Exception as e: #Shorthand for getting exceptions
#     print(e)

# Packing and Unpacking Arguments in Python
# Unpacking Lists
try:
    lst = [1, 2, 3, 4, 5]
    def sum_of_five_nums(a, b, c, d, e): #4 arguments in functions
        return a + b + c + d + e   
    print(sum_of_five_nums(*lst))  # 15   #* added to the list means lst represent as much 
except Exception as e:
    print(e)

# Unpacking Dictionaries
def unpacking_person_info(name, country, city, age):
    return f'{name} lives in {country}, {city}. He is {age} year old.'
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpacking_person_info(**dct)) # Asabeneh lives in Finland, Helsinki. He is 250 years old.


# Packing Lists
def sum_all(*args):
    s = 0
    for i in args:
        s += i
    return s
print(sum_all(1, 2, 3))             # 6
print(sum_all(1, 2, 3, 4, 5, 6, 7)) # 28

#Packing Dictionaries
def packing_person_info(**kwargs):
    # check the type of kwargs and it is a dict type
    # print(type(kwargs))
    # Printing dictionary items
    for key in kwargs:
        print(f"{key} = {kwargs[key]}")
    return kwargs

print(packing_person_info(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))


# Spreading in Python
lst_one = [1, 2]
lst_two = [4, 5, 6, 7]
lst = [0, *lst_one, 3, *lst_two ]
print(lst)

# Using Enumerate to get the index
# Syntax
# for index, item in enumerate([20, 30, 40]):
#    print(index, item)

countries = ['Nigeria', 'Ghana', 'Benin']
for index, item in enumerate(countries):
    if item in countries:
        print(f"The country {item} is found in index {index}")


# Combining list together while looping them using ZIP
fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
fruits_and_vegies = []
for f, v in zip(fruits,vegetables):
    fruits_and_vegies.append({'fruits': f, 'vegies': v})
print(fruits_and_vegies)


# Exercise DAY 17 
# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print('The nordic countries: ', nordic_countries)