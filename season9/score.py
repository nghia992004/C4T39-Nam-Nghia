items = [45,67,56,78]
print("High score: ")
for i, item in enumerate(items):
    print(i,".",item)
a = input("Enter your new score: ")
print("High score: ")
items.append(a)

for i, item in enumerate(items):
    print(i,".",item)