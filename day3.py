#Exercise 3
age = int(56)
height =float(76.5)
comp_var = 1 + 4j


#  Exercise 3 question 4
# base= int (input('Enter base: '))
# height= int(input('Enter height: '))
# area_of_triangle = base * height
# print('area of triangle is ', area_of_triangle)

#  Exercise 3 question 5
# side_a= int(input('Enter side a: '))
# side_b= int(input('Enter side b: '))
# side_c= int(input('Enter side c: '))
# perimeter_of_triangle = side_a + side_b + side_c
# print('The perimeter of triangle is ', perimeter_of_triangle)


#  Exercise 3 question 6
# lenght= int (input('Enter lenght: '))
# width= int(input('Enter width: '))
# area_of_rectangle = lenght * width
# perimeter_of_rectangle = (2* (lenght + width))
# print('The area of the rectangle is ', area_of_rectangle)
# print('The perimeter of rectangle is ', perimeter_of_rectangle)


#  Exercise 3 question 7
# radius= int (input('Enter the radius: '))
# pi= 3.142
# area_of_circle = (pi * (radius**2))
# circumference_of_circle = (2 * pi * radius)
# print('the area of the circle is ', area_of_circle)
# print('the circumference of the circle is ', circumference_of_circle)


# x_1= int(input('Enter the value of x1'))
# y_1= int(input('Enter the value of y1'))
# x_2= int(input('Enter the value of x2'))
# y_2= int(input('Enter the value of y2'))
# m = (y_2 - y_1)/(x_2 - x_1)
# print('The slope of the line is ', m)



# Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# x =int(input('Please enter the value of x: '))
# y = ((x**2) + (6*x) + 9)
# print(y)
# if y == 0:
#     print('The value of y is now zero')


# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
p = 'Python'
d = 'Dragon'

if len(p) > len(d):
    print('The lenght of p is greater than d')
elif len(p) < len(d):
    print('the lenght of p is lesser than d')
else :
    print('the lenght of both is the same')

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
if "on" in p and d:
    print('The word on exist in both p and d')

#I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
course = 'I hope this course is not full of jargon'
if 'jargon' in course:
    print('the word jargon exists in this course')

#There is no 'on' in both dragon and python 
print('on' != p and 'on' != d )

#Find the length of the text python and convert the value to float and convert it to string
print(float(len('python')))
print(str(len('python')))

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# input_number= int(input('Enter the number of you want to check: '))
# if input_number % 2 == 0:
#     print('The number inputed is an even number')
# else:
#     print('The number is not an even number and might be an odd number')


#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
check_div= 7//3
if type(check_div) is int:
    print('convert check_div to 2.7')
    check_div = 2.7
    print(check_div)


#Check if type of '10' is equal to type of 10
print (type('10') == type(10))

#Check if int('9.8') is equal to 10
# print(type(int('9.8')) == type(10))


#Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
# input_hours = int(input('Enter the number of hours worked per week:'))
# input_rate = int(input('Please enter the rate per hour:'))
# weekly_earning = input_hours * input_rate
# print(weekly_earning)


# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# input_years = int(input('Enter the number of years you have lived: '))
# lived_seconds = input_years * 60 * 60 * 24 * 365
# print('The number of seconds you have spent alive is at least', lived_seconds)


#Write a Python script that displays the following table
for i in range(1, 6):
    print(f"{i} | {1} | {i**1} | {i**2} | {i**3} ")
