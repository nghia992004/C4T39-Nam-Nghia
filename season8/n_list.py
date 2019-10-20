a= input("Name your things: ")
print("Your things: ")
b = a.split(',')
print(*b,sep='\n')