# BlackJack yay haha

from random import randint
import time

comp_rand1 = randint(1,13)
comp_rand2 = randint(1,13)
comp_rand3 = 0
total_comp = comp_rand1 + comp_rand2
hum_rand1  = -1
hum_rand2  = -1
hum_rand3  = 0
total_hum  = hum_rand1 + hum_rand2

play_again = 1
game_num   = 1
card_again = -1

print("=======================================================================")
print("BLACKJACK")
print("You VS Computer")
time.sleep(1)

while play_again == 1:
    print("-----------------------------------------------------------------------")
    print("GAME #", game_num)
    time.sleep(1)

    hum_rand1 = randint(1,13)
    hum_rand2 = randint(1,13)
    total_hum  = hum_rand1 + hum_rand2

    print("Displaying your cards..")
    time.sleep(1)
    
    print("Your CARD 1: ", hum_rand1)
    print("Your CARD 2: ", hum_rand2)

    #Display Comp CARD1:
    print('\n')
    time.sleep(3)
    print("Displaying Computer's First Card..")
    time.sleep(0.5)
    print("Comp CARD 1: ", comp_rand1)

    #Pick Card Again?
    print('\n')
    print("Would you like to pick a card again?")
    card_again = int(input("Enter 1 for YES and 0 for NO: "))

    if card_again == 1:
            hum_rand3 = randint(1,13)
            time.sleep(0.5)
            print('\n')
            print("CARD 3: ", hum_rand3)
            total_hum = total_hum + hum_rand3

    #AI should be smart:
    if total_comp < 16:
        comp_rand3 = randint(1,13)
        total_comp = total_comp + comp_rand3


    #Display Hum's CARDS
    time.sleep(1)
    print('\n')
    print("Let's display your CARDS")
    time.sleep(1)
    print("Your CARD 1: ", hum_rand1)
    print("Your CARD 2: ", hum_rand2)

    if hum_rand3 > 0:
        print("Your CARD 3: ", hum_rand3)
                     
    #Display Comp's CARDS
    print('\n')    
    print("Let's display Computer's CARDS")
    print("Comp CARD 1: ", comp_rand1)
    print("Comp CARD 2: ", comp_rand2)

    if comp_rand3 > 0:
        print("Comp CARD 3: ", comp_rand3)

    #Print TOTALS
    print('\n')    
    print("Total Your CARDS: ", total_hum)
    print("Total Comp CARDS: ", total_comp)
                     
    if total_hum > 21 and total_comp > 21:
        print("Human LOST")
        print("Computer LOST")
    elif total_hum < 21 and total_comp > 21:
        print("Human WIN")
        print("Computer LOST")
    elif total_hum > 21 and total_comp < 21:
        print("Human LOST")
        print("Computer WIN")
    elif total_hum == 21 and total_comp == 21:
        print("Human WIN")
        print("Computer WIN")
    elif total_hum < 21 and total_comp < 21:
        if total_hum > total_comp:
            print("Human WIN")
            print("Computer LOST")
        elif total_hum < total_comp:
            print("Human LOST")
            print("Computer WIN")

    time.sleep(7)
    print('\n')
    print("This is the end of the game")
    print("Would you like to play again?")
    time.sleep(1)
    play_again = int(input("Press 1 for YES and 0 for NO: "))

if play_again == 0:
    print("GAME WILL NOW CLOSE")
    print("=======================================================================")
