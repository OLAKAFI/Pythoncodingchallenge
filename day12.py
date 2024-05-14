# MODULES
#   A module is a file containing a set of codes or a set of functions which can be included to an application.
# Write a function which generates a six digit/character random_user_id.
from random import*
import string
# def generate_user_id():
#     char_num = int(input('Please enter the number of the desired character: '))
#     user_num = int(input('Please enter the number of user id you want to generate: '))
#     characters = string.ascii_letters + string.digits       #type and combination of characters in the random userid
#     random_id = lambda char_num, user_num: [''.join(choices(characters, k=char_num)) for n in range(user_num)]    # k is the lenght of characters    
#     print(random_id(char_num, user_num))
# generate_user_id()

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen(num):
    for i in range(num):
        r = randrange(255)
        g = randrange(255)
        b = randrange(255)
        rand_color = (r, g, b)
        print('rgb', rand_color)
rgb_color_gen(6)

print('-------------------------------------------------------------------------------------------------------------')

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).
# Write a function generate_colors which can generate any number of hexa or rgb colors.
def list_of_hexa_colors(color_type, num):
    if color_type == 'hexa':
        character = string.digits + string.ascii_uppercase[:6]
        color = ['#' + ''.join(choices(character, k=6)) for i in range(num)]
        print(tuple(color))
    elif color_type == 'rgb':
        for x in range(num):
            r = randrange(255)
            g = randrange(255)
            b = randrange(255)
            color=(r,g,b)
            print('rgb', color)
list_of_hexa_colors('hexa', 4)

print('-------------------------------------------------------------------------------------------------------------')

# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
def shuffle_list(lists):
    shuffled_list = sample(lists, len(lists))
    return shuffled_list
print('My shuffled list is:', shuffle_list([1,2,5,4,67,7,8]))

print('-------------------------------------------------------------------------------------------------------------')

# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def array_random_seven():
    rand= string.digits
    random_seven = set([''.join(choices(rand, k=1)) for i in range(9)])
    unique_random_seven = list(random_seven)
    print('Generated list of seven random unique numbers within the range of 9: ', unique_random_seven)
array_random_seven()

print('-----------------------------------------------------------------------------------------------------------')

