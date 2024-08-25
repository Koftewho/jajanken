import random

rsp = ["rock","scissor","paper"]
cont = 'c'

while cont != 'q':
    move = input("What is your move?")
    a = random.randint(0,2)
    if (move == "rock" and rsp[a] == "paper") or (move == "scissor" and rsp[a] == "rock") or (move == "paper" and rsp[a] == "scissor"):
        print("Player: " + move)
        print("PC: " + rsp[a])
        cont = input("You lose. Do you want to quit or continue?(q/c)")
    elif move == rsp[a]:
        print("Player: " + move)
        print("PC: " + rsp[a])
        cont = input("It is a draw. Do you want to quit or continue?(q/c)")
    elif (move == "paper" and rsp[a] == "rock") or (move == "rock" and rsp[a] == "scissor") or (move == "scissor" and rsp[a] == "paper"):
        print("Player: " + move)
        print("PC: " + rsp[a])
        cont = input("You win. Do you want to quit or continue?(q/c)")
    else :
        cont = input("Take it seriously. Do you want to quit or continue?(q/c)")

print("Thanks for playing.")