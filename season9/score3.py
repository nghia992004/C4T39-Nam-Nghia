items = [45,67,56,78,8,35]
items.sort(reverse = True)
print("High score: ")
for i, item in enumerate(items):
    print(i,".",item)
a = int(input("Enter your new score: "))
print("High score: ")
items.append(a)
tong = 0
items.sort(reverse = True)
for i in range(5):
    print("{} . {}".format(i,items[i]))
