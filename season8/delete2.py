items = ['Spider man','LoL','Dragon Ball']
while True:
    if "LoL" in items:
        items.remove('LoL')
        print(items)
        break
    elif "LoL" not in items:
        print("Phan tu nay khong ton tai: ")
        break     