import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the URL
url = 'https://shubham7204.github.io/sampleweb_for_webmining/'
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product cards
cards = soup.find_all('div', class_='card')

# Initialize a list to store the data
data = []

# Iterate over each card and extract information
for card in cards:
    title = card.find('h5', class_='card-title').text.strip()
    description = card.find('p', class_='card-text').text.strip()
    price = card.find(
        'p', class_='card-text').find_next_sibling('p').text.strip().split(':')[1].strip()
    img_url = card.find('img', class_='card-img-top')['src']
    data.append([title, description, price, img_url])

# Define the CSV filename
filename = 'product_data.csv'

# Write the data to a CSV file
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Description', 'Price', 'Image URL'])
    writer.writerows(data)

print(f'Data has been scraped and saved to {filename}')
