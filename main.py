from flask import Flask, request, jsonify, render_template
import random
import json
import requests

app = Flask(__name__)

with open("quotes.txt") as file:
    quotes = file.readlines()

@app.route("/")
def home():
    try:
        response = requests.get("http://localhost/api/text")
        if response.status_code == 200:
            message = "API available!"
        else:
            message = "API is currently offline!"
    except:
        message = "API is currently offline!"
    return render_template("index.html", message=message)

@app.route("/api/text")
def get_quote():
    quote = random.choice(quotes)
    return quote.strip()

@app.route("/api/json")
def get_quote_json():
    quote = random.choice(quotes)
    quote_dict = {"content": quote.strip(), "author": ""}
    if "-" in quote:
        quote_dict["content"], quote_dict["author"] = quote.strip().split(" - ")
    return json.dumps(quote_dict)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
