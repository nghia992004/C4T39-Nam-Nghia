items = ['blue','red','teal','green']
print("Our color list: ")
for i, item in enumerate(items):
    print(i,".",item)
a = input("Item to delete: ")
if a.isdigit():
    items.pop(int(a))
    print(*items,sep='\n')
elif a.isalpha():
    items.remove(a)
    print(*items,sep='\n')
    