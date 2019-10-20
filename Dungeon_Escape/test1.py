from random import randint
p1 = randint(1,16)
p2 = randint(1,16)
k1 = randint(1,16)
k2 = randint(1,16)
e1 = randint(1,16)
e2 = randint(1,16)
# print(p1,p2,k1,k2,e1,e2)

player = {
    "x" : 1,
    "y" : 2,
}

key = {
    "x" : 2,
    "y" : 1,
}

exit = {
    "x" : 3,
    "y" : 2,
}
checked = False
while True:
    for i in range(4):
        for j in range(4):

            if i == player["y"] and j == player["x"]:
                print("P",end=" ")
            elif i == key["y"] and j == key["x"]:
                if checked == False:
                    print("K",end=" ")
                else:
                    print("-",end=" ")
            elif i == exit["y"] and j == exit["x"]:
                print("E",end=" ")
            else:
                print("-",end=" ")
        print(" ")


    move = input("Your move: ")
    if move == "a":
        player["x"] -= 1
    elif move == "d":
        player["x"] += 1
    elif move == "w":
        player["y"] -= 1
    elif move == "s":
        player["y"] += 1

    if player["y"] == key["y"] and player["x"] == key["x"]:
        checked = True
        print("You’ve just picked up a key!!!")
    elif player["y"] == exit["y"] and player["x"] == exit["x"] and checked == False:
        print("You can't exit, please acquire the key(s) first")
    elif player["y"] == exit["y"] and player["x"] == exit["x"] and checked == True:
        print("Congrats, you’ve just escaped the dungeon")
        break

    
    
    