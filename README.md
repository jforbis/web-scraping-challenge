# web-scraping-challenge

This challenge utilizes web scraping techniques to grab information from Nasa's website on Mars. Then it loads the information into a MongoDB and renders it to a web page using HTML coding and Flask.

To scrape the site I used Pandas via a Jupyter Notebook file to make sure it all worked - then I converted the Jupyter Notebook file to a python script.

The scraping pulls all information/data requested and stores it in a dictionary within Mongo. Then, each time you run the 'Scrape' route it will run through the process, scraping all updated info, and then rendering it back to the website.
