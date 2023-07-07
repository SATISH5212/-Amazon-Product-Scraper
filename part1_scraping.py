import requests
from bs4 import BeautifulSoup
import csv

def scrape_product_listing(listing):
    product_url_element = listing.find("a", class_="a-link-normal a-text-normal")
    product_url = product_url_element["href"] if product_url_element else None

    product_name_element = listing.find("span", class_="a-size-medium a-color-base a-text-normal")
    product_name = product_name_element.text.strip() if product_name_element else None

    product_price_element = listing.find("span", class_="a-price-whole")
    product_price = product_price_element.text.strip() if product_price_element else None

    rating_element = listing.find("span", class_="a-icon-alt")
    rating = rating_element.text.strip().split()[0] if rating_element else None

    num_reviews_element = listing.find("span", class_="a-size-base")
    num_reviews = num_reviews_element.text.strip() if num_reviews_element else None

    return product_url, product_name, product_price, rating, num_reviews

url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1"

csv_file = open("products.csv", "w", newline="", encoding="utf-8")
writer = csv.writer(csv_file)
writer.writerow(["Product URL", "Product Name", "Product Price", "Rating", "Number of Reviews"])

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36",
}

page_count = 1
max_pages = 20

while page_count <= max_pages:
    print(f"Scraping page {page_count}...")
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    product_listings = soup.find_all("div", class_="sg-col-inner")

    for listing in product_listings:
        if "sponsored" in listing.get("data-component-type", ""):
            continue  # Skip sponsored listings

        product_data = scrape_product_listing(listing)

        if product_data[0] is not None:  # Check if product_url is not None
            writer.writerow(product_data)

    next_page_element = soup.find("a", class_="s-pagination-item s-pagination-next")
    next_page_url = next_page_element["href"] if next_page_element else None

    if not next_page_url:
        break  # No next page found, exit the loop

    url = f"https://www.amazon.in{next_page_url}"
    page_count += 1

csv_file.close()
