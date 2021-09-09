#Rock_Paper_Scissors Game
import random
print("Rock_Paper_Scissors Game")
history_a=[]
history_b=[]
player_a=False
counta=0
countb=0
while player_a == False:
    for i in range(10):
        print('''Please pick one:
            rock
            scissors
            paper''')
        game_list=('rock','scissors','paper')
        player_a=str(input("player_a : "))
        history_a.append(player_a)
        player_b = random.choice(game_list)
        history_b.append(player_b)
        print("player_b :",player_b)
        if player_a==player_b:

            print(player_a,"tie",player_b)
        elif player_a=="rock":
            if player_b=="scissors":
              print(player_a, "smashes",player_b, "you win! player a")
              counta += 1
            else:
              print("paper coverd",player_a,"You win player b")
              countb +=1
        elif player_a=="paper":
            if player_b=="rock":
               print(player_a,"covers",player_b, "you win player a")
               counta += 1
            else:
               print("scissors cuts",player_a," you win player b")
               countb += 1
        elif player_a=="scissors":
            if player_b=="paper":
               print(player_a,"cuts",player_b,"you win player a")
               counta += 1
            else:
               prinr("rock smashes",player_a," you win player b")
               countb += 1
        else:
            print("That's not a valid play. Check your spelling!")
#check the winner
if counta>countb:
    print("Palayer A is the Winner, The score is : ",counta,countb)
elif counta<countb:
    print("Palayer B is the Winner, The score is : ", counta, countb)
else:
    print("The Player A and Player B is win this game,The score is : ",counta,countb,)
#take the history
num=int(input("Enter the round for which you need the information : "))
print(history_a[num])
print(history_b[num])