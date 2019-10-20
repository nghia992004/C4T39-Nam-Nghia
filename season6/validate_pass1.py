while True:
    a = input("Ten cua ban la:")
    if a.isalpha():
        print("Khong dung:")
    else:
        print("Dung :")
        break
        
#str.isnumeric: Kiểm tra có số hay không