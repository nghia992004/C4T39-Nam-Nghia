a = input("So thich dau tien cua ban la: ")
b = input("So thich thu 2 cua ban la: ")
c = input("So thich thu 3 cua ban la: ")
items = ['Spider man','LoL','Dragon Ball']
items.append(a)
items.append(b)
items.append(c)
l = len(items)
for i in items:
    if 'e' in i or 'E' in i:
        print(i)


    