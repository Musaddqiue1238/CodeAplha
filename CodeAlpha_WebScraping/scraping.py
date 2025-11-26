import requests
from bs4 import BeautifulSoup
import pandas as pd

# Amazon URL (Bestselling Books)
url = "https://www.amazon.in/gp/bestsellers/books/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")

titles = []
ratings = []
prices = []

books = soup.find_all("div", {"class": "p13n-sc-uncoverable-faceout"})

for book in books:
    title = book.find("img", {"class": "p13n-sc-dynamic-image"}).get("alt")
    titles.append(title)

    rating_tag = book.find("span", {"class": "a-icon-alt"})
    rating = rating_tag.text.split(" ")[0] if rating_tag else "No Rating"
    ratings.append(rating)

    price_tag = book.find("span", {"class": "p13n-sc-price"})
    price = price_tag.text if price_tag else "No Price"
    prices.append(price)

df = pd.DataFrame({
    "Title": titles,
    "Rating": ratings,
    "Price": prices
})

df.to_csv("books.csv", index=False)

print("Scraping completed. CSV file saved as books.csv")
