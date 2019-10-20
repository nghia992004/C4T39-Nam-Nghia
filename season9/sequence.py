items = [5,1,8,92,7,30]
print("Enter a list of numbers, separated by ‘,’: ",*items,sep=',')
item = []
for i in items:
    if i % 2 == 0:  
        item.append(i)

print("All even number: ", *item,sep=',')    