print("How many legs an octopus has: ")
person = {
    "1":"One leg",
    "2":"Two legs",
    "3":"Four legs",
    "4":"Eight legs",
}
print(person,sep='\n')
a = input("Your answer: ")
if int(a) == 4:
    print("Hura")
else:
    print("Not a correct answer")