import random
items = ['Spider man','LoL','Dragon Ball']
while True:
    a = random.choice(items)
    import random
    
    shuffled = list(a)
    random.shuffle(shuffled)
    print(*shuffled,sep=',')
    b = input("Tu ban muon nhap vao: ")
    if b == a:
        print("Ban nhap dung.")
        break
    else:
        print("Ban nhap sai.")
        break
    
