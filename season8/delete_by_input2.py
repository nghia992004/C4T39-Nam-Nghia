items = ['Spider man','LoL','Dragon Ball']
print("List truoc khi thay doi: ",items)
a =(input("Trong ban gia tri tren ban muon xoa cai nao ? "))
items.remove(a)
print(*items,sep=', ')