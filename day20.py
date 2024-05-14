# DAY 20
# Python PIP - Python Package Manager
# Installing PIP
# pip install pip
# pip install numpy
# pip install pandas

# Opening website with webbrowser module
import webbrowser
# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]
# opens the above list of websites in a different tab
# for url in url_lists:
#     webbrowser.open_new_tab(url)

# To show details of a package
# pip show package_name


# Reading from URL
# install Requests
# get(): to open a network and fetch data from url - it returns a response object
# status_code: After we fetched data, we can check the status of the operation (success, error, etc)
# headers: To check the header types
# text: to extract the text from the fetched response object
# json: to extract json data 
# Let's read a txt file from this website, https://www.w3.org/TR/PNG/iso_8859-1.txt.

import requests # importing the request module

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website

response = requests.get(url) # opening a network and fetching a data
# print(response)
# print('-----------------------------------------------------------------------------------------------------')
# print(response.status_code) # status code, success:200
# print('-----------------------------------------------------------------------------------------------------')
# print(response.headers)     # headers information
# print('-----------------------------------------------------------------------------------------------------')
# print(response.text) # gives all the text from the page
# print('-----------------------------------------------------------------------------------------------------')



#GETTING DATA FROM AN API
# import requests
# url = 'https://restcountries.eu/rest/v2/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[:1])  # we sliced only the first country, remove the slicing to see all countries

print('-----------------------------------------------------------------------------------------------------')

# EXERCISE
# Read this url and find the 10 most frequent words
import requests
from parsel import Selector
from collections import Counter
url = 'https://api.slingacademy.com/v1/examples/sample-page.html'
response = requests.get(url).text
# print(response)
selector = Selector(response)
# print(selector)
plain_text = selector.xpath('//text()').getall()  #print out only text and exclude html tags
words = " ".join(plain_text)
# print(words)

words_split = words.split()
words_count = Counter(words_split)
print(words_count)
top_10 = words_count.most_common(10)
print(top_10)

print('---------------------------------------------------------------------------------')

import requests
api = 'https://api.thecatapi.com/v1/breeds'
response= requests.get(api).json()
print(response)

for items in response:
    for key, value in items['weight'].items():
        if 'metric' in key :
            result = key, value
            print(result)

print('-------------------------------------------------------------------------------------------')

import requests
from bs4 import BeautifulSoup

url= 'https://archive.ics.uci.edu/ml/datasets.php'
response= requests.get(url)
songSoup = BeautifulSoup(response.content, 'lxml')
data_dict = []
for song in songSoup.findAll('tr')[1:101]:
    tittle =song.findAll('a')[0].string
    artist =song.findAll('a')[1].string
    print(tittle, ',', artist)
    data_dict[tittle] = [artist]
print(data_dict)

            
