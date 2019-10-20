items = ['Sport','LoL','BTS']
a = input("Bo phim ban muon thay: ")
b = input("Bo truyen ban muon thay: ")
items[0] = a
items[2] = b
print(*items,sep=', ')