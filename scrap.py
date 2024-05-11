import requests
from bs4 import BeautifulSoup
import csv

# URL of the webpage
url = "http://127.0.0.1:5500/index.html"

# Send a GET request to the webpage
response = requests.get(url)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all product cards
product_cards = soup.find_all(class_='card')

# Create a list to store the data
data = []

# Iterate over each product card and extract information
for card in product_cards:
    title = card.find(class_='card-title').text.strip()
    description = card.find(class_='card-text').text.strip()
    # Extracting the price
    price = card.find_all(
        'p', class_='card-text')[1].text.strip().split(':')[1].strip()
    data.append([title, description, price])

# Save data to CSV
with open('products.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Description', 'Price'])  # Write header
    writer.writerows(data)  # Write data rows

print("Data saved to products.csv")
