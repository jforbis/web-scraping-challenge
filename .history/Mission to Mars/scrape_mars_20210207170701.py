# Importing Dependencies
from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time

# Run browser from installed location
executable_path = {"executable_path": "/Users/johnforbis/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver"}
browser = Browser("chrome", headless=False, **executable_path)

# Dictionary to return
mars_data = {}

def mars_news_scrape(browser):    
# Mars News
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')
    list_item = soup.select_one("ul.item_list li.slide")
    time.sleep(5)
    title = list_item.find('div', class_="content_title").text.strip() 
    article = list_item.find('div', class_="article_teaser_body").text.strip()
    
    return title, article

def mars_facts_scrape():
# Mars Facts Table
    mars_facts = pd.read_html("https://space-facts.com/mars")[0]
    mars_table = mars_facts
    mars_facts_df = pd.DataFrame(mars_table)
    mars_facts_df = mars_facts_df.rename(columns={0:"Metric", 1:"Value"})
    mars_facts_df = mars_facts_df.set_index("Metric")
    mars_facts_df = mars_facts_df.to_html()

    return mars_facts_df

def mars_hemispheres(browser):
# Mars Hemispheres
    mars_hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(mars_hemi_url)
    hemi_html = browser.html
    soups = bs(hemi_html, 'html.parser')
    hemis = soups.find_all('div', class_='item')
    base_url = "https://astrogeology.usgs.gov"
    full_res_urls = []
    title_ls = []
    hemisphere_image_urls = []

    for item in hemis:
        titles = item.find('h3').text
        title_ls.append(titles)
        endpoints = item.find('a', class_='itemLink product-item')['href']
        complete_url = base_url + endpoints
        browser.visit(complete_url)
        complete_url_html = browser.html
        soup3 = bs(complete_url_html, 'html.parser')
        lg_endpoints = soup3.find('img', class_="wide-image")['src']
        lg_url = base_url + lg_endpoints
        full_res_urls.append(lg_url)
        hemisphere_image_urls.append({"title" : titles, "img_url" : lg_url})
        
    return hemisphere_image_urls

def scrape():
    executable_path = {"executable_path": "/Users/johnforbis/.wdm/drivers/chromedriver/mac64/88.0.4324.96/chromedriver"}
    browser = Browser("chrome", headless=False, **executable_path)
    title, article = mars_news_scrape(browser)
    mars_facts_df_html = mars_facts_scrape()
    hemisphere_image_urls = mars_hemispheres(browser)

    mars_data = {
        "Title": title,
        "Article": article,
        "Mars Facts": mars_facts_df_html,
        "Hemispheres": hemisphere_image_urls,
    }

    return mars_data 

if __name__ == "__main__":
    
    browser.quit()