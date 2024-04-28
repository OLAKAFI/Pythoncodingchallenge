#CONDITION STATMENT
# Get user input using input(“Enter your age: ”). 
# If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

# age= int(input('Enter age:'))
# if age >= 18:
#     print('You are old enough to drive')
# else:
#     print('You are not of legal age to drive, you have {}years left to be able to drive'.format(18 - age))

# Compare your age and my age
# my_age= int(input('Enter my age: '))
# your_age= int(input('Enter your age: '))
# if my_age > your_age:
#     print('I am  older than you')
#     if my_age - your_age == 1:
#         print('I am a year older than you')
#     elif my_age - your_age > 1:
#         print('I am {}years older than you'.format(my_age - your_age))
# elif my_age == your_age:
#     print('Am afraid we are of the same age')
# else:
#     print ('You are {}years older than me'. format(your_age - my_age))


# # Get two numbers from the user using input prompt. 
# #If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b

# a =int(input('Enter number one: '))
# b =int(input('Enter number two: '))

# if a > b:
#     print('a is greater than b')
# elif a < b:
#     print(' a is smaller than b')
# else:
#     print('a is equals to b')


# #EXERCISE 2
# # Write a code which gives grade to students according to theirs scores:
# # 80-100, A, 70-79, B 60-69, C 50-59, D 0-49, F
# student_score = int(input('Enter your score here to know your grade: '))
# if student_score >= 80:
#     print('You have scored an A')
# elif student_score <= 79 and student_score >= 70:
#     print('You have scored an B')
# elif student_score <= 69 and student_score >= 60:
#     print('You have scored an  C')
# elif student_score <= 59 and student_score >= 50:
#     print('You have scored an  D')
# elif student_score <= 49:
#     print('You have scored an  F')
# else:
#     print('We cannot determine your grade, re-enter your score')


# # Check Season September, October or November(Autum), December, January or February (Winter), March, April or May (Spring)
# # June, July or August (summer)
# month= input('Enter the month of the year to predict the current season: ')
# if month == 'September' or month == 'October' or month == 'November':
#     print('The present season is likely to be Autum')
# elif month == 'December' or month == 'January' or month == 'February':
#     print('The present season is likely to be Winter')
# elif month == 'March' or month == 'April' or month == 'May':
#     print('The present season is likely to be Spring')
# elif month == 'June' or month == 'July' or month == 'August':
#     print('The present season is likely to be Summer')
# else:
#     print('The month entered is unknown and season cannot be predicted')


# # If a fruit doesn't exist in the list add the fruit to the list and print the modified list.
# # If the fruit exists print('That fruit already exist in the list')
# fruits = ['banana', 'orange', 'mango', 'lemon']
# input_fruit=input('Enter the name of the fruit here: ')


# if input_fruit in fruits:
#     print('That fruit already exist in the list and the fruit list remains', fruits)
# else:
#     add_new= fruits.append(input_fruit)
#     print('This fruit is new and the new list is ', fruits)


# Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
# Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
# If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
# If the person is married and if he lives in Finland, print the information in the following format:
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
mid_skills= (len(person['skills'])-1) // 2
if 'skills' in person.keys():
    print('The middle skill in the skills list is ', person['skills'][mid_skills])
else:
    print('the skills key does not exist in person')

if 'Python' in person['skills']:
    print('The python skill set exist in the skills key items')

# if 'Javascript' in person['skills'] and 'React' in person['skills']:
#     print('He is a front end developer')

if 'Python' in person['skills'] and 'MongoDB' in person['skills'] and 'Node' in person['skills'] and 'Javascript' in person['skills'] and 'React' in person['skills']:
    print('He is a full stack developer')

if ['Javascript','React'] in person['skills']:
    print('He is a front end developer')

# if 'Javascript' and 'React' in person['skills']:
#     print('He is a front end developer')

# if 'Python' in person['skills'] and 'MongoDB' in person['skills'] and 'Node' in person['skills']:
#     print('He is a backend end developer')

if person['is_married'] == True and person['country'] == 'Finland':
    print('{} {} lives in {}. He is married'.format(person['first_name'], person['last_name'], person['country']) )