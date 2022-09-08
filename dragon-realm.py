import random
import time
def jugar():
    print ("")
    print ("""\n\tEstamos en una tierra llena de dragones. Delante nuestro,
    \n\tse ven dos cuevas. En una cueva, el dragon es amigable
    \n\ty compartira el tesoro contigo. El otro dragon
    \n\tes codicioso y hambriento, y te va a comer ni bien te vea.""")

    time.sleep(2)
    print ("")
    c="vidas"
    oro = 0
    for i in c*3:
        cueva = ""
        while cueva != "1" and cueva != "2":
            print ("\n\tHa que cueva quieres entrar? 1 o 2?")
            cueva = input("\n\t")


        print ("\n\tTe acercas a la Cueva...")
        time.sleep(2)
        print ("\n\tEsta oscuro y tenebroso...")
        time.sleep(2)
        print ("\n\tUn gran dragon salta delante tuyo, abre su boca y...")
        print ("")
        time.sleep(2)
        FriendlyCueva = random.randint (1,2)

    
    
        if cueva == str(FriendlyCueva):
            print ("\n\tTe entrega el tesoro...")
            oro += 100
            print("\n\tTu oro actual es: " + str(oro))
            if oro == 1000:
                print("Ganaste!")
                break
        elif cueva != str(FriendlyCueva):
            print ("\n\tEl dragon te come de un bocado....")
            print("\n\tPerdiste el oro acumulado!: " + str(oro))
            n=input("\n\tQuieres juegar de nuevo?: \n\tSi o No \n\t: ")
            if n == "s" or n == ("si"):
                jugar()
            elif n == "n" or n == ("no"):
                break
jugar()