#!usr/bin/env python3
import random
# data of questions and answers
quizlist = [
    {
        "question": "Which of the following is Ross NOT allergic to?",
        "correct_answer": ["Bananas"],
        "incorrect_answers": ["Lobster", "Kiwi","Peanuts"]
    },
    {
        "question": "What's in Monica's locked closet?",
        "correct_answer": ["A whole bunch of junk"],
        "incorrect_answers": ["Candy and chocolate", "Skeletons","Cleaning equipment"]
    },
    {
        "question": "Ross' bald girlfriend was named:",
        "correct_answer": ["Bonnie"],
        "incorrect_answers": ["Beth", "Veronica","Vanessa"]
    },
    {
        "question": "What famous person does Phoebe think is her grandfather?",
        "correct_answer": ["Albert Einstein"],
        "incorrect_answers": ["Gary Grant", "Dwight D. Eisenhower","Robert Redford"]
    },
    {
        "question": "Which Friend has a tattoo?",
        "correct_answer": ["Rachel"],
        "incorrect_answers": ["Monica", "Phoebe","Ross"]
    },
    {
        "question": "Who said, 'Could I BE wearing any more clothes?'",
        "correct_answer": ["Joey"],
        "incorrect_answers": ["Monica", "Gunther","Chandler"]
    },
    {
        "question": "What song does Ross sing to Emma to get her to stop crying?'",
        "correct_answer": ["Baby Got Back"],
        "incorrect_answers": ["Thong Song", "Walk This Way","Sweet Child O'Mine"]
    },
    {
        "question": "What toy is always on Joey and Chandler's door?",
        "correct_answer": ["A Magna Doodle"],
        "incorrect_answers": ["A Slinky", "An Etch-a-Sketch","A Wooly Willy"]
    },
    {
        "question": "Whose pizza do the girls get by accident in Season 1?",
        "correct_answer": ["George Stephanopoulous"],
        "incorrect_answers": ["Tom Cruise's", "John F. Kennedy Jr.'s","Ethan Hawke's"]
    },
    {
        "question": "Which Friend has only nine toes?",
        "correct_answer": ["Chandler"],
        "incorrect_answers": ["Ross", "phoebe","Joey"]
    },
]

def main(list):
    #random display the questions every time
    random.shuffle(list)
    try:
        i=0
        right = 0 #track how many right answers the user get
        print("\nThis game is to test how well do you know 'Friends'.\nThere are 10 questions to answer and you only got one chance to guess the correct answer.\nYou can exit the game by typing q or ctrl c at any time. Good luck!")
       
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
            if user_input.lower() not in ["a", "b", "c", "d"] and user_input.lower() != "q":
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
             
            i+=1
           
    #exit game by ctrl c
    except KeyboardInterrupt:
        print("Goodbye!")
        exit()

    #print congratulations if user got them all right
   
    if right == 10:
        print("Congratulations! You guessed all of the questions right. You are a pro!")


main(quizlist)