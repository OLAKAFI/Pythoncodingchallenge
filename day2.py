#Day 2: 30 Days of python programming
first_name= "Olatunbosun"
last_name = "Kafisanwo"
full_name = first_name, last_name
country= 'UK'
year= 2024
city='London'
age='75'
is_married='False'


print(first_name)
print(last_name)
print(full_name)
print(country)
print(year)
print(is_married)



# Exercise Level 2 (1) Check the datatype of the above
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(year))
print(type(is_married))

# Exercise Level 2 (2) Check the lenght of the above varriables
print(len(first_name))
print(len(last_name))
print(len(full_name))
print(len(country))
print(len(is_married))

#Exercise Level 2 (3): Compare lenght of firstname and last name
if len(first_name) > len(last_name):
    print('the lenght of my firstname is greater than my lastname')
else:
    print('the lenght of my lastname is greater')


#Exercise Level 2 (4)
num_one= 5
num_two= 4
total = num_one + num_two
diff = num_one - num_two
product =num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two
print(total, diff, division, remainder, product, exp, floor_division)



#Exercise Level 2 (5) Radius of a circle
radius= 30
pi= 3.142
area_of_circle= (pi)* (radius**2)
circum_of_circle = 2 * pi * radius

print('area of the circle is ', area_of_circle)
print('circumference of the circle is ', circum_of_circle)

input_radius= int (input(' Please enter the radius of the circle'))
input_area_of_circle= (pi) * (input_radius**2)
print(input_area_of_circle)


#Exercise Level 2 (6) Input
first_name = input(' Enter the first name')
last_name = input (' Enter the last name')
country = input (' Enter the name of the country')
age = input('Please input your age')
print('My name is', first_name, ' ', last_name, ' and i am ', age, 'years old', ' ','. I am from ', country)


#Exercise Level 2 (7) KEYWORD HELP
print(help('str'))
