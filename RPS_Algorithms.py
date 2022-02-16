import random
import numpy as np

import math
import itertools
import time
from collections import Counter
import random
import itertools
from array import *
## We keep the times of the moves in these lists.
action = 0 #It means player0 move ( 1 for Rock, 2 for Paper, 3 for Scissors)
action1 = 0 ##It means player1 move ( 1 for Rock, 2 for Paper, 3 for Scissors)

name= '' #It means player0 move's name ( "Rock" for 1, "Paper" for 2, "Scissors" for 3
name1= '' #It means player1 move's name ( "Rock" for 1, "Paper" for 2, "Scissors" for 3

RR=0 #It keeps sum of move R after R
RP=0 #It keeps sum of move P after R
RS=0 #It keeps sum of move S after R

PP=0 #It keeps sum of move P after P
PR=0 #It keeps sum of move R after P
PS=0 #It keeps sum of move S after P

SS=0 #It keeps sum of move S after S
SR=0 #It keeps sum of move R after S
SP=0 #It keeps sum of move P after S


i = 0


arry=[]

player0_rock = [] #It keeps player0's rock move
player0_paper = [] #It keeps player0's paper move
player0_scissors = [] #It keeps player0's scissors move
player0_move =[] #It keeps player0's all move

##ai move's times
player1_rock = [] #It keeps player1's rock move
player1_paper = [] #It keeps player1's paper move
player1_scissors = [] #It keeps player1's scissors move


## move time
counter = 1

count = 0
numerate = 0

## counters for possible states
player0_win = 0
player1_win = 0
draw = 0

arr= [] #It keeps last move of player0. For example for Rock [1,0,0] - for Scissors [0,0,1]
# We need arr[] for MarkovChain Algorithm
marcov_arr = [] #It keeps player0's possible next move probability. (3*3 matrix)
#For example:
#     R     P    S
# R [ 0.3  0.2  0.5]    R P S
# P [ 0.1  0.2  0.6] * [0,0,1] (arr)
# S [ 0.2  0.4  0.3]
#It gives probabilities of next move after S like [0.2,0.4,0.3]
#Markov chain algorithm predict next move of player0 as P because P has highest probability so
#Markov chain move S to win
reward = 0 #final total point of player0
reward1 = 0 #final total point of player1

res = []
first_move = 0
## for select mode ai vs user or ai vs comp
mode = int(input("Which mode do you prefer? (Press 1 or 2)\n(1)Constant Agent VS Nash Equilibrium \n(2)Mirror Shift Constant Agent VS Mirror Opponent Agent\n(3)MarcovChain\n(4)User game vs Our developed Random Agent\n"))

## how many times do you want
n_times = int(input("How many times do you want to play ?\n"))

#function for player0 (first player)
def player0(counter) :
    global player0_rock
    global player0_paper
    global player0_scissors
    global action
    global first_move
    global name
    global player0_move
    global numerate

    ## if constant agent play, its choice always be Rock
    if mode == 1:
        action = 1 #You can change 1 as 2 or 3. #If you want to be user instead of constant agent
        #the if statement on the bottom line You can run it by adding the mode 1 state.
        name = 'Rock'
        player0_move.append(action)
        player0_rock.append(counter)
    #player0 is user in mode3 and mode4
    if mode == 3 or mode == 4:
        constant_role = int(input("What role should the constant agent play? \n Press (1) for Rock \n Press (2) for Paper \n Press (3) for Scissors"))
        if constant_role == 1:
                action = 1
                name = 'Rock'
                player0_move.append(action)
                player0_rock.append(counter)

        if constant_role == 2:
                action = 2
                name = 'Paper'
                player0_move.append(action)
                player0_paper.append(counter)

        if constant_role == 3:
                action = 3
                name = 'Scissors'
                player0_move.append(action)
                player0_scissors.append(counter)


        if action < 1 or action > 3 or action == " ":
             print("select again")
             player0(counter)
    # Mirror shift with constant agent
    if mode == 2 : #player0 always move RRSSPPRRSS... in mode2
        if(numerate%2==0):
            if(numerate%6 == 0 and numerate != 0):
                first_move = 1
                action = first_move
            else:
                first_move += 1
                action = first_move

        numerate += 1
        action = first_move

        if action == 1 :
            player0_rock.append(counter)
            player0_move.append(action)

            name = 'Rock'

        if action == 2:
            player0_scissors.append(counter)
            player0_move.append(action)
            name = 'Scissors'

        if action == 3:
            player0_paper.append(counter)
            player0_move.append(action)
            name = 'Paper'
    #In mode3:
    #If you dont want to be user against to Markov Chain you can use Nash Equilibrium Algorithm for random choice
    #In mode4:
    #If you dont want to be user against our developed algorithm you can use Nash Equilibrium Algorithm
    #The algorithm we developed shows over 30% success so it will usually win against Nash Equilibrium.
    """if mode == 3:  #(if mode == 4:)
        action = random.choice([1, 2, 3])
        if action == 1:
            player0_rock.append(counter)
            player0_move.append(action)
            name = 'Rock'
        if action == 2:
            player0_paper.append(counter)
            player0_move.append(action)
            name = 'Paper'
        if action == 3:
            player0_scissors.append(counter)
            player0_move.append(action)
            name = 'Scissors'"""



    return action,name, player0_rock, player0_paper, player0_scissors,player0_move


#function for player1
def player1(counter) :
    global arr
    global action1
    global name1
    global i
    global count
    global res
    #Nash Equilibrium
    if mode == 1:
       action1 = random.choice([1, 2, 3])
       if action1 == 1 :
         player1_rock.append(counter)
         name1= 'Rock'
       if action1 == 2 :
         player1_paper.append(counter)
         name1= 'Paper'
       if action1 == 3 :
         player1_scissors.append(counter)
         name1 = 'Scissors'


    #Mirror Opponent Agent
    if mode == 2 :

        if count == 0 :
            action1 = 1
            player1_rock.append(counter)
            name1 = 'Rock'
            count += 1
        else:
            #print('***************')
            #print(player0_move)
            action1 = player0_move[i]
            i += 1
            if action1 == 1:
             player1_rock.append(counter)
             name1 = 'Rock'
            if action1 == 2:
             player1_scissors.append(counter)
             name1 = 'Scissors'
            if action1 == 3:
             player1_paper.append(counter)
             name1 = 'Paper'

    #MarkovChain
    #First move always rock
    if mode==3 and counter<=2:
        action1 = 1
        name1 = 'Rock'
        player1_rock.append(counter)
    #check last action of player0
    if mode==3 and counter>=3:
        lastaction = player0_move[counter-2]
        print(lastaction)
        if lastaction == 1:
            arr = [1,0,0]
        if lastaction ==2:
            arr = [0,1,0]
        if lastaction ==3:
            arr = [0,0,1]
    #print(arr)
    #print(marcov_arr)
    #markov chain matrix
    if (counter>=3 and mode==3) :
        res = [[0 for x in range(3)] for y in range(1)]
        a = marcov_arr[0][0] * arr[0] +  marcov_arr[1][0] * arr[1] + marcov_arr[2][0] * arr[2]
        b = marcov_arr[0][1] * arr[0] +  marcov_arr[1][1] * arr[1] + marcov_arr[2][1] * arr[2]
        c = marcov_arr[0][2] * arr[0] +  marcov_arr[1][2] * arr[1] + marcov_arr[2][2] * arr[2]
        res.append(a)
        res.append(b)
        res.append(c)
        print(res)
        #Player1 moves against to prediction moves of player0
        if res[1] > res [2] and res[1] > res[3] :
            action1 = 2
            name1 = 'Paper'
            player1_paper.append(counter)
        if res[2] > res[1] and res[2] > res[3] :
            action1 = 3
            name1 = 'Scissors'
            player1_scissors.append(counter)
        if res[3] > res [2] and res[3] > res[1] :
            action1 = 1
            name1= 'Rock'
            player1_rock.append(counter)
        #If two of them greater than other. In the first if statement:
        # It check total number of rock move and number of player move
        #Whichever of the moves player0 has made more, player1 plays against that move.
        if res[1] == res [2] and res[1] > res[3] :
            if player0_rock > player0_paper :
                action1 = 2
                name1 = 'Paper'
                player1_paper.append(counter)
            else :
                action1 = 2
                name1 = 'Rock'
                player1_rock.append(counter)

        if res[2] == res[3] and res[2] > res[1]:
            if player0_paper > player0_scissors:
                action1 = 3
                name1 = 'Scissors'
                player1_scissors.append(counter)
            else :
                action1 = 1
                name1 = 'Rock'
                player1_rock.append(counter)
        if res[1] == res [3] and res[3] > res[2]:
            if player0_rock > player0_scissors:
                action1 = 2
                name1 = 'Paper'
                player1_paper.append(counter)
            else:
                action1 = 1
                name1 = 'Rock'
                player1_rock.append(counter)
        #If all probabilities are equal use nash equilibrium
        if res[1] == res[2] and res[2] == res[3]:
            action1 = random.choice([1, 2, 3])
            if action1 == 1:
                player1_rock.append(counter)
                name1 = 'Rock'
            if action1 == 2:
                player1_paper.append(counter)
                name1 = 'Paper'
            if action1 == 3:
                player1_scissors.append(counter)
                name1 = 'Scissors'
    #Our developed algorithm
    #It starts with Nash Equilibrium and after n_times/ 3 it uses player0_moves  array
    #It predicts player0's next move on player0_moves array using random function
    if mode == 4:
        j = 0

        if (len(player0_move) - 1) <= (n_times / 3):
            action1 = random.choice([1, 2, 3])
            if action1 == 1:
                name1 = 'Rock'
                player1_rock.append(counter)

            if action1 == 2:
                name1 = 'Paper'
                player1_paper.append(counter)

            if action1 == 3:
                name1 = 'Scissors'
                player1_scissors.append(counter)


            if counter == (n_times / 3) or counter == ((n_times-1) / 3) or counter == ((n_times+1) / 3):
                R = diverConter(player0_move)
                RockNum = R[1]
                PaperNum = R[2]
                ScissorsNum = R[3]
                arrayCreater(RockNum, PaperNum, ScissorsNum)
                print(arry)


        else:

            action1 = random.choice(arry)
            if action1 == 1:
                name1 = 'Rock'
                player1_rock.append(counter)


            if action1 == 2:
                name1 = 'Paper'
                player1_paper.append(counter)


            if action1 == 3:
                name1 = 'Scissors'
                player1_scissors.append(counter)



    return action1, name1,player1_rock, player1_paper, player1_scissors


def diverConter(arr):
    d = Counter(arr)
    return d


def arrayCreater(RockNum, PaperNum, ScissorsNum):
    #Tr = ScissorsNum - 1
    #Pn = RockNum - 1
    #Sn = PaperNum - 1

    for m in range(RockNum):
        arry.append(2)
    for n in range(PaperNum):
        arry.append(3)
    for k in range(ScissorsNum):
        arry.append(1)
    return arry
#MarcovChain function for mode3
def MarcovChain():
    global i
    global RR
    global RP
    global RS
    global PP
    global PR
    global PS
    global SS
    global SR
    global SP
    global marcov_arr
    if player0_move[i] == 1 and player0_move[i+1] == 1 :
        RR += 1
    if player0_move[i] == 1 and player0_move[i+1] == 2 :
        RP += 1
    if player0_move[i] == 1 and player0_move[i+1] == 3 :
        RS += 1
    if player0_move[i] == 2 and player0_move[i+1] == 2 :
        PP += 1
    if player0_move[i] == 2 and player0_move[i+1] == 1 :
        PR += 1
    if player0_move[i] == 2 and player0_move[i+1] == 3 :
        PS += 1
    if player0_move[i] == 3 and player0_move[i+1] == 3 :
        SS += 1
    if player0_move[i] == 3 and player0_move[i+1] == 1 :
        SR += 1
    if player0_move[i] == 3 and player0_move[i+1] == 2 :
        SP += 1

    total_r = RR + RS + RP

    if total_r == 0:
        RR_res = 0
        RP_res = 0
        RS_res = 0
    else:
        RR_res = RR / total_r
        RP_res = RP / total_r
        RS_res = RS / total_r

    total_p = PP + PR + PS

    if total_p == 0:
        PR_res = 0
        PP_res = 0
        PS_res = 0
    else :
        PR_res = PR/total_p
        PP_res = PP/total_p
        PS_res = PS/total_p

    total_s = SS + SR + SP

    if total_s == 0:
        SR_res = 0
        SP_res = 0
        SS_res = 0
    else :
        SR_res = SR/total_s
        SP_res = SP/total_s
        SS_res = SS/total_s

    marcov_arr = [[RR_res, RP_res, RS_res], [PR_res, PP_res, PS_res], [SR_res, SP_res, SS_res]]

    i += 1
    return marcov_arr
#Who won the game
def compare():
    global draw
    global player0_win
    global player1_win
    global reward
    global reward1

    rock_result_0 = counter in player0_rock
    rock_result_1 = counter in player1_rock

    paper_result_0 = counter in player0_paper
    paper_result_1 = counter in player1_paper

    scissors_result_0 = counter in player0_scissors
    scissors_result_1 = counter in player1_scissors

    if (rock_result_0 and rock_result_1) or (paper_result_0 and paper_result_1)\
            or (scissors_result_0 and scissors_result_1):
        print('    Result:                          Tie')

        draw += 1
        print('    Reward:         ' + str(reward) + '                                  ' + str(reward1) + '\n  ')
    if (rock_result_0 and paper_result_1) or (paper_result_0 and scissors_result_1) \
            or (scissors_result_0 and rock_result_1):
        print('    Result:                                             Win')
        player1_win += 1
        reward1 += 1
        reward -= 1
        print('    Reward:        ' + str(reward) + '                                   ' + str(reward1) + '\n  ')
    if (paper_result_0 and rock_result_1) or (rock_result_0 and scissors_result_1)\
            or (scissors_result_0 and paper_result_1):
        print('    Result:          Win')
        player0_win += 1
        reward += 1
        reward1 -= 1
        print('    Reward:        ' + str(reward) + '                                 ' + str(reward1) + '\n  ')


    return draw, player0_win, player1_win, reward, reward1

#print result for mode1
if mode==1:
    while counter > 0 and counter <= n_times:

         a = player0(counter)
         b = player1(counter)

         print("                  Constant Agent     VS      Nash Equilibrium Agent")
         print('    Action :          ' + str(a[0]) + '                                ' + str(b[0]) + '' )
         print('    Name:           ' + str(a[1]) + '                             ' + str(b[1]) + '' )
         compare()
         counter += 1
    if(reward > reward1) :
            print("                 >< Constant Agent Won The Game ><")
    elif(reward < reward1) :
            print("                 >< Nash Equilibrium Agent Won The Game ><")
    else:
            print("                 >< The Game Ended In A Draw ><")
#print result for mode2
if mode==2:
    while counter > 0 and counter <= n_times:

        x = player0(counter)
        y = player1(counter)


        print("          Mirror Shift Constant Agent     VS      Mirror Opponent Agent")
        print('    Action :        ' + str(x[0]) + '                                   ' + str(y[0]) + '')
        print('    Name:           ' + str(x[1]) + '                            ' + str(y[1]) + '')
        compare()
        counter += 1

        #if (first_move > 2):
         #    first_move = 0

    if (reward > reward1):
        print("                 >< Mirror Shift Constant Agent Won The Game ><")
    elif (reward < reward1):
        print("                 >< Mirror Opponent Agent Won The Game ><")
    else:
        print("                 >< The Game Ended In A Draw ><")


#print result for mode3
if mode==3:
    while counter > 0 and counter <= n_times:

        x = player0(counter)

        y = player1(counter)
        if counter>=2:
           MarcovChain()
        print("          Mirror Shift Constant(User)     VS                 Markov Chain")
        print('    Action :        ' + str(x[0]) + '                                   ' + str(y[0]) + '')
        print('    Name:           ' + str(x[1]) + '                            ' + str(y[1]) + '')

        compare()
        counter += 1


    if (reward > reward1):
        print("                 >< User Won The Game ><")
    elif (reward < reward1):
        print("                 >< Markov Chain Won The Game ><")
    else:
        print("                 >< The Game Ended In A Draw ><")
#print result for mode4
if mode==4:
    while counter > 0 and counter <= n_times:

        x = player0(counter)
        y = player1(counter)


        print("          User play Agent     VS      Our developed Random Agent")
        print('    Action :        ' + str(x[0]) + '                                   ' + str(y[0]) + '')
        print('    Name:           ' + str(x[1]) + '                            ' + str(y[1]) + '')
        compare()
        counter += 1

        #if (first_move > 2):
         #    first_move = 0

    if (reward > reward1):
        print("                 >< User play Agent Won The Game ><")
    elif (reward < reward1):
        print("                 >< Our developed  Agent Won The Game ><")
    else:
        print("                 >< The Game Ended In A Draw ><")
