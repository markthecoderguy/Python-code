#This is a code for a slot machine 
#fruits dont work on cmd 
#thonny works fine
#made by markthecoderguy on github
import random
import time
coins = 5
score = 0
print ("you have 5 coins")
while coins > 0:
    print("coins:")
    print(coins)
    print("score:")
    print(score)
    play = (input("INSERT COIN\n  "))
    pick = random.randint(1,5)
    if pick == 1:
        print("914")
        time.sleep(0.5)
        print("🍉🍉🍉")
        time.sleep(0.5)
        print("🥥21")
        time.sleep(0.7)
        print("🍒🍒🍒")
        time.sleep(1)
    elif pick == 2:
        time.sleep(0.5)
        print("🍒🍒2")
        time.sleep(0.6)
        print("2🥝0")
        time.sleep(0.8)
    elif pick == 3:
        print("🥝🥝🥝")
        time.sleep(0.7)
        print("0🥑1")
        time.sleep(1)
    elif pick == 4:
        print("893")
        time.sleep(0.4)
        print("🍒01")
        time.sleep(0.7)
        print("🍉🍉7")
        time.sleep(1)
    elif pick == 5:
        print("🍐12")
        time.sleep(0.5)
        print("🍒🍒🍒")
        time.sleep(1)
    else:
        print("error")
        
    win = random.randint(1,10)
    if win == 1:
        print("386")
        time.sleep(1)
        print("no points added! total score:")
        print(score)
        coins = coins - 1
    elif win == 2:
        print("962")
        time.sleep(1)
        print("no points added! total score:")
        print(score)
        coins = coins - 1
    elif win == 3:
        print("529")
        time.sleep(1)
        print("no points added! total score:")
        print(score)
        coins = coins - 1
    elif win == 4:
        print("670")
        time.sleep(1)
        print("no points added! total score:")
        print(score)
        coins = coins - 1
    elif win == 5:
        print("406")
        time.sleep(1)
        print("no points added! total score:")
        print(score)
        coins = coins - 1
    elif win == 6:
        print("2🍉0")
        time.sleep(1)
        print("1 point added! total score:")
        score = score + 1
        print(score)
        coins = coins - 1
    elif win == 7:
        print("🍒🍒🍒")
        time.sleep(1)
        print("BIG WIN")
        print("5 POINTS ADDED! total score:")
        score = score + 5
        print(score)
        coins = coins - 1
    elif win == 8:
        print("🍒🍒🍎")
        time.sleep(1)
        print("small win! 2 points added! total score:")
        score = score + 2
        print(score)
        coins = coins - 1
    elif win == 9:
        print("🍉2🍉")
        time.sleep(1)
        print("medium win! 3 points added! total score:")
        score = score + 3
        print(score)
        coins = coins - 1
    elif win == 10:
        print("🥥67")
        time.sleep(1)
        print("1 point added! total score:")
        score = score + 1
        print(score)
        coins = coins - 1
    else:
        print("error")
if coins == 0:
    print("NO COINS LEFT")
    print("score:")
    print(score)
      
        
    
    
    
    
    
    
