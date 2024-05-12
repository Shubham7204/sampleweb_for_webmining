import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
url = 'http://127.0.0.1:5500/webmining/indexwithcss.html'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product cards
cards = soup.find_all('div', class_='card')

# Initialize a list to store the data
data = []

# Iterate over each card and extract information
for card in cards:
    img_url = card.find('img')['src']
    title = card.find('div', class_='title').text.strip()
    description = card.find('div', class_='description').text.strip()
    price = card.find('div', class_='price').text.strip()
    data.append([title, description, price, img_url])

# Define the CSV filename
filename = 'product_data2.csv'

# Write the data to a CSV file
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Description', 'Price', 'Image URL'])
    writer.writerows(data)

print(f'Data has been scraped and saved to {filename}')
