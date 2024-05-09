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
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
print(response)
print(response.headers)
print(response.text)

