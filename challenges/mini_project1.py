#!usr/bin/env python3
import random
import mini_project1_data

print("-------------------------------------------------------------------\nThis game is to test how well do you know 'Friends'.\nThere are 2 versions to play.\nLong version consists of 10 questions and short version consists of 5 questions.\nYou only got one chance to guess the correct answer.\nYou can exit the game by typing q or ctrl c at any time. Good luck!\n--------------------------------------------------------------------")

def main(list):
    #random display the questions every time
    random.shuffle(list)
    
    try:
        i=0
        right = 0 #track how many right answers the user get
        user_choice = input("Type L for long version, and type S for short version:\n>")
        #users are only allowed to type l or s
        if user_choice.upper() not in ["L", "S"] and user_choice.lower() != "q":
            print("You can only type L or S. Try again.")
            main(mini_project1_data.quizlist)
        #exit game if input is q
        elif user_choice.lower()=="q":
            print("Goodbye!")
            exit()
        #slice the original list to 5 element if user chose to play a short version
        elif user_choice.upper()=="S":
            list = list[:5]
            # print(len(list))

       #loop through the list, slice the question and answers
        while i<len(list):
            question=list[i]["question"]
            #combine the correct answer and incorrect answser
            choices = list[i]["correct_answer"] + list[i]["incorrect_answers"]
            #then shuffle them and put them into a dictionary
            random.shuffle(choices)
            answers_dic = {}
            answers_dic["A"] = choices[0]
            answers_dic["B"] = choices[1]
            answers_dic["C"] = choices[2]
            answers_dic["D"] = choices[3]

            #print question and answers 
            print(f"\nQuestion: {question}")
            choice_a=answers_dic["A"]
            choice_b=answers_dic["B"]
            choice_c=answers_dic["C"]
            choice_d=answers_dic["D"]
            print(f"A: {choice_a}")
            print(f"B: {choice_b}")
            print(f"C: {choice_c}")
            print(f"D: {choice_d}")
            
            #let user type his choice
            user_input = input("What's your choice?(A,B,C or D)\n>").upper()
          
            #check whether the choice is the correct answer and move to next question if it is, exit the game if it isn't
            if user_input.lower() not in ["a", "b", "c", "d", "q"]:
                print("You must type A, B, C or D. Try again!")
                continue
            #user can type q to exit the game
            elif user_input.lower() == "q":
                print("Goodbye!")
                break
            elif answers_dic[user_input] == list[i]["correct_answer"][0]:
                right += 1
                print("You guessed right.")
            
            else:
                print(f"{user_input} is not the correct answer! you guessed {right} question(s) right! Try it next time!")
                break   

            #update the counter
            i+=1
           
    #exit game by ctrl c
    except KeyboardInterrupt:
        print("Goodbye!")
        exit()

    #print congratulations if user got them all right
    if right == len(list):
        print(f"Congratulations! You guessed all of the {right} questions right. You are a pro!")


main(mini_project1_data.quizlist)