# Importing Dependencies
from flask import Flask, render_template
import scrape_mars.py
import pymong

app = Flask(__name__)

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

@app.route("/")
def main():
    mars = client.db.mars.find_one()
    return render_template("index.html", mars=mars)