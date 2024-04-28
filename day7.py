# SETS
# Add items to set
set_fruits={'Apple', 'Berry', 'Carrot'}
print(set_fruits)
set_fruits.add('Lettuce')
print(set_fruits)

# Add multiple items using the update()
set_fruits.update(['Orange', 'Vegetable'])
print(set_fruits)

# Joining Two sets using .union()
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage','onion', 'carrot'}
print(fruits.union(vegetables)) # {'lemon', 'carrot', 'tomato', 'banana', 'mango', 'orange', 'cabbage', 'potato', 'onion'}

# Intersection gives items that occur in both set
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.intersection(even_numbers)) # {0, 2, 4, 6, 8, 10}

# Subset and Supersets
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
print(whole_numbers.issubset(even_numbers)) # False, because it is a super set
print(whole_numbers.issuperset(even_numbers)) # True

#Difference of two sets (What is in set A that is absent in setB
python = {'p', 'y', 't', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.difference(dragon))     # {'p', 'y', 't'}  - the result is unordered (characteristic of sets)
print(dragon.difference(python))     # {'d', 'r', 'a', 'g'}


# Sysmettric Difference (It means that it returns a set that contains all items from both sets, except items that are present in both sets)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
print(python.symmetric_difference(dragon))  # {'r', 't', 'p', 'y', 'g', 'a', 'd', 'h'}


# Joint (set with one or more common items) and Disjiont set(set with no common items)
python = {'p', 'y', 't', 'h', 'o','n'}
dragon = {'d', 'r', 'a', 'g', 'o','n'}
python.isdisjoint(dragon)  # False, there are common items {'o', 'n'}


# EXERCISES
#LEVEL 1

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Find the length of the set it_companies
print('The lenght of the set it_companies is ', len(it_companies))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['OpenAI', 'Tesla' 'Starling'])
print('The new list of IT Companies are: ', it_companies)

# Remove one of the companies from the set it_companies
it_companies.pop()
print('The set of IT Companies after removing one random company ', it_companies)

# What is the difference between remove and discard
# Remove gives error when the item is not found, while discard does not give an error when item is not found in the set


# EXERCISSE LEVEL 2
# Join A and B
print('The union of the setA and setB ', A.union(B))

# Find A intersection B
print('A intersection B: ', A.intersection(B))

# Is A subset of B
print(A.issubset(B))

#Are A and B disjoint sets
print(A.isdisjoint(B))

# Join A with B and B with A
print('The union of the setA and setB ', A.union(B))
print('The union of the setB and setA ', B.union(A))

# What is the symmetric difference between A and B
print('The symmetric difference between A and B ', A.symmetric_difference(B))

# Delete the sets completely
del A, B, it_companies

# EXERCISE LEVEL 3
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
print(type(age))
age_set= set(age)
print(age_set)
print(type(age_set))

if len(age) > len(age_set):
    print('The lenght of the list is greater than the set')
elif len(age) < len(age_set):
    print('The lenght of the list is lesser than the set')
else:
    print('The lenght of the list and the set are the same')

# Explain the difference between the following data types: string, list, tuple and set
# set items cannot be the same, you can add to a set
# tuple cannot be updated after created unless converted to list first

# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
