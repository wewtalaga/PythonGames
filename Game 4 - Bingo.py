#BINGO
#STEPS FOR IMPROVEMENT:
#   Different layout designs to be achieved
#   Mas magandang itsura ng bingo card? Haha
#       (is it possible kaya na maging 2d game siya?)
#   CODES! Dahil tamad tayo, wag na nating pahabain ang codes haha
#       3/12: iedit ang codes. pangit eh. ang gulo-gulo. CLEAN CLEAN CLEAN
#   Gawing human vs AI

#Import needed docs
from    random   import randint
from    pyfiglet import Figlet
import  time

#Global Variable
fl = []
fl_str = []

#Def
def bingo_column(num_start, num_end):
    cnt = 0
    cnt2 = 0
    rand1_str = ""
    setA = [0,0,0,0,0]

    while cnt <= 4:
        rand1 = randint(num_start,num_end)
        if rand1 not in setA:
            setA[cnt] = rand1
            fl.append(rand1)

            #append to fl_str
            rand1_str = str(rand1)
            fl_str.append(rand1_str)
            
            cnt = cnt + 1
    return setA


def make_bingo_card():
    bingo1 = [1,15]
    bingo2 = [16,30]
    bingo3 = [31,45]
    bingo4 = [46,60]
    bingo5 = [61,75]
    
    list1 = [0,0,0,0,0]
    list2 = [0,0,0,0,0]
    list3 = [0,0,0,0,0]
    list4 = [0,0,0,0,0]
    list5 = [0,0,0,0,0]

    num_start = 0
    num_end   = 0
    cnt  = 0
    cnt1 = 0
    x = 0
    y = 0

    while cnt <= 4:
        if cnt == 0:
            num_start = bingo1[0]
            num_end   = bingo1[1]
    
            list1 = bingo_column(num_start,num_end)
            
        elif cnt == 1:
            num_start = bingo2[0]
            num_end   = bingo2[1]

            list2 = bingo_column(num_start,num_end)
             
        elif cnt == 2:
            num_start = bingo3[0]
            num_end   = bingo3[1]

            list3 = bingo_column(num_start,num_end)
                
        elif cnt == 3:
            num_start = bingo4[0]
            num_end   = bingo4[1]

            list4 = bingo_column(num_start,num_end)

        elif cnt == 4:
            num_start = bingo5[0]
            num_end   = bingo5[1]

            list5 = bingo_column(num_start,num_end)

        cnt = cnt + 1
   

def show_bingo_card():
    list1 = []
    a = 0
    b = 5
    c = 10
    d = 15
    e = 20

    str_a = ""
    
    print("==========================")
    print("= B  = I  = N  = G  = O  =")
    print("==========================")

    while a <= 4:
        #To add leading zero if len = 1
        str_a = fl_str[a]
        if len(str_a) == 1:
            str_a       = str(str_a).zfill(2)
            fl_str[a]   = str_a
    
        print("=",fl_str[a], "=",fl_str[b], "=", fl_str[c], "=", fl_str[d], "=", fl_str[e], "= ")
        print("==========================")
        
        a += 1
        b += 1
        c += 1
        d += 1
        e += 1
    

#Generate random numbers and check if aligned
def generate_rand():
    ctr  = 0
    setB = []
    column_char = ''
    index = -1
    bingo = 0
    ready = 1

    while len(setB) <= 20 and bingo == 0 and ready == 1:
        time.sleep(0.5)
        gr_rand = randint(1,75)

        #Compare generated number
        if gr_rand not in setB:
            setB.append(gr_rand)

            if gr_rand <= 15:
                column_char = "B"
            elif gr_rand <= 30 and gr_rand > 15:
                column_char = "I"
            elif gr_rand <= 45 and gr_rand > 30:
                column_char = "N"
            elif gr_rand <= 60 and gr_rand > 45:
                column_char = "G"
            elif gr_rand <= 75 and gr_rand > 60:
                column_char = "O"

            #Print raffled number:   
            print("\nRAFFLE", len(setB), ":", column_char, gr_rand)

            #Check if raffled number exists in the bingo card
            if gr_rand in fl:
                index = fl.index(gr_rand)
                fl_str[index] = "00"

            #Show bingo card
            show_bingo_card()

            #Check if Bingo
            if fl[0] == "00" and fl[4] == "00":
                if fl[6] == "00" and fl[8] == "00":
                    if fl[12] == "00":
                        if fl[16] == "00" and fl[18] == "00":
                            if fl[20] == "00" and fl[24] == "00":
                                bingo = 1
                                print("\n BINGO")
                                show_bingo_card()

            ready == int(input("\nReady? Press 1 if YES and 0 for NO: "))

    custom_fig = Figlet(font='helv')
    if len(setB) >= 21 and bingo == 0:
        print(custom_fig.renderText('Better Luck Next Time'))
    elif len(setB) <= 21 and bingo == 1:
        print(custom_fig.renderText('B I N G O !'))

    show_bingo_card()                
    
#Main Program
play_again = 1
cnt = 0

while play_again == 1:
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++                       WELCOME                        ++")
    print("++                         TO                           ++")
    print("++                    BINGO BONANZA                     ++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    time.sleep(2)

    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++                    INSTRUCTIONS                      ++")
    print("++  You will be given a Bingo Card with random numbers. ++")
    print("++ Computer will produce a random number and the player ++")
    print("++  will check if the generated number matches the ones ++")
    print("++                    in the card.                      ++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    time.sleep(5)
    print("\n")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++                      LET'S PLAY!                     ++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    time.sleep(1)

    make_bingo_card()
    show_bingo_card()
    generate_rand()

    time.sleep(2)
    play_again = int(input("\nPlay Again? "))






















