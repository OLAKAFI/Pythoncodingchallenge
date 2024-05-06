# FILE HANDLING
# Syntax
# open('filename', mode) # mode(r, a, w, x, t,b)  could be to read, write, update

# #Opening File for reading
f = open('./myfile.txt', mode='r')
print(f) # <_io.TextIOWrapper name='./files/reading_file_example.txt' mode='r' encoding='UTF-8'>

# # To read on specific part of the file
word_to_read = f.read(10)
print('The first 10 words in the file: ', word_to_read)
f.close()

# To read just a line
f = open('./myfile.txt', mode='r')
read_line = f.readline()
print('The first line in the file: ', read_line)
f.close()

# To read multiple lines
f = open('./myfile.txt', mode='r')
read_lines = f.readlines()
print('The lines in the file: ', read_lines)
f.close()



# Opening Files for Writing and Updating
with open('./myfile.txt', 'a') as f:
    f.write('Add this')
    f.close()
print(read_lines)

with open('./newfile.txt', 'w') as j:
    j.write('This is added to a new file called newfile')
j = open('./newfile.txt', mode='r')
new_file = j.readlines()
print('The content of new file: ',new_file)
f.close()


# Deleting File
import os
if os.path.exists('./newfiles.txt'):
    os.remove('./newfiles.txt')
else:
    print('The file does not exist')


# File Type
# cHANGING FROM JSON TO DICTIONARY
import json
# JSON
person_json = '''{
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"]
}'''
# let's change JSON to dictionary
person_dct = json.loads(person_json)
print(type(person_dct))
print(person_dct)
print(person_dct['name'])

print('----------------------------------------------------------------------------------------------------')

# # cHANGING FROM  DICTIONARY to JSON
person_dict = json.dumps(person_json, indent=3)
print(type(person_dct))
print('New Dict: ', person_dict)
print(person_dct['name'])

print('----------------------------------------------------------------------------------------------------')
# IMPORT CSV DATA
import csv
with open('./mycsv.csv') as f:
    csv_reader = csv.reader(f, delimiter=',') # w use, reader method to read csv
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are :{", ".join(row)}')
            line_count += 1
        else:
            print(
                f'\t{row[0]} is a teachers. He lives in {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Number of lines:  {line_count}')

print('----------------------------------------------------------------------------------------------------')
# OPEN WORKBOOK
# import xlrd
# excel_book = xlrd.open_workbook('sample.xls')
# print(excel_book.nsheets)
# print(excel_book.sheet_names)


# EXERCISE LEVEL 1
with open('./michelle.txt', 'w') as m:
    m.write('Speech is a human vocal communication using language. Each language uses phonetic combinations of vowel and consonant sounds that form the sound of its words')
m.close()

speach = open('./michelle.txt', 'r')
speach_read = speach.read()

words_list= speach_read.split(' ')
    
print('The words in the list: {} and the number of words in the list is {}'.format(words_list, len(words_list)))
speach.close()

speach = open('./michelle.txt', 'r')
number_line = 0

for item in speach:
    number_line += 1

speach.close()
print('The number of line in the speach: ', number_line)

print('------------------------------------------------------------------------------------------------------------------')