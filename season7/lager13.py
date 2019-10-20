x = True
while x:
    a = input("So ban muon nhap la:")
    if a.isnumeric() and int(a)>13:
        print("So cua ban lon hon 13. ")
        x= False
    if a.isalpha():
        print("Ban can nhap dung so:")
    if a.isnumeric() and int(a)<=13:
        print("So cua ban nho hon 13. ")
        x = False
    

