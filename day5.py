# Third Example about unpacking list
countries = ['Germany', 'France','Belgium','Sweden','Denmark','Finland','Norway','Iceland','Estonia']
gr, fr, bg, sw, *scandic, es = countries
print(gr)
print(fr)
print(bg)
print(sw)
print(scandic)
print(es)

# Sorting List using sort
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.sort()
print(fruits)             # sorted in alphabetical order, ['banana', 'lemon', 'mango', 'orange']
fruits.sort(reverse=True)
print(fruits) # ['orange', 'mango', 'lemon', 'banana']
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages) #  [19, 22, 24, 24, 24, 25, 25, 26]


# sorted(): returns the ordered list without modifying the original list
fruits = ['banana', 'orange', 'mango', 'lemon']
print(sorted(fruits))   # ['banana', 'lemon', 'mango', 'orange']
# Reverse order
fruits = ['banana', 'orange', 'mango', 'lemon']
fruits = sorted(fruits,reverse=True)
print(fruits)     # ['orange', 'mango', 'lemon', 'banana']



# Exercises
# 1 Declare an empty list
my_list= [ ]
my_list2 = list()

# 2 Declare a list with more than 5 items
my_list = ['Oluwashina','Adenike','Omotoyosi','Olatunbosun','Omotoya', 'Omotola', 'Tolulope']
print(len(my_list))

print( 'The first item is {}, while the last item is {}, and the middle item is {}'.format(my_list[0], my_list[-1], my_list[3]))

# 5 Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Ola', 30, 187, 'Single', 'UK']

# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("List of IT Companies: ", it_companies)
print('Numbers of IT Companies: ', len(it_companies))

# Modify List
it_companies[3]= 'Meta'
print(it_companies)

#Add new IT Company
it_companies.append('Bizzy')
print(it_companies)

#Insert new IT Company in the Middle
it_companies.insert(3, 'ChatPGT')
print('The list of IT Companies after inserting CHATPGT in the middle: ', it_companies)

# Join the it_companies with a string '#;  '
print('#; '.join(it_companies))

# Check if a certain company exists in the it_companies list
print('IBM' in it_companies)

# 16 Sort the list using sort() method
it_companies.sort()
print(it_companies)
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[:3])

# Slice out the last 3 companies from the list
print(it_companies[-3:])

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop(-1)
print(it_companies)

# Delete the list items
it_companies.clear()
print(it_companies)

# Destroy the list
it_companies.clear()
print(it_companies)

# Join the following list
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

front_end.extend(back_end)
print(front_end)

full_stack = front_end.copy()
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)


# Exercise 2
ages = [19, 22, 19, 23, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('The minimum age in this list is {} while the maximum age is {}'.format(ages[0], ages[-1]))
ages.insert(-1, ages[0])
ages.insert(-1, ages[-1])
print(ages)

#Range and average
min_age = min(ages)
max_age = max(ages)
sum_age = sum(ages)
average_age = sum_age/len(ages)
range_age = max_age - min_age
print('The range of the ages is ', range_age)
print('The average of the ages is', average_age)


ages.sort()
age_lenght = len(ages)
mid_index = (age_lenght - 1) // 2
mid_index_2 = mid_index + 1
mid_2 = (ages[mid_index] + ages[mid_index_2])/2
print(ages)
if age_lenght % 2:
    print('The median age for the list is', ages[mid_index])
else:
    print((ages[mid_index] + ages[mid_index +1])/2)



# countries
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
  'Zimbadwe',
  
]

countries.sort()
len_countries= len(countries)
midcountry_index = (len_countries - 1) // 2
list1_even = countries[0: midcountry_index]
list2_even = countries[midcountry_index:len_countries]
list3_noteven = countries[midcountry_index:]
print(midcountry_index)
if len_countries % 2:
    print(countries[midcountry_index])
else:
    print('The median countries are {} and {}'.format(countries[midcountry_index], countries[midcountry_index + 1] ))

if len_countries % 2 == 0:
    print('The first half of the list is ', list1_even)
    print('The second half of the list is ', list2_even)
else:
    print('The first half of the not even list is ', list1_even)
    print('The second half of the not even list is ', list3_noteven)


# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
unpack_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
CH, RS, US, *scandic = unpack_countries
print(scandic)
print(CH)