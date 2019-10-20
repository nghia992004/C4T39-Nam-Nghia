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