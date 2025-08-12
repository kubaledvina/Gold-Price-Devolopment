import requests
from bs4 import BeautifulSoup
from datetime import date
import csv
import os


def gold_price():
    url = requests.get("https://markets.businessinsider.com/commodities/gold-price")
    soup = BeautifulSoup(url.text, "html.parser")
    gold_price = soup.find(class_="price-section__current-value")

    return gold_price.text.strip()

def scraper_date():
    s_date = date.today().strftime("%d.%m.%Y")

    return s_date

def create_csv():
    csv_exist = os.path.isfile("gold_price.csv")

    with open("gold_price.csv", mode= "a", encoding="utf-8", newline="") as file:

        f_writer = csv.writer(file)
        if not csv_exist:
            f_writer.writerow(["Date", "Price"])
        f_writer.writerow([scraper_date(), gold_price()])

    print("Save data to csv file.")

if __name__ == "__main__":
    create_csv()


