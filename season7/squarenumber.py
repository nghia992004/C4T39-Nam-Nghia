
x = True 
while x:
    a = input("So ban muon nhap: ")
    if a.isnumeric():
        print("So do la:",int(a)**2)
        x = False
    else:
        print("Ban can nhap lai: ")
