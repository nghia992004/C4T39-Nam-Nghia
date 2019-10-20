items = [5,1,8,92,-1,30]
print("List có sẵn: " , *items , sep=', ')
a = int(input("Enter a number: "))
if a in items:
    print("Found")
else:
    print("Not Found")
