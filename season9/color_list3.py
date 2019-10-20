items = ['blue','red','teal','green']
print("Our color list: ",*items)
a = input("Mau ban muon them: ")
items.append(a)
print(*items,sep=',')