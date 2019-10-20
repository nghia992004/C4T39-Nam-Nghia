items = ['Spider man','LoL','Dragon Ball']
print("List truoc khi thay doi: ",items)
a = int(input("Vi tri ma ban muon xoa: "))
items.pop(a)
print(*items,sep=', ')