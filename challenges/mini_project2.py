#!/usr/bin/python3
from flask import Flask, redirect, url_for, render_template,request
import requests
import random

# Flask constructor takes the name of current module (__name__) as argument
app = Flask(__name__)

# list of characters name for users to choose from
characterlist = []
# call simpsons api here so I don't need to cal api and get different data every time when i go to the quotes endpoint
data=requests.get('https://thesimpsonsquoteapi.glitch.me/quotes?count=10').json()

for obj in data:
    character = obj["character"]
    characterlist.append(character)
# shuffle the character names inside of the list
random.shuffle(characterlist)
     
index =0 # track the current position
rightcharacter="" # track the right answer
righturl="" # track the url of the character's image
quote=""

@app.route("/yaping") # if someone goes to 127.0.0.1:2224/yaping
def hello_world():
    return "Welcome to The Simpsons's quotes\n"

@app.route("/quotes")
def display_quotes():
    # quotes.clear() #clear the data every time when you refreash
    # for obj in data:
    #     quote = obj["quote"]
    #     character = obj["character"]
    #     newquote =f"{quote} --- {character}"
    #     quotes.append(newquote)
    # return quotes
    return data

@app.route("/quotes/<num>")
def display_quote(num):
    global index
    global rightcharacter
    global righturl
    global quote
    num = int(num)
    index = num
    rightcharacter = data[num]["character"]
    quote = data[num]["quote"]
    righturl = data[num]["image"]
    # return quotes[num]
    return render_template("guessquote.html",quote = quote, list = characterlist)

@app.route("/quotes/checkanswer",methods=["POST","GET"])
def checktheanswer():
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            character = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            character = "defaultuser"
    # GET would likely come from a user interacting with a browser
    elif request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            character = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            character = "defaultuser"
    
    if character.upper() == rightcharacter.upper():
        num = index+1
        return redirect(url_for("display_quote", num=num))
    else:
        return render_template("wrongguess.html", name=character,quote=quote, link=righturl,character=rightcharacter)

            

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
   # app.run(host="0.0.0.0", port=2224, debug=True) # DEBUG MODE
