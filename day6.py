# TUPLES
# Creating a tuple
tpl_fruits = ('banana', 'orange', 'mango', 'lemon')
print(tpl_fruits)

#Changing Tuples to Lists
lst_fruits = list(tpl_fruits)
print(lst_fruits)

# Exercises: Level 1
#1 Empty Tuple
empty_tpl = ()

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters= ('BX','Mat', 'HL' )
brothers = ('NO', 'SO', 'RN')
siblings = sisters + brothers
print('I have {} siblings and their names are {} '.format(len(siblings),siblings))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings_lst = list(siblings)
siblings_lst.append('Mum')
siblings_lst.append('Dad')
family_member_tpl =tuple(siblings_lst)
print(siblings_lst)
print(family_member_tpl)

# Unpack siblings and parents from family_members
*SIBLINGS, PARENT = family_member_tpl
print(SIBLINGS)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('Apple', 'Bannana', 'Berries')
vegetables = ('Carrot', 'Lettuce', 'Cabbage')
animal_product= ('Beef', 'Ham', 'Chicken', 'Turkey')
food_stuff_tp = fruits + vegetables + animal_product
food_stuff_lst = list(food_stuff_tp)
mid_index = (len(food_stuff_lst) - 1) // 2
mid_food_stuff_lst = food_stuff_lst[mid_index]
food_stuff_lst.sort()
print(food_stuff_lst)
print('The middle foodstuff in the list is ', mid_food_stuff_lst)
print('The first 3 items in the foodstuff list are {} while the last 3 foodstuff in list are: {}'.format(food_stuff_lst[:3], food_stuff_lst[-3: ]))


# Check if an item exists in tuple:
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print("Estonia" in nordic_countries)
print("Iceland" in nordic_countries)