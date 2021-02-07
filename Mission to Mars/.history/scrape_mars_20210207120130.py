# Dependencies
from bs4 import BeautifulSoup as bs
from webdriver_manager.chrome import ChromeDriverManager
from splinter import Browser
import pandas as pd
import time

# Install chrome driver
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Dictionary to return
mars_data = {}

def scrape():
# Mars News
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

    mars_data["title"] = title
    mars_data["article"] = article
    mars_data["link"] = link

# Mars Facts Table
    mars_facts = pd.read_html("https://space-facts.com/mars")[0]
    mars_table = mars_facts
    mars_facts_df = pd.DataFrame(mars_table)
    mars_facts_df = mars_facts_df.rename(columns={0:"Metric", 1:"Value"})
    mars_facts_df = mars_facts_df.set_index("Metric")
    mars_facts_df_html = mars_facts_df.to_html()



    return mars_data

    browser.quit()