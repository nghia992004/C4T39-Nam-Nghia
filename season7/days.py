while True:
    a = int(input("So thang ban muon nhap la: "))
    if a>12 or a<=0:
        print("Ban can nhap khong dung yeu cau. ")
    elif  a==1 or a==3 or a==5 or a==7 or a==9 or a==11 and a<=12:
        print("Thang cua ban co 31 ngay. ")
        break
    elif a==4 or a==6 or a==8 or a==10 and a<=12:
        print("Thang cua ban co 30 ngay")
        break
    elif a==2:
        print("Thang cua ban co 28 hoac 29 ngay")
        break