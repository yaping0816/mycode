#!usr/bin/env python3

def main():

    try:
        while True:
                char_name=input("which character do you want to know about?(Starlord, Mystique, Hulk)\n>").capitalize()
                char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)\n>").lower()

                marvelchars= {
                  "Starlord":
                    {"real name": "peter quill",
                     "powers": "dance moves",
                     "archenemy": "Thanos"},

                  "Mystique":
                    {"real name": "raven darkholme",
                     "powers": "shape shifter",
                     "archenemy": "Professor X"},

                  "Hulk":
                    {"real name": "bruce banner",
                     "powers": "super strength",
                     "archenemy": "adrenaline"}
                               }
                result = (marvelchars[char_name][char_stat]).title() if char_stat=="real name" else marvelchars[char_name][char_stat]

                print(f" {char_name}'s {char_stat} is: {result}")

    except KeyboardInterrupt:
        exit

if __name__ == "__main__":
    main()



