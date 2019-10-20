while True:
    a = input("Ten dang nhap: ")
    b = input("Mat khau:")
    c = input("email: ")
    d = input("Nhap lai mat khau: ")   
    if "@" not in c  or "." not in c:
        print("Ban nhap sai")
    else:
        if len(b)>8 and b==d:
            print("Ban nhap dung")
            break

    