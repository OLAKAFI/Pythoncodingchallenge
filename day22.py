# WEB SCRAPPING

import requests
from bs4 import BeautifulSoup
import json
url = 'http://www.bu.edu/president/boston-university-facts-stats/'

# Lets use the requests get method to fetch the data from url

response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')

title = soup.title.get_text()   #title of the site

body = soup.body.get_text()     # return body of the site
print(title)
print(body)


print('--------------------------------------------------------------------------------------------------------------------')

# Extract the table in this url (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) and change it to a json file
# import pandas as pd
# import requests

# url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# col_name = ["sepal_length", "sepal_width", "petal_length", "petal_width", "class"]
# iris = pd.read_csv(url, header=None, names=col_name)

# # Covert to dict
# iris_dict = iris.to_dict(orient="records")

# # Create a json file and add iris_dict
# output_file = "iris_dataset.json"
# with open(output_file, "w") as json_file:  
#     json.dump(iris_dict, json_file, indent=2)

# print(f"Saved the Iris Dataset as {output_file}")

# Extract the table in this url (https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data) and change it to a json file
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
response = requests.get(url)
content = response.content
soup = BeautifulSoup(content, 'html.parser')
table = soup.find('table')

with open('table.json', 'w') as json_file:
    json.dump(table, json_file, indent='3')
print('Data scraped and stored as table.json')




# Scrape the presidents table and store the data as json(https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). The table is not very structured and the scrapping may take very long time.
import requests
from bs4 import BeautifulSoup
import json

# Fetch the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Find the presidents table
presidents_table = soup.find("table", class_="wikitable")


# Extract relevant data (name, term, party) from the table
presidents_data = []
for row in presidents_table.find_all("tr")[1:]:   #row is tr starting from the second row, that is excluding the header row
    columns = row.find_all("td")
    name = columns[1].text.strip()
    term = columns[2].text.strip()
    party = columns[4].text.strip()
    vice_president = columns[6].text.strip()
    election = columns[5].text.strip()
    presidents_data.append({"name": name, "term": term, "party": party, "vice-president": vice_president, "election": election})

# Store as JSON
with open("presidents_data.json", "w") as json_file:
    json.dump(presidents_data, json_file, indent=4)

print("Data scraped and stored as presidents_data.json")
