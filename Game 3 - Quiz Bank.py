#Quiz Game

#Define functions
def question_bank(question_num,number):
    question = ""
    answer = ""
    user_answer = ""
    num_corr_ans = 0
    
    if number == 1:
        question = "What is the country's national bird?"
        answer   = "Philippine Eagle"
    elif number == 2: 
        question = "Who is the first President of the Philippines?"
        answer   = "Emilio Aguinaldo"
    elif number == 3:
        question = "Who is the current President of the Philippines?"
        answer   = "Rodrigo Duterte"
    elif number == 4:
        question = "Who is the Philippine's National Hero?"
        answer   = "Jose Rizal"
    elif number == 5:
        question = "What is the capital of Philippines?"
        answer   = "Manila"
    elif number == 6:
        question = "What is the Filipino term for the color blue?"
        answer   = "Bughaw"
    elif number == 7:
        question = "Find the product: 4 x 100?"
        answer   = "400"
    elif number == 8:
        question = "What is the sum: 567 + 875?"
        answer   = "1442"
    elif number == 9:
        question = "What is the Filipino term for burnt rice?"
        answer   = "Tutong"
    elif number == 10:
        question = "Who is the author of Florante at Laura?"
        answer   = "Francisco Balagtas"

    time.sleep(1)
    print("\nQuestion #", question_num, ":", question)
    user_answer = str(input("Your Answer: "))

    if user_answer == answer:
        num_corr_ans = 1
    
    return num_corr_ans


#Import needed docs
from random import randint
import time

#Global Variables
play_again = 1
number = 0
question_num = 0
total_corr_ans = 0
num_corr_ans = 0

#Main Logic
while play_again == 1:
    question_num = 0
    
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("+++                                                      +++")
    print("+++                       QUIZLET                        +++")
    print("+++                                                      +++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++New Game++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    time.sleep(1)

    print("\nInstructions: 5 random questions are given to be answered.")
    print("              Correct spelling is observed.")

    time.sleep(2.5)
    print(" LET'S START")

    
    while question_num < 5:
        question_num = question_num + 1
        number = randint(1,10)

        #Match Rand Num, ask the question and check answers
        num_corr_ans = question_bank(question_num,number)

        total_corr_ans = total_corr_ans + num_corr_ans
        
    
    print("\nTotal Correct Answers: ", total_corr_ans)
    
    time.sleep(1)
    print("Do you want to play again?")
    print("Press 1 for YES and 0 for NO")
    play_again = int(input("\nPlay again? "))











