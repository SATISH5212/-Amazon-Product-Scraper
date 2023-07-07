
# Amazon Product Scraper

This project provides a web scraping solution for extracting product data from Amazon. It consists of two scripts: `part1_scraping.py` and `part2_scraping.py`. 

## Features

- `part1_scraping.py`: Scrapes product listings from Amazon search results and saves them in a CSV file (`products.csv`), including product URL, name, price, rating, and number of reviews.
- `part2_scraping.py`: Retrieves additional details for each product URL from the `products.csv` file, including description, ASIN, product description, and manufacturer, and saves them in a separate CSV file (`product_details.csv`).

## Requirements

- Python 3.6 or higher
- Requests library (`pip install requests`)
- BeautifulSoup library (`pip install beautifulsoup4`)

## Usage

1. Run `part1_scraping.py` to scrape product listings from Amazon and save them in `products.csv`.
2. Run `part2_scraping.py` to retrieve additional product details using the URLs from `products.csv` and save them in `product_details.csv`.

## Note

- Make sure to respect Amazon's Terms of Service and avoid excessive scraping or any unethical use of the code.
- Adjust the code as needed to handle any changes in the Amazon website structure or data format.

Feel free to modify this README file to provide more specific instructions or information about your project.

