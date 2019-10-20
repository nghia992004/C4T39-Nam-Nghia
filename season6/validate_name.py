while True:
    a = input("Ten cua ban la:")
    if a.isalpha():
        print("Dung yeu cau:")
        break
    else:
        print("Khong dung yeu cau:")
        
#str.isalpha:Kiểm tra có phải TOÀN CHỮ hay không