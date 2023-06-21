import random
import time
def compra():
    n=int(input("INGRESE EL MONTO TOTAL DE LA COMPRA: $ "))
    if n >= 100:
        print("SU GASTO IGUALA O SUPERA LOS $100.00 Y POR LO TANTO PARTICIPA EN LA PROMOCION.")
        print("\n\t\tCOLOR" + "\t\t      DESCUENTO")
        print("")
        print("\t     BOLA BLANCA" + "\t       NO TIENE")
        print("\t     BOLA ROJA" + "\t    10 POR CIENTO")
        print("\t     BOLA AZUL" + "\t    20 POR CIENTO")
        print("\t     BOLA VERDE" + "\t    25 POR CIENTO")
        print("\t     BOLA AMARILLA" + "\t    50 POR CIENTO")
        print("")
        num=random.randint(1,5)
        if num == 1:
            print("ALEATORIAMENTE USTED OBTUVO UNA BOLA BLANCA")
            time.sleep(1)
            print("LAMENTABLEMENTE NO TIENE DESCUENTO")
            time.sleep(1)
            print("SU TOTAL A PAGAR ES: " + str(n))       
        elif num == 2:
            print("ALEATORIAMENTE USTED OBTUVO UNA BOLA ROJA")
            time.sleep(1)
            print("FELICIDADES OBTUVO UN DESCUENTO DE 10 POR CIENTO")
            time.sleep(1)
            print("SU NUEVO TOTAL A PAGAR ES: " + str((10*n)/100))  
        elif num == 3:
            print("ALEATORIAMENTE USTED OBTUVO UNA BOLA AZUL")
            time.sleep(1)
            print("FELICIDADES OBTUVO UN DESCUENTO DE 20 POR CIENTO")
            time.sleep(1)
            print("SU NUEVO TOTAL A PAGAR ES: " + str((20*n)/100))   
        elif num == 4:
            print("ALEATORIAMENTE USTED OBTUVO UNA BOLA VERDE")
            time.sleep(1)
            print("FELICIDADES OBTUVO UN DESCUENTO DE 25 POR CIENTO")
            time.sleep(1)
            print("SU NUEVO TOTAL A PAGAR ES: " + str((25*n)/100)) 
        elif num == 5:
            print("ALEATORIAMENTE USTED OBTUVO UNA BOLA AMARILLA")
            time.sleep(1)
            print("FELICIDADES OBTUVO UN DESCUENTO DE 50 POR CIENTO")
            time.sleep(1)
            print("SU NUEVO TOTAL A PAGAR ES: " + str((50*n)/100))
    elif n < 100:
        print("SU GASTO NO IGUALA O SUPERA LOS $100.00 Y POR LO TANTO NO PARTICIPA EN LA PROMOCION.")
compra()
time.sleep(2)
m=input("SI DESEA SALIR PRESIONE N DE LO CONTRARIO PRESIONE Y: ")
a=0
if m=="y" or m=="Y":
    compra()
else:
    while a == 0:
        break