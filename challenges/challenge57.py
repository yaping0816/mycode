#! usr/bin/env python3

import html

def main():

    trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
           }

    question = trivia["question"]
    print(question)
    answera = trivia["correct_answer"]
    answerb = trivia["incorrect_answers"][0]
    answerc = trivia["incorrect_answers"][1]
    answerd = trivia["incorrect_answers"][2]
    print(f"A: {html.unescape(answera)}") 
    print(f"B: {html.unescape(answerb)}")
    print(f"C: {html.unescape(answerc)}")
    print(f"D: {html.unescape(answerd)}")

    userinput = input("What's your answer\n>").upper()
    result = "Your answer is correct" if userinput=="A" else "Your answer is wrong."
    print(result)

#    if userinput == "A":
#        print("Your answer is correct")
#    else:
#        print("Your answer is wrong")
#
main()

