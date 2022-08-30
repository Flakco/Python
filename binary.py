import random
import time

while True:
    r = 1010100010010101001000101001010010101001010101011000010
    h = ""
    for w in str(r):
        h = str(random.randint(0,1)) + h
    
    time.sleep(0.3)
    print("\t\t\t",h)
   