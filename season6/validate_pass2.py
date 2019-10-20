while True:
    a = input("Ten cua ban la:")
    if a.isalpha() or len(a)<=8:
        print("Khong dung:")
    else:
        print("Dung:")
        break
        