#String Interpolation / f-Strings (Python 3.6+)
# a = 4
# b = 3
# print(f'{a} + {b} = {a +b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')


#Python Strings as Sequences of Characters
# language = 'Python'
# a,b,c,d,e,f = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n


# endswith(): Checks if a string ends with a specified ending
# challenge = 'thirty days of python'
# print(challenge.endswith('on'))   # True
# print(challenge.endswith('tion')) # False


# find(): Returns the index of the first occurrence of a substring, if not found returns -1
# challenge = 'thirty days of python'
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0

# Format
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# age = 250
# job = 'teacher'
# country = 'Finland'
# sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
# print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
# print(result) # The area of a circle with radius 10 is 314


#Exercise
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
my_string_1 = ('Thirty', 'Days', 'Of', 'Python')
my_string_1a = ' '.join(my_string_1)
print(my_string_1a)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
my_string_2 = ('Coding', 'For' , 'All')
my_string_2a = ' '.join(my_string_2)
print(my_string_2a)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = ('Coding for All')
print(company)

# Print the length of the company string using len() method and print()
print(len(company))

# Change all the characters to uppercase letters using upper() method.
upper_company = company.upper()
print(upper_company)

# Change all the characters to lowercase letters using lower() method.
lower_company = company.lower()
print(lower_company)

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
company_1 = 'Coding For All'
print(company.capitalize())
print(company.title())
print(company.swapcase())

# 9 Cut(slice) out the first word of Coding For All string.
print(company_1[0:6])

# 10 Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(company_1.find('Coding'))

# Replace the word coding in the string 'Coding For All' to Python.
print(company_1.replace('Coding', 'Python'))

# 13 Split the string 'Coding For All' using space as the separator (split()) .
print(company_1.split(' '))

# 14 "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
social_media = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(social_media.split(','))

# 15 What is the character at index 0 in the string Coding For All.
print(company_1[0])
print(company_1[-1])

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
course = ('Python', 'For', 'Everyone')
P, F, E = course
print(P, F, E )

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company_1.find('C'))
print(company_1.find('F'))


# 22 Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company_1.rfind('l'))

# 23 Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent.find('because')) #first coccurrence
print(sent.rfind('because')) #last occurrence

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sent[31: 55])

# 28 & 29 Does ''Coding For All' start with a substring Coding? Does 'Coding For All' end with a substring coding?
print(company_1.startswith('Coding'))
print(company_1.endswith('coding'))

# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
py_lib = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print('# '.join(py_lib))

# 33 Use the new line escape sequence to separate the following sentences
new_line = 'I am enjoying this challenge \nI just wonder what is next.'
print(new_line)

# 34 Use a tab escape sequence to write the following lines.
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelinski')

# 35 Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius, area))

# 36 Make the following using string formatting methods:
a = 8
b = 6

print('{} + {} = {}'.format(a,b, a+b))
print('{} - {} = {}'.format(a,b, a-b))
print('{} / {} = {:.1f}'.format(a,b, a/b))
print('{} % {} = {}'.format(a,b, a%b))
print('{} // {} = {}'.format(a,b, a//b))
print('{} ** {} = {}'.format(a,b, a**b))