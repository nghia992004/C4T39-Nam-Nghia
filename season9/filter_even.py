items = [5,1,8,92,7,30]
item = []
for i in items:
    if i % 2 == 0:  
        item.append(i)

print("All even number: ", *item,sep=',')    