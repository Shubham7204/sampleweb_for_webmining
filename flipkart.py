import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=iphone&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

# print(soup.prettify())
divs = soup.find_all(class_="KzDlHZ")

dict = {"Product": [], "Price": []}

for div in divs:
    # print(div.get_text())
    dict["Product"].append(div.get_text())

prices = soup.find_all(class_="Nx9bqj _4b5DiR")

for price in prices:
    # print(price.get_text())
    p = price.get_text()[1:]
    dict["Price"].append(p)


# print(dict)
df = pd.DataFrame(dict)
df.to_csv("Flipkart_products.csv", index=False)
# print(df)
