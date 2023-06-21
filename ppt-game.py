import random

def play():
    user = input("Choice 'r' for rock, 'p' for paper, 's' for scissors: ")
    computer = random.choice(['r', 'p', 's'])

    if user==computer:
        return 'It\'s a tie'

    if iswin(user,computer):
        return 'YOU WON!'

    return 'YOU LOST'

def iswin(player, opponent):

    if (player=='r' and opponent=='s') or (player=='p' and opponent=='r') \
        or (player=='s' and opponent=='p'):
         return True

print(play())

