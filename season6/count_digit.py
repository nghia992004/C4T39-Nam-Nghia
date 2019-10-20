a = input("Enter a number: ")
while True:
    b = a
    if b.isalpha():
        print("Khong dung:")
    else:
        print("The number you entered has",len(b),"digits")
        break
        