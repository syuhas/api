from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import json

# Set the path to the chromedriver executable
webdriver_service = Service('/usr/bin/chromedriver')

# Set the options for the Chrome browser
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode (without GUI)

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=webdriver_service, options=options)

# Navigate to the URL
url = "https://www.reddit.com/r/webscraping/comments/m8b05v/is_there_a_standard_time_to_sleep_between_requests/"
driver.get(url)

print(driver.page_source)
# Perform scraping operations using Selenium


# # Find all prices for "g502" in this page using beatifulsoup and print them out

# sample_html = "/home/syuhas/dev/api/amazontext.html"

# with open(url, "r") as file:
#     html = file.read()


soup = bs(url, "html.parser")

divs = soup.find_all("div")

for div in divs:
    print(div)



# # Close the browser
# driver.quit()


# url = "https://www.amazon.com/s?k=g502+x&crid=1TMC8ZB295Q9G&sprefix=g502+x%2Caps%2C81&ref=nav_ya_signin"
# def get_html(url):
#     """Get the HTML of the page."""
#     response = requests.get(url)
#     return response.text

# text = get_html(url)



# soup = bs(text, "html.parser")
# print(soup.prettify())
# ## find all items and prices in this page under the section "Shop Holiday Deals"

# items = soup.find_all("div", {"class": "a-section a-spacing-none g-item-sortable"})

# for item in items:
#     name = item.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).text
#     price = item.find("span", {"class": "a-price-whole"}).text
#     print(name, price)

## find all items and prices in this page under the section "Shop Holiday Deals" and save them in a csv file

# import csv

# with open("amazon.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Name", "Price"])
#     for item in items:
#         name = item.find("span", {"class": "a-size-base-plus a-color-base a-text-normal"}).text
#         price = item.find("span", {"class": "a-price-whole"}).text
#         writer.writerow([name, price])