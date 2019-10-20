quan    = [  'ST',       'BD',     'BTL',     'CG',     'DD',     'HBT']
danso   = ['150.300',  '247.100','333.300','266.800','420.900','318.000']
km      =[ '117.43',    '9.224',  '43.35',  '12.04',   '9.96',  '10.09']
matDoDanSo = []
listNew = zip(quan, danso, km)

for j in listNew:
    matdo = j[1]
    dancu = j[2]
    a = float(j[1]) / float(j[2])
    matDoDanSo.append(a)
    

print("Quan:",*quan,sep='        ')
print("Danso: ",*danso,sep='   ')
print("Km:  ",*km,sep='     ')
print("Mat Do dan so:  ", *matDoDanSo, sep="    ")
