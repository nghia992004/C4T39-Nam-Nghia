x= True
while x:
    a = input("So ban can nhap la: ")
    if a.isalpha():
        print("Ban can nhap so")
    if a.isnumeric() and (int(a)%2)==0 :
        print("So ban la so chan.")
        x = False
    else:
        print("So ban la so le")
        x = False