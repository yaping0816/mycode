#!/usr/bin/python3
from flask import Flask, redirect, url_for, render_template,request
import requests
import random

# Flask constructor takes the name of current module (__name__) as argument
app = Flask(__name__)

# list of characters name for users to choose from
characterlist = []
# call simpsons api here so I don't need to cal api and get different data every time when i go to the quotes endpoint
data=requests.get('https://thesimpsonsquoteapi.glitch.me/quotes?count=5').json()


for obj in data:
    character = obj["character"]
    characterlist.append(character)
# remove the duplicate names from the list
characterlist = list(dict.fromkeys(characterlist))
# shuffle the character names inside of the list
random.shuffle(characterlist)
     
index =0 # track the current position
rightcharacter="" # track the right answer
righturl="" # track the url of the character's image
quote="" #track the current quote

# This is the home page to start the game (127.0.0.1:2224/home)
@app.route("/home") 
def hello_world():
    return render_template("homepage.html")

# Whoever go to /quotes endpoint can cheat because he can see all of the quotes with the characters
@app.route("/quotes")
def display_quotes():
    return data

@app.route("/quotes/<num>")
def display_quote(num):
    global index
    global rightcharacter
    global righturl
    global quote
    num = int(num)
    index = num
    if num < len(data):
        rightcharacter = data[num]["character"]
        quote = data[num]["quote"]
        righturl = data[num]["image"]
        return render_template("guessquote.html",quote = quote, list = characterlist)
    elif num == len(data):
        return render_template("winthegame.html")
    else:
        return "Something went wrong!"

@app.route("/quotes/checkanswer",methods=["POST","GET"])
def checktheanswer():
    if request.method == "POST":
        character = request.form.get("nm") 
    
    elif request.method == "GET":
        character = request.args.get("nm")

    # check whether user didn't type anything
    if len(character) == 0:
        return render_template("emptyinput.html", num=index)
    # if user typed a right answer
    elif character.upper() == rightcharacter.upper():
        num = index+1
        return redirect(url_for("display_quote", num=num))
    else:
    #if user typed a wrong answer
        random.shuffle(data)
        return render_template("wrongguess.html", name=character,quote=quote, link=righturl,character=rightcharacter)

            

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
  
