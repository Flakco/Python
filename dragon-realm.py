import random
import time
def play():
    print ("")
    print ("""\n\tYou are in a land full of dragons. In front of you,
    \n\tyou see two caves. In one cave, the dragon is friendly
    \n\tand will share his treasure with you. The other dragon
    \n\tis greedy and hungry, and will eat you on sight.
    """)

    time.sleep(2)
    print ("")
    c = "vidas"
    gold = 0
    for i in c*3:
        cave = ""
        while cave != "1" and cave != "2":
            print ("\n\tWhich cave will you go into? (1 or 2)")
            cave = input("\n\t")


        print ("\n\tYou approach the cave...")
        time.sleep(2)
        print ("\n\tIt is dark and spooky...")
        time.sleep(2)
        print ("\n\tA large dragon jumps out in front of you! He opens his jaws and...")
        print ("")
        time.sleep(2)
        FriendlyCave = random.randint (1,2)

    
    
        if cave == str(FriendlyCave):
            print ("\n\tGobbles you down in one bite!")
            gold += 100
            print("\n\tTu oro actual es: " + str(gold))
            if gold == 1000:
                print("Ganaste!")
                break
        elif cave != str(FriendlyCave):
            print ("\n\tEl dragon te come de un bocado....")
            print("\n\tPerdiste el oro acumulado!: " + str(gold))
            PlayAgain = input("\n\tDo you want to play again?: \n\t(yes or no) \n\t ")
            if PlayAgain == "y" or PlayAgain == "yes":
                play()
            elif PlayAgain == "n" or PlayAgain == "no":
                break
play()
