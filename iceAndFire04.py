#!/usr/bin/python3
"""Alta3 Research - Exploring OpenAPIs with requests"""
# documentation for this API is at
# https://anapioficeandfire.com/Documentation

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
        ## Ask user for input
        got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )

        ## Send HTTPS GET to the API of ICE and Fire character resource
        gotresp = requests.get(AOIF_CHAR + got_charToLookup)

        ## Decode the response
        got_dj = gotresp.json()
        # pprint.pprint(got_dj)
        name = got_dj["name"]
        aliases = got_dj["aliases"][0]

        print(f"The character you choose is {name}.") if len(name)!=0 else print(f"The character you choose don't have a name, but his/her aliases is {aliases}.")
        allegianceslist = got_dj["allegiances"]
        bookslist = got_dj["books"]
        povbookslist = got_dj["povBooks"]
        
        if len(allegianceslist) == 0:
            print("This character don't have allegiances.")
        else:
            
            for allegiance in allegianceslist:
                print("This character belongs to:")
                data = requests.get(allegiance).json()
                allegiancename = data["name"]
                print(allegiancename)

        
        if len(bookslist)==0:
            print("This character doesn't appear in any books.")
        else:
            print("This character appears in the following book(s):")
            for book in bookslist:
                data=requests.get(book).json()
                bookname = data["name"]
                print(bookname)

        if len(povbookslist) == 0:
            print("This character doesn't appear in any povBooks.")
        else:
            for povbook in povbookslist:
                print("This character appears in the following povBook(s):")
                data=requests.get(povbook).json()
                povbooknmame = data["name"]
                print(povbooknmame)
            



if __name__ == "__main__":
        main()

