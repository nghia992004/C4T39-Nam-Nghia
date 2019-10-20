items = [45,67,56,78]
items.sort(reverse = True)
print("High score: ")
for i, item in enumerate(items):
    print(i,".",item)
a = int(input("Enter your new score: "))
print("High score: ")
items.append(a)

items.sort(reverse = True)
for i, item in enumerate(items):
    print(i,".",item)