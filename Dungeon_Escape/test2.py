from random import randint
p1 = randint(1,16)
p2 = randint(1,16)
k1 = randint(1,16)
k2 = randint(1,16)
e1 = randint(1,16)
e2 = randint(1,16)
# print(p1,p2,k1,k2,e1,e2)


#tao dic 
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

wall = {
    "x" : 0,
    "y" : 1,
}
checked = False

#in map va check 

#level 1
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
            elif i == wall["y"] and j == wall["x"]:
                print("W",end=" ")
            else:
                print("-",end=" ")
        print(" ")

    #di chuyen
    move = input("Your move: ")
    if move == "a":
        player["x"] -= 1
    elif move == "d":
        player["x"] += 1
    elif move == "w":
        player["y"] -= 1
    elif move == "s":
        player["y"] += 1

    #nhat key va out

    if int(player["y"]) - int(wall["y"]) == 1 or int(player["x"]) - int(wall["x"]) == 1:
        print("Ban dang o gan tuong")
    if player["y"] == key["y"] and player["x"] == key["x"]:
        checked = True
        print("You’ve just picked up a key!!!")
    elif player["y"] == exit["y"] and player["x"] == exit["x"] and checked == False:
        print("You can't exit, please acquire the key(s) first")   
    elif player["y"] == exit["y"] and player["x"] == exit["x"] and checked == True:
        print("Congrats, you’ve just escaped the dungeon")
        break

    


#Level 2

print("Your level is: 2 ")

key2 = {
    "x" : 3,
    "y" : 0,
}

checked2  = True

while True:
    for i in range(4):
        for j in range(4):

            if i == player["y"] and j == player["x"]:
                print("P",end=" ")
            elif i == key["y"] and j == key["x"]:
                if checked == True:
                    print("K",end=" ")
                else:
                    print("-",end=" ")
            elif i == key2["y"] and j == key2["x"]:
                if checked2 == True:
                    print("K",end=" ")
                else:
                    print("-",end=" ")
            elif i == exit["y"] and j == exit["x"]:
                print("E",end=" ")
            elif i == wall["y"] and j == wall["x"]:
                print("W",end=" ")
            else:
                print("-",end=" ")
        print(" ")

    #di chuyen
    move = input("Your move: ")
    if move == "a":
        player["x"] -= 1
    elif move == "d":
        player["x"] += 1
    elif move == "w":
        player["y"] -= 1
    elif move == "s":
        player["y"] += 1

    #nhap key va out

    if int(player["y"]) - int(wall["y"]) == 1 or int(player["x"]) - int(wall["x"]) == 1:
        print("Ban dang o gan tuong")
    if player["y"] == key["y"] and player["x"] == key["x"]:
        checked = False
        print("You’ve just picked up a key!!!")
    if player["y"] == key2["y"] and player["x"] == key2["x"]:
        checked2 = False  
        print("You’ve just picked up a key!!!")
    elif player["y"] == exit["y"] and player["x"] == exit["x"] and  checked == True and checked2 == True:
        print("You can't exit, please acquire the key(s) first")   
    elif player["y"] == exit["y"] and player["x"] == exit["x"] and checked == False and checked2 == False:
        print("Congrats, you’ve just escaped the dungeon")
        break


    
    
    