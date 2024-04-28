# Dictionaries
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}

# Accessing dictionaries
print(person['skills'])

# Modifying a Dictionary
person['country']= 'United Kingdom'
print(person['country'])

# Changing Dictionary to a List of Items

print(person.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])


#EXERCISE 
# Create an empty dictionary called dog
dog= {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Sniper'
dog['color'] = 'Multi color'
dog['breed'] = 'German Sherperd'
dog['age'] = 5

print(dog)
print(dog.keys())
print(dog.values())

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {}
student['first_name']= ' '
student['last_name'] = ' '
student['gender'] = ''
student['age'] = int()
student['marital_status'] = ''
student['skills']= ['HTML', 'Java', 'React', 'CSS']
student['country'] = ''
student['city'] = ''
student['address']= ''
print(student)
print(len(student))

# Get the value of skills and check the data type, it should be a list
print('The value of skills in the dic student is ', student['skills'], 'The data type is ', type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].append('UI/UX')
student['skills'].append('mySQL')
print(student['skills'])

print(student.keys())
print(student.values())

# Change the dictionary to a list of tuples using items() method
print(student.items())

student.pop('skills')
print(student)