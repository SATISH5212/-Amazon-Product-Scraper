import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_details(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    description_element = soup.find("div", id="feature-bullets")
    description = description_element.get_text(strip=True) if description_element else None

    asin_element = soup.find("th", string="ASIN")
    asin = asin_element.find_next("td").text.strip() if asin_element else None

    product_description_element = soup.find("div", id="productDescription")
    product_description = product_description_element.get_text(strip=True) if product_description_element else None

    manufacturer_element = soup.find("th", string="Manufacturer")
    manufacturer = manufacturer_element.find_next("td").text.strip() if manufacturer_element else None

    return url, description, asin, product_description, manufacturer




product_urls = []

with open("products.csv", "r", encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip the header row
    for row in reader:
        product_urls.append(row[0])

csv_file = open("product_details.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csv_file)
writer.writerow(["Product URL", "Description", "ASIN", "Product Description", "Manufacturer"])

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
}

for url in product_urls:
    product_data = scrape_product_details(url)
    writer.writerow(product_data)

csv_file.close()
