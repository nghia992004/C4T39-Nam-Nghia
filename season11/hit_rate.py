from random import randint
person = {
    "Name": "Light",

    "Age": 17,

    "Strength": 8,

    "Defense": 10,

    "HP": 100,

    "Backpack": "Shield, Bread Loaf",

    "Gold": 100,

    "Level": 2,
}
person["Gold"] = 150
person["Backpack"] = "Shield, Bread Loaf,FlintStone"
person["Pocket"] ="MonsterDex, Flashlight"
 

 
skill1 ={
    "Name": "Tackle",

    "Minimum level": 1,

    "Damage": 5,

    "Hit rate": 0.3,
}


skill2 ={
    "Name": "Quick attack",

    "Minimum level": 2,

    "Damage": 3,

    "Hit rate": 0.5,
}


skill3 = {
    "Name": "Strong Kick",

    "Minimum level": 4,

    "Damage": 9,

    "Hit rate": 0.2,
}

skill_list = [skill1,skill2,skill3]
for index,skill in enumerate(skill_list): 
    print(index,".",skill["Name"]) 

num = randint(0, 1)
level = 3
print("Now your level is : 3 ")
a = input("what skill do you choose? (Tackle,Quick_attack,Strong_Kick): ")
if a == "Tackle": #Co th dung a == skill[n]["Name"]
    if num > skill1["Hit rate"]:
        print("Ban danh khong trung muc tieu.")
    else:    
        if level > skill1["Minimum level"]:
            print("Damage = 5")
        else:
            print("Level cua ban khong du de thuc hien.")
if a == "Quick_attack":
    if num > skill1["Hit rate"]:
        print("Ban danh khong trung muc tieu.")
    else:
        if level > skill2["Minimum level"]:
            print("Damgae = 3")
        else:
            print("Level cua ban khong du de thuc hien.")
if a == "Strong_Kick":
    if num > skill1["Hit rate"]:
        print("Ban danh khong trung muc tieu.")
    else:
        if level > skill3["Minimum level"]:
            print("Damage =9")
        else:
            print("Level cua ban khong du de thuc hien.")


