# Tính tổng với Sum
# items = [5,1,8,92,-1,30]
# print("List có sẵn: " , *items , sep=', ')
# a = sum(items)
# print(a)   


#Tính tổng không có Sum
items = [5,1,8,92,-1,30]
print("List có sẵn: " , *items , sep=', ')
tong = 0
for i in items:
    tong = tong +i
print("Sum of all entered numbers: ", tong)
    