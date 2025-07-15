import json
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL = "https://home.biedronka.pl/bestsellery/"

def parse_offers():
    """
    Parses offers from the Biedronka Home bestsellery page and saves them to a JSON file.
    """
    try:
        response = requests.get(URL)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.binary_location = "/usr/bin/google-chrome"

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.get(URL)
    time.sleep(5)  # Wait for the page to load dynamically

    soup = BeautifulSoup(driver.page_source, "lxml")
    products = soup.find_all("div", class_="product-tile")

    offers = []
    for product in products:
        try:
            name = product.find("div", class_="product-tile__name").text.strip()
            price_element = product.find("div", class_="price-tile__sales")
            price = price_element.text.strip() if price_element else "N/A"

            offers.append({"name": name, "price": price})
        except AttributeError:
            continue

    with open("offers.json", "w", encoding="utf-8") as f:
        json.dump(offers, f, ensure_ascii=False, indent=4)

    print("Offers have been successfully parsed and saved to offers.json")
    driver.quit()

    print("Offers have been successfully parsed and saved to offers.json")

if __name__ == "__main__":
    parse_offers()
