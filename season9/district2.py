quan    = [  'ST',       'BD',     'BTL',     'CG',     'DD',     'HBT']
print("Quan:",*quan,sep='        ')
danso   = ['150.300',  '247.100','333.300','266.800','420.900','318.000']
print("Danso: ",*danso,sep='   ')
km      =[ '117.43',    '9.224',  '43.35',  '12.04',   '9.96',  '10.09']
print("Km:  ",*km,sep='     ')
listNew = zip(quan, danso)

for i in listNew:
    for j in range(len(i)):
        saveMin = i[1]
        if saveMin == min(danso):
            print(i[j])