# PANDAS
# pip install conda
# pip install pandas

import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

# Creating Pandas Series with custom index
names= ['Olatunbosun', 'Olasunkanmi', 'Olamideleni']
custom_pdseries = pd.Series(names, index=[1,2,3])
print(custom_pdseries)


print('---------------------------------------------------------------------------------------')
# Creating Pandas Series from a Dictionary
dct = {'name':'Asabeneh','country':'Finland','city':'Helsinki'}
dct_pdseries = pd.Series(dct)
print(dct_pdseries)

print('---------------------------------------------------------------------------------------')
# Creating panda series with a constant
constant_series = pd.Series(10, index=[1,2,3,4,5,6])
print(constant_series)


print('-------------------------------------------------------------------------------------------')
# DATAFRAMES
print('-------------------------------------------------------------------------------------------')
# Creating DataFrames from List of Lists
data = [
    ['Asabeneh', 'Finland', 'Helsink','Europe'], 
    ['David', 'UK', 'London','Britain'],
    ['John', 'Sweden', 'Stockholm','Sweedish'],
    ['John', 'Sweden', 'Stockholm','Sweedish']
]
df = pd.DataFrame(data, columns=['Names','Country','City','Origin'], index=[np.arange(1,len(data)+1)])
print(df)


print('-------------------------------------------------------------------------------------------')
# Creating DataFrames using Dictionairies
data = {'Name': ['Asabeneh', 'David', 'John'], 'Country':[
    'Finland', 'UK', 'Sweden'], 'City': ['Helsiki', 'London', 'Stockholm']}
df = pd.DataFrame(data, index=[np.arange(1,len(data)+1)])
print(df)

print('-------------------------------------------------------------------------------------------')
# Reading CSV File Using Pandas
df = pd.read_csv('weight-height.csv')   # pd.read_csv('filename.csv)
print(df)

print('-------------------------------------------------------------------------------------------')
print('First Five rows')
print( df.head())

print('-------------------------------------------------------------------------------------------')
print('Last Five rows')
print( df.tail())

print('-------------------------------------------------------------------------------------------')

print( 'The shape of the dataframe is ', df.shape)
print( 'The size of the dataframe is ', df.size)
print('The columns in dataframe: ', df.columns)

heights = df['Height']
print('Height Column')
print(heights)


# Descriptive Statistics
print('-------------------------------------------------------------------------------------------')

print('Statistics for the whole data frame: ')
stats_df = df.describe()
print(stats_df)

print('-------------------------------------------------------------------------------------------')

stats = heights.describe()
print('Statistics for height colum: ')
print(stats)

print('-------------------------------------------------------------------------------------------')
# Modifying a dataframe
import pandas as pd
import numpy as np
data = [
    {"Name": "Asabeneh", "Country":"Finland","City":"Helsinki"},
    {"Name": "David", "Country":"UK","City":"London"},
    {"Name": "John", "Country":"Sweden","City":"Stockholm"}]
df = pd.DataFrame(data)
print(df)

print('-------------------------------------------------------------------------------------------')
weights = np.random.randint(68, 78, size=len(data))
heights = np.random.randint(169, 175, size=len(data))
df['Weight'] = weights 
df['Height'] = heights*  0.01
birthyear = ['1769','2002','2007']
currentyear = pd.Series(2024, index=[0,1,2])
df['Birth Year'] = birthyear
df['Current Year'] = currentyear.astype('int')


print('The new dataframe after adding other Columns')
print(df)

print('-------------------------------------------------------------------------------------------')
# A function to calculate the Age
def calculate_age():
    currentyear = df['Current Year']
    birthyear = df['Birth Year']
    age=[]
    for c, b in zip(currentyear,birthyear):
        a= c-int(b)
        age.append(a)
    return age
calculate_age()

age = calculate_age()
df['Age'] = age
df['Age']= round(df['Age'], 1)


# A function to calculate the BMI
def calculate_bmi():
    height = df['Height']
    weight = df['Weight']
    bmi = []
    for w, h in zip(weight,height):
        b = w/(h*h)
        bmi.append(b)
    return bmi
calculate_bmi()

bmi= calculate_bmi()
df['BMI'] = bmi
df['BMI'] = round(df['BMI'], 1)
print('The new dataframe with BMI')
print(df)

print('---------------------------------------------------------------------------')
# Filtering the data based on a condition Age < 85
print('The new dataframe exclusing ages less than 85: ')
print(df[df['Age'] < 85])


# PLOT A GRAPH OF AGE vs BMI
# import matplotlib.pyplot as plt
# plt.plot(df['BMI'], df['Weight'])
# plt.xlabel('Weight')
# plt.ylabel('BMI')
# plt.title('PLOT OF AGE vs BMI')
# plt.show()
print('-------------------------------------------------------------------------------------------')
# Formatting DataFrames



# EXERCISE
hdt = pd.read_csv('hacker_news.csv')
print(hdt)
top5 = hdt.head()
last5 =hdt.tail()
print('First five rows of hacker data: ')
print(top5)
print('-------------------------------------------------------------------------------------------')
print('Last five rows of hacker data: ')
print(last5)
print('-------------------------------------------------------------------------------------------')

print('Title as as a series')
title = pd.Series(hdt['title'])
print(title)

print('-------------------------------------------------------------------------------------------')

hdt_shape =hdt.shape
rows, columns = hdt_shape
print('The hacker data contains {}rows and {}columns'.format(rows, columns))

print('-------------------------------------------------------------------------------------------')

python = 'python'
hdt_python =hdt[~hdt['title'].str.contains('python', na=False)]
print('List of title with no Python')
print(hdt_python)
hdt_python_shape = hdt_python.shape
print('count: ', hdt_python_shape)

rows, columns = hdt_python_shape
print('The filtered hacker data without python in title contains {}rows and {}columns'.format(rows, columns))


print('-------------------------------------------------------------------------------------------')
hdt_javascript = hdt[hdt['title'].str.contains('JavaScript', na=False)]
print('Table with title consisting of Javascript')
print(hdt_javascript)
hdt_javascript_shape = hdt_javascript.shape
rows, columns = hdt_javascript_shape
print('The filtered hacker data with Javascript in title contains {}rows and {}columns'.format(rows, columns))

