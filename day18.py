# REGEX
# MATCH return index of occurrence if it matches the pattern
import re

txt = 'I love to teach python and javaScript'
# It returns an object with span, and match
match = re.match('I love to teach', txt, re.I)
print(match)  # <re.Match object; span=(0, 15), match='I love to teach'>
# We can get the starting and ending position of the match as tuple using span
span = match.span()
print(span)     # (0, 15)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 0, 15
substring = txt[start:end]
print(substring)       # I love to teach

print('--------------------------------------------------------------------------------------------------------')

# SEARCH returns index of first occurence
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

search = re.search('language', txt, re.I)
print(search)
span = search.span()
print(span)     # (29, 37)
# Lets find the start and stop position from the span
start, end = span
print(start, end)  # 29, 37
substring = txt[start:end]
print(substring)       # language


print('------------------------------------------------------------------------------------------------------------')
#FINDALL Display where all the substring occurs in the text

find_all= re.findall('python', txt, re.I)
print(find_all)


print('------------------------------------------------------------------------------------------------------------')
#sUB Replacing a searched text with another string

python_replace = re.sub('Python|python', 'React', txt, re.I)
print(python_replace)


txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing. 
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs. 
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

make_readable = re.sub('%', '', txt)
print(make_readable)

print('------------------------------------------------------------------------------------------------------------')
# Splitting Text Using RegEx Split
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
split_txt = re.split('/n', txt)
print('Splitted page: ', split_txt)

print('----------------------------------------------------------------------------')
# SHORTHANDS FOR REGEX
# [A-Za-z0-9] any single character, that is a to z, A to Z or 0 to 9
# \: uses to escape special characters
# \d means: match where the string contains digits (numbers from 0-9)
# \D means: match where the string does not contain digits
# . : any character except new line character(\n)
# ^: starts with
# r'^substring' eg r'^love', a sentence that starts with a word love
# r'[^abc] means not a, not b, not c.
# $: ends with
# r'substring$' eg r'love$', sentence that ends with a word love
# *: zero or more times
# r'[a]*' means a optional or it can occur many times.
# +: one or more times
# r'[a]+' means at least once (or more)
# ?: zero or one time
# r'[a]?' means zero times or once
# {3}: Exactly 3 characters
# {3,}: At least 3 characters
# {3,8}: 3 to 8 characters
# |: Either or
# r'apple|banana' means either apple or a banana
# (): Capture and group


# EXERCISE
# What is the most frequent word in the following paragraph?
# paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
# for i in paragraph:
#     new_i = re.findall('[i]', paragraph, re.I)
#     print(new_i)

# Write a pattern which identifies if a string is a valid python variablet
# python_var_name = input('Please eneter your python varriable name here: ')
# is_valid_varriable = [ python_var_name if re.findall(r'^\d', python_var_name) is True else False, 'This is an invalid python varriable name']
# print('Valid python variable: ',python_var_name)

# stringed = '4firstaname'
# print(int(stringed[0]))
# print(type(int(stringed[0])))
# print(int(stringed[1]))


def is_valid_varriable(var_name):
#     if '-' and '/' and '*' and '+' in var_name[:]:
#          print('This username is invalid, variables should not')
    if str(range(10)) in var_name[0]:
         print('This username is invalid, varriable should not start with digits')
    else:
         print('This username is valid')
is_valid_varriable('6firstame')

# Clean the following text. After cleaning, count three most frequent words in the string.

from collections import Counter
sentence = '%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'
clean_text = re.sub(r'%|$|@|&|!|#|;','', sentence)
print('Cleaned Sentence: ', clean_text)


words = re.findall(r'\w+', clean_text)
new_top = Counter(words).most_common(20)
top_3 = new_top[:3]
print(top_3)
list_top_10 = [(word,count) for word,count in top_3]
print(list(list_top_10))

