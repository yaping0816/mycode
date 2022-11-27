#!/usr/bin/python3
# An object of Flask class is our WSGI application
from flask import Flask
import requests
#    module       class

# Flask constructor takes the name of current
# module (__name__) as argument
# varaibale "app" represents our entire api!
# this whole script is teaching our little app pbject to behave
app = Flask(__name__)

quotes = []
# call simpsons api here so I don't need to cal api and get different data every time when i go to the quotes endpoint
data=requests.get('https://thesimpsonsquoteapi.glitch.me/quotes?count=10').json()

# route() function of the Flask class is a
# decorator, tells the application which URL
# should call the associated function
@app.route("/yaping") # if someone goes to 127.0.0.1:2224/yaping
def hello_world():
    return "Welcome to The Simpsons's quotes\n"

@app.route("/quotes")
def display_quotes():
    quotes.clear() #clear the data every time when you refreash
    for obj in data:
        quote = obj["quote"]
        character = obj["character"]
        newquote =f"{quote} --- {character}"
        quotes.append(newquote)
    return quotes

@app.route("/quotes/<num>")
def dispaly_quote(num):
    num = int(num)
    return quotes[num]

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE

