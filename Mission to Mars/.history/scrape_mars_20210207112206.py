# Dependencies
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd
import time

# Install chrome driver
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

def scrape():
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = bs(html, 'html.parser')
    title = list_item.find('div', class_="content_title").text.strip() 
    article = list_item.find('div', class_="article_teaser_body").text.strip()
    element2 = soup.find('div', class_="image_and_description_container")
    link = element2.a["href"]
    short_url = "https://mars.nasa.gov"
    link = short_url + link
    link