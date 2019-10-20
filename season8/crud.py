c = 0
r = 0
u = 0
d = 0
items = ['Spider man','LoL','Dragon Ball']
print("List luc dau: ",items)
while True:
    a = input("Ban muon nhap thao tac nao ? c , r ,u ,d ?: ")
    if a == "c":
        b = input("Ban muon them thu yeu thich nao ?: ")
        items.append(b)
        print(items)
        break
    elif a == "r":
        print("List cua ban la: ")
        print(*items,sep='\n')
        break
    elif a == "u":
        x = input("Thu ban muon thay: ")
        y = int(input("Ban muon thay o vi tri: "))
        items[y] = x 
        print(*items,sep=', ')
        break
    elif a == "d":
        z = int(input("Ban muon so item o vi tri: "))
        items.pop(z)
        print(*items,sep=', ')
        break
