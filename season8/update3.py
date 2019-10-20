items = ['Spider man','LoL','Dragon Ball']
a = int(input("Vi tri ma ban muon thay doi: "))
b = input("Noi dung ban muon thay doi o vi tri: ")
items[a] = b
print(*items,sep=', ')