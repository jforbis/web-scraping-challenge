# Importing Dependencies
from flask import Flask, render_template
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

@app.route("/")
def main():
    mars = mongo.db.mars.find_one()
    return render_template("index.html", mars=mars)

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    mars.update({}, mars_data, upsert=True)
    return "Scraping Done!"

if __name__ == "__main__":
    app.run(debug=True)